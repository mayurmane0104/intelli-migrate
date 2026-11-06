# Type Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/type.html](https://docs.python.org/c-api/type.html)

---

# Type Objects[¶](#type-objects)

- 
type PyTypeObject[¶](#c.PyTypeObject)
- *Part of the*- [Limited API](stable.html#stable)(as an opaque struct).- The C structure of the objects used to describe built-in types. 

- 
[PyTypeObject](#c.PyTypeObject)PyType_Type[¶](#c.PyType_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the type object for type objects; it is the same object as - `type`

- 
int PyType_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyType_Check)
- Return non-zero if the object - *o*is a type object, including instances of types derived from the standard type object. Return 0 in all other cases. This function always succeeds.

- 
int PyType_CheckExact([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyType_CheckExact)
- Return non-zero if the object - *o*is a type object, but not a subtype of the standard type object. Return 0 in all other cases. This function always succeeds.

- 
unsigned int PyType_ClearCache()[¶](#c.PyType_ClearCache)
- *Part of the*- [Stable ABI](stable.html#stable).- Clear the internal lookup cache. Return the current version tag. 

- 
unsigned long PyType_GetFlags([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetFlags)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the - `tp_flags`- *type*. This function is primarily meant for use with- `Py_LIMITED_API`; the individual flag bits are guaranteed to be stable across Python releases, but access to- `tp_flags`itself is not part of the- [limited API](stable.html#limited-c-api).- Added in version 3.2. - Changed in version 3.4: The return type is now - `unsigned long`rather than- `long`.

- 
[PyObject](structures.html#c.PyObject)*PyType_GetDict([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetDict)
- Return the type object’s internal namespace, which is otherwise only exposed via a read-only proxy ( - `cls.__dict__`- `tp_dict`- This function is meant for specific embedding and language-binding cases, where direct access to the dict is necessary and indirect access (e.g. via the proxy or - `PyObject_GetAttr()`- Extension modules should continue to use - `tp_dict`, directly or indirectly, when setting up their own types.- Added in version 3.12. 

- 
void PyType_Modified([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_Modified)
- *Part of the*- [Stable ABI](stable.html#stable).- Invalidate the internal lookup cache for the type and all of its subtypes. This function must be called after any manual modification of the attributes or base classes of the type. 

- 
int PyType_AddWatcher([PyType_WatchCallback](#c.PyType_WatchCallback)callback)[¶](#c.PyType_AddWatcher)
- Register - *callback*as a type watcher. Return a non-negative integer ID which must be passed to future calls to- `PyType_Watch()`- `-1`and set an exception.- In free-threaded builds, - `PyType_AddWatcher()`- Added in version 3.12. 

- 
int PyType_ClearWatcher(int watcher_id)[¶](#c.PyType_ClearWatcher)
- Clear watcher identified by - *watcher_id*(previously returned from- `PyType_AddWatcher()`- `0`on success,- `-1`on error (e.g. if- *watcher_id*was never registered.)- An extension should never call - `PyType_ClearWatcher`with a- *watcher_id*that was not returned to it by a previous call to- `PyType_AddWatcher()`- Added in version 3.12. 

- 
int PyType_Watch(int watcher_id, [PyObject](structures.html#c.PyObject)*type)[¶](#c.PyType_Watch)
- Mark - *type*as watched. The callback granted- *watcher_id*by- `PyType_AddWatcher()`- `PyType_Modified()`- *type*. (The callback may be called only once for a series of consecutive modifications to- *type*, if- `_PyType_Lookup()`is not called on- *type*between the modifications; this is an implementation detail and subject to change.)- An extension should never call - `PyType_Watch`with a- *watcher_id*that was not returned to it by a previous call to- `PyType_AddWatcher()`- Added in version 3.12. 

- 
int PyType_Unwatch(int watcher_id, [PyObject](structures.html#c.PyObject)*type)[¶](#c.PyType_Unwatch)
- Mark - *type*as not watched. This undoes a previous call to- `PyType_Watch()`- *type*must not be- `NULL`.- An extension should never call this function with a - *watcher_id*that was not returned to it by a previous call to- `PyType_AddWatcher()`- On success, this function returns - `0`. On failure, this function returns- `-1`with an exception set.- Added in version 3.12. 

- 
typedef int (*PyType_WatchCallback)([PyObject](structures.html#c.PyObject)*type)[¶](#c.PyType_WatchCallback)
- Type of a type-watcher callback function. - The callback must not modify - *type*or cause- `PyType_Modified()`- *type*or any type in its MRO; violating this rule could cause infinite recursion.- Added in version 3.12. 

- 
int PyType_HasFeature([PyTypeObject](#c.PyTypeObject)*o, int feature)[¶](#c.PyType_HasFeature)
- Return non-zero if the type object - *o*sets the feature- *feature*. Type features are denoted by single bit flags.

- 
int PyType_FastSubclass([PyTypeObject](#c.PyTypeObject)*type, int flag)[¶](#c.PyType_FastSubclass)
- Return non-zero if the type object - *type*sets the subclass flag- *flag*. Subclass flags are denoted by- `Py_TPFLAGS_*_SUBCLASS`- `_Check`functions for common types.- See also - `PyObject_TypeCheck()`- `_Check`functions for types that don’t come with subclass flags.

- 
int PyType_IS_GC([PyTypeObject](#c.PyTypeObject)*o)[¶](#c.PyType_IS_GC)
- Return true if the type object includes support for the cycle detector; this tests the type flag - `Py_TPFLAGS_HAVE_GC`

- 
int PyType_IsSubtype([PyTypeObject](#c.PyTypeObject)*a,[PyTypeObject](#c.PyTypeObject)*b)[¶](#c.PyType_IsSubtype)
- *Part of the*- [Stable ABI](stable.html#stable).- Return true if - *a*is a subtype of- *b*.- This function only checks for actual subtypes, which means that - `__subclasscheck__()`- *b*. Call- `PyObject_IsSubclass()`- `issubclass()`

- 
[PyObject](structures.html#c.PyObject)*PyType_GenericAlloc([PyTypeObject](#c.PyTypeObject)*type,[Py_ssize_t](intro.html#c.Py_ssize_t)nitems)[¶](#c.PyType_GenericAlloc)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Generic handler for the - `tp_alloc`- `PyObject_Init()`- `PyObject_InitVar()`- Do not call this directly to allocate memory for an object; call the type’s - `tp_alloc`- For types that support garbage collection (i.e., the - `Py_TPFLAGS_HAVE_GC`- `PyObject_GC_New`- `PyObject_GC_NewVar`- `PyObject_GC_Del()`- `tp_free`- `PyObject_New`- `PyObject_NewVar`- `PyObject_Free()`- `tp_free`.

- 
[PyObject](structures.html#c.PyObject)*PyType_GenericNew([PyTypeObject](#c.PyTypeObject)*type,[PyObject](structures.html#c.PyObject)*args,[PyObject](structures.html#c.PyObject)*kwds)[¶](#c.PyType_GenericNew)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Generic handler for the - `tp_new`- `tp_alloc`

- 
int PyType_Ready([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_Ready)
- *Part of the*- [Stable ABI](stable.html#stable).- Finalize a type object. This should be called on all type objects to finish their initialization. This function is responsible for adding inherited slots from a type’s base class. Return - `0`on success, or return- `-1`and sets an exception on error.- Note - If some of the base classes implements the GC protocol and the provided type does not include the - `Py_TPFLAGS_HAVE_GC`- `Py_TPFLAGS_HAVE_GC`in its flags then it- **must**implement the GC protocol itself by at least implementing the- `tp_traverse`

- 
[PyObject](structures.html#c.PyObject)*PyType_GetName([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetName)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Return the type’s name. Equivalent to getting the type’s - `__name__`- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyType_GetQualName([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetQualName)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Return the type’s qualified name. Equivalent to getting the type’s - `__qualname__`- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyType_GetFullyQualifiedName([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetFullyQualifiedName)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return the type’s fully qualified name. Equivalent to - `f"{type.__module__}.{type.__qualname__}"`, or- `type.__qualname__`- `type.__module__`- `"builtins"`.- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyType_GetModuleName([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetModuleName)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return the type’s module name. Equivalent to getting the - `type.__module__`- Added in version 3.13. 

- 
void *PyType_GetSlot([PyTypeObject](#c.PyTypeObject)*type, int slot)[¶](#c.PyType_GetSlot)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.4.- Return the function pointer stored in the given slot. If the result is - `NULL`, this indicates that either the slot is- `NULL`, or that the function was called with invalid parameters. Callers will typically cast the result pointer into the appropriate function type.- See - `PyType_Slot.slot`- *slot*argument.- Added in version 3.4. - Changed in version 3.10: - `PyType_GetSlot()`- [heap types](typeobj.html#heap-types).

- 
[PyObject](structures.html#c.PyObject)*PyType_GetModule([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetModule)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Return the module object associated with the given type when the type was created using - `PyType_FromModuleAndSpec()`- The returned reference is - [borrowed](../glossary.html#term-borrowed-reference)from- *type*, and will be valid as long as you hold a reference to- *type*. Do not release it with- `Py_DECREF()`- If no module is associated with the given type, sets - `TypeError`- `NULL`.- This function is usually used to get the module in which a method is defined. Note that in such a method, - `PyType_GetModule(Py_TYPE(self))`may not return the intended result.- `Py_TYPE(self)`may be a- *subclass*of the intended class, and subclasses are not necessarily defined in the same module as their superclass. See- `PyCMethod`- `PyType_GetModuleByDef()`- `PyCMethod`cannot be used.- Added in version 3.9. 

- 
void *PyType_GetModuleState([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_GetModuleState)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Return the state of the module object associated with the given type. This is a shortcut for calling - `PyModule_GetState()`- `PyType_GetModule()`- If no module is associated with the given type, sets - `TypeError`- `NULL`.- If the - *type*has an associated module but its state is- `NULL`, returns- `NULL`without setting an exception.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyType_GetModuleByDef([PyTypeObject](#c.PyTypeObject)*type, struct[PyModuleDef](module.html#c.PyModuleDef)*def)[¶](#c.PyType_GetModuleByDef)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Find the first superclass whose module was created from the given - `PyModuleDef`- *def*, and return that module.- If no module is found, raises a - `TypeError`- `NULL`.- This function is intended to be used together with - `PyModule_GetState()`- `tp_init`- `nb_add`- `PyCMethod`- The returned reference is - [borrowed](../glossary.html#term-borrowed-reference)from- *type*, and will be valid as long as you hold a reference to- *type*. Do not release it with- `Py_DECREF()`- Added in version 3.11. 

- 
int PyType_GetBaseByToken([PyTypeObject](#c.PyTypeObject)*type, void *token,[PyTypeObject](#c.PyTypeObject)**result)[¶](#c.PyType_GetBaseByToken)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Find the first superclass in - *type*’s- [method resolution order](../glossary.html#term-method-resolution-order)whose- `Py_tp_token`- If found, set - **result*to a new- [strong reference](../glossary.html#term-strong-reference)to it and return- `1`.
- If not found, set - **result*to- `NULL`and return- `0`.
- On error, set - **result*to- `NULL`and return- `-1`with an exception set.
 - The - *result*argument may be- `NULL`, in which case- **result*is not set. Use this if you need only the return value.- The - *token*argument may not be- `NULL`.- Added in version 3.14. 

- 
int PyUnstable_Type_AssignVersionTag([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyUnstable_Type_AssignVersionTag)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Attempt to assign a version tag to the given type. - Returns 1 if the type already had a valid version tag or a new one was assigned, or 0 if a new tag could not be assigned. - Added in version 3.12. 

- 
int PyType_SUPPORTS_WEAKREFS([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_SUPPORTS_WEAKREFS)
- Return true if instances of - *type*support creating weak references, false otherwise. This function always succeeds.- *type*must not be- `NULL`.- See also 

## Creating Heap-Allocated Types[¶](#creating-heap-allocated-types)

The following functions and structs are used to create
[heap types](typeobj.html#heap-types).

- 
[PyObject](structures.html#c.PyObject)*PyType_FromMetaclass([PyTypeObject](#c.PyTypeObject)*metaclass,[PyObject](structures.html#c.PyObject)*module,[PyType_Spec](#c.PyType_Spec)*spec,[PyObject](structures.html#c.PyObject)*bases)[¶](#c.PyType_FromMetaclass)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Create and return a - [heap type](typeobj.html#heap-types)from the- *spec*(see- `Py_TPFLAGS_HEAPTYPE`- The metaclass - *metaclass*is used to construct the resulting type object. When- *metaclass*is- `NULL`, the metaclass is derived from- *bases*(or- *Py_tp_base[s]*slots if- *bases*is- `NULL`, see below).- Metaclasses that override - `tp_new`- `tp_new`is- `NULL`.- The - *bases*argument can be used to specify base classes; it can either be only one class or a tuple of classes. If- *bases*is- `NULL`, the- `Py_tp_bases`- `NULL`, the- `Py_tp_base`- `NULL`, the new type derives from- `object`- The - *module*argument can be used to record the module in which the new class is defined. It must be a module object or- `NULL`. If not- `NULL`, the module is associated with the new type and can later be retrieved with- `PyType_GetModule()`- This function calls - `PyType_Ready()`- Note that this function does - *not*fully match the behavior of calling- `type()`- `class`- [calling](call.html#capi-call)- `type`(or the metaclass) over- `PyType_From*`functions. Specifically:- `__new__()`- `type.__new__`).
- `__init__()`
- `__init_subclass__()`
- `__set_name__()`
 - Added in version 3.12. 

- 
[PyObject](structures.html#c.PyObject)*PyType_FromModuleAndSpec([PyObject](structures.html#c.PyObject)*module,[PyType_Spec](#c.PyType_Spec)*spec,[PyObject](structures.html#c.PyObject)*bases)[¶](#c.PyType_FromModuleAndSpec)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Equivalent to - `PyType_FromMetaclass(NULL, module, spec, bases)`.- Added in version 3.9. - Changed in version 3.10: The function now accepts a single class as the - *bases*argument and- `NULL`as the- `tp_doc`slot.- Changed in version 3.12: The function now finds and uses a metaclass corresponding to the provided base classes. Previously, only - `type`- The - `tp_new`- *ignored*. which may result in incomplete initialization. Creating classes whose metaclass overrides- `tp_new`is deprecated.- Changed in version 3.14: Creating classes whose metaclass overrides - `tp_new`

- 
[PyObject](structures.html#c.PyObject)*PyType_FromSpecWithBases([PyType_Spec](#c.PyType_Spec)*spec,[PyObject](structures.html#c.PyObject)*bases)[¶](#c.PyType_FromSpecWithBases)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.3.- Equivalent to - `PyType_FromMetaclass(NULL, NULL, spec, bases)`.- Added in version 3.3. - Changed in version 3.12: The function now finds and uses a metaclass corresponding to the provided base classes. Previously, only - `type`- The - `tp_new`- *ignored*. which may result in incomplete initialization. Creating classes whose metaclass overrides- `tp_new`is deprecated.- Changed in version 3.14: Creating classes whose metaclass overrides - `tp_new`

- 
[PyObject](structures.html#c.PyObject)*PyType_FromSpec([PyType_Spec](#c.PyType_Spec)*spec)[¶](#c.PyType_FromSpec)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Equivalent to - `PyType_FromMetaclass(NULL, NULL, spec, NULL)`.- Changed in version 3.12: The function now finds and uses a metaclass corresponding to the base classes provided in - *Py_tp_base[s]*slots. Previously, only- `type`- The - `tp_new`- *ignored*. which may result in incomplete initialization. Creating classes whose metaclass overrides- `tp_new`is deprecated.- Changed in version 3.14: Creating classes whose metaclass overrides - `tp_new`

- 
int PyType_Freeze([PyTypeObject](#c.PyTypeObject)*type)[¶](#c.PyType_Freeze)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Make a type immutable: set the - `Py_TPFLAGS_IMMUTABLETYPE`- All base classes of - *type*must be immutable.- On success, return - `0`. On error, set an exception and return- `-1`.- The type must not be used before it’s made immutable. For example, type instances must not be created before the type is made immutable. - Added in version 3.14. 

- 
type PyType_Spec[¶](#c.PyType_Spec)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Structure defining a type’s behavior. - 
const char *name[¶](#c.PyType_Spec.name)
- Name of the type, used to set - `PyTypeObject.tp_name`
 - 
int basicsize[¶](#c.PyType_Spec.basicsize)
- If positive, specifies the size of the instance in bytes. It is used to set - `PyTypeObject.tp_basicsize`- If zero, specifies that - `tp_basicsize`- If negative, the absolute value specifies how much space instances of the class need - *in addition*to the superclass. Use- `PyObject_GetTypeData()`- `basicsize`, Python will insert padding when needed to meet- `tp_basicsize`- Changed in version 3.12: Previously, this field could not be negative. 
 - 
int itemsize[¶](#c.PyType_Spec.itemsize)
- Size of one element of a variable-size type, in bytes. Used to set - `PyTypeObject.tp_itemsize`- `tp_itemsize`documentation for caveats.- If zero, - `tp_itemsize`- `itemsize`is only possible in the following situations:- The base is not variable-sized (its - `tp_itemsize`
- The requested - `PyType_Spec.basicsize`
- The requested - `PyType_Spec.basicsize`
- With the - `Py_TPFLAGS_ITEMS_AT_END`
 
 - 
unsigned int flags[¶](#c.PyType_Spec.flags)
- Type flags, used to set - `PyTypeObject.tp_flags`- If the - `Py_TPFLAGS_HEAPTYPE`flag is not set,- `PyType_FromSpecWithBases()`
 - 
[PyType_Slot](#c.PyType_Slot)*slots[¶](#c.PyType_Spec.slots)
- Array of - `PyType_Slot`- `{0, NULL}`.- Each slot ID should be specified at most once. 
 
- 
const char *name

- 
type PyType_Slot[¶](#c.PyType_Slot)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Structure defining optional functionality of a type, containing a slot ID and a value pointer. - 
int slot[¶](#c.PyType_Slot.slot)
- A slot ID. - Slot IDs are named like the field names of the structures - `PyTypeObject`- `PyNumberMethods`- `PySequenceMethods`- `PyMappingMethods`- `PyAsyncMethods`- `Py_`prefix. For example, use:
- `Py_nb_add`- `PyNumberMethods.nb_add`
 - An additional slot is supported that does not correspond to a - `PyTypeObject`struct field:- The following “offset” fields cannot be set using - `PyType_Slot`- `tp_weaklistoffset`- `Py_TPFLAGS_MANAGED_WEAKREF`
- `tp_dictoffset`- `Py_TPFLAGS_MANAGED_DICT`
- `tp_vectorcall_offset`- `"__vectorcalloffset__"`in- [PyMemberDef](structures.html#pymemberdef-offsets))
 - If it is not possible to switch to a - `MANAGED`flag (for example, for vectorcall or to support Python older than 3.12), specify the offset in- `Py_tp_members`- [PyMemberDef documentation](structures.html#pymemberdef-offsets)for details.- The following internal fields cannot be set at all when creating a heap type: - `tp_dict`- `tp_mro`- `tp_cache`- `tp_subclasses`- `tp_weaklist`
 - Setting - `Py_tp_bases`- `Py_tp_base`- *bases*argument of- `PyType_FromSpecWithBases()`- Changed in version 3.9: Slots in - `PyBufferProcs`- Changed in version 3.11: - `bf_getbuffer`- `bf_releasebuffer`- [limited API](stable.html#limited-c-api).- Changed in version 3.14: The field - `tp_vectorcall`- `Py_tp_vectorcall`
 - 
void *pfunc[¶](#c.PyType_Slot.pfunc)
- The desired value of the slot. In most cases, this is a pointer to a function. - *pfunc*values may not be- `NULL`, except for the following slots:
- `Py_tp_token`- `Py_TP_USE_SPEC`- `NULL`)
 
 
- 
int slot

- 
Py_tp_token[¶](#c.Py_tp_token)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- A - `slot`- If the - `PyType_Spec`- `Py_TP_USE_SPEC`- static PyType_Slot foo_slots[] = { {Py_tp_token, Py_TP_USE_SPEC}, - It can also be set to an arbitrary pointer, but you must ensure that: - The pointer outlives the class, so it’s not reused for something else while the class exists. 
- It “belongs” to the extension module where the class lives, so it will not clash with other extensions. 
 - Use - `PyType_GetBaseByToken()`- To get the token for a given class (without considering superclasses), use - `PyType_GetSlot()`- `Py_tp_token`.- Added in version 3.14. - 
Py_TP_USE_SPEC[¶](#c.Py_TP_USE_SPEC)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Used as a value with - `Py_tp_token`- `PyType_Spec`- `NULL`.- Added in version 3.14.