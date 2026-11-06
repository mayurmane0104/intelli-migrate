# Supporting Cyclic Garbage Collection — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/gcsupport.html](https://docs.python.org/c-api/gcsupport.html)

---

# Supporting Cyclic Garbage Collection[¶](#supporting-cyclic-garbage-collection)

Python’s support for detecting and collecting garbage which involves circular references requires support from object types which are “containers” for other objects which may also be containers. Types which do not store references to other objects, or which only store references to atomic types (such as numbers or strings), do not need to provide any explicit support for garbage collection.

To create a container type, the [ tp_flags](typeobj.html#c.PyTypeObject.tp_flags) field of the type object must
include the 

[and provide an implementation of the](typeobj.html#c.Py_TPFLAGS_HAVE_GC)

`Py_TPFLAGS_HAVE_GC`[handler. If instances of the type are mutable, a](typeobj.html#c.PyTypeObject.tp_traverse)

`tp_traverse`[implementation must also be provided.](typeobj.html#c.PyTypeObject.tp_clear)

`tp_clear`- `Py_TPFLAGS_HAVE_GC`
- Objects with a type with this flag set must conform with the rules documented here. For convenience these objects will be referred to as container objects. 

Constructors for container types must conform to two rules:

- The memory for the object must be allocated using - `PyObject_GC_New`- `PyObject_GC_NewVar`
- Once all the fields which may contain references to other containers are initialized, it must call - `PyObject_GC_Track()`

Similarly, the deallocator for the object must conform to a similar pair of rules:

- Before fields which refer to other containers are invalidated, - `PyObject_GC_UnTrack()`
- The object’s memory must be deallocated using - `PyObject_GC_Del()`- Warning - If a type adds the Py_TPFLAGS_HAVE_GC, then it - *must*implement at least a- `tp_traverse`- When calling - `PyType_Ready()`- `PyType_FromSpecWithBases()`- `PyType_FromSpec()`- `tp_flags`- `tp_traverse`- `tp_clear`- *not*include the- `Py_TPFLAGS_HAVE_GC`

- 
PyObject_GC_New(TYPE, typeobj)[¶](#c.PyObject_GC_New)
- Analogous to - `PyObject_New`- `Py_TPFLAGS_HAVE_GC`- Do not call this directly to allocate memory for an object; call the type’s - `tp_alloc`- When populating a type’s - `tp_alloc`- `PyType_GenericAlloc()`- Memory allocated by this macro must be freed with - `PyObject_GC_Del()`- `tp_free`

- 
PyObject_GC_NewVar(TYPE, typeobj, size)[¶](#c.PyObject_GC_NewVar)
- Analogous to - `PyObject_NewVar`- `Py_TPFLAGS_HAVE_GC`- Do not call this directly to allocate memory for an object; call the type’s - `tp_alloc`- When populating a type’s - `tp_alloc`- `PyType_GenericAlloc()`- Memory allocated by this macro must be freed with - `PyObject_GC_Del()`- `tp_free`

- 
[PyObject](structures.html#c.PyObject)*PyUnstable_Object_GC_NewWithExtraData([PyTypeObject](type.html#c.PyTypeObject)*type, size_t extra_size)[¶](#c.PyUnstable_Object_GC_NewWithExtraData)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Analogous to - `PyObject_GC_New`- *extra_size*bytes at the end of the object (at offset- `tp_basicsize`- `Python object header`- The extra data will be deallocated with the object, but otherwise it is not managed by Python. - Memory allocated by this function must be freed with - `PyObject_GC_Del()`- `tp_free`- Warning - The function is marked as unstable because the final mechanism for reserving extra data after an instance is not yet decided. For allocating a variable number of fields, prefer using - `PyVarObject`- `tp_itemsize`- Added in version 3.12. 

- 
PyObject_GC_Resize(TYPE, op, newsize)[¶](#c.PyObject_GC_Resize)
- Resize an object allocated by - `PyObject_NewVar`- `TYPE*`(refers to any C type) or- `NULL`on failure.- *op*must be of type- [PyVarObject](structures.html#c.PyVarObject)* and must not be tracked by the collector yet.- *newsize*must be of type- `Py_ssize_t`

- 
void PyObject_GC_Track([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyObject_GC_Track)
- *Part of the*- [Stable ABI](stable.html#stable).- Adds the object - *op*to the set of container objects tracked by the collector. The collector can run at unexpected times so objects must be valid while being tracked. This should be called once all the fields followed by the- `tp_traverse`

- 
int PyObject_IS_GC([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyObject_IS_GC)
- Returns non-zero if the object implements the garbage collector protocol, otherwise returns 0. - The object cannot be tracked by the garbage collector if this function returns 0. 

- 
int PyObject_GC_IsTracked([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyObject_GC_IsTracked)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Returns 1 if the object type of - *op*implements the GC protocol and- *op*is being currently tracked by the garbage collector and 0 otherwise.- This is analogous to the Python function - `gc.is_tracked()`- Added in version 3.9. 

- 
int PyObject_GC_IsFinalized([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyObject_GC_IsFinalized)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Returns 1 if the object type of - *op*implements the GC protocol and- *op*has been already finalized by the garbage collector and 0 otherwise.- This is analogous to the Python function - `gc.is_finalized()`- Added in version 3.9. 

- 
void PyObject_GC_Del(void *op)[¶](#c.PyObject_GC_Del)
- *Part of the*- [Stable ABI](stable.html#stable).- Releases memory allocated to an object using - `PyObject_GC_New`- `PyObject_GC_NewVar`- Do not call this directly to free an object’s memory; call the type’s - `tp_free`- Do not use this for memory allocated by - `PyObject_New`- `PyObject_NewVar`- `PyObject_Free()`- See also - `PyObject_Free()`
 

- 
void PyObject_GC_UnTrack(void *op)[¶](#c.PyObject_GC_UnTrack)
- *Part of the*- [Stable ABI](stable.html#stable).- Remove the object - *op*from the set of container objects tracked by the collector. Note that- `PyObject_GC_Track()`- `tp_dealloc`- `tp_traverse`

Changed in version 3.8: The `_PyObject_GC_TRACK()` and `_PyObject_GC_UNTRACK()` macros
have been removed from the public C API.

The [ tp_traverse](typeobj.html#c.PyTypeObject.tp_traverse) handler accepts a function parameter of this type:

- 
typedef int (*visitproc)([PyObject](structures.html#c.PyObject)*object, void *arg)[¶](#c.visitproc)
- *Part of the*- [Stable ABI](stable.html#stable).- Type of the visitor function passed to the - `tp_traverse`- *object*and the third parameter to the- `tp_traverse`handler as- *arg*. The Python core uses several visitor functions to implement cyclic garbage detection; it’s not expected that users will need to write their own visitor functions.

The [ tp_traverse](typeobj.html#c.PyTypeObject.tp_traverse) handler must have the following type:

- 
typedef int (*traverseproc)([PyObject](structures.html#c.PyObject)*self,[visitproc](#c.visitproc)visit, void *arg)[¶](#c.traverseproc)
- *Part of the*- [Stable ABI](stable.html#stable).- Traversal function for a container object. Implementations must call the - *visit*function for each object directly contained by- *self*, with the parameters to- *visit*being the contained object and the- *arg*value passed to the handler. The- *visit*function must not be called with a- `NULL`object argument. If- *visit*returns a non-zero value that value should be returned immediately.- The traversal function must not have any side effects. Implementations may not modify the reference counts of any Python objects nor create or destroy any Python objects. 

To simplify writing [ tp_traverse](typeobj.html#c.PyTypeObject.tp_traverse) handlers, a 

[macro is provided. In order to use this macro, the](#c.Py_VISIT)

`Py_VISIT()``tp_traverse` implementation
must name its arguments exactly *visit*and

*arg*:

- 
Py_VISIT(o)[¶](#c.Py_VISIT)
- If the - [PyObject](structures.html#c.PyObject)*- *o*is not- `NULL`, call the- *visit*callback, with arguments- *o*and- *arg*. If- *visit*returns a non-zero value, then return it. Using this macro,- `tp_traverse`- static int my_traverse(Noddy *self, visitproc visit, void *arg) { Py_VISIT(self->foo); Py_VISIT(self->bar); return 0; } 

The [ tp_clear](typeobj.html#c.PyTypeObject.tp_clear) handler must be of the 

[type, or](#c.inquiry)

`inquiry``NULL`
if the object is immutable.- 
typedef int (*inquiry)([PyObject](structures.html#c.PyObject)*self)[¶](#c.inquiry)
- *Part of the*- [Stable ABI](stable.html#stable).- Drop references that may have created reference cycles. Immutable objects do not have to define this method since they can never directly create reference cycles. Note that the object must still be valid after calling this method (don’t just call - `Py_DECREF()`

## Controlling the Garbage Collector State[¶](#controlling-the-garbage-collector-state)

The C-API provides the following functions for controlling garbage collection runs.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyGC_Collect(void)[¶](#c.PyGC_Collect)
- *Part of the*- [Stable ABI](stable.html#stable).- Perform a full garbage collection, if the garbage collector is enabled. (Note that - `gc.collect()`- Returns the number of collected + unreachable objects which cannot be collected. If the garbage collector is disabled or already collecting, returns - `0`immediately. Errors during garbage collection are passed to- `sys.unraisablehook`

- 
int PyGC_Enable(void)[¶](#c.PyGC_Enable)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Enable the garbage collector: similar to - `gc.enable()`- Added in version 3.10. 

- 
int PyGC_Disable(void)[¶](#c.PyGC_Disable)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Disable the garbage collector: similar to - `gc.disable()`- Added in version 3.10. 

- 
int PyGC_IsEnabled(void)[¶](#c.PyGC_IsEnabled)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Query the state of the garbage collector: similar to - `gc.isenabled()`- Added in version 3.10. 

## Querying Garbage Collector State[¶](#querying-garbage-collector-state)

The C-API provides the following interface for querying information about the garbage collector.

- 
void PyUnstable_GC_VisitObjects([gcvisitobjects_t](#c.gcvisitobjects_t)callback, void *arg)[¶](#c.PyUnstable_GC_VisitObjects)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Run supplied - *callback*on all live GC-capable objects.- *arg*is passed through to all invocations of- *callback*.- Warning - If new objects are (de)allocated by the callback it is undefined if they will be visited. - Garbage collection is disabled during operation. Explicitly running a collection in the callback may lead to undefined behaviour e.g. visiting the same objects multiple times or not at all. - Added in version 3.12. 

- 
typedef int (*gcvisitobjects_t)([PyObject](structures.html#c.PyObject)*object, void *arg)[¶](#c.gcvisitobjects_t)
- Type of the visitor function to be passed to - `PyUnstable_GC_VisitObjects()`- *arg*is the same as the- *arg*passed to- `PyUnstable_GC_VisitObjects`. Return- `1`to continue iteration, return- `0`to stop iteration. Other return values are reserved for now so behavior on returning anything else is undefined.- Added in version 3.12.