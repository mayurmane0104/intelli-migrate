# Weak Reference Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/weakref.html](https://docs.python.org/c-api/weakref.html)

---

# Weak Reference Objects[¶](#weak-reference-objects)

Python supports *weak references* as first-class objects.  There are two
specific object types which directly implement weak references.  The first is a
simple reference object, and the second acts as a proxy for the original object
as much as it can.

- 
int PyWeakref_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyWeakref_Check)
- Return non-zero if - *ob*is either a reference or proxy object. This function always succeeds.

- 
int PyWeakref_CheckRef([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyWeakref_CheckRef)
- Return non-zero if - *ob*is a reference object or a subclass of the reference type. This function always succeeds.

- 
int PyWeakref_CheckRefExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyWeakref_CheckRefExact)
- Return non-zero if - *ob*is a reference object, but not a subclass of the reference type. This function always succeeds.

- 
int PyWeakref_CheckProxy([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyWeakref_CheckProxy)
- Return non-zero if - *ob*is a proxy object. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyWeakref_NewRef([PyObject](structures.html#c.PyObject)*ob,[PyObject](structures.html#c.PyObject)*callback)[¶](#c.PyWeakref_NewRef)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a weak reference object for the object - *ob*. This will always return a new reference, but is not guaranteed to create a new object; an existing reference object may be returned. The second parameter,- *callback*, can be a callable object that receives notification when- *ob*is garbage collected; it should accept a single parameter, which will be the weak reference object itself.- *callback*may also be- `None`or- `NULL`. If- *ob*is not a weakly referenceable object, this will raise- `TypeError`- `NULL`.- See also - `PyType_SUPPORTS_WEAKREFS()`- *ob*is weakly referenceable.

- 
[PyObject](structures.html#c.PyObject)*PyWeakref_NewProxy([PyObject](structures.html#c.PyObject)*ob,[PyObject](structures.html#c.PyObject)*callback)[¶](#c.PyWeakref_NewProxy)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a weak reference proxy object for the object - *ob*. This will always return a new reference, but is not guaranteed to create a new object; an existing proxy object may be returned. The second parameter,- *callback*, can be a callable object that receives notification when- *ob*is garbage collected; it should accept a single parameter, which will be the weak reference object itself.- *callback*may also be- `None`or- `NULL`. If- *ob*weakly referenceable object, this will raise- `TypeError`- `NULL`.- See also - `PyType_SUPPORTS_WEAKREFS()`- *ob*is weakly referenceable.

- 
int PyWeakref_GetRef([PyObject](structures.html#c.PyObject)*ref,[PyObject](structures.html#c.PyObject)**pobj)[¶](#c.PyWeakref_GetRef)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Get a - [strong reference](../glossary.html#term-strong-reference)to the referenced object from a weak reference,- *ref*, into- **pobj*.- On success, set - **pobj*to a new- [strong reference](../glossary.html#term-strong-reference)to the referenced object and return 1.
- If the reference is dead, set - **pobj*to- `NULL`and return 0.
- On error, raise an exception and return -1. 
 - Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyWeakref_GetObject([PyObject](structures.html#c.PyObject)*ref)[¶](#c.PyWeakref_GetObject)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a - [borrowed reference](../glossary.html#term-borrowed-reference)to the referenced object from a weak reference,- *ref*. If the referent is no longer live, returns- `Py_None`.- Note - This function returns a - [borrowed reference](../glossary.html#term-borrowed-reference)to the referenced object. This means that you should always call- `Py_INCREF()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyWeakref_GetRef()`

- 
[PyObject](structures.html#c.PyObject)*PyWeakref_GET_OBJECT([PyObject](structures.html#c.PyObject)*ref)[¶](#c.PyWeakref_GET_OBJECT)
- *Return value: Borrowed reference.*- Similar to - `PyWeakref_GetObject()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyWeakref_GetRef()`

- 
int PyWeakref_IsDead([PyObject](structures.html#c.PyObject)*ref)[¶](#c.PyWeakref_IsDead)
- Test if the weak reference - *ref*is dead. Returns 1 if the reference is dead, 0 if it is alive, and -1 with an error set if- *ref*is not a weak reference object.- Added in version 3.14. 

- 
void PyObject_ClearWeakRefs([PyObject](structures.html#c.PyObject)*object)[¶](#c.PyObject_ClearWeakRefs)
- *Part of the*- [Stable ABI](stable.html#stable).- This function is called by the - `tp_dealloc`- This iterates through the weak references for - *object*and calls callbacks for those references which have one. It returns when all callbacks have been attempted.

- 
void PyUnstable_Object_ClearWeakRefsNoCallbacks([PyObject](structures.html#c.PyObject)*object)[¶](#c.PyUnstable_Object_ClearWeakRefsNoCallbacks)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Clears the weakrefs for - *object*without calling the callbacks.- This function is called by the - `tp_dealloc`- `__del__()`- `PyObject_ClearWeakRefs()`- In most circumstances, it’s more appropriate to use - `PyObject_ClearWeakRefs()`- Added in version 3.13.