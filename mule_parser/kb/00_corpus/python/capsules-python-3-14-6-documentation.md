# Capsules — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/capsule.html](https://docs.python.org/c-api/capsule.html)

---

# Capsules[¶](#capsules)

Refer to [Providing a C API for an Extension Module](../extending/extending.html#using-capsules) for more information on using these objects.

Added in version 3.1.

- 
type PyCapsule[¶](#c.PyCapsule)
- This subtype of - `PyObject`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCapsule_Type[¶](#c.PyCapsule_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object corresponding to capsule objects. This is the same object as - `types.CapsuleType`

- 
type PyCapsule_Destructor[¶](#c.PyCapsule_Destructor)
- *Part of the*- [Stable ABI](stable.html#stable).- The type of a destructor callback for a capsule. Defined as: - typedef void (*PyCapsule_Destructor)(PyObject *); - See - `PyCapsule_New()`

- 
int PyCapsule_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyCapsule_CheckExact)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return true if its argument is a - `PyCapsule`

- 
[PyObject](structures.html#c.PyObject)*PyCapsule_New(void *pointer, const char *name,[PyCapsule_Destructor](#c.PyCapsule_Destructor)destructor)[¶](#c.PyCapsule_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Create a - `PyCapsule`- *pointer*. The- *pointer*argument may not be- `NULL`.- On failure, set an exception and return - `NULL`.- The - *name*string may either be- `NULL`or a pointer to a valid C string. If non-- `NULL`, this string must outlive the capsule. (Though it is permitted to free it inside the- *destructor*.)- If the - *destructor*argument is not- `NULL`, it will be called with the capsule as its argument when it is destroyed.- If this capsule will be stored as an attribute of a module, the - *name*should be specified as- `modulename.attributename`. This will enable other modules to import the capsule using- `PyCapsule_Import()`

- 
void *PyCapsule_GetPointer([PyObject](structures.html#c.PyObject)*capsule, const char *name)[¶](#c.PyCapsule_GetPointer)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Retrieve the - *pointer*stored in the capsule. On failure, set an exception and return- `NULL`.- The - *name*parameter must compare exactly to the name stored in the capsule. If the name stored in the capsule is- `NULL`, the- *name*passed in must also be- `NULL`. Python uses the C function- `strcmp()`to compare capsule names.

- 
[PyCapsule_Destructor](#c.PyCapsule_Destructor)PyCapsule_GetDestructor([PyObject](structures.html#c.PyObject)*capsule)[¶](#c.PyCapsule_GetDestructor)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Return the current destructor stored in the capsule. On failure, set an exception and return - `NULL`.- It is legal for a capsule to have a - `NULL`destructor. This makes a- `NULL`return code somewhat ambiguous; use- `PyCapsule_IsValid()`- `PyErr_Occurred()`

- 
void *PyCapsule_GetContext([PyObject](structures.html#c.PyObject)*capsule)[¶](#c.PyCapsule_GetContext)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Return the current context stored in the capsule. On failure, set an exception and return - `NULL`.- It is legal for a capsule to have a - `NULL`context. This makes a- `NULL`return code somewhat ambiguous; use- `PyCapsule_IsValid()`- `PyErr_Occurred()`

- 
const char *PyCapsule_GetName([PyObject](structures.html#c.PyObject)*capsule)[¶](#c.PyCapsule_GetName)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Return the current name stored in the capsule. On failure, set an exception and return - `NULL`.- It is legal for a capsule to have a - `NULL`name. This makes a- `NULL`return code somewhat ambiguous; use- `PyCapsule_IsValid()`- `PyErr_Occurred()`

- 
void *PyCapsule_Import(const char *name, int no_block)[¶](#c.PyCapsule_Import)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call from multiple threads with external synchronization only](../library/threadsafety.html#threadsafety-level-compatible).- Import a pointer to a C object from a capsule attribute in a module. The - *name*parameter should specify the full name to the attribute, as in- `module.attribute`. The- *name*stored in the capsule must match this string exactly.- This function splits - *name*on the- `.`character, and imports the first element. It then processes further elements using attribute lookups.- Return the capsule’s internal - *pointer*on success. On failure, set an exception and return- `NULL`.- Note - If - *name*points to an attribute of some submodule or subpackage, this submodule or subpackage must be previously imported using other means (for example, by using- `PyImport_ImportModule()`- Changed in version 3.3: - *no_block*has no effect anymore.

- 
int PyCapsule_IsValid([PyObject](structures.html#c.PyObject)*capsule, const char *name)[¶](#c.PyCapsule_IsValid)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Determines whether or not - *capsule*is a valid capsule. A valid capsule is non-- `NULL`, passes- `PyCapsule_CheckExact()`- `NULL`pointer stored in it, and its internal name matches the- *name*parameter. (See- `PyCapsule_GetPointer()`- In other words, if - `PyCapsule_IsValid()`- `PyCapsule_Get`) are guaranteed to succeed.- Return a nonzero value if the object is valid and matches the name passed in. Return - `0`otherwise. This function will not fail.

- 
int PyCapsule_SetContext([PyObject](structures.html#c.PyObject)*capsule, void *context)[¶](#c.PyCapsule_SetContext)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Set the context pointer inside - *capsule*to- *context*.- Return - `0`on success. Return nonzero and set an exception on failure.

- 
int PyCapsule_SetDestructor([PyObject](structures.html#c.PyObject)*capsule,[PyCapsule_Destructor](#c.PyCapsule_Destructor)destructor)[¶](#c.PyCapsule_SetDestructor)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Set the destructor inside - *capsule*to- *destructor*.- Return - `0`on success. Return nonzero and set an exception on failure.

- 
int PyCapsule_SetName([PyObject](structures.html#c.PyObject)*capsule, const char *name)[¶](#c.PyCapsule_SetName)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Set the name inside - *capsule*to- *name*. If non-- `NULL`, the name must outlive the capsule. If the previous- *name*stored in the capsule was not- `NULL`, no attempt is made to free it.- Return - `0`on success. Return nonzero and set an exception on failure.

- 
int PyCapsule_SetPointer([PyObject](structures.html#c.PyObject)*capsule, void *pointer)[¶](#c.PyCapsule_SetPointer)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Set the void pointer inside - *capsule*to- *pointer*. The pointer may not be- `NULL`.- Return - `0`on success. Return nonzero and set an exception on failure.