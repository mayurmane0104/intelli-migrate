# Type Object Structures — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/typeobj.html](https://docs.python.org/c-api/typeobj.html)

---

# Type Object Structures[¶](#type-object-structures)

Perhaps one of the most important structures of the Python object system is the
structure that defines a new type: the [ PyTypeObject](type.html#c.PyTypeObject) structure.  Type
objects can be handled using any of the 

`PyObject_*` or
`PyType_*` functions, but do not offer much that’s interesting to most
Python applications. These objects are fundamental to how objects behave, so
they are very important to the interpreter itself and to any extension module
that implements new types.Type objects are fairly large compared to most of the standard types. The reason for the size is that each type object stores a large number of values, mostly C function pointers, each of which implements a small part of the type’s functionality. The fields of the type object are examined in detail in this section. The fields will be described in the order in which they occur in the structure.

In addition to the following quick reference, the [Examples](#typedef-examples)
section provides at-a-glance insight into the meaning and use of
[ PyTypeObject](type.html#c.PyTypeObject).

## Quick Reference[¶](#quick-reference)

### “tp slots”[¶](#tp-slots)

| PyTypeObject Slot  | special methods/attrs | Info  | ||||
|---|---|---|---|---|---|---|
| O | T | D | I | |||
| <R>  | const char * | __name__ | X | X | ||
| X | X | X | ||||
| X | X | |||||
| X | X | X | ||||
| X | X | |||||
| __getattribute__, __getattr__ | G | |||||
| __setattr__, __delattr__ | G | |||||
| % | ||||||
| __repr__ | X | X | X | |||
| % | ||||||
| % | ||||||
| % | ||||||
| __hash__ | X | G | ||||
| __call__ | X | X | ||||
| __str__ | X | X | ||||
| __getattribute__, __getattr__ | X | X | G | |||
| __setattr__, __delattr__ | X | X | G | |||
| % | ||||||
| unsigned long | X | X | ? | |||
| const char * | __doc__ | X | X | |||
| X | G | |||||
| X | G | |||||
| __lt__, __le__, __eq__, __ne__, __gt__, __ge__ | X | G | ||||
| X | ? | |||||
| __iter__ | X | |||||
| __next__ | X | |||||
| 
 | X | X | ||||
| 
 | X | |||||
| 
 | X | X | ||||
| __base__ | X | |||||
| 
 | __dict__ | ? | ||||
| __get__ | X | |||||
| __set__, __delete__ | X | |||||
| X | ? | |||||
| __init__ | X | X | X | |||
| X | ? | ? | ||||
| __new__ | X | X | ? | ? | ||
| X | X | ? | ? | |||
| X | X | |||||
| < | 
 | __bases__ | ~ | |||
| < | 
 | __mro__ | ~ | |||
| [ | 
 | |||||
| void * | __subclasses__ | |||||
| 
 | ||||||
| ( | ||||||
| unsigned int | ||||||
| __del__ | X | |||||
| unsigned char | ||||||

### sub-slots[¶](#sub-slots)

| Slot | special methods | |
|---|---|---|
| __await__ | ||
| __aiter__ | ||
| __anext__ | ||
| __add__ __radd__ | ||
| __iadd__ | ||
| __sub__ __rsub__ | ||
| __isub__ | ||
| __mul__ __rmul__ | ||
| __imul__ | ||
| __mod__ __rmod__ | ||
| __imod__ | ||
| __divmod__ __rdivmod__ | ||
| __pow__ __rpow__ | ||
| __ipow__ | ||
| __neg__ | ||
| __pos__ | ||
| __abs__ | ||
| __bool__ | ||
| __invert__ | ||
| __lshift__ __rlshift__ | ||
| __ilshift__ | ||
| __rshift__ __rrshift__ | ||
| __irshift__ | ||
| __and__ __rand__ | ||
| __iand__ | ||
| __xor__ __rxor__ | ||
| __ixor__ | ||
| __or__ __ror__ | ||
| __ior__ | ||
| __int__ | ||
| void * | ||
| __float__ | ||
| __floordiv__ | ||
| __ifloordiv__ | ||
| __truediv__ | ||
| __itruediv__ | ||
| __index__ | ||
| __matmul__ __rmatmul__ | ||
| __imatmul__ | ||
| __len__ | ||
| __getitem__ | ||
| __setitem__, __delitem__ | ||
| __len__ | ||
| __add__ | ||
| __mul__ | ||
| __getitem__ | ||
| __setitem__ __delitem__ | ||
| __contains__ | ||
| __iadd__ | ||
| __imul__ | ||
| __buffer__ | ||
| __release_buffer__ | ||

### slot typedefs[¶](#slot-typedefs)

| typedef | Parameter Types | Return Type | 
|---|---|---|
| 
 | ||
| 
 | void | |
| void * | void | |
| int | ||
| 
 | ||
| int | ||
| 
 | 
 | |
| *`PyObject`const char * | 
 | |
| int | ||
| 
 | ||
| int | ||
| 
 | ||
| int | ||
| 
 | Py_hash_t | |
| 
 | ||
| 
 | 
 | |
| 
 | 
 | |
| 
 | ||
| int | ||
| void | ||
| 
 | int | |
| *`PyObject` | 
 | |
| 
 | ||
| 
 | ||
| 
 | ||
| int | ||
| int | ||
| int | 

See [Slot Type typedefs](#id6) below for more detail.

## PyTypeObject Definition[¶](#pytypeobject-definition)

The structure definition for [ PyTypeObject](type.html#c.PyTypeObject) can be found in

`Include/cpython/object.h`.  For convenience of reference, this repeats the
definition found there:```
typedef struct _typeobject {
    PyObject_VAR_HEAD
    const char *tp_name; /* For printing, in format "<module>.<name>" */
    Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */
    /* Methods to implement standard operations */
    destructor tp_dealloc;
    Py_ssize_t tp_vectorcall_offset;
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    PyAsyncMethods *tp_as_async; /* formerly known as tp_compare (Python 2)
                                    or tp_reserved (Python 3) */
    reprfunc tp_repr;
    /* Method suites for standard classes */
    PyNumberMethods *tp_as_number;
    PySequenceMethods *tp_as_sequence;
    PyMappingMethods *tp_as_mapping;
    /* More standard operations (here for binary compatibility) */
    hashfunc tp_hash;
    ternaryfunc tp_call;
    reprfunc tp_str;
    getattrofunc tp_getattro;
    setattrofunc tp_setattro;
    /* Functions to access object as input/output buffer */
    PyBufferProcs *tp_as_buffer;
    /* Flags to define presence of optional/expanded features */
    unsigned long tp_flags;
    const char *tp_doc; /* Documentation string */
    /* Assigned meaning in release 2.0 */
    /* call function for all accessible objects */
    traverseproc tp_traverse;
    /* delete references to contained objects */
    inquiry tp_clear;
    /* Assigned meaning in release 2.1 */
    /* rich comparisons */
    richcmpfunc tp_richcompare;
    /* weak reference enabler */
    Py_ssize_t tp_weaklistoffset;
    /* Iterators */
    getiterfunc tp_iter;
    iternextfunc tp_iternext;
    /* Attribute descriptor and subclassing stuff */
    PyMethodDef *tp_methods;
    PyMemberDef *tp_members;
    PyGetSetDef *tp_getset;
    // Strong reference on a heap type, borrowed reference on a static type
    PyTypeObject *tp_base;
    PyObject *tp_dict;
    descrgetfunc tp_descr_get;
    descrsetfunc tp_descr_set;
    Py_ssize_t tp_dictoffset;
    initproc tp_init;
    allocfunc tp_alloc;
    newfunc tp_new;
    freefunc tp_free; /* Low-level free-memory routine */
    inquiry tp_is_gc; /* For PyObject_IS_GC */
    PyObject *tp_bases;
    PyObject *tp_mro; /* method resolution order */
    PyObject *tp_cache; /* no longer used */
    void *tp_subclasses;  /* for static builtin types this is an index */
    PyObject *tp_weaklist; /* not used for static builtin types */
    destructor tp_del;
    /* Type attribute cache version tag. Added in version 2.6.
     * If zero, the cache is invalid and must be initialized.
     */
    unsigned int tp_version_tag;
    destructor tp_finalize;
    vectorcallfunc tp_vectorcall;
    /* bitset of which type-watchers care about this type */
    unsigned char tp_watched;
    /* Number of tp_version_tag values used.
     * Set to _Py_ATTR_CACHE_UNUSED if the attribute cache is
     * disabled for this type (e.g. due to custom MRO entries).
     * Otherwise, limited to MAX_VERSIONS_PER_CLASS (defined elsewhere).
     */
    uint16_t tp_versions_used;
} PyTypeObject;
```
## PyObject Slots[¶](#pyobject-slots)

The type object structure extends the [ PyVarObject](structures.html#c.PyVarObject) structure. The

[field is used for dynamic types (created by](structures.html#c.PyVarObject.ob_size)

`ob_size``type_new()`,
usually called from a class statement). Note that [(the metatype) initializes](type.html#c.PyType_Type)

`PyType_Type`[, which means that its instances (i.e. type objects)](#c.PyTypeObject.tp_itemsize)

`tp_itemsize`*must*have the

`ob_size` field.The type object’s reference count is initialized to

`1`by the`PyObject_HEAD_INIT`macro. Note that for[statically allocated type objects](#static-types), the type’s instances (objects whose[points back to the type) do](structures.html#c.PyObject.ob_type)`ob_type`notcount as references. But for[dynamically allocated type objects](#heap-types), the instancesdocount as references.

Inheritance:This field is not inherited by subtypes.


This is the type’s type, in other words its metatype. It is initialized by the argument to the

`PyObject_HEAD_INIT`macro, and its value should normally be`&PyType_Type`. However, for dynamically loadable extension modules that must be usable on Windows (at least), the compiler complains that this is not a valid initializer. Therefore, the convention is to pass`NULL`to the`PyObject_HEAD_INIT`macro and to initialize this field explicitly at the start of the module’s initialization function, before doing anything else. This is typically done like this:Foo_Type.ob_type = &PyType_Type;This should be done before any instances of the type are created.

[checks if](type.html#c.PyType_Ready)`PyType_Ready()`[is](structures.html#c.PyObject.ob_type)`ob_type``NULL`, and if so, initializes it to the`ob_type`field of the base class.`PyType_Ready()`will not change this field if it is non-zero.

Inheritance:This field is inherited by subtypes.


## PyVarObject Slots[¶](#pyvarobject-slots)

For

[statically allocated type objects](#static-types), this should be initialized to zero. For[dynamically allocated type objects](#heap-types), this field has a special internal meaning.This field should be accessed using the

[macro.](structures.html#c.Py_SIZE)`Py_SIZE()`

Inheritance:This field is not inherited by subtypes.


## PyTypeObject Slots[¶](#pytypeobject-slots)

Each slot has a section describing inheritance.  If [ PyType_Ready()](type.html#c.PyType_Ready)
may set a value when the field is set to 

`NULL` then there will also be
a “Default” section.  (Note that many fields set on [and](structures.html#c.PyBaseObject_Type)

`PyBaseObject_Type`[effectively act as defaults.)](type.html#c.PyType_Type)

`PyType_Type`- 
const char *[PyTypeObject](type.html#c.PyTypeObject).tp_name[¶](#c.PyTypeObject.tp_name)
- Pointer to a NUL-terminated string containing the name of the type. For types that are accessible as module globals, the string should be the full module name, followed by a dot, followed by the type name; for built-in types, it should be just the type name. If the module is a submodule of a package, the full package name is part of the full module name. For example, a type named - `T`defined in module- `M`in subpackage- `Q`in package- `P`should have the- `tp_name`- `"P.Q.M.T"`.- For - [dynamically allocated type objects](#heap-types), this should just be the type name, and the module name explicitly stored in the type dict as the value for key- `'__module__'`.- For - [statically allocated type objects](#static-types), the- *tp_name*field should contain a dot. Everything before the last dot is made accessible as the- `__module__`- `__name__`- If no dot is present, the entire - `tp_name`- `__name__`- `__module__`- This field must not be - `NULL`. It is the only required field in- `PyTypeObject()`- `tp_itemsize`- **Inheritance:**- This field is not inherited by subtypes. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)[PyTypeObject](type.html#c.PyTypeObject).tp_basicsize[¶](#c.PyTypeObject.tp_basicsize)
- 
[Py_ssize_t](intro.html#c.Py_ssize_t)[PyTypeObject](type.html#c.PyTypeObject).tp_itemsize[¶](#c.PyTypeObject.tp_itemsize)
- These fields allow calculating the size in bytes of instances of the type. - There are two kinds of types: types with fixed-length instances have a zero - `tp_itemsize`field, types with variable-length instances have a non-zero- `tp_itemsize`field. For a type with fixed-length instances, all instances have the same size, given in- `tp_basicsize`. (Exceptions to this rule can be made using- `PyUnstable_Object_GC_NewWithExtraData()`- For a type with variable-length instances, the instances must have an - `ob_size`- `tp_basicsize`plus N times- `tp_itemsize`, where N is the “length” of the object.- Functions like - `PyObject_NewVar()`- `ob_size`- `ob_size`field may later be used for other purposes. For example,- `int`- `ob_size`in an implementation-defined way; the underlying storage and its size should be accessed using- `PyLong_Export()`- Note - The - `ob_size`- `Py_SIZE()`- `Py_SET_SIZE()`- Also, the presence of an - `ob_size`- `list`- `ob_size`field. (As with- `int`- `ob_size`directly. Call- `PyList_Size()`- The - `tp_basicsize`includes size needed for data of the type’s- `tp_base`- The correct way to set - `tp_basicsize`is to use the- `sizeof`operator on the struct used to declare the instance layout. This struct must include the struct used to declare the base type. In other words,- `tp_basicsize`must be greater than or equal to the base’s- `tp_basicsize`.- Since every type is a subtype of - `object`- `PyObject`- `PyVarObject`- `ob_size`- `PyObject_HEAD`- `PyObject_VAR_HEAD`- The basic size does not include the GC header size, as that header is not part of - `PyObject_HEAD`- For cases where struct used to declare the base type is unknown, see - `PyType_Spec.basicsize`- `PyType_FromMetaclass()`- Notes about alignment: - `tp_basicsize`must be a multiple of- `_Alignof(PyObject)`. When using- `sizeof`on a- `struct`that includes- `PyObject_HEAD`- `struct`, or when using compiler extensions like- `__attribute__((packed))`, it is up to you.
- If the variable items require a particular alignment, - `tp_basicsize`and- `tp_itemsize`must each be a multiple of that alignment. For example, if a type’s variable part stores a- `double`, it is your responsibility that both fields are a multiple of- `_Alignof(double)`.
 - **Inheritance:**- These fields are inherited separately by subtypes. (That is, if the field is set to zero, - `PyType_Ready()`- If the base type has a non-zero - `tp_itemsize`- `tp_itemsize`to a different non-zero value in a subtype (though this depends on the implementation of the base type).

- 
[destructor](#c.destructor)[PyTypeObject](type.html#c.PyTypeObject).tp_dealloc[¶](#c.PyTypeObject.tp_dealloc)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_dealloc`is part of the- [Stable ABI](stable.html#stable).- A pointer to the instance destructor function. The function signature is: - void tp_dealloc(PyObject *self); - The destructor function should remove all references which the instance owns (e.g., call - `Py_CLEAR()`- `tp_free`- If you may call functions that may set the error indicator, you must use - `PyErr_GetRaisedException()`- `PyErr_SetRaisedException()`- static void foo_dealloc(foo_object *self) { PyObject *et, *ev, *etb; PyObject *exc = PyErr_GetRaisedException(); ... PyErr_SetRaisedException(exc); } - The dealloc handler itself must not raise an exception; if it hits an error case it should call - `PyErr_FormatUnraisable()`- No guarantees are made about when an object is destroyed, except: - Python will destroy an object immediately or some time after the final reference to the object is deleted, unless its finalizer ( - `tp_finalize`
- An object will not be destroyed while it is being automatically finalized ( - `tp_finalize`- `tp_clear`
 - CPython currently destroys an object immediately from - `Py_DECREF()`- It is recommended to call - `PyObject_CallFinalizerFromDealloc()`- `tp_dealloc`to guarantee that the object is always finalized before destruction.- If the type supports garbage collection (the - `Py_TPFLAGS_HAVE_GC`- `PyObject_GC_UnTrack()`- It is permissible to call - `tp_clear`- `tp_dealloc`to reduce code duplication and to guarantee that the object is always cleared before destruction. Beware that- `tp_clear`might have already been called.- If the type is heap allocated ( - `Py_TPFLAGS_HEAPTYPE`- `Py_DECREF()`- static void foo_dealloc(PyObject *op) { foo_object *self = (foo_object *) op; PyObject_GC_UnTrack(self); Py_CLEAR(self->ref); Py_TYPE(self)->tp_free(self); } - `tp_dealloc`must leave the exception status unchanged. If it needs to call something that might raise an exception, the exception state must be backed up first and restored later (after logging any exceptions with- `PyErr_WriteUnraisable()`- Example: - static void foo_dealloc(PyObject *self) { PyObject *exc = PyErr_GetRaisedException(); if (PyObject_CallFinalizerFromDealloc(self) < 0) { // self was resurrected. goto done; } PyTypeObject *tp = Py_TYPE(self); if (tp->tp_flags & Py_TPFLAGS_HAVE_GC) { PyObject_GC_UnTrack(self); } // Optional, but convenient to avoid code duplication. if (tp->tp_clear && tp->tp_clear(self) < 0) { PyErr_WriteUnraisable(self); } // Any additional destruction goes here. tp->tp_free(self); self = NULL; // In case PyErr_WriteUnraisable() is called below. if (tp->tp_flags & Py_TPFLAGS_HEAPTYPE) { Py_CLEAR(tp); } done: // Optional, if something was called that might have raised an // exception. if (PyErr_Occurred()) { PyErr_WriteUnraisable(self); } PyErr_SetRaisedException(exc); } - `tp_dealloc`may be called from any Python thread, not just the thread which created the object (if the object becomes part of a refcount cycle, that cycle might be collected by a garbage collection on any thread). This is not a problem for Python API calls, since the thread on which- `tp_dealloc`is called with an- [attached thread state](../glossary.html#term-attached-thread-state). However, if the object being destroyed in turn destroys objects from some other C library, care should be taken to ensure that destroying those objects on the thread which called- `tp_dealloc`will not violate any assumptions of the library.- **Inheritance:**- This field is inherited by subtypes. - See also - [Object Life Cycle](lifecycle.html#life-cycle)for details about how this slot relates to other slots.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)[PyTypeObject](type.html#c.PyTypeObject).tp_vectorcall_offset[¶](#c.PyTypeObject.tp_vectorcall_offset)
- An optional offset to a per-instance function that implements calling the object using the - [vectorcall protocol](call.html#vectorcall), a more efficient alternative of the simpler- `tp_call`- This field is only used if the flag - `Py_TPFLAGS_HAVE_VECTORCALL`- `vectorcallfunc`- The - *vectorcallfunc*pointer may be- `NULL`, in which case the instance behaves as if- `Py_TPFLAGS_HAVE_VECTORCALL`- `tp_call`- Any class that sets - `Py_TPFLAGS_HAVE_VECTORCALL`must also set- `tp_call`- *vectorcallfunc*function. This can be done by setting- *tp_call*to- `PyVectorcall_Call()`- Changed in version 3.8: Before version 3.8, this slot was named - `tp_print`. In Python 2.x, it was used for printing to a file. In Python 3.0 to 3.7, it was unused.- Changed in version 3.12: Before version 3.12, it was not recommended for - [mutable heap types](#heap-types)to implement the vectorcall protocol. When a user sets- `__call__`- *tp_call*is updated, likely making it inconsistent with the vectorcall function. Since 3.12, setting- `__call__`will disable vectorcall optimization by clearing the- `Py_TPFLAGS_HAVE_VECTORCALL`- **Inheritance:**- This field is always inherited. However, the - `Py_TPFLAGS_HAVE_VECTORCALL`- [vectorcall](call.html#vectorcall), except when- `PyVectorcall_Call()`

- 
[getattrfunc](#c.getattrfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_getattr[¶](#c.PyTypeObject.tp_getattr)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_getattr`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to the get-attribute-string function. - This field is deprecated. When it is defined, it should point to a function that acts the same as the - `tp_getattro`- **Inheritance:**- Group: - `tp_getattr`- `tp_getattro`- This field is inherited by subtypes together with - `tp_getattro`- `tp_getattr`- `tp_getattro`from its base type when the subtype’s- `tp_getattr`and- `tp_getattro`are both- `NULL`.

- 
[setattrfunc](#c.setattrfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_setattr[¶](#c.PyTypeObject.tp_setattr)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_setattr`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to the function for setting and deleting attributes. - This field is deprecated. When it is defined, it should point to a function that acts the same as the - `tp_setattro`- **Inheritance:**- Group: - `tp_setattr`- `tp_setattro`- This field is inherited by subtypes together with - `tp_setattro`- `tp_setattr`- `tp_setattro`from its base type when the subtype’s- `tp_setattr`and- `tp_setattro`are both- `NULL`.

- 
[PyAsyncMethods](#c.PyAsyncMethods)*[PyTypeObject](type.html#c.PyTypeObject).tp_as_async[¶](#c.PyTypeObject.tp_as_async)
- Pointer to an additional structure that contains fields relevant only to objects which implement - [awaitable](../glossary.html#term-awaitable)and- [asynchronous iterator](../glossary.html#term-asynchronous-iterator)protocols at the C-level. See- [Async Object Structures](#async-structs)for details.- Added in version 3.5: Formerly known as - `tp_compare`and- `tp_reserved`.- **Inheritance:**- The - `tp_as_async`

- 
[reprfunc](#c.reprfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_repr[¶](#c.PyTypeObject.tp_repr)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_repr`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function that implements the built-in function - `repr()`- The signature is the same as for - `PyObject_Repr()`- PyObject *tp_repr(PyObject *self); - The function must return a string or a Unicode object. Ideally, this function should return a string that, when passed to - `eval()`- `'<'`and ending with- `'>'`from which both the type and the value of the object can be deduced.- **Inheritance:**- This field is inherited by subtypes. - **Default:**- When this field is not set, a string of the form - `<%s object at %p>`is returned, where- `%s`is replaced by the type name, and- `%p`by the object’s memory address.

- 
[PyNumberMethods](#c.PyNumberMethods)*[PyTypeObject](type.html#c.PyTypeObject).tp_as_number[¶](#c.PyTypeObject.tp_as_number)
- Pointer to an additional structure that contains fields relevant only to objects which implement the number protocol. These fields are documented in - [Number Object Structures](#number-structs).- **Inheritance:**- The - `tp_as_number`

- 
[PySequenceMethods](#c.PySequenceMethods)*[PyTypeObject](type.html#c.PyTypeObject).tp_as_sequence[¶](#c.PyTypeObject.tp_as_sequence)
- Pointer to an additional structure that contains fields relevant only to objects which implement the sequence protocol. These fields are documented in - [Sequence Object Structures](#sequence-structs).- **Inheritance:**- The - `tp_as_sequence`

- 
[PyMappingMethods](#c.PyMappingMethods)*[PyTypeObject](type.html#c.PyTypeObject).tp_as_mapping[¶](#c.PyTypeObject.tp_as_mapping)
- Pointer to an additional structure that contains fields relevant only to objects which implement the mapping protocol. These fields are documented in - [Mapping Object Structures](#mapping-structs).- **Inheritance:**- The - `tp_as_mapping`

- 
[hashfunc](#c.hashfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_hash[¶](#c.PyTypeObject.tp_hash)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_hash`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function that implements the built-in function - `hash()`- The signature is the same as for - `PyObject_Hash()`- Py_hash_t tp_hash(PyObject *); - The value - `-1`should not be returned as a normal return value; when an error occurs during the computation of the hash value, the function should set an exception and return- `-1`.- When this field is not set ( - *and*- `tp_richcompare`- `TypeError`- `PyObject_HashNotImplemented()`- This field can be set explicitly to - `PyObject_HashNotImplemented()`- `__hash__ = None`at the Python level, causing- `isinstance(o, collections.Hashable)`to correctly return- `False`. Note that the converse is also true - setting- `__hash__ = None`on a class at the Python level will result in the- `tp_hash`slot being set to- `PyObject_HashNotImplemented()`.- **Inheritance:**- Group: - `tp_hash`- `tp_richcompare`- This field is inherited by subtypes together with - `tp_richcompare`- `tp_richcompare`and- `tp_hash`- `tp_richcompare`and- `tp_hash`are both- `NULL`.- **Default:**

- 
[ternaryfunc](#c.ternaryfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_call[¶](#c.PyTypeObject.tp_call)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_call`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function that implements calling the object. This should be - `NULL`if the object is not callable. The signature is the same as for- `PyObject_Call()`- PyObject *tp_call(PyObject *self, PyObject *args, PyObject *kwargs); - **Inheritance:**- This field is inherited by subtypes. 

- 
[reprfunc](#c.reprfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_str[¶](#c.PyTypeObject.tp_str)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_str`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function that implements the built-in operation - `str()`- `str`- `str()`calls the constructor for that type. This constructor calls- `PyObject_Str()`- `PyObject_Str()`will call this handler.)- The signature is the same as for - `PyObject_Str()`- PyObject *tp_str(PyObject *self); - The function must return a string or a Unicode object. It should be a “friendly” string representation of the object, as this is the representation that will be used, among other things, by the - `print()`- **Inheritance:**- This field is inherited by subtypes. - **Default:**- When this field is not set, - `PyObject_Repr()`

- 
[getattrofunc](#c.getattrofunc)[PyTypeObject](type.html#c.PyTypeObject).tp_getattro[¶](#c.PyTypeObject.tp_getattro)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_getattro`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to the get-attribute function. - The signature is the same as for - `PyObject_GetAttr()`- PyObject *tp_getattro(PyObject *self, PyObject *attr); - It is usually convenient to set this field to - `PyObject_GenericGetAttr()`- **Inheritance:**- Group: - `tp_getattr`- `tp_getattro`- This field is inherited by subtypes together with - `tp_getattr`- `tp_getattr`and- `tp_getattro`- `tp_getattr`and- `tp_getattro`are both- `NULL`.- **Default:**

- 
[setattrofunc](#c.setattrofunc)[PyTypeObject](type.html#c.PyTypeObject).tp_setattro[¶](#c.PyTypeObject.tp_setattro)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_setattro`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to the function for setting and deleting attributes. - The signature is the same as for - `PyObject_SetAttr()`- int tp_setattro(PyObject *self, PyObject *attr, PyObject *value); - In addition, setting - *value*to- `NULL`to delete an attribute must be supported. It is usually convenient to set this field to- `PyObject_GenericSetAttr()`- **Inheritance:**- Group: - `tp_setattr`- `tp_setattro`- This field is inherited by subtypes together with - `tp_setattr`- `tp_setattr`and- `tp_setattro`- `tp_setattr`and- `tp_setattro`are both- `NULL`.- **Default:**

- 
[PyBufferProcs](#c.PyBufferProcs)*[PyTypeObject](type.html#c.PyTypeObject).tp_as_buffer[¶](#c.PyTypeObject.tp_as_buffer)
- Pointer to an additional structure that contains fields relevant only to objects which implement the buffer interface. These fields are documented in - [Buffer Object Structures](#buffer-structs).- **Inheritance:**- The - `tp_as_buffer`

- 
unsigned long [PyTypeObject](type.html#c.PyTypeObject).tp_flags[¶](#c.PyTypeObject.tp_flags)
- This field is a bit mask of various flags. Some flags indicate variant semantics for certain situations; others are used to indicate that certain fields in the type object (or in the extension structures referenced via - `tp_as_number`- `tp_as_sequence`- `tp_as_mapping`- `tp_as_buffer`- `NULL`value instead.- **Inheritance:**- Inheritance of this field is complicated. Most flag bits are inherited individually, i.e. if the base type has a flag bit set, the subtype inherits this flag bit. The flag bits that pertain to extension structures are strictly inherited if the extension structure is inherited, i.e. the base type’s value of the flag bit is copied into the subtype together with a pointer to the extension structure. The - `Py_TPFLAGS_HAVE_GC`- `tp_traverse`- `tp_clear`- `Py_TPFLAGS_HAVE_GC`flag bit is clear in the subtype and the- `tp_traverse`and- `tp_clear`fields in the subtype exist and have- `NULL`values.- **Default:**- `PyBaseObject_Type`- `Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE`.- **Bit Masks:**- The following bit masks are currently defined; these can be ORed together using the - `|`operator to form the value of the- `tp_flags`- `PyType_HasFeature()`- *tp*and- *f*, and checks whether- `tp->tp_flags & f`is non-zero.- 
Py_TPFLAGS_HEAPTYPE[¶](#c.Py_TPFLAGS_HEAPTYPE)
- This bit is set when the type object itself is allocated on the heap, for example, types created dynamically using - `PyType_FromSpec()`- `ob_type`- [support garbage collection](gcsupport.html#supporting-cycle-detection)as they can form a reference cycle with their own module object.- **Inheritance:**- ??? 
 - 
Py_TPFLAGS_BASETYPE[¶](#c.Py_TPFLAGS_BASETYPE)
- *Part of the*- [Stable ABI](stable.html#stable).- This bit is set when the type can be used as the base type of another type. If this bit is clear, the type cannot be subtyped (similar to a “final” class in Java). - **Inheritance:**- ??? 
 - 
Py_TPFLAGS_READY[¶](#c.Py_TPFLAGS_READY)
- This bit is set when the type object has been fully initialized by - `PyType_Ready()`- **Inheritance:**- ??? 
 - 
Py_TPFLAGS_READYING[¶](#c.Py_TPFLAGS_READYING)
- This bit is set while - `PyType_Ready()`- **Inheritance:**- ??? 
 - 
Py_TPFLAGS_HAVE_GC[¶](#c.Py_TPFLAGS_HAVE_GC)
- *Part of the*- [Stable ABI](stable.html#stable).- This bit is set when the object supports garbage collection. If this bit is set, memory for new instances (see - `tp_alloc`- `PyObject_GC_New`- `PyType_GenericAlloc()`- `tp_free`- `PyObject_GC_Del()`- [Supporting Cyclic Garbage Collection](gcsupport.html#supporting-cycle-detection).- **Inheritance:**- Group: - `Py_TPFLAGS_HAVE_GC`- `tp_traverse`- `tp_clear`- The - `Py_TPFLAGS_HAVE_GC`- `tp_traverse`- `tp_clear`- `Py_TPFLAGS_HAVE_GC`flag bit is clear in the subtype and the- `tp_traverse`and- `tp_clear`fields in the subtype exist and have- `NULL`values.
 - 
Py_TPFLAGS_DEFAULT[¶](#c.Py_TPFLAGS_DEFAULT)
- *Part of the*- [Stable ABI](stable.html#stable).- This is a bitmask of all the bits that pertain to the existence of certain fields in the type object and its extension structures. Currently, it includes the following bits: - `Py_TPFLAGS_HAVE_STACKLESS_EXTENSION`- **Inheritance:**- ??? 
 - 
Py_TPFLAGS_METHOD_DESCRIPTOR[¶](#c.Py_TPFLAGS_METHOD_DESCRIPTOR)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- This bit indicates that objects behave like unbound methods. - If this flag is set for - `type(meth)`, then:- `meth.__get__(obj, cls)(*args, **kwds)`(with- `obj`not None) must be equivalent to- `meth(obj, *args, **kwds)`.
- `meth.__get__(None, cls)(*args, **kwds)`must be equivalent to- `meth(*args, **kwds)`.
 - This flag enables an optimization for typical method calls like - `obj.meth()`: it avoids creating a temporary “bound method” object for- `obj.meth`.- Added in version 3.8. - **Inheritance:**- This flag is never inherited by types without the - `Py_TPFLAGS_IMMUTABLETYPE`- `tp_descr_get`
 - 
Py_TPFLAGS_MANAGED_DICT[¶](#c.Py_TPFLAGS_MANAGED_DICT)
- This bit indicates that instances of the class have a - `__dict__`- If this flag is set, - `Py_TPFLAGS_HAVE_GC`- The type traverse function must call - `PyObject_VisitManagedDict()`- `PyObject_ClearManagedDict()`- Added in version 3.12. - **Inheritance:**- This flag is inherited unless the - `tp_dictoffset`
 - 
Py_TPFLAGS_MANAGED_WEAKREF[¶](#c.Py_TPFLAGS_MANAGED_WEAKREF)
- This bit indicates that instances of the class should be weakly referenceable. - Added in version 3.12. - **Inheritance:**- This flag is inherited unless the - `tp_weaklistoffset`
 - 
Py_TPFLAGS_ITEMS_AT_END[¶](#c.Py_TPFLAGS_ITEMS_AT_END)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Only usable with variable-size types, i.e. ones with non-zero - `tp_itemsize`- Indicates that the variable-sized portion of an instance of this type is at the end of the instance’s memory area, at an offset of - `Py_TYPE(obj)->tp_basicsize`(which may be different in each subclass).- When setting this flag, be sure that all superclasses either use this memory layout, or are not variable-sized. Python does not check this. - Added in version 3.12. - **Inheritance:**- This flag is inherited. 
 - 
Py_TPFLAGS_LONG_SUBCLASS[¶](#c.Py_TPFLAGS_LONG_SUBCLASS)
 - 
Py_TPFLAGS_LIST_SUBCLASS[¶](#c.Py_TPFLAGS_LIST_SUBCLASS)
 - 
Py_TPFLAGS_TUPLE_SUBCLASS[¶](#c.Py_TPFLAGS_TUPLE_SUBCLASS)
 - 
Py_TPFLAGS_BYTES_SUBCLASS[¶](#c.Py_TPFLAGS_BYTES_SUBCLASS)
 - 
Py_TPFLAGS_UNICODE_SUBCLASS[¶](#c.Py_TPFLAGS_UNICODE_SUBCLASS)
 - 
Py_TPFLAGS_DICT_SUBCLASS[¶](#c.Py_TPFLAGS_DICT_SUBCLASS)
 - 
Py_TPFLAGS_BASE_EXC_SUBCLASS[¶](#c.Py_TPFLAGS_BASE_EXC_SUBCLASS)
 - 
Py_TPFLAGS_TYPE_SUBCLASS[¶](#c.Py_TPFLAGS_TYPE_SUBCLASS)
- Functions such as - `PyLong_Check()`- `PyType_FastSubclass()`- `PyObject_IsInstance()`- `tp_flags`
 - 
Py_TPFLAGS_HAVE_FINALIZE[¶](#c.Py_TPFLAGS_HAVE_FINALIZE)
- This bit is set when the - `tp_finalize`- Added in version 3.4. - Deprecated since version 3.8: This flag isn’t necessary anymore, as the interpreter assumes the - `tp_finalize`
 - 
Py_TPFLAGS_HAVE_VECTORCALL[¶](#c.Py_TPFLAGS_HAVE_VECTORCALL)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- This bit is set when the class implements the - [vectorcall protocol](call.html#vectorcall). See- `tp_vectorcall_offset`- **Inheritance:**- This bit is inherited if - `tp_call`- Added in version 3.8: as - `_Py_TPFLAGS_HAVE_VECTORCALL`- Changed in version 3.9. - Renamed to the current name, without the leading underscore. The old provisional name is - [soft deprecated](../glossary.html#term-soft-deprecated).- Changed in version 3.12: This flag is now removed from a class when the class’s - `__call__()`- This flag can now be inherited by mutable classes. 
 - 
Py_TPFLAGS_IMMUTABLETYPE[¶](#c.Py_TPFLAGS_IMMUTABLETYPE)
- This bit is set for type objects that are immutable: type attributes cannot be set nor deleted. - `PyType_Ready()`- [static types](#static-types).- **Inheritance:**- This flag is not inherited. - Added in version 3.10. 
 - 
Py_TPFLAGS_DISALLOW_INSTANTIATION[¶](#c.Py_TPFLAGS_DISALLOW_INSTANTIATION)
- Disallow creating instances of the type: set - `tp_new`- `__new__`key in the type dictionary.- The flag must be set before creating the type, not after. For example, it must be set before - `PyType_Ready()`- The flag is set automatically on - [static types](#static-types)if- `tp_base`- `&PyBaseObject_Type`and- `tp_new`- **Inheritance:**- This flag is not inherited. However, subclasses will not be instantiable unless they provide a non-NULL - `tp_new`- Note - To disallow instantiating a class directly but allow instantiating its subclasses (e.g. for an - [abstract base class](../glossary.html#term-abstract-base-class)), do not use this flag. Instead, make- `tp_new`- Added in version 3.10. 
 - 
Py_TPFLAGS_MAPPING[¶](#c.Py_TPFLAGS_MAPPING)
- This bit indicates that instances of the class may match mapping patterns when used as the subject of a - `match`- `collections.abc.Mapping`- `collections.abc.Sequence`- Note - `Py_TPFLAGS_MAPPING`- `Py_TPFLAGS_SEQUENCE`- **Inheritance:**- This flag is inherited by types that do not already set - `Py_TPFLAGS_SEQUENCE`- See also - **PEP 634**- Added in version 3.10. 
 - 
Py_TPFLAGS_SEQUENCE[¶](#c.Py_TPFLAGS_SEQUENCE)
- This bit indicates that instances of the class may match sequence patterns when used as the subject of a - `match`- `collections.abc.Sequence`- `collections.abc.Mapping`- Note - `Py_TPFLAGS_MAPPING`- `Py_TPFLAGS_SEQUENCE`- **Inheritance:**- This flag is inherited by types that do not already set - `Py_TPFLAGS_MAPPING`- See also - **PEP 634**- Added in version 3.10. 
 - 
Py_TPFLAGS_VALID_VERSION_TAG[¶](#c.Py_TPFLAGS_VALID_VERSION_TAG)
- Internal. Do not set or unset this flag. To indicate that a class has changed call - `PyType_Modified()`- Warning - This flag is present in header files, but is not be used. It will be removed in a future version of CPython 
 - 
Py_TPFLAGS_HAVE_VERSION_TAG[¶](#c.Py_TPFLAGS_HAVE_VERSION_TAG)
- This is a - [soft deprecated](../glossary.html#term-soft-deprecated)macro that does nothing. Historically, this would indicate that the- `tp_version_tag`
 - 
Py_TPFLAGS_INLINE_VALUES[¶](#c.Py_TPFLAGS_INLINE_VALUES)
- This bit indicates that instances of this type will have an “inline values” array (containing the object’s attributes) placed directly after the end of the object. - This requires that - `Py_TPFLAGS_HAVE_GC`- **Inheritance:**- This flag is not inherited. - Added in version 3.13. 
 - 
Py_TPFLAGS_IS_ABSTRACT[¶](#c.Py_TPFLAGS_IS_ABSTRACT)
- This bit indicates that this is an abstract type and therefore cannot be instantiated. - **Inheritance:**- This flag is not inherited. - See also 
 - 
Py_TPFLAGS_HAVE_STACKLESS_EXTENSION[¶](#c.Py_TPFLAGS_HAVE_STACKLESS_EXTENSION)
- Internal. Do not set or unset this flag. Historically, this was a reserved flag for use in Stackless Python. - Warning - This flag is present in header files, but is not be used. This may be removed in a future version of CPython. 
 
- 
Py_TPFLAGS_HEAPTYPE

- 
const char *[PyTypeObject](type.html#c.PyTypeObject).tp_doc[¶](#c.PyTypeObject.tp_doc)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_doc`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a NUL-terminated C string giving the docstring for this type object. This is exposed as the - `__doc__`- **Inheritance:**- This field is - *not*inherited by subtypes.

- 
[traverseproc](gcsupport.html#c.traverseproc)[PyTypeObject](type.html#c.PyTypeObject).tp_traverse[¶](#c.PyTypeObject.tp_traverse)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_traverse`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a traversal function for the garbage collector. This is only used if the - `Py_TPFLAGS_HAVE_GC`- int tp_traverse(PyObject *self, visitproc visit, void *arg); - More information about Python’s garbage collection scheme can be found in section - [Supporting Cyclic Garbage Collection](gcsupport.html#supporting-cycle-detection).- The - `tp_traverse`- `tp_traverse`function simply calls- `Py_VISIT()`- `local_traverse()`from the- `_thread`extension module:- static int local_traverse(PyObject *op, visitproc visit, void *arg) { localobject *self = (localobject *) op; Py_VISIT(self->args); Py_VISIT(self->kw); Py_VISIT(self->dict); return 0; } - Note that - `Py_VISIT()`- `self->key`member, it can only be- `NULL`or a Python string and therefore cannot be part of a reference cycle.- On the other hand, even if you know a member can never be part of a cycle, as a debugging aid you may want to visit it anyway just so the - `gc`- `get_referents()`- Heap types ( - `Py_TPFLAGS_HEAPTYPE`- Py_VISIT(Py_TYPE(self)); - It is only needed since Python 3.9. To support Python 3.8 and older, this line must be conditional: - #if PY_VERSION_HEX >= 0x03090000 Py_VISIT(Py_TYPE(self)); #endif - If the - `Py_TPFLAGS_MANAGED_DICT`- `tp_flags`- `PyObject_VisitManagedDict()`- PyObject_VisitManagedDict((PyObject*)self, visit, arg); - Warning - When implementing - `tp_traverse`- *owns*(by having- [strong references](../glossary.html#term-strong-reference)to them) must be visited. For instance, if an object supports weak references via the- `tp_weaklist`- *tp_weaklist*points to) must- **not**be visited as the instance does not directly own the weak references to itself (the weakreference list is there to support the weak reference machinery, but the instance has no strong reference to the elements inside it, as they are allowed to be removed even if the instance is still alive).- Warning - The traversal function must not have any side effects. It must not modify the reference counts of any Python objects nor create or destroy any Python objects. - Note that - `Py_VISIT()`- *visit*and- *arg*parameters to- `local_traverse()`to have these specific names; don’t name them just anything.- Instances of - [heap-allocated types](#heap-types)hold a reference to their type. Their traversal function must therefore either visit- `Py_TYPE(self)`- `tp_traverse`of another heap-allocated type (such as a heap-allocated superclass). If they do not, the type object may not be garbage-collected.- Note - The - `tp_traverse`- Changed in version 3.9: Heap-allocated types are expected to visit - `Py_TYPE(self)`in- `tp_traverse`. In earlier versions of Python, due to- [bug 40217](https://bugs.python.org/issue40217), doing this may lead to crashes in subclasses.- **Inheritance:**- Group: - `Py_TPFLAGS_HAVE_GC`- `tp_traverse`- `tp_clear`- This field is inherited by subtypes together with - `tp_clear`- `Py_TPFLAGS_HAVE_GC`- `tp_traverse`- `tp_clear`are all inherited from the base type if they are all zero in the subtype.

- 
[inquiry](gcsupport.html#c.inquiry)[PyTypeObject](type.html#c.PyTypeObject).tp_clear[¶](#c.PyTypeObject.tp_clear)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_clear`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a clear function. The signature is: - int tp_clear(PyObject *); - The purpose of this function is to break reference cycles that are causing a - [cyclic isolate](../glossary.html#term-cyclic-isolate)so that the objects can be safely destroyed. A cleared object is a partially destroyed object; the object is not obligated to satisfy design invariants held during normal use.- `tp_clear`does not need to delete references to objects that can’t participate in reference cycles, such as Python strings or Python integers. However, it may be convenient to clear all references, and write the type’s- `tp_dealloc`- `tp_clear`to avoid code duplication. (Beware that- `tp_clear`might have already been called. Prefer calling idempotent functions like- `Py_CLEAR()`- Any non-trivial cleanup should be performed in - `tp_finalize`- `tp_clear`.- Note - If - `tp_clear`fails to break a reference cycle then the objects in the- [cyclic isolate](../glossary.html#term-cyclic-isolate)may remain indefinitely uncollectable (“leak”). See- `gc.garbage`- Note - Referents (direct and indirect) might have already been cleared; they are not guaranteed to be in a consistent state. - Note - The - `tp_clear`- Note - An object is not guaranteed to be automatically cleared before its destructor ( - `tp_dealloc`- This function differs from the destructor ( - `tp_dealloc`- The purpose of clearing an object is to remove references to other objects that might participate in a reference cycle. The purpose of the destructor, on the other hand, is a superset: it must release - *all*resources it owns, including references to objects that cannot participate in a reference cycle (e.g., integers) as well as the object’s own memory (by calling- `tp_free`
- When - `tp_clear`is called, other objects might still hold references to the object being cleared. Because of this,- `tp_clear`must not deallocate the object’s own memory (- `tp_free`
- `tp_clear`might never be automatically called. An object’s destructor, on the other hand, will be automatically called some time after the object becomes unreachable (i.e., either there are no references to the object or the object is a member of a- [cyclic isolate](../glossary.html#term-cyclic-isolate)).
 - No guarantees are made about when, if, or how often Python automatically clears an object, except: - Python will not automatically clear an object if it is reachable, i.e., there is a reference to it and it is not a member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate).
- Python will not automatically clear an object if it has not been automatically finalized (see - `tp_finalize`
- If an object is a member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate), Python will not automatically clear it if any member of the cyclic isolate has not yet been automatically finalized (- `tp_finalize`
- Python will not destroy an object until after any automatic calls to its - `tp_clear`function have returned. This ensures that the act of breaking a reference cycle does not invalidate the- `self`pointer while- `tp_clear`is still executing.
- Python will not automatically call - `tp_clear`multiple times concurrently.
 - CPython currently only automatically clears objects as needed to break reference cycles in a - [cyclic isolate](../glossary.html#term-cyclic-isolate), but future versions might clear objects regularly before their destruction.- Taken together, all - `tp_clear`- `tp_clear`function. For example, the tuple type does not implement a- `tp_clear`function, because it’s possible to prove that no reference cycle can be composed entirely of tuples. Therefore the- `tp_clear`functions of other types are responsible for breaking any cycle containing a tuple. This isn’t immediately obvious, and there’s rarely a good reason to avoid implementing- `tp_clear`.- Implementations of - `tp_clear`- `NULL`, as in the following example:- static int local_clear(PyObject *op) { localobject *self = (localobject *) op; Py_CLEAR(self->key); Py_CLEAR(self->args); Py_CLEAR(self->kw); Py_CLEAR(self->dict); return 0; } - The - `Py_CLEAR()`- `Py_DECREF()`- `NULL`. This is because releasing the reference may cause the contained object to become trash, triggering a chain of reclamation activity that may include invoking arbitrary Python code (due to finalizers, or weakref callbacks, associated with the contained object). If it’s possible for such code to reference- *self*again, it’s important that the pointer to the contained object be- `NULL`at that time, so that- *self*knows the contained object can no longer be used. The- `Py_CLEAR()`macro performs the operations in a safe order.- If the - `Py_TPFLAGS_MANAGED_DICT`- `tp_flags`- `PyObject_ClearManagedDict()`- PyObject_ClearManagedDict((PyObject*)self); - More information about Python’s garbage collection scheme can be found in section - [Supporting Cyclic Garbage Collection](gcsupport.html#supporting-cycle-detection).- **Inheritance:**- Group: - `Py_TPFLAGS_HAVE_GC`- `tp_traverse`- `tp_clear`- This field is inherited by subtypes together with - `tp_traverse`- `Py_TPFLAGS_HAVE_GC`- `tp_traverse`, and- `tp_clear`- See also - [Object Life Cycle](lifecycle.html#life-cycle)for details about how this slot relates to other slots.

- 
[richcmpfunc](#c.richcmpfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_richcompare[¶](#c.PyTypeObject.tp_richcompare)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_richcompare`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to the rich comparison function, whose signature is: - PyObject *tp_richcompare(PyObject *self, PyObject *other, int op); - The first parameter is guaranteed to be an instance of the type that is defined by - `PyTypeObject`- The function should return the result of the comparison (usually - `Py_True`or- `Py_False`). If the comparison is undefined, it must return- `Py_NotImplemented`, if another error occurred it must return- `NULL`and set an exception condition.- The following constants are defined to be used as the third argument for - `tp_richcompare`- `PyObject_RichCompare()`- The following macro is defined to ease writing rich comparison functions: - 
Py_RETURN_RICHCOMPARE(VAL_A, VAL_B, op)[¶](#c.Py_RETURN_RICHCOMPARE)
- Return - `Py_True`or- `Py_False`from the function, depending on the result of a comparison. VAL_A and VAL_B must be orderable by C comparison operators (for example, they may be C ints or floats). The third argument specifies the requested operation, as for- `PyObject_RichCompare()`- The returned value is a new - [strong reference](../glossary.html#term-strong-reference).- On error, sets an exception and returns - `NULL`from the function.- Added in version 3.7. 
 - **Inheritance:**- Group: - `tp_hash`- `tp_richcompare`- This field is inherited by subtypes together with - `tp_hash`- `tp_richcompare`- `tp_hash`when the subtype’s- `tp_richcompare`and- `tp_hash`are both- `NULL`.- **Default:**- `PyBaseObject_Type`- `tp_richcompare`- `tp_hash`
- 
Py_RETURN_RICHCOMPARE(VAL_A, VAL_B, op)

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)[PyTypeObject](type.html#c.PyTypeObject).tp_weaklistoffset[¶](#c.PyTypeObject.tp_weaklistoffset)
- While this field is still supported, - `Py_TPFLAGS_MANAGED_WEAKREF`- If the instances of this type are weakly referenceable, this field is greater than zero and contains the offset in the instance structure of the weak reference list head (ignoring the GC header, if present); this offset is used by - `PyObject_ClearWeakRefs()`- `PyWeakref_*`functions. The instance structure needs to include a field of type- [PyObject](structures.html#c.PyObject)* which is initialized to- `NULL`.- Do not confuse this field with - `tp_weaklist`- It is an error to set both the - `Py_TPFLAGS_MANAGED_WEAKREF`- `tp_weaklistoffset`- **Inheritance:**- This field is inherited by subtypes, but see the rules listed below. A subtype may override this offset; this means that the subtype uses a different weak reference list head than the base type. Since the list head is always found via - `tp_weaklistoffset`- **Default:**- If the - `Py_TPFLAGS_MANAGED_WEAKREF`- `tp_flags`- `tp_weaklistoffset`

- 
[getiterfunc](#c.getiterfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_iter[¶](#c.PyTypeObject.tp_iter)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_iter`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function that returns an - [iterator](../glossary.html#term-iterator)for the object. Its presence normally signals that the instances of this type are- [iterable](../glossary.html#term-iterable)(although sequences may be iterable without this function).- This function has the same signature as - `PyObject_GetIter()`- PyObject *tp_iter(PyObject *self); - **Inheritance:**- This field is inherited by subtypes. 

- 
[iternextfunc](#c.iternextfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_iternext[¶](#c.PyTypeObject.tp_iternext)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_iternext`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function that returns the next item in an - [iterator](../glossary.html#term-iterator). The signature is:- PyObject *tp_iternext(PyObject *self); - When the iterator is exhausted, it must return - `NULL`; a- `StopIteration`- `NULL`too. Its presence signals that the instances of this type are iterators.- Iterator types should also define the - `tp_iter`- This function has the same signature as - `PyIter_Next()`- **Inheritance:**- This field is inherited by subtypes. 

- 
struct [PyMethodDef](structures.html#c.PyMethodDef)*[PyTypeObject](type.html#c.PyTypeObject).tp_methods[¶](#c.PyTypeObject.tp_methods)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_methods`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a static - `NULL`-terminated array of- `PyMethodDef`- For each entry in the array, an entry is added to the type’s dictionary (see - `tp_dict`- **Inheritance:**- This field is not inherited by subtypes (methods are inherited through a different mechanism). 

- 
struct [PyMemberDef](structures.html#c.PyMemberDef)*[PyTypeObject](type.html#c.PyTypeObject).tp_members[¶](#c.PyTypeObject.tp_members)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_members`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a static - `NULL`-terminated array of- `PyMemberDef`- For each entry in the array, an entry is added to the type’s dictionary (see - `tp_dict`- **Inheritance:**- This field is not inherited by subtypes (members are inherited through a different mechanism). 

- 
struct [PyGetSetDef](structures.html#c.PyGetSetDef)*[PyTypeObject](type.html#c.PyTypeObject).tp_getset[¶](#c.PyTypeObject.tp_getset)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_getset`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a static - `NULL`-terminated array of- `PyGetSetDef`- For each entry in the array, an entry is added to the type’s dictionary (see - `tp_dict`- **Inheritance:**- This field is not inherited by subtypes (computed attributes are inherited through a different mechanism). 

- 
[PyTypeObject](type.html#c.PyTypeObject)*[PyTypeObject](type.html#c.PyTypeObject).tp_base[¶](#c.PyTypeObject.tp_base)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_base`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a base type from which type properties are inherited. At this level, only single inheritance is supported; multiple inheritance require dynamically creating a type object by calling the metatype. - Note - Slot initialization is subject to the rules of initializing globals. C99 requires the initializers to be “address constants”. Function designators like - `PyType_GenericNew()`- However, the unary ‘&’ operator applied to a non-static variable like - `PyBaseObject_Type`- Consequently, - `tp_base`- **Inheritance:**- This field is not inherited by subtypes (obviously). - **Default:**- This field defaults to - `&PyBaseObject_Type`(which to Python programmers is known as the type- `object`

- 
[PyObject](structures.html#c.PyObject)*[PyTypeObject](type.html#c.PyTypeObject).tp_dict[¶](#c.PyTypeObject.tp_dict)
- The type’s dictionary is stored here by - `PyType_Ready()`- This field should normally be initialized to - `NULL`before PyType_Ready is called; it may also be initialized to a dictionary containing initial attributes for the type. Once- `PyType_Ready()`- `__add__()`- Some types may not store their dictionary in this slot. Use - `PyType_GetDict()`- Changed in version 3.12: Internals detail: For static builtin types, this is always - `NULL`. Instead, the dict for such types is stored on- `PyInterpreterState`. Use- `PyType_GetDict()`- **Inheritance:**- This field is not inherited by subtypes (though the attributes defined in here are inherited through a different mechanism). - **Default:**- If this field is - `NULL`,- `PyType_Ready()`- Warning - It is not safe to use - `PyDict_SetItem()`- `tp_dict`

- 
[descrgetfunc](#c.descrgetfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_descr_get[¶](#c.PyTypeObject.tp_descr_get)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_descr_get`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a “descriptor get” function. - The function signature is: - PyObject * tp_descr_get(PyObject *self, PyObject *obj, PyObject *type); - **Inheritance:**- This field is inherited by subtypes. 

- 
[descrsetfunc](#c.descrsetfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_descr_set[¶](#c.PyTypeObject.tp_descr_set)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_descr_set`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function for setting and deleting a descriptor’s value. - The function signature is: - int tp_descr_set(PyObject *self, PyObject *obj, PyObject *value); - The - *value*argument is set to- `NULL`to delete the value.- **Inheritance:**- This field is inherited by subtypes. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)[PyTypeObject](type.html#c.PyTypeObject).tp_dictoffset[¶](#c.PyTypeObject.tp_dictoffset)
- While this field is still supported, - `Py_TPFLAGS_MANAGED_DICT`- If the instances of this type have a dictionary containing instance variables, this field is non-zero and contains the offset in the instances of the type of the instance variable dictionary; this offset is used by - `PyObject_GenericGetAttr()`- Do not confuse this field with - `tp_dict`- The value specifies the offset of the dictionary from the start of the instance structure. - The - `tp_dictoffset`- `PyObject_GenericGetDict()`- `PyObject_GenericGetDict()`may need to allocate memory for the dictionary, so it is may be more efficient to call- `PyObject_GetAttr()`- It is an error to set both the - `Py_TPFLAGS_MANAGED_DICT`- `tp_dictoffset`- **Inheritance:**- This field is inherited by subtypes. A subtype should not override this offset; doing so could be unsafe, if C code tries to access the dictionary at the previous offset. To properly support inheritance, use - `Py_TPFLAGS_MANAGED_DICT`- **Default:**- This slot has no default. For - [static types](#static-types), if the field is- `NULL`then no- `__dict__`- If the - `Py_TPFLAGS_MANAGED_DICT`- `tp_flags`- `tp_dictoffset`- `-1`, to indicate that it is unsafe to use this field.

- 
[initproc](#c.initproc)[PyTypeObject](type.html#c.PyTypeObject).tp_init[¶](#c.PyTypeObject.tp_init)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_init`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to an instance initialization function. - This function corresponds to the - `__init__()`- `__init__()`, it is possible to create an instance without calling- `__init__()`, and it is possible to reinitialize an instance by calling its- `__init__()`method again.- The function signature is: - int tp_init(PyObject *self, PyObject *args, PyObject *kwds); - The self argument is the instance to be initialized; the - *args*and- *kwds*arguments represent positional and keyword arguments of the call to- `__init__()`- The - `tp_init`- `NULL`, is called when an instance is created normally by calling its type, after the type’s- `tp_new`- `tp_new`function returns an instance of some other type that is not a subtype of the original type, no- `tp_init`function is called; if- `tp_new`returns an instance of a subtype of the original type, the subtype’s- `tp_init`is called.- Returns - `0`on success,- `-1`and sets an exception on error.- **Inheritance:**- This field is inherited by subtypes. - **Default:**- For - [static types](#static-types)this field does not have a default.

- 
[allocfunc](#c.allocfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_alloc[¶](#c.PyTypeObject.tp_alloc)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_alloc`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to an instance allocation function. - The function signature is: - PyObject *tp_alloc(PyTypeObject *self, Py_ssize_t nitems); - **Inheritance:**- Static subtypes inherit this slot, which will be - `PyType_GenericAlloc()`- `object`- [Heap subtypes](#heap-types)do not inherit this slot.- **Default:**- For heap subtypes, this field is always set to - `PyType_GenericAlloc()`- For static subtypes, this slot is inherited (see above). 

- 
[newfunc](#c.newfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_new[¶](#c.PyTypeObject.tp_new)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_new`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to an instance creation function. - The function signature is: - PyObject *tp_new(PyTypeObject *subtype, PyObject *args, PyObject *kwds); - The - *subtype*argument is the type of the object being created; the- *args*and- *kwds*arguments represent positional and keyword arguments of the call to the type. Note that- *subtype*doesn’t have to equal the type whose- `tp_new`- The - `tp_new`- `subtype->tp_alloc(subtype, nitems)`to allocate space for the object, and then do only as much further initialization as is absolutely necessary. Initialization that can safely be ignored or repeated should be placed in the- `tp_init`- `tp_new`, while for mutable types, most initialization should be deferred to- `tp_init`.- Set the - `Py_TPFLAGS_DISALLOW_INSTANTIATION`- **Inheritance:**- This field is inherited by subtypes, except it is not inherited by - [static types](#static-types)whose- `tp_base`- `NULL`or- `&PyBaseObject_Type`.- **Default:**- For - [static types](#static-types)this field has no default. This means if the slot is defined as- `NULL`, the type cannot be called to create new instances; presumably there is some other way to create instances, like a factory function.

- 
[freefunc](#c.freefunc)[PyTypeObject](type.html#c.PyTypeObject).tp_free[¶](#c.PyTypeObject.tp_free)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_free`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to an instance deallocation function. Its signature is: - void tp_free(void *self); - This function must free the memory allocated by - `tp_alloc`- **Inheritance:**- Static subtypes inherit this slot, which will be - `PyObject_Free()`- `object`- `Py_TPFLAGS_HAVE_GC`- `tp_flags`- `PyObject_Free()`, then this slot is not inherited but instead defaults to- `PyObject_GC_Del()`- [Heap subtypes](#heap-types)do not inherit this slot.- **Default:**- For - [heap subtypes](#heap-types), this slot defaults to a deallocator suitable to match- `PyType_GenericAlloc()`- `Py_TPFLAGS_HAVE_GC`- For static subtypes, this slot is inherited (see above). 

- 
[inquiry](gcsupport.html#c.inquiry)[PyTypeObject](type.html#c.PyTypeObject).tp_is_gc[¶](#c.PyTypeObject.tp_is_gc)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_is_gc`is part of the- [Stable ABI](stable.html#stable).- An optional pointer to a function called by the garbage collector. - The garbage collector needs to know whether a particular object is collectible or not. Normally, it is sufficient to look at the object’s type’s - `tp_flags`- `Py_TPFLAGS_HAVE_GC`- `1`for a collectible instance, and- `0`for a non-collectible instance. The signature is:- int tp_is_gc(PyObject *self); - (The only example of this are types themselves. The metatype, - `PyType_Type`- [dynamically allocated types](#heap-types).)- **Inheritance:**- This field is inherited by subtypes. - **Default:**- This slot has no default. If this field is - `NULL`,- `Py_TPFLAGS_HAVE_GC`

- 
[PyObject](structures.html#c.PyObject)*[PyTypeObject](type.html#c.PyTypeObject).tp_bases[¶](#c.PyTypeObject.tp_bases)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_bases`is part of the- [Stable ABI](stable.html#stable).- Tuple of base types. - This field should be set to - `NULL`and treated as read-only. Python will fill it in when the type is- `initialized`- For dynamically created classes, the - `Py_tp_bases`- `slot`- *bases*argument of- `PyType_FromSpecWithBases()`- Warning - Multiple inheritance does not work well for statically defined types. If you set - `tp_bases`to a tuple, Python will not raise an error, but some slots will only be inherited from the first base.- **Inheritance:**- This field is not inherited. 

- 
[PyObject](structures.html#c.PyObject)*[PyTypeObject](type.html#c.PyTypeObject).tp_mro[¶](#c.PyTypeObject.tp_mro)
- Tuple containing the expanded set of base types, starting with the type itself and ending with - `object`- This field should be set to - `NULL`and treated as read-only. Python will fill it in when the type is- `initialized`- **Inheritance:**- This field is not inherited; it is calculated fresh by - `PyType_Ready()`

- 
[PyObject](structures.html#c.PyObject)*[PyTypeObject](type.html#c.PyTypeObject).tp_cache[¶](#c.PyTypeObject.tp_cache)
- Unused. Internal use only. - **Inheritance:**- This field is not inherited. 

- 
void *[PyTypeObject](type.html#c.PyTypeObject).tp_subclasses[¶](#c.PyTypeObject.tp_subclasses)
- A collection of subclasses. Internal use only. May be an invalid pointer. - To get a list of subclasses, call the Python method - `__subclasses__()`- Changed in version 3.12: For some types, this field does not hold a valid - [PyObject](structures.html#c.PyObject)*. The type was changed to void* to indicate this.- **Inheritance:**- This field is not inherited. 

- 
[PyObject](structures.html#c.PyObject)*[PyTypeObject](type.html#c.PyTypeObject).tp_weaklist[¶](#c.PyTypeObject.tp_weaklist)
- Weak reference list head, for weak references to this type object. Not inherited. Internal use only. - Changed in version 3.12: Internals detail: For the static builtin types this is always - `NULL`, even if weakrefs are added. Instead, the weakrefs for each are stored on- `PyInterpreterState`. Use the public C-API or the internal- `_PyObject_GET_WEAKREFS_LISTPTR()`macro to avoid the distinction.- **Inheritance:**- This field is not inherited. 

- 
[destructor](#c.destructor)[PyTypeObject](type.html#c.PyTypeObject).tp_del[¶](#c.PyTypeObject.tp_del)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_del`is part of the- [Stable ABI](stable.html#stable).- This field is deprecated. Use - `tp_finalize`

- 
unsigned int [PyTypeObject](type.html#c.PyTypeObject).tp_version_tag[¶](#c.PyTypeObject.tp_version_tag)
- Used to index into the method cache. Internal use only. - **Inheritance:**- This field is not inherited. 

- 
[destructor](#c.destructor)[PyTypeObject](type.html#c.PyTypeObject).tp_finalize[¶](#c.PyTypeObject.tp_finalize)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_finalize`is part of the- [Stable ABI](stable.html#stable)since version 3.5.- An optional pointer to an instance finalization function. This is the C implementation of the - `__del__()`- void tp_finalize(PyObject *self); - The primary purpose of finalization is to perform any non-trivial cleanup that must be performed before the object is destroyed, while the object and any other objects it directly or indirectly references are still in a consistent state. The finalizer is allowed to execute arbitrary Python code. - Before Python automatically finalizes an object, some of the object’s direct or indirect referents might have themselves been automatically finalized. However, none of the referents will have been automatically cleared ( - `tp_clear`- Other non-finalized objects might still be using a finalized object, so the finalizer must leave the object in a sane state (e.g., invariants are still met). - Note - After Python automatically finalizes an object, Python might start automatically clearing ( - `tp_clear`- Note - An object is not guaranteed to be automatically finalized before its destructor ( - `tp_dealloc`- `PyObject_CallFinalizerFromDealloc()`- `tp_dealloc`to guarantee that the object is always finalized before destruction.- Note - The - `tp_finalize`- [GIL](../glossary.html#term-GIL)will be held.- Note - The - `tp_finalize`function can be called during shutdown, after some global variables have been deleted. See the documentation of the- `__del__()`- When Python finalizes an object, it behaves like the following algorithm: - Python might mark the object as - *finalized*. Currently, Python always marks objects whose type supports garbage collection (i.e., the- `Py_TPFLAGS_HAVE_GC`- `tp_flags`
- If the object is not marked as - *finalized*and its- `tp_finalize`finalizer function is non-- `NULL`, the finalizer function is called.
- If the finalizer function was called and the finalizer made the object reachable (i.e., there is a reference to the object and it is not a member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate)), then the finalizer is said to have- *resurrected*the object. It is unspecified whether the finalizer can also resurrect the object by adding a new reference to the object that does not make it reachable, i.e., the object is (still) a member of a cyclic isolate.
- If the finalizer resurrected the object, the object’s pending destruction is canceled and the object’s - *finalized*mark might be removed if present. Currently, Python never removes the- *finalized*mark; this might change in a future version.
 - *Automatic finalization*refers to any finalization performed by Python except via calls to- `PyObject_CallFinalizer()`- `PyObject_CallFinalizerFromDealloc()`- Python will not automatically finalize an object if it is reachable, i.e., there is a reference to it and it is not a member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate).
- Python will not automatically finalize an object if finalizing it would not mark the object as - *finalized*. Currently, this applies to objects whose type does not support garbage collection, i.e., the- `Py_TPFLAGS_HAVE_GC`- `PyObject_CallFinalizer()`- `PyObject_CallFinalizerFromDealloc()`
- Python will not automatically finalize any two members of a - [cyclic isolate](../glossary.html#term-cyclic-isolate)concurrently.
- Python will not automatically finalize an object after it has automatically cleared ( - `tp_clear`
- If an object is a member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate), Python will not automatically finalize it after automatically clearing (see- `tp_clear`
- Python will automatically finalize every member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate)before it automatically clears (see- `tp_clear`
- If Python is going to automatically clear an object ( - `tp_clear`
 - Python currently only automatically finalizes objects that are members of a - [cyclic isolate](../glossary.html#term-cyclic-isolate), but future versions might finalize objects regularly before their destruction.- To manually finalize an object, do not call this function directly; call - `PyObject_CallFinalizer()`- `PyObject_CallFinalizerFromDealloc()`- `tp_finalize`- `PyErr_GetRaisedException()`- `PyErr_SetRaisedException()`- `PyErr_WriteUnraisable()`- `PyErr_FormatUnraisable()`- static void foo_finalize(PyObject *self) { // Save the current exception, if any. PyObject *exc = PyErr_GetRaisedException(); // ... if (do_something_that_might_raise() != success_indicator) { PyErr_WriteUnraisable(self); goto done; } done: // Restore the saved exception. This silently discards any exception // raised above, so be sure to call PyErr_WriteUnraisable first if // necessary. PyErr_SetRaisedException(exc); } - **Inheritance:**- This field is inherited by subtypes. - Added in version 3.4. - Changed in version 3.8: Before version 3.8 it was necessary to set the - `Py_TPFLAGS_HAVE_FINALIZE`- See also - **PEP 442**
- [Object Life Cycle](lifecycle.html#life-cycle)for details about how this slot relates to other slots.
 

- 
[vectorcallfunc](call.html#c.vectorcallfunc)[PyTypeObject](type.html#c.PyTypeObject).tp_vectorcall[¶](#c.PyTypeObject.tp_vectorcall)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_tp_vectorcall`is part of the- [Stable ABI](stable.html#stable)since version 3.14.- A - [vectorcall function](call.html#vectorcall)to use for calls of this type object (rather than instances). In other words,- `tp_vectorcall`can be used to optimize- `type.__call__`, which typically returns a new instance of- *type*.- As with any vectorcall function, if - `tp_vectorcall`is- `NULL`, the- *tp_call*protocol (- `Py_TYPE(type)->tp_call`) is used instead.- Note - The - [vectorcall protocol](call.html#vectorcall)requires that the vectorcall function has the same behavior as the corresponding- `tp_call`. This means that- `type->tp_vectorcall`must match the behavior of- `Py_TYPE(type)->tp_call`.- Specifically, if - *type*uses the default metaclass,- `type->tp_vectorcall`must behave the same as- [PyType_Type](type.html#c.PyType_Type)->tp_call, which:- calls - `type->tp_new`,
- if the result is a subclass of - *type*, calls- `type->tp_init`on the result of- `tp_new`, and
- returns the result of - `tp_new`.
 - Typically, - `tp_vectorcall`is overridden to optimize this process for specific- `tp_new`- `tp_init`- `__new__()`- `__init__()`- **Inheritance:**- This field is never inherited. - Added in version 3.9: (the field exists since 3.8 but it’s only used since 3.9) 

- 
unsigned char [PyTypeObject](type.html#c.PyTypeObject).tp_watched[¶](#c.PyTypeObject.tp_watched)
- Internal. Do not use. - Added in version 3.12. 

## Static Types[¶](#static-types)

Traditionally, types defined in C code are *static*, that is,
a static [ PyTypeObject](type.html#c.PyTypeObject) structure is defined directly in code
and initialized using 

[.](type.html#c.PyType_Ready)

`PyType_Ready()`This results in types that are limited relative to types defined in Python:

- Static types are limited to one base, i.e. they cannot use multiple inheritance. 
- Static type objects (but not necessarily their instances) are immutable. It is not possible to add or modify the type object’s attributes from Python. 
- Static type objects are shared across - [sub-interpreters](subinterpreters.html#sub-interpreter-support), so they should not include any subinterpreter-specific state.

Also, since [ PyTypeObject](type.html#c.PyTypeObject) is only part of the 

[Limited API](stable.html#limited-c-api)as an opaque struct, any extension modules using static types must be compiled for a specific Python minor version.

## Heap Types[¶](#heap-types)

An alternative to [static types](#static-types) is *heap-allocated types*,
or *heap types* for short, which correspond closely to classes created by
Python’s `class` statement. Heap types have the [ Py_TPFLAGS_HEAPTYPE](#c.Py_TPFLAGS_HEAPTYPE)
flag set.

This is done by filling a [ PyType_Spec](type.html#c.PyType_Spec) structure and calling

[,](type.html#c.PyType_FromSpec)

`PyType_FromSpec()`[,](type.html#c.PyType_FromSpecWithBases)

`PyType_FromSpecWithBases()`[, or](type.html#c.PyType_FromModuleAndSpec)

`PyType_FromModuleAndSpec()`[.](type.html#c.PyType_FromMetaclass)

`PyType_FromMetaclass()`## Number Object Structures[¶](#number-object-structures)

- 
type PyNumberMethods[¶](#c.PyNumberMethods)
- This structure holds pointers to the functions which an object uses to implement the number protocol. Each function is used by the function of similar name documented in the - [Number Protocol](number.html#number)section.- Here is the structure definition: - typedef struct { binaryfunc nb_add; binaryfunc nb_subtract; binaryfunc nb_multiply; binaryfunc nb_remainder; binaryfunc nb_divmod; ternaryfunc nb_power; unaryfunc nb_negative; unaryfunc nb_positive; unaryfunc nb_absolute; inquiry nb_bool; unaryfunc nb_invert; binaryfunc nb_lshift; binaryfunc nb_rshift; binaryfunc nb_and; binaryfunc nb_xor; binaryfunc nb_or; unaryfunc nb_int; void *nb_reserved; unaryfunc nb_float; binaryfunc nb_inplace_add; binaryfunc nb_inplace_subtract; binaryfunc nb_inplace_multiply; binaryfunc nb_inplace_remainder; ternaryfunc nb_inplace_power; binaryfunc nb_inplace_lshift; binaryfunc nb_inplace_rshift; binaryfunc nb_inplace_and; binaryfunc nb_inplace_xor; binaryfunc nb_inplace_or; binaryfunc nb_floor_divide; binaryfunc nb_true_divide; binaryfunc nb_inplace_floor_divide; binaryfunc nb_inplace_true_divide; unaryfunc nb_index; binaryfunc nb_matrix_multiply; binaryfunc nb_inplace_matrix_multiply; } PyNumberMethods; - Note - Binary and ternary functions must check the type of all their operands, and implement the necessary conversions (at least one of the operands is an instance of the defined type). If the operation is not defined for the given operands, binary and ternary functions must return - `Py_NotImplemented`, if another error occurred they must return- `NULL`and set an exception.- Note - The - `nb_reserved`- `NULL`. It was previously called- `nb_long`, and was renamed in Python 3.0.1.

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_add[¶](#c.PyNumberMethods.nb_add)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_add`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_subtract[¶](#c.PyNumberMethods.nb_subtract)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_subtract`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_multiply[¶](#c.PyNumberMethods.nb_multiply)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_multiply`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_remainder[¶](#c.PyNumberMethods.nb_remainder)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_remainder`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_divmod[¶](#c.PyNumberMethods.nb_divmod)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_divmod`is part of the- [Stable ABI](stable.html#stable).

- 
[ternaryfunc](#c.ternaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_power[¶](#c.PyNumberMethods.nb_power)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_power`is part of the- [Stable ABI](stable.html#stable).

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_negative[¶](#c.PyNumberMethods.nb_negative)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_negative`is part of the- [Stable ABI](stable.html#stable).

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_positive[¶](#c.PyNumberMethods.nb_positive)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_positive`is part of the- [Stable ABI](stable.html#stable).

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_absolute[¶](#c.PyNumberMethods.nb_absolute)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_absolute`is part of the- [Stable ABI](stable.html#stable).

- 
[inquiry](gcsupport.html#c.inquiry)[PyNumberMethods](#c.PyNumberMethods).nb_bool[¶](#c.PyNumberMethods.nb_bool)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_bool`is part of the- [Stable ABI](stable.html#stable).

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_invert[¶](#c.PyNumberMethods.nb_invert)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_invert`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_lshift[¶](#c.PyNumberMethods.nb_lshift)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_lshift`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_rshift[¶](#c.PyNumberMethods.nb_rshift)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_rshift`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_and[¶](#c.PyNumberMethods.nb_and)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_and`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_xor[¶](#c.PyNumberMethods.nb_xor)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_xor`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_or[¶](#c.PyNumberMethods.nb_or)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_or`is part of the- [Stable ABI](stable.html#stable).

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_int[¶](#c.PyNumberMethods.nb_int)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_int`is part of the- [Stable ABI](stable.html#stable).

- 
void *[PyNumberMethods](#c.PyNumberMethods).nb_reserved[¶](#c.PyNumberMethods.nb_reserved)

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_float[¶](#c.PyNumberMethods.nb_float)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_float`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_add[¶](#c.PyNumberMethods.nb_inplace_add)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_add`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_subtract[¶](#c.PyNumberMethods.nb_inplace_subtract)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_subtract`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_multiply[¶](#c.PyNumberMethods.nb_inplace_multiply)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_multiply`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_remainder[¶](#c.PyNumberMethods.nb_inplace_remainder)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_remainder`is part of the- [Stable ABI](stable.html#stable).

- 
[ternaryfunc](#c.ternaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_power[¶](#c.PyNumberMethods.nb_inplace_power)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_power`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_lshift[¶](#c.PyNumberMethods.nb_inplace_lshift)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_lshift`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_rshift[¶](#c.PyNumberMethods.nb_inplace_rshift)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_rshift`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_and[¶](#c.PyNumberMethods.nb_inplace_and)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_and`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_xor[¶](#c.PyNumberMethods.nb_inplace_xor)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_xor`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_or[¶](#c.PyNumberMethods.nb_inplace_or)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_or`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_floor_divide[¶](#c.PyNumberMethods.nb_floor_divide)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_floor_divide`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_true_divide[¶](#c.PyNumberMethods.nb_true_divide)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_true_divide`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_floor_divide[¶](#c.PyNumberMethods.nb_inplace_floor_divide)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_floor_divide`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_true_divide[¶](#c.PyNumberMethods.nb_inplace_true_divide)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_true_divide`is part of the- [Stable ABI](stable.html#stable).

- 
[unaryfunc](#c.unaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_index[¶](#c.PyNumberMethods.nb_index)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_index`is part of the- [Stable ABI](stable.html#stable).

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_matrix_multiply[¶](#c.PyNumberMethods.nb_matrix_multiply)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_matrix_multiply`is part of the- [Stable ABI](stable.html#stable)since version 3.5.

- 
[binaryfunc](#c.binaryfunc)[PyNumberMethods](#c.PyNumberMethods).nb_inplace_matrix_multiply[¶](#c.PyNumberMethods.nb_inplace_matrix_multiply)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_nb_inplace_matrix_multiply`is part of the- [Stable ABI](stable.html#stable)since version 3.5.

## Mapping Object Structures[¶](#mapping-object-structures)

- 
type PyMappingMethods[¶](#c.PyMappingMethods)
- This structure holds pointers to the functions which an object uses to implement the mapping protocol. It has three members: 

- 
[lenfunc](#c.lenfunc)[PyMappingMethods](#c.PyMappingMethods).mp_length[¶](#c.PyMappingMethods.mp_length)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_mp_length`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PyMapping_Size()`- `PyObject_Size()`- `NULL`if the object has no defined length.

- 
[binaryfunc](#c.binaryfunc)[PyMappingMethods](#c.PyMappingMethods).mp_subscript[¶](#c.PyMappingMethods.mp_subscript)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_mp_subscript`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PyObject_GetItem()`- `PySequence_GetSlice()`- `PyObject_GetItem()`. This slot must be filled for the- `PyMapping_Check()`- `1`, it can be- `NULL`otherwise.

- 
[objobjargproc](#c.objobjargproc)[PyMappingMethods](#c.PyMappingMethods).mp_ass_subscript[¶](#c.PyMappingMethods.mp_ass_subscript)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_mp_ass_subscript`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PyObject_SetItem()`- `PyObject_DelItem()`- `PySequence_SetSlice()`- `PySequence_DelSlice()`- `PyObject_SetItem()`, but- *v*can also be set to- `NULL`to delete an item. If this slot is- `NULL`, the object does not support item assignment and deletion.

## Sequence Object Structures[¶](#sequence-object-structures)

- 
type PySequenceMethods[¶](#c.PySequenceMethods)
- This structure holds pointers to the functions which an object uses to implement the sequence protocol. 

- 
[lenfunc](#c.lenfunc)[PySequenceMethods](#c.PySequenceMethods).sq_length[¶](#c.PySequenceMethods.sq_length)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_length`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_Size()`- `PyObject_Size()`- `sq_item`- `sq_ass_item`

- 
[binaryfunc](#c.binaryfunc)[PySequenceMethods](#c.PySequenceMethods).sq_concat[¶](#c.PySequenceMethods.sq_concat)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_concat`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_Concat()`- `+`operator, after trying the numeric addition via the- `nb_add`

- 
[ssizeargfunc](#c.ssizeargfunc)[PySequenceMethods](#c.PySequenceMethods).sq_repeat[¶](#c.PySequenceMethods.sq_repeat)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_repeat`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_Repeat()`- `*`operator, after trying numeric multiplication via the- `nb_multiply`

- 
[ssizeargfunc](#c.ssizeargfunc)[PySequenceMethods](#c.PySequenceMethods).sq_item[¶](#c.PySequenceMethods.sq_item)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_item`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_GetItem()`- `PyObject_GetItem()`- `mp_subscript`- `PySequence_Check()`- `1`, it can be- `NULL`otherwise.- Negative indexes are handled as follows: if the - `sq_length`- `sq_item`- `sq_length`is- `NULL`, the index is passed as is to the function.

- 
[ssizeobjargproc](#c.ssizeobjargproc)[PySequenceMethods](#c.PySequenceMethods).sq_ass_item[¶](#c.PySequenceMethods.sq_ass_item)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_ass_item`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_SetItem()`- `PyObject_SetItem()`- `PyObject_DelItem()`- `mp_ass_subscript`- `NULL`if the object does not support item assignment and deletion.

- 
[objobjproc](#c.objobjproc)[PySequenceMethods](#c.PySequenceMethods).sq_contains[¶](#c.PySequenceMethods.sq_contains)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_contains`is part of the- [Stable ABI](stable.html#stable).- This function may be used by - `PySequence_Contains()`- `NULL`, in this case- `PySequence_Contains()`simply traverses the sequence until it finds a match.

- 
[binaryfunc](#c.binaryfunc)[PySequenceMethods](#c.PySequenceMethods).sq_inplace_concat[¶](#c.PySequenceMethods.sq_inplace_concat)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_inplace_concat`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_InPlaceConcat()`- `NULL`, in this case- `PySequence_InPlaceConcat()`will fall back to- `PySequence_Concat()`- `+=`, after trying numeric in-place addition via the- `nb_inplace_add`

- 
[ssizeargfunc](#c.ssizeargfunc)[PySequenceMethods](#c.PySequenceMethods).sq_inplace_repeat[¶](#c.PySequenceMethods.sq_inplace_repeat)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_sq_inplace_repeat`is part of the- [Stable ABI](stable.html#stable).- This function is used by - `PySequence_InPlaceRepeat()`- `NULL`, in this case- `PySequence_InPlaceRepeat()`will fall back to- `PySequence_Repeat()`- `*=`, after trying numeric in-place multiplication via the- `nb_inplace_multiply`

## Buffer Object Structures[¶](#buffer-object-structures)

- 
type PyBufferProcs[¶](#c.PyBufferProcs)
- This structure holds pointers to the functions required by the - [Buffer protocol](buffer.html#bufferobjects). The protocol defines how an exporter object can expose its internal data to consumer objects.

- 
[getbufferproc](#c.getbufferproc)[PyBufferProcs](#c.PyBufferProcs).bf_getbuffer[¶](#c.PyBufferProcs.bf_getbuffer)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_bf_getbuffer`is part of the- [Stable ABI](stable.html#stable)since version 3.11.- The signature of this function is: - int (PyObject *exporter, Py_buffer *view, int flags); - Handle a request to - *exporter*to fill in- *view*as specified by- *flags*. Except for point (3), an implementation of this function MUST take these steps:- Check if the request can be met. If not, raise - `BufferError`- `view->obj`to- `NULL`and return- `-1`.
- Fill in the requested fields. 
- Increment an internal counter for the number of exports. 
- Set - `view->obj`to- *exporter*and increment- `view->obj`.
- Return - `0`.
 - **Thread safety:**- In the - [free-threaded build](../glossary.html#term-free-threaded-build), implementations must ensure:- The export counter increment in step (3) is atomic. 
- The underlying buffer data remains valid and at a stable memory location for the lifetime of all exports. 
- For objects that support resizing or reallocation (such as - `bytearray`- `BufferError`
- The function is safe to call concurrently from multiple threads. 
 - See also - [Thread safety for memoryview objects](../library/threadsafety.html#thread-safety-memoryview)for the Python-level thread safety guarantees of- `memoryview`- If - *exporter*is part of a chain or tree of buffer providers, two main schemes can be used:- Re-export: Each member of the tree acts as the exporting object and sets - `view->obj`to a new reference to itself.
- Redirect: The buffer request is redirected to the root object of the tree. Here, - `view->obj`will be a new reference to the root object.
 - The individual fields of - *view*are described in section- [Buffer structure](buffer.html#buffer-structure), the rules how an exporter must react to specific requests are in section- [Buffer request types](buffer.html#buffer-request-types).- All memory pointed to in the - `Py_buffer`- `format`- `shape`- `strides`- `suboffsets`- `internal`- `PyBuffer_FillInfo()`- `PyObject_GetBuffer()`

- 
[releasebufferproc](#c.releasebufferproc)[PyBufferProcs](#c.PyBufferProcs).bf_releasebuffer[¶](#c.PyBufferProcs.bf_releasebuffer)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_bf_releasebuffer`is part of the- [Stable ABI](stable.html#stable)since version 3.11.- The signature of this function is: - void (PyObject *exporter, Py_buffer *view); - Handle a request to release the resources of the buffer. If no resources need to be released, - `PyBufferProcs.bf_releasebuffer`- `NULL`. Otherwise, a standard implementation of this function will take these optional steps:- Decrement an internal counter for the number of exports. 
- If the counter is - `0`, free all memory associated with- *view*.
 - **Thread safety:**- In the - [free-threaded build](../glossary.html#term-free-threaded-build):- The export counter decrement in step (1) must be atomic. 
- Resource cleanup when the counter reaches zero must be done atomically, as the final release may race with concurrent releases from other threads and dellocation must only happen once. 
 - The exporter MUST use the - `internal`- *view*argument.- This function MUST NOT decrement - `view->obj`, since that is done automatically in- `PyBuffer_Release()`- `PyBuffer_Release()`

## Async Object Structures[¶](#async-object-structures)

Added in version 3.5.

- 
type PyAsyncMethods[¶](#c.PyAsyncMethods)
- This structure holds pointers to the functions required to implement - [awaitable](../glossary.html#term-awaitable)and- [asynchronous iterator](../glossary.html#term-asynchronous-iterator)objects.- Here is the structure definition: - typedef struct { unaryfunc am_await; unaryfunc am_aiter; unaryfunc am_anext; sendfunc am_send; } PyAsyncMethods; 

- 
[unaryfunc](#c.unaryfunc)[PyAsyncMethods](#c.PyAsyncMethods).am_await[¶](#c.PyAsyncMethods.am_await)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_am_await`is part of the- [Stable ABI](stable.html#stable)since version 3.5.- The signature of this function is: - PyObject *am_await(PyObject *self); - The returned object must be an - [iterator](../glossary.html#term-iterator), i.e.- `PyIter_Check()`- `1`for it.- This slot may be set to - `NULL`if an object is not an- [awaitable](../glossary.html#term-awaitable).

- 
[unaryfunc](#c.unaryfunc)[PyAsyncMethods](#c.PyAsyncMethods).am_aiter[¶](#c.PyAsyncMethods.am_aiter)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_am_aiter`is part of the- [Stable ABI](stable.html#stable)since version 3.5.- The signature of this function is: - PyObject *am_aiter(PyObject *self); - Must return an - [asynchronous iterator](../glossary.html#term-asynchronous-iterator)object. See- `__anext__()`- This slot may be set to - `NULL`if an object does not implement asynchronous iteration protocol.

- 
[unaryfunc](#c.unaryfunc)[PyAsyncMethods](#c.PyAsyncMethods).am_anext[¶](#c.PyAsyncMethods.am_anext)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_am_anext`is part of the- [Stable ABI](stable.html#stable)since version 3.5.- The signature of this function is: - PyObject *am_anext(PyObject *self); - Must return an - [awaitable](../glossary.html#term-awaitable)object. See- `__anext__()`- `NULL`.

- 
[sendfunc](#c.sendfunc)[PyAsyncMethods](#c.PyAsyncMethods).am_send[¶](#c.PyAsyncMethods.am_send)
- *The corresponding*- [slot ID](type.html#c.PyType_Slot)- `Py_am_send`is part of the- [Stable ABI](stable.html#stable)since version 3.10.- The signature of this function is: - PySendResult am_send(PyObject *self, PyObject *arg, PyObject **result); - See - `PyIter_Send()`- `NULL`.- Added in version 3.10. 

## Slot Type typedefs[¶](#slot-type-typedefs)

- 
typedef [PyObject](structures.html#c.PyObject)*(*allocfunc)([PyTypeObject](type.html#c.PyTypeObject)*cls,[Py_ssize_t](intro.html#c.Py_ssize_t)nitems)[¶](#c.allocfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- The purpose of this function is to separate memory allocation from memory initialization. It should return a pointer to a block of memory of adequate length for the instance, suitably aligned, and initialized to zeros, but with - `ob_refcnt`- `1`and- `ob_type`- `tp_itemsize`- `ob_size`- *nitems*and the length of the allocated memory block should be- `tp_basicsize + nitems*tp_itemsize`, rounded up to a multiple of- `sizeof(void*)`; otherwise,- *nitems*is not used and the length of the block should be- `tp_basicsize`- This function should not do any other instance initialization, not even to allocate additional memory; that should be done by - `tp_new`

- 
typedef void (*destructor)([PyObject](structures.html#c.PyObject)*)[¶](#c.destructor)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef [PyObject](structures.html#c.PyObject)*(*newfunc)([PyTypeObject](type.html#c.PyTypeObject)*,[PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.newfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_new`

- 
typedef [PyObject](structures.html#c.PyObject)*(*reprfunc)([PyObject](structures.html#c.PyObject)*)[¶](#c.reprfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_repr`

- 
typedef [PyObject](structures.html#c.PyObject)*(*getattrfunc)([PyObject](structures.html#c.PyObject)*self, char *attr)[¶](#c.getattrfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the value of the named attribute for the object. 

- 
typedef int (*setattrfunc)([PyObject](structures.html#c.PyObject)*self, char *attr,[PyObject](structures.html#c.PyObject)*value)[¶](#c.setattrfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the value of the named attribute for the object. The value argument is set to - `NULL`to delete the attribute.

- 
typedef [PyObject](structures.html#c.PyObject)*(*getattrofunc)([PyObject](structures.html#c.PyObject)*self,[PyObject](structures.html#c.PyObject)*attr)[¶](#c.getattrofunc)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the value of the named attribute for the object. - See - `tp_getattro`

- 
typedef int (*setattrofunc)([PyObject](structures.html#c.PyObject)*self,[PyObject](structures.html#c.PyObject)*attr,[PyObject](structures.html#c.PyObject)*value)[¶](#c.setattrofunc)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the value of the named attribute for the object. The value argument is set to - `NULL`to delete the attribute.- See - `tp_setattro`

- 
typedef [PyObject](structures.html#c.PyObject)*(*descrgetfunc)([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.descrgetfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_descr_get`

- 
typedef int (*descrsetfunc)([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.descrsetfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_descr_set`

- 
typedef [Py_hash_t](hash.html#c.Py_hash_t)(*hashfunc)([PyObject](structures.html#c.PyObject)*)[¶](#c.hashfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_hash`

- 
typedef [PyObject](structures.html#c.PyObject)*(*richcmpfunc)([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*, int)[¶](#c.richcmpfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_richcompare`

- 
typedef [PyObject](structures.html#c.PyObject)*(*getiterfunc)([PyObject](structures.html#c.PyObject)*)[¶](#c.getiterfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_iter`

- 
typedef [PyObject](structures.html#c.PyObject)*(*iternextfunc)([PyObject](structures.html#c.PyObject)*)[¶](#c.iternextfunc)
- *Part of the*- [Stable ABI](stable.html#stable).- See - `tp_iternext`

- 
typedef [Py_ssize_t](intro.html#c.Py_ssize_t)(*lenfunc)([PyObject](structures.html#c.PyObject)*)[¶](#c.lenfunc)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef int (*getbufferproc)([PyObject](structures.html#c.PyObject)*,[Py_buffer](buffer.html#c.Py_buffer)*, int)[¶](#c.getbufferproc)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.

- 
typedef void (*releasebufferproc)([PyObject](structures.html#c.PyObject)*,[Py_buffer](buffer.html#c.Py_buffer)*)[¶](#c.releasebufferproc)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.

- 
typedef [PyObject](structures.html#c.PyObject)*(*unaryfunc)([PyObject](structures.html#c.PyObject)*)[¶](#c.unaryfunc)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef [PyObject](structures.html#c.PyObject)*(*binaryfunc)([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.binaryfunc)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef [PyObject](structures.html#c.PyObject)*(*ssizeargfunc)([PyObject](structures.html#c.PyObject)*,[Py_ssize_t](intro.html#c.Py_ssize_t))[¶](#c.ssizeargfunc)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef int (*ssizeobjargproc)([PyObject](structures.html#c.PyObject)*,[Py_ssize_t](intro.html#c.Py_ssize_t),[PyObject](structures.html#c.PyObject)*)[¶](#c.ssizeobjargproc)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef int (*objobjproc)([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.objobjproc)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
typedef int (*objobjargproc)([PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*,[PyObject](structures.html#c.PyObject)*)[¶](#c.objobjargproc)
- *Part of the*- [Stable ABI](stable.html#stable).

## Examples[¶](#examples)

The following are simple examples of Python type definitions.  They
include common usage you may encounter.  Some demonstrate tricky corner
cases.  For more examples, practical info, and a tutorial, see
[Defining Extension Types: Tutorial](../extending/newtypes_tutorial.html#defining-new-types) and [Defining Extension Types: Assorted Topics](../extending/newtypes.html#new-types-topics).

A basic [static type](#static-types):

```
typedef struct {
    PyObject_HEAD
    const char *data;
} MyObject;
static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
    .tp_basicsize = sizeof(MyObject),
    .tp_doc = PyDoc_STR("My objects"),
    .tp_new = myobj_new,
    .tp_dealloc = (destructor)myobj_dealloc,
    .tp_repr = (reprfunc)myobj_repr,
};
```
You may also find older code (especially in the CPython code base) with a more verbose initializer:

```
static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "mymod.MyObject",               /* tp_name */
    sizeof(MyObject),               /* tp_basicsize */
    0,                              /* tp_itemsize */
    (destructor)myobj_dealloc,      /* tp_dealloc */
    0,                              /* tp_vectorcall_offset */
    0,                              /* tp_getattr */
    0,                              /* tp_setattr */
    0,                              /* tp_as_async */
    (reprfunc)myobj_repr,           /* tp_repr */
    0,                              /* tp_as_number */
    0,                              /* tp_as_sequence */
    0,                              /* tp_as_mapping */
    0,                              /* tp_hash */
    0,                              /* tp_call */
    0,                              /* tp_str */
    0,                              /* tp_getattro */
    0,                              /* tp_setattro */
    0,                              /* tp_as_buffer */
    0,                              /* tp_flags */
    PyDoc_STR("My objects"),        /* tp_doc */
    0,                              /* tp_traverse */
    0,                              /* tp_clear */
    0,                              /* tp_richcompare */
    0,                              /* tp_weaklistoffset */
    0,                              /* tp_iter */
    0,                              /* tp_iternext */
    0,                              /* tp_methods */
    0,                              /* tp_members */
    0,                              /* tp_getset */
    0,                              /* tp_base */
    0,                              /* tp_dict */
    0,                              /* tp_descr_get */
    0,                              /* tp_descr_set */
    0,                              /* tp_dictoffset */
    0,                              /* tp_init */
    0,                              /* tp_alloc */
    myobj_new,                      /* tp_new */
};
```
A type that supports weakrefs, instance dicts, and hashing:

```
typedef struct {
    PyObject_HEAD
    const char *data;
} MyObject;
static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
    .tp_basicsize = sizeof(MyObject),
    .tp_doc = PyDoc_STR("My objects"),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE |
         Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_MANAGED_DICT |
         Py_TPFLAGS_MANAGED_WEAKREF,
    .tp_new = myobj_new,
    .tp_traverse = (traverseproc)myobj_traverse,
    .tp_clear = (inquiry)myobj_clear,
    .tp_alloc = PyType_GenericNew,
    .tp_dealloc = (destructor)myobj_dealloc,
    .tp_repr = (reprfunc)myobj_repr,
    .tp_hash = (hashfunc)myobj_hash,
    .tp_richcompare = PyBaseObject_Type.tp_richcompare,
};
```
A str subclass that cannot be subclassed and cannot be called
to create instances (e.g. uses a separate factory func) using
[ Py_TPFLAGS_DISALLOW_INSTANTIATION](#c.Py_TPFLAGS_DISALLOW_INSTANTIATION) flag:

```
typedef struct {
    PyUnicodeObject raw;
    char *extra;
} MyStr;
static PyTypeObject MyStr_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyStr",
    .tp_basicsize = sizeof(MyStr),
    .tp_base = NULL,  // set to &PyUnicode_Type in module init
    .tp_doc = PyDoc_STR("my custom str"),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .tp_repr = (reprfunc)myobj_repr,
};
```
The simplest [static type](#static-types) with fixed-length instances:

```
typedef struct {
    PyObject_HEAD
} MyObject;
static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
};
```
The simplest [static type](#static-types) with variable-length instances:

```
typedef struct {
    PyObject_VAR_HEAD
    const char *data[1];
} MyObject;
static PyTypeObject MyObject_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymod.MyObject",
    .tp_basicsize = sizeof(MyObject) - sizeof(char *),
    .tp_itemsize = sizeof(char *),
};
```