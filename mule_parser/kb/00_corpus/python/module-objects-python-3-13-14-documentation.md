# Module Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/module.html](https://docs.python.org/3.13/c-api/module.html)

---

# Module Objects[¶](#module-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyModule_Type[¶](#c.PyModule_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `types.ModuleType`

- 
int PyModule_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyModule_Check)
- Return true if - *p*is a module object, or a subtype of a module object. This function always succeeds.

- 
int PyModule_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyModule_CheckExact)
- Return true if - *p*is a module object, but not a subtype of- `PyModule_Type`

- 
[PyObject](structures.html#c.PyObject)*PyModule_NewObject([PyObject](structures.html#c.PyObject)*name)[¶](#c.PyModule_NewObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return a new module object with - `module.__name__`- *name*. The module’s- `__name__`,- `__doc__`- `__package__`- `__loader__`- `__name__`are set to- `None`). The caller is responsible for setting a- `__file__`- Return - `NULL`with an exception set on error.- Added in version 3.3. - Changed in version 3.4: - `__package__`- `__loader__`- `None`.

- 
[PyObject](structures.html#c.PyObject)*PyModule_New(const char *name)[¶](#c.PyModule_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyModule_NewObject()`

- 
[PyObject](structures.html#c.PyObject)*PyModule_GetDict([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetDict)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the dictionary object that implements - *module*’s namespace; this object is the same as the- `__dict__`- *module*is not a module object (or a subtype of a module object),- `SystemError`- `NULL`is returned.- It is recommended extensions use other - `PyModule_*`and- `PyObject_*`functions rather than directly manipulate a module’s- `__dict__`- The returned reference is borrowed from the module; it is valid until the module is destroyed. 

- 
[PyObject](structures.html#c.PyObject)*PyModule_GetNameObject([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetNameObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return - *module*’s- `__name__`- `SystemError`- `NULL`is returned.- Added in version 3.3. 

- 
const char *PyModule_GetName([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetName)
- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyModule_GetNameObject()`- `'utf-8'`.- The returned buffer is only valid until the module is renamed or destroyed. Note that Python code may rename a module by setting its - `__name__`

- 
void *PyModule_GetState([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetState)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the “state” of the module, that is, a pointer to the block of memory allocated at module creation time, or - `NULL`. See- `PyModuleDef.m_size`

- 
[PyModuleDef](#c.PyModuleDef)*PyModule_GetDef([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetDef)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a pointer to the - `PyModuleDef`- `NULL`if the module wasn’t created from a definition.- On error, return - `NULL`with an exception set. Use- `PyErr_Occurred()`- `PyModuleDef`.

- 
[PyObject](structures.html#c.PyObject)*PyModule_GetFilenameObject([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetFilenameObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the name of the file from which - *module*was loaded using- *module*’s- `__file__`- `SystemError`- `NULL`; otherwise return a reference to a Unicode object.- Added in version 3.2. 

- 
const char *PyModule_GetFilename([PyObject](structures.html#c.PyObject)*module)[¶](#c.PyModule_GetFilename)
- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyModule_GetFilenameObject()`- The returned buffer is only valid until the module’s - `__file__`- Deprecated since version 3.2: - `PyModule_GetFilename()`- `UnicodeEncodeError`- `PyModule_GetFilenameObject()`

## Initializing C modules[¶](#initializing-c-modules)

Modules objects are usually created from extension modules (shared libraries
which export an initialization function), or compiled-in modules
(where the initialization function is added using [ PyImport_AppendInittab()](import.html#c.PyImport_AppendInittab)).
See 

[Building C and C++ Extensions](../extending/building.html#building)or

[Extending Embedded Python](../extending/embedding.html#extending-with-embedding)for details.

The initialization function can either pass a module definition instance
to [ PyModule_Create()](#c.PyModule_Create), and return the resulting module object,
or request “multi-phase initialization” by returning the definition struct itself.

- 
type PyModuleDef[¶](#c.PyModuleDef)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- The module definition struct, which holds all information needed to create a module object. There is usually only one statically initialized variable of this type for each module. - 
PyModuleDef_Base m_base[¶](#c.PyModuleDef.m_base)
- Always initialize this member to - `PyModuleDef_HEAD_INIT`.
 - 
const char *m_name[¶](#c.PyModuleDef.m_name)
- Name for the new module. 
 - 
const char *m_doc[¶](#c.PyModuleDef.m_doc)
- Docstring for the module; usually a docstring variable created with - `PyDoc_STRVAR`
 - 
[Py_ssize_t](intro.html#c.Py_ssize_t)m_size[¶](#c.PyModuleDef.m_size)
- Module state may be kept in a per-module memory area that can be retrieved with - `PyModule_GetState()`- This memory area is allocated based on - *m_size*on module creation, and freed when the module object is deallocated, after the- `m_free`- Setting - `m_size`to- `-1`means that the module does not support sub-interpreters, because it has global state.- Setting it to a non-negative value means that the module can be re-initialized and specifies the additional amount of memory it requires for its state. Non-negative - `m_size`is required for multi-phase initialization.- See - **PEP 3121**
 - 
[PyMethodDef](structures.html#c.PyMethodDef)*m_methods[¶](#c.PyModuleDef.m_methods)
- A pointer to a table of module-level functions, described by - `PyMethodDef`- `NULL`if no functions are present.
 - 
[PyModuleDef_Slot](#c.PyModuleDef_Slot)*m_slots[¶](#c.PyModuleDef.m_slots)
- An array of slot definitions for multi-phase initialization, terminated by a - `{0, NULL}`entry. When using single-phase initialization,- *m_slots*must be- `NULL`.
 - 
[traverseproc](gcsupport.html#c.traverseproc)m_traverse[¶](#c.PyModuleDef.m_traverse)
- A traversal function to call during GC traversal of the module object, or - `NULL`if not needed.- This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed ( - `Py_mod_exec`- `m_size`- `PyModule_GetState()`- `NULL`.- Changed in version 3.9: No longer called before the module state is allocated. 
 - 
[inquiry](gcsupport.html#c.inquiry)m_clear[¶](#c.PyModuleDef.m_clear)
- A clear function to call during GC clearing of the module object, or - `NULL`if not needed.- This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed ( - `Py_mod_exec`- `m_size`- `PyModule_GetState()`- `NULL`.- Like - `PyTypeObject.tp_clear`- *always*called before a module is deallocated. For example, when reference counting is enough to determine that an object is no longer used, the cyclic garbage collector is not involved and- `m_free`- Changed in version 3.9: No longer called before the module state is allocated. 
 - 
[freefunc](typeobj.html#c.freefunc)m_free[¶](#c.PyModuleDef.m_free)
- A function to call during deallocation of the module object, or - `NULL`if not needed.- This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed ( - `Py_mod_exec`- `m_size`- `PyModule_GetState()`- `NULL`.- Changed in version 3.9: No longer called before the module state is allocated. 
 
- 
PyModuleDef_Base m_base

- 
[PyTypeObject](type.html#c.PyTypeObject)PyModuleDef_Type[¶](#c.PyModuleDef_Type)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.5.- The type of - `PyModuleDef`objects.

### Single-phase initialization[¶](#single-phase-initialization)

The module initialization function may create and return the module object directly. This is referred to as “single-phase initialization”, and uses one of the following two module creation functions:

- 
[PyObject](structures.html#c.PyObject)*PyModule_Create([PyModuleDef](#c.PyModuleDef)*def)[¶](#c.PyModule_Create)
- *Return value: New reference.*- Create a new module object, given the definition in - *def*. This behaves like- `PyModule_Create2()`- *module_api_version*set to- `PYTHON_API_VERSION`.

- 
[PyObject](structures.html#c.PyObject)*PyModule_Create2([PyModuleDef](#c.PyModuleDef)*def, int module_api_version)[¶](#c.PyModule_Create2)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a new module object, given the definition in - *def*, assuming the API version- *module_api_version*. If that version does not match the version of the running interpreter, a- `RuntimeWarning`- Return - `NULL`with an exception set on error.- Note - Most uses of this function should be using - `PyModule_Create()`

Before it is returned from in the initialization function, the resulting module
object is typically populated using functions like [ PyModule_AddObjectRef()](#c.PyModule_AddObjectRef).

### Multi-phase initialization[¶](#multi-phase-initialization)

An alternate way to specify extensions is to request “multi-phase initialization”.
Extension modules created this way behave more like Python modules: the
initialization is split between the *creation phase*, when the module object
is created, and the *execution phase*, when it is populated.
The distinction is similar to the [ __new__()](../reference/datamodel.html#object.__new__) and

[methods of classes.](../reference/datamodel.html#object.__init__)

`__init__()`Unlike modules created using single-phase initialization, these modules are not
singletons.
For example, if the [ sys.modules](../library/sys.html#sys.modules) entry is removed and the module
is re-imported, a new module object is created, and typically populated with
fresh method and type objects.
The old module is subject to normal garbage collection.
This mirrors the behavior of pure-Python modules.

Additional module instances may be created in
[sub-interpreters](init.html#sub-interpreter-support)
or after after Python runtime reinitialization
([ Py_Finalize()](init.html#c.Py_Finalize) and 

[). In these cases, sharing Python objects between module instances would likely cause crashes or undefined behavior.](init.html#c.Py_Initialize)

`Py_Initialize()`To avoid such issues, each instance of an extension module should
be *isolated*: changes to one instance should not implicitly affect the others,
and all state, including references to Python objects, should be specific to
a particular module instance.
See [Isolating Extension Modules](../howto/isolating-extensions.html#isolating-extensions-howto) for more details and a practical guide.

A simpler way to avoid these issues is
[raising an error on repeated initialization](../howto/isolating-extensions.html#isolating-extensions-optout).

All modules created using multi-phase initialization are expected to support
[sub-interpreters](init.html#sub-interpreter-support), or otherwise explicitly
signal a lack of support.
This is usually achieved by isolation or blocking repeated initialization,
as above.
A module may also be limited to the main interpreter using
the [ Py_mod_multiple_interpreters](#c.Py_mod_multiple_interpreters) slot.

To request multi-phase initialization, the initialization function
(PyInit_modulename) returns a [ PyModuleDef](#c.PyModuleDef) instance with non-empty

[. Before it is returned, the](#c.PyModuleDef.m_slots)

`m_slots``PyModuleDef`
instance must be initialized with the following function:- 
[PyObject](structures.html#c.PyObject)*PyModuleDef_Init([PyModuleDef](#c.PyModuleDef)*def)[¶](#c.PyModuleDef_Init)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.5.- Ensures a module definition is a properly initialized Python object that correctly reports its type and reference count. - Returns - *def*cast to- `PyObject*`, or- `NULL`if an error occurred.- Added in version 3.5. 

The *m_slots* member of the module definition must point to an array of
`PyModuleDef_Slot` structures:

- 
type PyModuleDef_Slot[¶](#c.PyModuleDef_Slot)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members) since version 3.5.- 
int slot[¶](#c.PyModuleDef_Slot.slot)
- A slot ID, chosen from the available values explained below. 
 - 
void *value[¶](#c.PyModuleDef_Slot.value)
- Value of the slot, whose meaning depends on the slot ID. 
 - Added in version 3.5. 
- 
int slot

The *m_slots* array must be terminated by a slot with id 0.

The available slot types are:

- 
Py_mod_create[¶](#c.Py_mod_create)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.5.- Specifies a function that is called to create the module object itself. The - *value*pointer of this slot must point to a function of the signature:- 
[PyObject](structures.html#c.PyObject)*create_module([PyObject](structures.html#c.PyObject)*spec,[PyModuleDef](#c.PyModuleDef)*def)[¶](#c.Py_mod_create.create_module)
 - The function receives a - `ModuleSpec`- **PEP 451**- `NULL`.- This function should be kept minimal. In particular, it should not call arbitrary Python code, as trying to import the same module again may result in an infinite loop. - Multiple - `Py_mod_create`slots may not be specified in one module definition.- If - `Py_mod_create`is not specified, the import machinery will create a normal module object using- `PyModule_New()`- *spec*, not the definition, to allow extension modules to dynamically adjust to their place in the module hierarchy and be imported under different names through symlinks, all while sharing a single module definition.- There is no requirement for the returned object to be an instance of - `PyModule_Type`- `PyModule_Type`instances may be returned if the- `PyModuleDef`has non-- `NULL`- `m_traverse`,- `m_clear`,- `m_free`; non-zero- `m_size`; or slots other than- `Py_mod_create`.- Added in version 3.5. 
- 

- 
Py_mod_exec[¶](#c.Py_mod_exec)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.5.- Specifies a function that is called to - *execute*the module. This is equivalent to executing the code of a Python module: typically, this function adds classes and constants to the module. The signature of the function is:- If multiple - `Py_mod_exec`slots are specified, they are processed in the order they appear in the- *m_slots*array.- Added in version 3.5. 

- 
Py_mod_multiple_interpreters[¶](#c.Py_mod_multiple_interpreters)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Specifies one of the following values: - 
Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED[¶](#c.Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED)
- The module does not support being imported in subinterpreters. 
 - 
Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED[¶](#c.Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED)
- The module supports being imported in subinterpreters, but only when they share the main interpreter’s GIL. (See - [Isolating Extension Modules](../howto/isolating-extensions.html#isolating-extensions-howto).)
 - 
Py_MOD_PER_INTERPRETER_GIL_SUPPORTED[¶](#c.Py_MOD_PER_INTERPRETER_GIL_SUPPORTED)
- The module supports being imported in subinterpreters, even when they have their own GIL. (See - [Isolating Extension Modules](../howto/isolating-extensions.html#isolating-extensions-howto).)
 - This slot determines whether or not importing this module in a subinterpreter will fail. - Multiple - `Py_mod_multiple_interpreters`slots may not be specified in one module definition.- If - `Py_mod_multiple_interpreters`is not specified, the import machinery defaults to- `Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED`.- Added in version 3.12. 
- 
Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED

- 
Py_mod_gil[¶](#c.Py_mod_gil)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Specifies one of the following values: - 
Py_MOD_GIL_USED[¶](#c.Py_MOD_GIL_USED)
- The module depends on the presence of the global interpreter lock (GIL), and may access global state without synchronization. 
 - 
Py_MOD_GIL_NOT_USED[¶](#c.Py_MOD_GIL_NOT_USED)
- The module is safe to run without an active GIL. 
 - This slot is ignored by Python builds not configured with - `--disable-gil`- [Free-threaded CPython](../whatsnew/3.13.html#whatsnew313-free-threaded-cpython)for more detail.- Multiple - `Py_mod_gil`slots may not be specified in one module definition.- If - `Py_mod_gil`is not specified, the import machinery defaults to- `Py_MOD_GIL_USED`.- Added in version 3.13. 
- 
Py_MOD_GIL_USED

See [ PEP 489](https://peps.python.org/pep-0489/) for more details on multi-phase initialization.

### Low-level module creation functions[¶](#low-level-module-creation-functions)

The following functions are called under the hood when using multi-phase
initialization. They can be used directly, for example when creating module
objects dynamically. Note that both `PyModule_FromDefAndSpec` and
`PyModule_ExecDef` must be called to fully initialize a module.

- 
[PyObject](structures.html#c.PyObject)*PyModule_FromDefAndSpec([PyModuleDef](#c.PyModuleDef)*def,[PyObject](structures.html#c.PyObject)*spec)[¶](#c.PyModule_FromDefAndSpec)
- *Return value: New reference.*- Create a new module object, given the definition in - *def*and the ModuleSpec- *spec*. This behaves like- `PyModule_FromDefAndSpec2()`- *module_api_version*set to- `PYTHON_API_VERSION`.- Added in version 3.5. 

- 
[PyObject](structures.html#c.PyObject)*PyModule_FromDefAndSpec2([PyModuleDef](#c.PyModuleDef)*def,[PyObject](structures.html#c.PyObject)*spec, int module_api_version)[¶](#c.PyModule_FromDefAndSpec2)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Create a new module object, given the definition in - *def*and the ModuleSpec- *spec*, assuming the API version- *module_api_version*. If that version does not match the version of the running interpreter, a- `RuntimeWarning`- Return - `NULL`with an exception set on error.- Note - Most uses of this function should be using - `PyModule_FromDefAndSpec()`- Added in version 3.5. 

- 
int PyModule_ExecDef([PyObject](structures.html#c.PyObject)*module,[PyModuleDef](#c.PyModuleDef)*def)[¶](#c.PyModule_ExecDef)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Process any execution slots ( - `Py_mod_exec`- *def*.- Added in version 3.5. 

- 
int PyModule_SetDocString([PyObject](structures.html#c.PyObject)*module, const char *docstring)[¶](#c.PyModule_SetDocString)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Set the docstring for - *module*to- *docstring*. This function is called automatically when creating a module from- `PyModuleDef`, using either- `PyModule_Create`or- `PyModule_FromDefAndSpec`.- Return - `0`on success. Return- `-1`with an exception set on error.- Added in version 3.5. 

- 
int PyModule_AddFunctions([PyObject](structures.html#c.PyObject)*module,[PyMethodDef](structures.html#c.PyMethodDef)*functions)[¶](#c.PyModule_AddFunctions)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Add the functions from the - `NULL`terminated- *functions*array to- *module*. Refer to the- `PyMethodDef`- `PyModuleDef`, using either- `PyModule_Create`or- `PyModule_FromDefAndSpec`.- The - *functions*array must be statically allocated (or otherwise guaranteed to outlive the module object).- Added in version 3.5. 

### Support functions[¶](#support-functions)

The module initialization function (if using single phase initialization) or a function called from a module execution slot (if using multi-phase initialization), can use the following functions to help initialize the module state:

- 
int PyModule_AddObjectRef([PyObject](structures.html#c.PyObject)*module, const char *name,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyModule_AddObjectRef)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Add an object to - *module*as- *name*. This is a convenience function which can be used from the module’s initialization function.- On success, return - `0`. On error, raise an exception and return- `-1`.- Example usage: - static int add_spam(PyObject *module, int value) { PyObject *obj = PyLong_FromLong(value); if (obj == NULL) { return -1; } int res = PyModule_AddObjectRef(module, "spam", obj); Py_DECREF(obj); return res; } - To be convenient, the function accepts - `NULL`- *value*with an exception set. In this case, return- `-1`and just leave the raised exception unchanged.- The example can also be written without checking explicitly if - *obj*is- `NULL`:- static int add_spam(PyObject *module, int value) { PyObject *obj = PyLong_FromLong(value); int res = PyModule_AddObjectRef(module, "spam", obj); Py_XDECREF(obj); return res; } - Note that - `Py_XDECREF()`should be used instead of- `Py_DECREF()`in this case, since- *obj*can be- `NULL`.- The number of different - *name*strings passed to this function should be kept small, usually by only using statically allocated strings as- *name*. For names that aren’t known at compile time, prefer calling- `PyUnicode_FromString()`- `PyObject_SetAttr()`- `PyUnicode_InternFromString()`- Added in version 3.10. 

- 
int PyModule_Add([PyObject](structures.html#c.PyObject)*module, const char *name,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyModule_Add)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Similar to - `PyModule_AddObjectRef()`- *value*. It can be called with a result of function that returns a new reference without bothering to check its result or even saving it to a variable.- Example usage: - if (PyModule_Add(module, "spam", PyBytes_FromString(value)) < 0) { goto error; } - Added in version 3.13. 

- 
int PyModule_AddObject([PyObject](structures.html#c.PyObject)*module, const char *name,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyModule_AddObject)
- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyModule_AddObjectRef()`- *value*on success (if it returns- `0`).- The new - `PyModule_Add()`- `PyModule_AddObjectRef()`- `PyModule_AddObject()`- Note - Unlike other functions that steal references, - `PyModule_AddObject()`only releases the reference to- *value*- **on success**.- This means that its return value must be checked, and calling code must - `Py_XDECREF()`- *value*manually on error.- Example usage: - PyObject *obj = PyBytes_FromString(value); if (PyModule_AddObject(module, "spam", obj) < 0) { // If 'obj' is not NULL and PyModule_AddObject() failed, // 'obj' strong reference must be deleted with Py_XDECREF(). // If 'obj' is NULL, Py_XDECREF() does nothing. Py_XDECREF(obj); goto error; } // PyModule_AddObject() stole a reference to obj: // Py_XDECREF(obj) is not needed here. - [Soft deprecated](../glossary.html#term-soft-deprecated)since version 3.13.

- 
int PyModule_AddIntConstant([PyObject](structures.html#c.PyObject)*module, const char *name, long value)[¶](#c.PyModule_AddIntConstant)
- *Part of the*- [Stable ABI](stable.html#stable).- Add an integer constant to - *module*as- *name*. This convenience function can be used from the module’s initialization function. Return- `-1`with an exception set on error,- `0`on success.- This is a convenience function that calls - `PyLong_FromLong()`- `PyModule_AddObjectRef()`

- 
int PyModule_AddStringConstant([PyObject](structures.html#c.PyObject)*module, const char *name, const char *value)[¶](#c.PyModule_AddStringConstant)
- *Part of the*- [Stable ABI](stable.html#stable).- Add a string constant to - *module*as- *name*. This convenience function can be used from the module’s initialization function. The string- *value*must be- `NULL`-terminated. Return- `-1`with an exception set on error,- `0`on success.- This is a convenience function that calls - `PyUnicode_InternFromString()`- `PyModule_AddObjectRef()`

- 
PyModule_AddIntMacro(module, macro)[¶](#c.PyModule_AddIntMacro)
- Add an int constant to - *module*. The name and the value are taken from- *macro*. For example- `PyModule_AddIntMacro(module, AF_INET)`adds the int constant- *AF_INET*with the value of- *AF_INET*to- *module*. Return- `-1`with an exception set on error,- `0`on success.

- 
PyModule_AddStringMacro(module, macro)[¶](#c.PyModule_AddStringMacro)
- Add a string constant to - *module*.

- 
int PyModule_AddType([PyObject](structures.html#c.PyObject)*module,[PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c.PyModule_AddType)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Add a type object to - *module*. The type object is finalized by calling internally- `PyType_Ready()`- `tp_name`- `-1`with an exception set on error,- `0`on success.- Added in version 3.9. 

- 
int PyUnstable_Module_SetGIL([PyObject](structures.html#c.PyObject)*module, void *gil)[¶](#c.PyUnstable_Module_SetGIL)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Indicate that - *module*does or does not support running without the global interpreter lock (GIL), using one of the values from- `Py_mod_gil`- *module*’s initialization function. If this function is not called during module initialization, the import machinery assumes the module does not support running without the GIL. This function is only available in Python builds configured with- `--disable-gil`- `-1`with an exception set on error,- `0`on success.- Added in version 3.13. 

## Module lookup[¶](#module-lookup)

Single-phase initialization creates singleton modules that can be looked up in the context of the current interpreter. This allows the module object to be retrieved later with only a reference to the module definition.

These functions will not work on modules created using multi-phase initialization, since multiple such modules can be created from a single definition.

- 
[PyObject](structures.html#c.PyObject)*PyState_FindModule([PyModuleDef](#c.PyModuleDef)*def)[¶](#c.PyState_FindModule)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Returns the module object that was created from - *def*for the current interpreter. This method requires that the module object has been attached to the interpreter state with- `PyState_AddModule()`- `NULL`.

- 
int PyState_AddModule([PyObject](structures.html#c.PyObject)*module,[PyModuleDef](#c.PyModuleDef)*def)[¶](#c.PyState_AddModule)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.3.- Attaches the module object passed to the function to the interpreter state. This allows the module object to be accessible via - `PyState_FindModule()`- Only effective on modules created using single-phase initialization. - Python calls - `PyState_AddModule`automatically after importing a module, so it is unnecessary (but harmless) to call it from module initialization code. An explicit call is needed only if the module’s own init code subsequently calls- `PyState_FindModule`. The function is mainly intended for implementing alternative import mechanisms (either by calling it directly, or by referring to its implementation for details of the required state updates).- The caller must hold the GIL. - Return - `-1`with an exception set on error,- `0`on success.- Added in version 3.3. 

- 
int PyState_RemoveModule([PyModuleDef](#c.PyModuleDef)*def)[¶](#c.PyState_RemoveModule)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.3.- Removes the module object created from - *def*from the interpreter state. Return- `-1`with an exception set on error,- `0`on success.- The caller must hold the GIL. - Added in version 3.3.