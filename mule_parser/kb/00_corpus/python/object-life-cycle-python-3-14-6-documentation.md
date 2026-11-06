# Object Life Cycle — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/lifecycle.html](https://docs.python.org/c-api/lifecycle.html)

---

# Object Life Cycle[¶](#object-life-cycle)

This section explains how a type’s slots relate to each other throughout the
life of an object.  It is not intended to be a complete canonical reference for
the slots; instead, refer to the slot-specific documentation in
[Type Object Structures](typeobj.html#type-structs) for details about a particular slot.

## Life Events[¶](#life-events)

The figure below illustrates the order of events that can occur throughout an
object’s life.  An arrow from *A* to *B* indicates that event *B* can occur
after event *A* has occurred, with the arrow’s label indicating the condition
that must be true for *B* to occur after *A*.

Explanation:

- When a new object is constructed by calling its type: - `tp_new`
- `tp_alloc`- `tp_new`
- `tp_init`- `tp_init`can be called again to re-initialize an object, if desired. The- `tp_init`call can also be skipped entirely, for example by Python code calling- `__new__()`
 
- After - `tp_init`completes, the object is ready to use.
- Some time after the last reference to an object is removed: - If an object is not marked as - *finalized*, it might be finalized by marking it as- *finalized*and calling its- `tp_finalize`- *not*finalize an object when the last reference to it is deleted; use- `PyObject_CallFinalizerFromDealloc()`- `tp_finalize`is always called.
- If the object is marked as finalized, - `tp_clear`- *not*called when the object’s reference count reaches zero.
- `tp_dealloc`- `tp_dealloc`typically calls into- `tp_clear`
- When - `tp_dealloc`- `tp_free`- `PyObject_Free()`- `PyObject_GC_Del()`
 
- The - `tp_finalize`- *resurrected*, preventing its pending destruction. (Only- `tp_finalize`is allowed to resurrect an object;- `tp_clear`- `tp_dealloc`- `tp_finalize`.) Resurrecting an object may or may not cause the object’s- *finalized*mark to be removed. Currently, Python does not remove the- *finalized*mark from a resurrected object if it supports garbage collection (i.e., the- `Py_TPFLAGS_HAVE_GC`
- `tp_dealloc`- `tp_finalize`- `PyObject_CallFinalizerFromDealloc()`- `tp_finalize`is always called before destruction. See the- `tp_dealloc`documentation for example code.
- If the object is a member of a - [cyclic isolate](../glossary.html#term-cyclic-isolate)and either- `tp_clear`- `gc.disable()`- `Py_TPFLAGS_HAVE_GC`- `gc.garbage`

If the object is marked as supporting garbage collection (the
[ Py_TPFLAGS_HAVE_GC](typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag is set in

[), the following events are also possible:](typeobj.html#c.PyTypeObject.tp_flags)

`tp_flags`- The garbage collector occasionally calls - `tp_traverse`- [cyclic isolates](../glossary.html#term-cyclic-isolate).
- When the garbage collector discovers a - [cyclic isolate](../glossary.html#term-cyclic-isolate), it finalizes one of the objects in the group by marking it as- *finalized*and calling its- `tp_finalize`
- `tp_finalize`- [cyclic isolate](../glossary.html#term-cyclic-isolate). The new reference causes the group of objects to no longer form a cyclic isolate (the reference cycle may still exist, but if it does the objects are no longer isolated).
- When the garbage collector discovers a - [cyclic isolate](../glossary.html#term-cyclic-isolate)and all of the objects in the group have already been marked as- *finalized*, the garbage collector clears one or more of the uncleared objects in the group (possibly concurrently) by calling each’s- `tp_clear`

## Cyclic Isolate Destruction[¶](#cyclic-isolate-destruction)

Listed below are the stages of life of a hypothetical [cyclic isolate](../glossary.html#term-cyclic-isolate)
that continues to exist after each member object is finalized or cleared.  It
is a memory leak if a cyclic isolate progresses through all of these stages; it should
vanish once all objects are cleared, if not sooner.  A cyclic isolate can
vanish either because the reference cycle is broken or because the objects are
no longer isolated due to finalizer resurrection (see
[ tp_finalize](typeobj.html#c.PyTypeObject.tp_finalize)).

- **Reachable**(not yet a cyclic isolate): All objects are in their normal, reachable state. A reference cycle could exist, but an external reference means the objects are not yet isolated.
- **Unreachable but consistent:**The final reference from outside the cyclic group of objects has been removed, causing the objects to become isolated (thus a cyclic isolate is born). None of the group’s objects have been finalized or cleared yet. The cyclic isolate remains at this stage until some future run of the garbage collector (not necessarily the next run because the next run might not scan every object).
- **Mix of finalized and not finalized:**Objects in a cyclic isolate are finalized one at a time, which means that there is a period of time when the cyclic isolate is composed of a mix of finalized and non-finalized objects. Finalization order is unspecified, so it can appear random. A finalized object must behave in a sane manner when non-finalized objects interact with it, and a non-finalized object must be able to tolerate the finalization of an arbitrary subset of its referents.
- **All finalized:**All objects in a cyclic isolate are finalized before any of them are cleared.
- **Mix of finalized and cleared:**The objects can be cleared serially or concurrently (but with the- [GIL](../glossary.html#term-GIL)held); either way, some will finish before others. A finalized object must be able to tolerate the clearing of a subset of its referents.- **PEP 442**
- **Leaked:**If a cyclic isolate still exists after all objects in the group have been finalized and cleared, then the objects remain indefinitely uncollectable (see- `gc.garbage`- `tp_clear`

If [ tp_clear](typeobj.html#c.PyTypeObject.tp_clear) did not exist, then Python would have no
way to safely break a reference cycle.  Simply destroying an object in a cyclic
isolate would result in a dangling pointer, triggering undefined behavior when
an object referencing the destroyed object is itself destroyed.  The clearing
step makes object destruction a two-phase process: first

`tp_clear` is called to partially destroy the objects
enough to detangle them from each other, then
[is called to complete the destruction.](typeobj.html#c.PyTypeObject.tp_dealloc)

`tp_dealloc`Unlike clearing, finalization is not a phase of destruction.  A finalized
object must still behave properly by continuing to fulfill its design
contracts.  An object’s finalizer is allowed to execute arbitrary Python code,
and is even allowed to prevent the impending destruction by adding a reference.
The finalizer is only related to destruction by call order—if it runs, it runs
before destruction, which starts with [ tp_clear](typeobj.html#c.PyTypeObject.tp_clear) (if
called) and concludes with 

[.](typeobj.html#c.PyTypeObject.tp_dealloc)

`tp_dealloc`The finalization step is not necessary to safely reclaim the objects in a cyclic isolate, but its existence makes it easier to design types that behave in a sane manner when objects are cleared. Clearing an object might necessarily leave it in a broken, partially destroyed state—it might be unsafe to call any of the cleared object’s methods or access any of its attributes. With finalization, only finalized objects can possibly interact with cleared objects; non-finalized objects are guaranteed to interact with only non-cleared (but potentially finalized) objects.

To summarize the possible interactions:

- A non-finalized object might have references to or from non-finalized and finalized objects, but not to or from cleared objects. 
- A finalized object might have references to or from non-finalized, finalized, and cleared objects. 
- A cleared object might have references to or from finalized and cleared objects, but not to or from non-finalized objects. 

Without any reference cycles, an object can be simply destroyed once its last
reference is deleted; the finalization and clearing steps are not necessary to
safely reclaim unused objects.  However, it can be useful to automatically call
[ tp_finalize](typeobj.html#c.PyTypeObject.tp_finalize) and 

[before destruction anyway because type design is simplified when all objects always experience the same series of events regardless of whether they participated in a cyclic isolate. Python currently only calls](typeobj.html#c.PyTypeObject.tp_clear)

`tp_clear``tp_finalize` and `tp_clear` as
needed to destroy a cyclic isolate; this may change in a future version.## Functions[¶](#functions)

To allocate and free memory, see [Allocating objects on the heap](allocation.html#allocating-objects).

- 
void PyObject_CallFinalizer([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyObject_CallFinalizer)
- Finalizes the object as described in - `tp_finalize`- `PyObject_CallFinalizerFromDealloc()`- `tp_finalize`directly because this function may deduplicate multiple calls to- `tp_finalize`. Currently, calls are only deduplicated if the type supports garbage collection (i.e., the- `Py_TPFLAGS_HAVE_GC`- Added in version 3.4. 

- 
int PyObject_CallFinalizerFromDealloc([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyObject_CallFinalizerFromDealloc)
- Same as - `PyObject_CallFinalizer()`- `tp_dealloc`- Added in version 3.4. - See also - `tp_dealloc`