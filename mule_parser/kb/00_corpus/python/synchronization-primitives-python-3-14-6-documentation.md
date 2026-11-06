# Synchronization primitives — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/synchronization.html](https://docs.python.org/c-api/synchronization.html)

---

# Synchronization primitives[¶](#synchronization-primitives)

The C-API provides a basic mutual exclusion lock.

- 
type PyMutex[¶](#c.PyMutex)
- A mutual exclusion lock. The - `PyMutex`should be initialized to zero to represent the unlocked state. For example:- PyMutex mutex = {0}; - Instances of - `PyMutex`should not be copied or moved. Both the contents and address of a- `PyMutex`are meaningful, and it must remain at a fixed, writable location in memory.- Note - A - `PyMutex`currently occupies one byte, but the size should be considered unstable. The size may change in future Python releases without a deprecation period.- Added in version 3.13. 

- 
void PyMutex_Lock([PyMutex](#c.PyMutex)*m)[¶](#c.PyMutex_Lock)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Lock mutex - *m*. If another thread has already locked it, the calling thread will block until the mutex is unlocked. While blocked, the thread will temporarily detach the- [thread state](../glossary.html#term-attached-thread-state)if one exists.- Added in version 3.13. 

- 
void PyMutex_Unlock([PyMutex](#c.PyMutex)*m)[¶](#c.PyMutex_Unlock)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Unlock mutex - *m*. The mutex must be locked — otherwise, the function will issue a fatal error.- Added in version 3.13. 

- 
int PyMutex_IsLocked([PyMutex](#c.PyMutex)*m)[¶](#c.PyMutex_IsLocked)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Returns non-zero if the mutex - *m*is currently locked, zero otherwise.- Note - This function is intended for use in assertions and debugging only and should not be used to make concurrency control decisions, as the lock state may change immediately after the check. - Added in version 3.14. 

## Python critical section API[¶](#python-critical-section-api)

The critical section API provides a deadlock avoidance layer on top of
per-object locks for [free-threaded](../glossary.html#term-free-threading) CPython.  They are
intended to replace reliance on the [global interpreter lock](../glossary.html#term-global-interpreter-lock), and are
no-ops in versions of Python with the global interpreter lock.

Critical sections are intended to be used for custom types implemented
in C-API extensions. They should generally not be used with built-in types like
[ list](../library/stdtypes.html#list) and 

[because their public C-APIs already use critical sections internally, with the notable exception of](../library/stdtypes.html#dict)

`dict`[, which requires critical section to be acquired externally.](dict.html#c.PyDict_Next)

`PyDict_Next()`Critical sections avoid deadlocks by implicitly suspending active critical
sections, hence, they do not provide exclusive access such as provided by
traditional locks like [ PyMutex](#c.PyMutex).  When a critical section is started,
the per-object lock for the object is acquired. If the code executed inside the
critical section calls C-API functions then it can suspend the critical section thereby
releasing the per-object lock, so other threads can acquire the per-object lock
for the same object.

Variants that accept [ PyMutex](#c.PyMutex) pointers rather than Python objects are also
available. Use these variants to start a critical section in a situation where
there is no 

[– for example, when working with a C type that does not extend or wrap](structures.html#c.PyObject)

`PyObject``PyObject` but still needs to call into the C
API in a manner that might lead to deadlocks.The functions and structs used by the macros are exposed for cases where C macros are not available. They should only be used as in the given macro expansions. Note that the sizes and contents of the structures may change in future Python versions.

Note

Operations that need to lock two objects at once must use
[ Py_BEGIN_CRITICAL_SECTION2](#c.Py_BEGIN_CRITICAL_SECTION2).  You 

*cannot*use nested critical sections to lock more than one object at once, because the inner critical section may suspend the outer critical sections. This API does not provide a way to lock more than two objects at once.

Example usage:

```
static PyObject *
set_field(MyObject *self, PyObject *value)
{
   Py_BEGIN_CRITICAL_SECTION(self);
   Py_SETREF(self->field, Py_XNewRef(value));
   Py_END_CRITICAL_SECTION();
   Py_RETURN_NONE;
}
```
In the above example, [ Py_SETREF](refcounting.html#c.Py_SETREF) calls 

[, which can call arbitrary code through an object’s deallocation function. The critical section API avoids potential deadlocks due to reentrancy and lock ordering by allowing the runtime to temporarily suspend the critical section if the code triggered by the finalizer blocks and calls](refcounting.html#c.Py_DECREF)

`Py_DECREF`[.](threads.html#c.PyEval_SaveThread)

`PyEval_SaveThread()`- 
Py_BEGIN_CRITICAL_SECTION(op)[¶](#c.Py_BEGIN_CRITICAL_SECTION)
- Acquires the per-object lock for the object - *op*and begins a critical section.- In the free-threaded build, this macro expands to: - { PyCriticalSection _py_cs; PyCriticalSection_Begin(&_py_cs, (PyObject*)(op)) - In the default build, this macro expands to - `{`.- Added in version 3.13. 

- 
Py_BEGIN_CRITICAL_SECTION_MUTEX(m)[¶](#c.Py_BEGIN_CRITICAL_SECTION_MUTEX)
- Locks the mutex - *m*and begins a critical section.- In the free-threaded build, this macro expands to: - { PyCriticalSection _py_cs; PyCriticalSection_BeginMutex(&_py_cs, m) - Note that unlike - `Py_BEGIN_CRITICAL_SECTION`- `PyMutex`- On the default build, this macro expands to - `{`.- Added in version 3.14. 

- 
Py_END_CRITICAL_SECTION()[¶](#c.Py_END_CRITICAL_SECTION)
- Ends the critical section and releases the per-object lock. - In the free-threaded build, this macro expands to: - PyCriticalSection_End(&_py_cs); } - In the default build, this macro expands to - `}`.- Added in version 3.13. 

- 
Py_BEGIN_CRITICAL_SECTION2(a, b)[¶](#c.Py_BEGIN_CRITICAL_SECTION2)
- Acquires the per-object locks for the objects - *a*and- *b*and begins a critical section. The locks are acquired in a consistent order (lowest address first) to avoid lock ordering deadlocks.- In the free-threaded build, this macro expands to: - { PyCriticalSection2 _py_cs2; PyCriticalSection2_Begin(&_py_cs2, (PyObject*)(a), (PyObject*)(b)) - In the default build, this macro expands to - `{`.- Added in version 3.13. 

- 
Py_BEGIN_CRITICAL_SECTION2_MUTEX(m1, m2)[¶](#c.Py_BEGIN_CRITICAL_SECTION2_MUTEX)
- Locks the mutexes - *m1*and- *m2*and begins a critical section.- In the free-threaded build, this macro expands to: - { PyCriticalSection2 _py_cs2; PyCriticalSection2_BeginMutex(&_py_cs2, m1, m2) - Note that unlike - `Py_BEGIN_CRITICAL_SECTION2`- `PyMutex`- On the default build, this macro expands to - `{`.- Added in version 3.14. 

- 
Py_END_CRITICAL_SECTION2()[¶](#c.Py_END_CRITICAL_SECTION2)
- Ends the critical section and releases the per-object locks. - In the free-threaded build, this macro expands to: - PyCriticalSection2_End(&_py_cs2); } - In the default build, this macro expands to - `}`.- Added in version 3.13. 

## Legacy locking APIs[¶](#legacy-locking-apis)

These APIs are obsolete since Python 3.13 with the introduction of
[ PyMutex](#c.PyMutex).

- 
type PyThread_type_lock[¶](#c.PyThread_type_lock)
- A pointer to a mutual exclusion lock. 

- 
type PyLockStatus[¶](#c.PyLockStatus)
- The result of acquiring a lock with a timeout. - 
enumerator PY_LOCK_FAILURE[¶](#c.PY_LOCK_FAILURE)
- Failed to acquire the lock. 
 - 
enumerator PY_LOCK_ACQUIRED[¶](#c.PY_LOCK_ACQUIRED)
- The lock was successfully acquired. 
 - 
enumerator PY_LOCK_INTR[¶](#c.PY_LOCK_INTR)
- The lock was interrupted by a signal. 
 
- 
enumerator PY_LOCK_FAILURE

- 
[PyThread_type_lock](#c.PyThread_type_lock)PyThread_allocate_lock(void)[¶](#c.PyThread_allocate_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Allocate a new lock. - On success, this function returns a lock; on failure, this function returns - `0`without an exception set.- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
void PyThread_free_lock([PyThread_type_lock](#c.PyThread_type_lock)lock)[¶](#c.PyThread_free_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Destroy - *lock*. The lock should not be held by any thread when calling this.- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
[PyLockStatus](#c.PyLockStatus)PyThread_acquire_lock_timed([PyThread_type_lock](#c.PyThread_type_lock)lock, long long microseconds, int intr_flag)[¶](#c.PyThread_acquire_lock_timed)
- *Part of the*- [Stable ABI](stable.html#stable).- Acquire - *lock*with a timeout.- This will wait for - *microseconds*microseconds to acquire the lock. If the timeout expires, this function returns- `PY_LOCK_FAILURE`- *microseconds*is- `-1`, this will wait indefinitely until the lock has been released.- If - *intr_flag*is- `1`, acquiring the lock may be interrupted by a signal, in which case this function returns- `PY_LOCK_INTR`- `Py_MakePendingCalls()`- If the lock is successfully acquired, this function returns - `PY_LOCK_ACQUIRED`- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
int PyThread_acquire_lock([PyThread_type_lock](#c.PyThread_type_lock)lock, int waitflag)[¶](#c.PyThread_acquire_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Acquire - *lock*.- If - *waitflag*is- `1`and another thread currently holds the lock, this function will wait until the lock can be acquired and will always return- `1`.- If - *waitflag*is- `0`and another thread holds the lock, this function will not wait and instead return- `0`. If the lock is not held by any other thread, then this function will acquire it and return- `1`.- Unlike - `PyThread_acquire_lock_timed()`- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
int PyThread_release_lock([PyThread_type_lock](#c.PyThread_type_lock)lock)[¶](#c.PyThread_release_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Release - *lock*. If- *lock*is not held, then this function issues a fatal error.- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).