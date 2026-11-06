# Thread states and the global interpreter lock — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/threads.html](https://docs.python.org/c-api/threads.html)

---

# Thread states and the global interpreter lock[¶](#thread-states-and-the-global-interpreter-lock)

Unless on a [free-threaded build](../glossary.html#term-free-threaded-build) of [CPython](../glossary.html#term-CPython),
the Python interpreter is generally not thread-safe.  In order to support
multi-threaded Python programs, there’s a global lock, called the [global
interpreter lock](../glossary.html#term-global-interpreter-lock) or [GIL](../glossary.html#term-GIL), that must be held by a thread before
accessing Python objects. Without the lock, even the simplest operations
could cause problems in a multi-threaded program: for example, when
two threads simultaneously increment the reference count of the same object, the
reference count could end up being incremented only once instead of twice.

As such, only a thread that holds the GIL may operate on Python objects or invoke Python’s C API.

In order to emulate concurrency, the interpreter regularly tries to switch
threads between bytecode instructions (see [ sys.setswitchinterval()](../library/sys.html#sys.setswitchinterval)).
This is why locks are also necessary for thread-safety in pure-Python code.

Additionally, the global interpreter lock is released around blocking I/O
operations, such as reading or writing to a file. From the C API, this is done
by [detaching the thread state](#detaching-thread-state).

The Python interpreter keeps some thread-local information inside
a data structure called [ PyThreadState](#c.PyThreadState), known as a 

[thread state](../glossary.html#term-thread-state). Each thread has a thread-local pointer to a

`PyThreadState`; a thread state
referenced by this pointer is considered to be [attached](../glossary.html#term-attached-thread-state).

A thread can only have one [attached thread state](../glossary.html#term-attached-thread-state) at a time. An attached
thread state is typically analogous with holding the GIL, except on
free-threaded builds.  On builds with the GIL enabled, attaching a thread state
will block until the GIL can be acquired. However, even on builds with the GIL
disabled, it is still required to have an attached thread state, as the interpreter
needs to keep track of which threads may access Python objects.

Note

Even on the free-threaded build, attaching a thread state may block, as the GIL can be re-enabled or threads might be temporarily suspended (such as during a garbage collection).

Generally, there will always be an attached thread state when using Python’s
C API, including during embedding and when implementing methods, so it’s uncommon
to need to set up a thread state on your own. Only in some specific cases, such
as in a [ Py_BEGIN_ALLOW_THREADS](#c.Py_BEGIN_ALLOW_THREADS) block or in a fresh thread, will the
thread not have an attached thread state.
If uncertain, check if 

[returns](#c.PyThreadState_GetUnchecked)

`PyThreadState_GetUnchecked()``NULL`.If it turns out that you do need to create a thread state, call [ PyThreadState_New()](#c.PyThreadState_New)
followed by 

[, or use the dangerous](#c.PyThreadState_Swap)

`PyThreadState_Swap()`[function.](#c.PyGILState_Ensure)

`PyGILState_Ensure()`## Detaching the thread state from extension code[¶](#detaching-the-thread-state-from-extension-code)

Most extension code manipulating the [thread state](../glossary.html#term-thread-state) has the following simple
structure:

```
Save the thread state in a local variable.
... Do some blocking I/O operation ...
Restore the thread state from the local variable.
```
This is so common that a pair of macros exists to simplify it:

```
Py_BEGIN_ALLOW_THREADS
... Do some blocking I/O operation ...
Py_END_ALLOW_THREADS
```
The [ Py_BEGIN_ALLOW_THREADS](#c.Py_BEGIN_ALLOW_THREADS) macro opens a new block and declares a
hidden local variable; the 

[macro closes the block.](#c.Py_END_ALLOW_THREADS)

`Py_END_ALLOW_THREADS`The block above expands to the following code:

```
PyThreadState *_save;
_save = PyEval_SaveThread();
... Do some blocking I/O operation ...
PyEval_RestoreThread(_save);
```
Here is how these functions work:

The attached thread state implies that the GIL is held for the interpreter.
To detach it, [ PyEval_SaveThread()](#c.PyEval_SaveThread) is called and the result is stored
in a local variable.

By detaching the thread state, the GIL is released, which allows other threads
to attach to the interpreter and execute while the current thread performs
blocking I/O. When the I/O operation is complete, the old thread state is
reattached by calling [ PyEval_RestoreThread()](#c.PyEval_RestoreThread), which will wait until
the GIL can be acquired.

Note

Performing blocking I/O is the most common use case for detaching
the thread state, but it is also useful to call it over long-running
native code that doesn’t need access to Python objects or Python’s C API.
For example, the standard [ zlib](../library/zlib.html#module-zlib) and 

[modules detach the](../library/hashlib.html#module-hashlib)

`hashlib`[thread state](../glossary.html#term-attached-thread-state)when compressing or hashing data.

On a [free-threaded build](../glossary.html#term-free-threaded-build), the [GIL](../glossary.html#term-GIL) is usually out of the question,
but **detaching the thread state is still required**, because the interpreter
periodically needs to block all threads to get a consistent view of Python objects
without the risk of race conditions.
For example, CPython currently suspends all threads for a short period of time
while running the garbage collector.

Warning

Detaching the thread state can lead to unexpected behavior during interpreter
finalization. See [Cautions regarding runtime finalization](interp-lifecycle.html#cautions-regarding-runtime-finalization) for more
details.

### APIs[¶](#apis)

The following macros are normally used without a trailing semicolon; look for example usage in the Python source distribution.

Note

These macros are still necessary on the [free-threaded build](../glossary.html#term-free-threaded-build) to prevent
deadlocks.

- 
Py_BEGIN_ALLOW_THREADS[¶](#c.Py_BEGIN_ALLOW_THREADS)
- *Part of the*- [Stable ABI](stable.html#stable).- This macro expands to - `{ PyThreadState *_save; _save = PyEval_SaveThread();`. Note that it contains an opening brace; it must be matched with a following- `Py_END_ALLOW_THREADS`

- 
Py_END_ALLOW_THREADS[¶](#c.Py_END_ALLOW_THREADS)
- *Part of the*- [Stable ABI](stable.html#stable).- This macro expands to - `PyEval_RestoreThread(_save); }`. Note that it contains a closing brace; it must be matched with an earlier- `Py_BEGIN_ALLOW_THREADS`

- 
Py_BLOCK_THREADS[¶](#c.Py_BLOCK_THREADS)
- *Part of the*- [Stable ABI](stable.html#stable).- This macro expands to - `PyEval_RestoreThread(_save);`: it is equivalent to- `Py_END_ALLOW_THREADS`

- 
Py_UNBLOCK_THREADS[¶](#c.Py_UNBLOCK_THREADS)
- *Part of the*- [Stable ABI](stable.html#stable).- This macro expands to - `_save = PyEval_SaveThread();`: it is equivalent to- `Py_BEGIN_ALLOW_THREADS`

## Non-Python created threads[¶](#non-python-created-threads)

When threads are created using the dedicated Python APIs (such as the
[ threading](../library/threading.html#module-threading) module), a thread state is automatically associated with them,
However, when a thread is created from native code (for example, by a
third-party library with its own thread management), it doesn’t hold an
attached thread state.

If you need to call Python code from these threads (often this will be part of a callback API provided by the aforementioned third-party library), you must first register these threads with the interpreter by creating a new thread state and attaching it.

The most robust way to do this is through [ PyThreadState_New()](#c.PyThreadState_New) followed
by 

[.](#c.PyThreadState_Swap)

`PyThreadState_Swap()`Note

`PyThreadState_New` requires an argument pointing to the desired
interpreter; such a pointer can be acquired via a call to
[ PyInterpreterState_Get()](subinterpreters.html#c.PyInterpreterState_Get) from the code where the thread was
created.

For example:

```
/* The return value of PyInterpreterState_Get() from the
   function that created this thread. */
PyInterpreterState *interp = thread_data->interp;
/* Create a new thread state for the interpreter. It does not start out
   attached. */
PyThreadState *tstate = PyThreadState_New(interp);
/* Attach the thread state, which will acquire the GIL. */
PyThreadState_Swap(tstate);
/* Perform Python actions here. */
result = CallSomeFunction();
/* evaluate result or handle exception */
/* Destroy the thread state. No Python API allowed beyond this point. */
PyThreadState_Clear(tstate);
PyThreadState_DeleteCurrent();
```
Warning

If the interpreter finalized before `PyThreadState_Swap` was called, then
`interp` will be a dangling pointer!

## Legacy API[¶](#legacy-api)

Another common pattern to call Python code from a non-Python thread is to use
[ PyGILState_Ensure()](#c.PyGILState_Ensure) followed by a call to 

[.](#c.PyGILState_Release)

`PyGILState_Release()`These functions do not work well when multiple interpreters exist in the Python
process. If no Python interpreter has ever been used in the current thread (which
is common for threads created outside Python), `PyGILState_Ensure` will create
and attach a thread state for the “main” interpreter (the first interpreter in
the Python process).

Additionally, these functions have thread-safety issues during interpreter
finalization. Using `PyGILState_Ensure` during finalization will likely
crash the process.

Usage of these functions look like such:

```
PyGILState_STATE gstate;
gstate = PyGILState_Ensure();
/* Perform Python actions here. */
result = CallSomeFunction();
/* evaluate result or handle exception */
/* Release the thread. No Python API allowed beyond this point. */
PyGILState_Release(gstate);
```
## Cautions about fork()[¶](#cautions-about-fork)

Another important thing to note about threads is their behaviour in the face
of the C `fork()` call. On most systems with `fork()`, after a
process forks only the thread that issued the fork will exist.  This has a
concrete impact both on how locks must be handled and on all stored state
in CPython’s runtime.

The fact that only the “current” thread remains
means any locks held by other threads will never be released. Python solves
this for [ os.fork()](../library/os.html#os.fork) by acquiring the locks it uses internally before
the fork, and releasing them afterwards. In addition, it resets any

[Lock objects](../library/threading.html#lock-objects)in the child. When extending or embedding Python, there is no way to inform Python of additional (non-Python) locks that need to be acquired before or reset after a fork. OS facilities such as

`pthread_atfork()` would need to be used to accomplish the same thing.
Additionally, when extending or embedding Python, calling `fork()`
directly rather than through `os.fork()` (and returning to or calling
into Python) may result in a deadlock by one of Python’s internal locks
being held by a thread that is defunct after the fork.
[tries to reset the necessary locks, but is not always able to.](sys.html#c.PyOS_AfterFork_Child)

`PyOS_AfterFork_Child()`The fact that all other threads go away also means that CPython’s
runtime state there must be cleaned up properly, which [ os.fork()](../library/os.html#os.fork)
does.  This means finalizing all other 

[objects belonging to the current interpreter and all other](#c.PyThreadState)

`PyThreadState`[objects. Due to this and the special nature of the](subinterpreters.html#c.PyInterpreterState)

`PyInterpreterState`[“main” interpreter](subinterpreters.html#sub-interpreter-support),

`fork()` should only be called in that interpreter’s “main”
thread, where the CPython global runtime was originally initialized.
The only exception is if `exec()` will be called immediately
after.## High-level APIs[¶](#high-level-apis)

These are the most commonly used types and functions when writing multi-threaded C extensions.

- 
type PyThreadState[¶](#c.PyThreadState)
- *Part of the*- [Limited API](stable.html#stable)(as an opaque struct).- This data structure represents the state of a single thread. The only public data member is: - 
[PyInterpreterState](subinterpreters.html#c.PyInterpreterState)*interp[¶](#c.PyThreadState.interp)
- This thread’s interpreter state. 
 
- 

- 
void PyEval_InitThreads()[¶](#c.PyEval_InitThreads)
- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated function which does nothing. - In Python 3.6 and older, this function created the GIL if it didn’t exist. - Changed in version 3.9: The function now does nothing. - Changed in version 3.7: This function is now called by - `Py_Initialize()`- Changed in version 3.2: This function cannot be called before - `Py_Initialize()`- Deprecated since version 3.9. 

- 
[PyThreadState](#c.PyThreadState)*PyEval_SaveThread()[¶](#c.PyEval_SaveThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Detach the - [attached thread state](../glossary.html#term-attached-thread-state)and return it. The thread will have no- [thread state](../glossary.html#term-thread-state)upon returning.

- 
void PyEval_RestoreThread([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyEval_RestoreThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the - [attached thread state](../glossary.html#term-attached-thread-state)to- *tstate*. The passed- [thread state](../glossary.html#term-thread-state)- **should not**be attached, otherwise deadlock ensues.- *tstate*will be attached upon returning.- Note - Calling this function from a thread when the runtime is finalizing will hang the thread until the program exits, even if the thread was not created by Python. Refer to - [Cautions regarding runtime finalization](interp-lifecycle.html#cautions-regarding-runtime-finalization)for more details.- Changed in version 3.14: Hangs the current thread, rather than terminating it, if called while the interpreter is finalizing. 

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_Get()[¶](#c.PyThreadState_Get)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the - [attached thread state](../glossary.html#term-attached-thread-state). If the thread has no attached thread state, (such as when inside of- `Py_BEGIN_ALLOW_THREADS`- `NULL`).- See also - `PyThreadState_GetUnchecked()`

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_GetUnchecked()[¶](#c.PyThreadState_GetUnchecked)
- Similar to - `PyThreadState_Get()`- Added in version 3.13: In Python 3.5 to 3.12, the function was private and known as - `_PyThreadState_UncheckedGet()`.

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_Swap([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Swap)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the - [attached thread state](../glossary.html#term-attached-thread-state)to- *tstate*, and return the- [thread state](../glossary.html#term-thread-state)that was attached prior to calling.- This function is safe to call without an - [attached thread state](../glossary.html#term-attached-thread-state); it will simply return- `NULL`indicating that there was no prior thread state.- See also - Note - Similar to - `PyGILState_Ensure()`

## GIL-state APIs[¶](#gil-state-apis)

The following functions use thread-local storage, and are not compatible with sub-interpreters:

- 
type PyGILState_STATE[¶](#c.PyGILState_STATE)
- *Part of the*- [Stable ABI](stable.html#stable).- The type of the value returned by - `PyGILState_Ensure()`- `PyGILState_Release()`- 
enumerator PyGILState_LOCKED[¶](#c.PyGILState_STATE.PyGILState_LOCKED)
- The GIL was already held when - `PyGILState_Ensure()`
 - 
enumerator PyGILState_UNLOCKED[¶](#c.PyGILState_STATE.PyGILState_UNLOCKED)
- The GIL was not held when - `PyGILState_Ensure()`
 
- 
enumerator PyGILState_LOCKED

- 
[PyGILState_STATE](#c.PyGILState_STATE)PyGILState_Ensure()[¶](#c.PyGILState_Ensure)
- *Part of the*- [Stable ABI](stable.html#stable).- Ensure that the current thread is ready to call the Python C API regardless of the current state of Python, or of the - [attached thread state](../glossary.html#term-attached-thread-state). This may be called as many times as desired by a thread as long as each call is matched with a call to- `PyGILState_Release()`- `PyGILState_Ensure()`- `PyGILState_Release()`calls as long as the thread state is restored to its previous state before the Release(). For example, normal usage of the- `Py_BEGIN_ALLOW_THREADS`- `Py_END_ALLOW_THREADS`- The return value is an opaque “handle” to the - [attached thread state](../glossary.html#term-attached-thread-state)when- `PyGILState_Ensure()`- `PyGILState_Release()`- *cannot*be shared - each unique call to- `PyGILState_Ensure()`must save the handle for its call to- `PyGILState_Release()`.- When the function returns, there will be an - [attached thread state](../glossary.html#term-attached-thread-state)and the thread will be able to call arbitrary Python code. Failure is a fatal error.- Warning - Calling this function when the runtime is finalizing is unsafe. Doing so will either hang the thread until the program ends, or fully crash the interpreter in rare cases. Refer to - [Cautions regarding runtime finalization](interp-lifecycle.html#cautions-regarding-runtime-finalization)for more details.- Changed in version 3.14: Hangs the current thread, rather than terminating it, if called while the interpreter is finalizing. 

- 
void PyGILState_Release([PyGILState_STATE](#c.PyGILState_STATE))[¶](#c.PyGILState_Release)
- *Part of the*- [Stable ABI](stable.html#stable).- Release any resources previously acquired. After this call, Python’s state will be the same as it was prior to the corresponding - `PyGILState_Ensure()`- Every call to - `PyGILState_Ensure()`- `PyGILState_Release()`

- 
[PyThreadState](#c.PyThreadState)*PyGILState_GetThisThreadState()[¶](#c.PyGILState_GetThisThreadState)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the - [attached thread state](../glossary.html#term-attached-thread-state)for this thread. May return- `NULL`if no GILState API has been used on the current thread. Note that the main thread always has such a thread-state, even if no auto-thread-state call has been made on the main thread. This is mainly a helper/diagnostic function.- Note - This function may return non- - `NULL`even when the- [thread state](../glossary.html#term-thread-state)is detached. Prefer- `PyThreadState_Get()`- `PyThreadState_GetUnchecked()`- See also 

- 
int PyGILState_Check()[¶](#c.PyGILState_Check)
- Return - `1`if the current thread is holding the- [GIL](../glossary.html#term-GIL)and- `0`otherwise. This function can be called from any thread at any time. Only if it has had its- [thread state](../glossary.html#term-attached-thread-state)initialized via- `PyGILState_Ensure()`- `1`. This is mainly a helper/diagnostic function. It can be useful for example in callback contexts or memory allocation functions when knowing that the GIL is locked can allow the caller to perform sensitive actions or otherwise behave differently.- Note - If the current Python process has ever created a subinterpreter, this function will - *always*return- `1`. Prefer- `PyThreadState_GetUnchecked()`- Added in version 3.4. 

## Low-level APIs[¶](#low-level-apis)

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_New([PyInterpreterState](subinterpreters.html#c.PyInterpreterState)*interp)[¶](#c.PyThreadState_New)
- *Part of the*- [Stable ABI](stable.html#stable).- Create a new thread state object belonging to the given interpreter object. An - [attached thread state](../glossary.html#term-attached-thread-state)is not needed.

- 
void PyThreadState_Clear([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Clear)
- *Part of the*- [Stable ABI](stable.html#stable).- Reset all information in a - [thread state](../glossary.html#term-thread-state)object.- *tstate*must be- [attached](../glossary.html#term-attached-thread-state)- Changed in version 3.9: This function now calls the - `PyThreadState.on_delete`callback. Previously, that happened in- `PyThreadState_Delete()`- Changed in version 3.13: The - `PyThreadState.on_delete`callback was removed.

- 
void PyThreadState_Delete([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Delete)
- *Part of the*- [Stable ABI](stable.html#stable).- Destroy a - [thread state](../glossary.html#term-thread-state)object.- *tstate*should not be- [attached](../glossary.html#term-attached-thread-state)to any thread.- *tstate*must have been reset with a previous call to- `PyThreadState_Clear()`

- 
void PyThreadState_DeleteCurrent(void)[¶](#c.PyThreadState_DeleteCurrent)
- Detach the - [attached thread state](../glossary.html#term-attached-thread-state)(which must have been reset with a previous call to- `PyThreadState_Clear()`- No - [thread state](../glossary.html#term-thread-state)will be- [attached](../glossary.html#term-attached-thread-state)upon returning.

- 
[PyFrameObject](frame.html#c.PyFrameObject)*PyThreadState_GetFrame([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_GetFrame)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the current frame of the Python thread state - *tstate*.- Return a - [strong reference](../glossary.html#term-strong-reference). Return- `NULL`if no frame is currently executing.- See also - `PyEval_GetFrame()`- *tstate*must not be- `NULL`, and must be- [attached](../glossary.html#term-attached-thread-state).- Added in version 3.9. 

- 
uint64_t PyThreadState_GetID([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_GetID)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the unique - [thread state](../glossary.html#term-thread-state)identifier of the Python thread state- *tstate*.- *tstate*must not be- `NULL`, and must be- [attached](../glossary.html#term-attached-thread-state).- Added in version 3.9. 

- 
[PyInterpreterState](subinterpreters.html#c.PyInterpreterState)*PyThreadState_GetInterpreter([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_GetInterpreter)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the interpreter of the Python thread state - *tstate*.- *tstate*must not be- `NULL`, and must be- [attached](../glossary.html#term-attached-thread-state).- Added in version 3.9. 

- 
void PyThreadState_EnterTracing([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_EnterTracing)
- Suspend tracing and profiling in the Python thread state - *tstate*.- Resume them using the - `PyThreadState_LeaveTracing()`- Added in version 3.11. 

- 
void PyThreadState_LeaveTracing([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_LeaveTracing)
- Resume tracing and profiling in the Python thread state - *tstate*suspended by the- `PyThreadState_EnterTracing()`- See also - `PyEval_SetTrace()`- `PyEval_SetProfile()`- Added in version 3.11. 

- 
int PyUnstable_ThreadState_SetStackProtection([PyThreadState](#c.PyThreadState)*tstate, void *stack_start_addr, size_t stack_size)[¶](#c.PyUnstable_ThreadState_SetStackProtection)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Set the stack protection start address and stack protection size of a Python thread state. - On success, return - `0`. On failure, set an exception and return- `-1`.- CPython implements - [recursion control](exceptions.html#recursion)for C code by raising- `RecursionError`- `Py_EnterRecursiveCall()`- `boost::context`, you must call- `PyUnstable_ThreadState_SetStackProtection()`- Call - `PyUnstable_ThreadState_SetStackProtection()`- See - `PyUnstable_ThreadState_ResetStackProtection()`- Added in version 3.15. 

- 
void PyUnstable_ThreadState_ResetStackProtection([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyUnstable_ThreadState_ResetStackProtection)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Reset the stack protection start address and stack protection size of a Python thread state to the operating system defaults. - See - `PyUnstable_ThreadState_SetStackProtection()`- Added in version 3.15. 

- 
[PyObject](structures.html#c.PyObject)*PyThreadState_GetDict()[¶](#c.PyThreadState_GetDict)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a dictionary in which extensions can store thread-specific state information. Each extension should use a unique key to use to store state in the dictionary. It is okay to call this function when no - [thread state](../glossary.html#term-thread-state)is- [attached](../glossary.html#term-attached-thread-state). If this function returns- `NULL`, no exception has been raised and the caller should assume no thread state is attached.

- 
void PyEval_AcquireThread([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyEval_AcquireThread)
- *Part of the*- [Stable ABI](stable.html#stable).- [Attach](../glossary.html#term-attached-thread-state)- *tstate*to the current thread, which must not be- `NULL`or already attached.- The calling thread must not already have an - [attached thread state](../glossary.html#term-attached-thread-state).- Note - Calling this function from a thread when the runtime is finalizing will hang the thread until the program exits, even if the thread was not created by Python. Refer to - [Cautions regarding runtime finalization](interp-lifecycle.html#cautions-regarding-runtime-finalization)for more details.- Changed in version 3.8: Updated to be consistent with - `PyEval_RestoreThread()`- `Py_END_ALLOW_THREADS()`- `PyGILState_Ensure()`- Changed in version 3.14: Hangs the current thread, rather than terminating it, if called while the interpreter is finalizing. - `PyEval_RestoreThread()`

- 
void PyEval_ReleaseThread([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyEval_ReleaseThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Detach the - [attached thread state](../glossary.html#term-attached-thread-state). The- *tstate*argument, which must not be- `NULL`, is only used to check that it represents the attached thread state — if it isn’t, a fatal error is reported.- `PyEval_SaveThread()`

# Asynchronous notifications[¶](#asynchronous-notifications)

A mechanism is provided to make asynchronous notifications to the main interpreter thread. These notifications take the form of a function pointer and a void pointer argument.

- 
int Py_AddPendingCall(int (*func)(void*), void *arg)[¶](#c.Py_AddPendingCall)
- *Part of the*- [Stable ABI](stable.html#stable).- Schedule a function to be called from the main interpreter thread. On success, - `0`is returned and- *func*is queued for being called in the main thread. On failure,- `-1`is returned without setting any exception.- When successfully queued, - *func*will be- *eventually*called from the main interpreter thread with the argument- *arg*. It will be called asynchronously with respect to normally running Python code, but with both these conditions met:- on a - [bytecode](../glossary.html#term-bytecode)boundary;
- with the main thread holding an - [attached thread state](../glossary.html#term-attached-thread-state)(- *func*can therefore use the full C API).
 - *func*must return- `0`on success, or- `-1`on failure with an exception set.- *func*won’t be interrupted to perform another asynchronous notification recursively, but it can still be interrupted to switch threads if the- [thread state](../glossary.html#term-attached-thread-state)is detached.- This function doesn’t need an - [attached thread state](../glossary.html#term-attached-thread-state). However, to call this function in a subinterpreter, the caller must have an attached thread state. Otherwise, the function- *func*can be scheduled to be called from the wrong interpreter.- Warning - This is a low-level function, only useful for very special cases. There is no guarantee that - *func*will be called as quick as possible. If the main thread is busy executing a system call,- *func*won’t be called before the system call returns. This function is generally- **not**suitable for calling Python code from arbitrary C threads. Instead, use the- [PyGILState API](#gilstate).- Added in version 3.1. - Changed in version 3.9: If this function is called in a subinterpreter, the function - *func*is now scheduled to be called from the subinterpreter, rather than being called from the main interpreter. Each subinterpreter now has its own list of scheduled calls.- Changed in version 3.12: This function now always schedules - *func*to be run in the main interpreter.

- 
int Py_MakePendingCalls(void)[¶](#c.Py_MakePendingCalls)
- *Part of the*- [Stable ABI](stable.html#stable).- Execute all pending calls. This is usually executed automatically by the interpreter. - This function returns - `0`on success, and returns- `-1`with an exception set on failure.- If this is not called in the main thread of the main interpreter, this function does nothing and returns - `0`. The caller must hold an- [attached thread state](../glossary.html#term-attached-thread-state).- Added in version 3.1. - Changed in version 3.12: This function only runs pending calls in the main interpreter. 

- 
int PyThreadState_SetAsyncExc(unsigned long id, [PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyThreadState_SetAsyncExc)
- *Part of the*- [Stable ABI](stable.html#stable).- Asynchronously raise an exception in a thread. The - *id*argument is the thread id of the target thread;- *exc*is the exception object to be raised. This function does not steal any references to- *exc*. To prevent naive misuse, you must write your own C extension to call this. Must be called with an- [attached thread state](../glossary.html#term-attached-thread-state). Returns the number of thread states modified; this is normally one, but will be zero if the thread id isn’t found. If- *exc*is- `NULL`, the pending exception (if any) for the thread is cleared. This raises no exceptions.- Changed in version 3.7: The type of the - *id*parameter changed from long to unsigned long.

# Operating system thread APIs[¶](#operating-system-thread-apis)

- 
PYTHREAD_INVALID_THREAD_ID[¶](#c.PYTHREAD_INVALID_THREAD_ID)
- Sentinel value for an invalid thread ID. - This is currently equivalent to - `(unsigned long)-1`.

- 
unsigned long PyThread_start_new_thread(void (*func)(void*), void *arg)[¶](#c.PyThread_start_new_thread)
- *Part of the*- [Stable ABI](stable.html#stable).- Start function - *func*in a new thread with argument- *arg*. The resulting thread is not intended to be joined.- *func*must not be- `NULL`, but- *arg*may be- `NULL`.- On success, this function returns the identifier of the new thread; on failure, this returns - `PYTHREAD_INVALID_THREAD_ID`- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
unsigned long PyThread_get_thread_ident(void)[¶](#c.PyThread_get_thread_ident)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the identifier of the current thread, which will never be zero. - This function cannot fail, and the caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).- See also 

- 
[PyObject](structures.html#c.PyObject)*PyThread_GetInfo(void)[¶](#c.PyThread_GetInfo)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.3.- Get general information about the current thread in the form of a - [struct sequence](tuple.html#struct-sequence-objects)object. This information is accessible as- `sys.thread_info`- On success, this returns a new - [strong reference](../glossary.html#term-strong-reference)to the thread information; on failure, this returns- `NULL`with an exception set.- The caller must hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
PY_HAVE_THREAD_NATIVE_ID[¶](#c.PY_HAVE_THREAD_NATIVE_ID)
- This macro is defined when the system supports native thread IDs. 

- 
unsigned long PyThread_get_thread_native_id(void)[¶](#c.PyThread_get_thread_native_id)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with native thread IDs.- Get the native identifier of the current thread as it was assigned by the operating system’s kernel, which will never be less than zero. - This function is only available when - `PY_HAVE_THREAD_NATIVE_ID`- This function cannot fail, and the caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).- See also 

- 
void PyThread_exit_thread(void)[¶](#c.PyThread_exit_thread)
- *Part of the*- [Stable ABI](stable.html#stable).- Terminate the current thread. This function is generally considered unsafe and should be avoided. It is kept solely for backwards compatibility. - This function is only safe to call if all functions in the full call stack are written to safely allow it. - Warning - If the current system uses POSIX threads (also known as “pthreads”), this calls - [pthread_exit(3)](https://manpages.debian.org/pthread_exit(3))- `noexcept`function is reached, it may terminate the process. Other systems, such as macOS, do unwinding.- On Windows, this function calls - `_endthreadex()`, which kills the thread without calling C++ destructors.- In any case, there is a risk of corruption on the thread’s stack. - Deprecated since version 3.14. 

- 
void PyThread_init_thread(void)[¶](#c.PyThread_init_thread)
- *Part of the*- [Stable ABI](stable.html#stable).- Initialize - `PyThread*`APIs. Python executes this function automatically, so there’s little need to call it from an extension module.

- 
int PyThread_set_stacksize(size_t size)[¶](#c.PyThread_set_stacksize)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the stack size of the current thread to - *size*bytes.- This function returns - `0`on success,- `-1`if- *size*is invalid, or- `-2`if the system does not support changing the stack size. This function does not set exceptions.- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
size_t PyThread_get_stacksize(void)[¶](#c.PyThread_get_stacksize)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the stack size of the current thread in bytes, or - `0`if the system’s default stack size is in use.- The caller does not need to hold an - [attached thread state](../glossary.html#term-attached-thread-state).