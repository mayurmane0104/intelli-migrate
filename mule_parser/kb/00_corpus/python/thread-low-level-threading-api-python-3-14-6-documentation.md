# _thread — Low-level threading API — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/_thread.html](https://docs.python.org/library/_thread.html)

---

`_thread` — Low-level threading API[¶](#module-_thread)

This module provides low-level primitives for working with multiple threads
(also called *light-weight processes* or *tasks*) — multiple threads of
control sharing their global data space.  For synchronization, simple locks
(also called *mutexes* or *binary semaphores*) are provided.
The [ threading](threading.html#module-threading) module provides an easier to use and higher-level
threading API built on top of this module.

Changed in version 3.7: This module used to be optional, it is now always available.

This module defines the following constants and functions:

- 
*exception*_thread.error[¶](#thread.error)
- Raised on thread-specific errors. - Changed in version 3.3: This is now a synonym of the built-in - `RuntimeError`

- 
_thread.start_new_thread(*function*,*args*[,*kwargs*])[¶](#thread.start_new_thread)
- Start a new thread and return its identifier. The thread executes the function - *function*with the argument list- *args*(which must be a tuple). The optional- *kwargs*argument specifies a dictionary of keyword arguments.- When the function returns, the thread silently exits. - When the function terminates with an unhandled exception, - `sys.unraisablehook()`- *object*attribute of the hook argument is- *function*. By default, a stack trace is printed and then the thread exits (but other threads continue to run).- When the function raises a - `SystemExit`- Raises an - [auditing event](sys.html#auditing)- `_thread.start_new_thread`with arguments- `function`,- `args`,- `kwargs`.- Changed in version 3.8: - `sys.unraisablehook()`

- 
_thread.interrupt_main(*signum=signal.SIGINT*,*/*)[¶](#thread.interrupt_main)
- Simulate the effect of a signal arriving in the main thread. A thread can use this function to interrupt the main thread, though there is no guarantee that the interruption will happen immediately. - If given, - *signum*is the number of the signal to simulate. If- *signum*is not given,- `signal.SIGINT`- If the given signal isn’t handled by Python (it was set to - `signal.SIG_DFL`- `signal.SIG_IGN`- Changed in version 3.10: The - *signum*argument is added to customize the signal number.- Note - This does not emit the corresponding signal but schedules a call to the associated handler (if it exists). If you want to truly emit the signal, use - `signal.raise_signal()`

- 
_thread.exit()[¶](#thread.exit)
- Raise the - `SystemExit`

- 
_thread.allocate_lock()[¶](#thread.allocate_lock)
- Return a new lock object. Methods of locks are described below. The lock is initially unlocked. 

- 
_thread.get_ident()[¶](#thread.get_ident)
- Return the ‘thread identifier’ of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created. 

- 
_thread.get_native_id()[¶](#thread.get_native_id)
- Return the native integral Thread ID of the current thread assigned by the kernel. This is a non-negative integer. Its value may be used to uniquely identify this particular thread system-wide (until the thread terminates, after which the value may be recycled by the OS). - [Availability](intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD.- Added in version 3.8. - Changed in version 3.13: Added support for GNU/kFreeBSD. 

- 
_thread.stack_size([*size*])[¶](#thread.stack_size)
- Return the thread stack size used when creating new threads. The optional - *size*argument specifies the stack size to be used for subsequently created threads, and must be 0 (use platform or configured default) or a positive integer value of at least 32,768 (32 KiB). If- *size*is not specified, 0 is used. If changing the thread stack size is unsupported, a- `RuntimeError`- `ValueError`- [Availability](intro.html#availability): Windows, pthreads.- Unix platforms with POSIX threads support. 

- 
_thread.TIMEOUT_MAX[¶](#thread.TIMEOUT_MAX)
- The maximum value allowed for the - *timeout*parameter of- `Lock.acquire`- `OverflowError`- Added in version 3.2. 

- 
*class*_thread.LockType[¶](#thread.LockType)
- This is the type of lock objects. - Lock objects have the following methods: - 
acquire(*blocking=True*,*timeout=-1*)[¶](#thread.LockType.acquire)
- Without any optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread (only one thread at a time can acquire a lock — that’s their reason for existence). - If the - *blocking*argument is present, the action depends on its value: if it is false, the lock is only acquired if it can be acquired immediately without waiting, while if it is true, the lock is acquired unconditionally as above.- If the floating-point - *timeout*argument is present and positive, it specifies the maximum wait time in seconds before returning. A negative- *timeout*argument specifies an unbounded wait. You cannot specify a- *timeout*if- *blocking*is false.- The return value is - `True`if the lock is acquired successfully,- `False`if not.- Changed in version 3.2: The - *timeout*parameter is new.- Changed in version 3.2: Lock acquires can now be interrupted by signals on POSIX. - Changed in version 3.14: Lock acquires can now be interrupted by signals on Windows. 
 - 
release()[¶](#thread.LockType.release)
- Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread. 
 - 
locked()[¶](#thread.LockType.locked)
- Return the status of the lock: - `True`if it has been acquired by some thread,- `False`if not.
 - In addition to these methods, lock objects can also be used via the - `with`- import _thread a_lock = _thread.allocate_lock() with a_lock: print("a_lock is locked while this executes") 
- 
acquire(

**Caveats:**

- Interrupts always go to the main thread (the - `KeyboardInterrupt`
- Calling - `sys.exit()`- `SystemExit`- `_thread.exit()`
- When the main thread exits, it is system defined whether the other threads survive. On most systems, they are killed without executing - `try`- `finally`