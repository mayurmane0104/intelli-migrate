# Operating System Utilities — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/sys.html](https://docs.python.org/c-api/sys.html)

---

# Operating System Utilities[¶](#operating-system-utilities)

- 
[PyObject](structures.html#c.PyObject)*PyOS_FSPath([PyObject](structures.html#c.PyObject)*path)[¶](#c.PyOS_FSPath)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.6.- Return the file system representation for - *path*. If the object is a- `str`- `bytes`- [strong reference](../glossary.html#term-strong-reference)is returned. If the object implements the- `os.PathLike`- `__fspath__()`- `str`or- `bytes`object. Otherwise- `TypeError`- `NULL`is returned.- Added in version 3.6. 

- 
int Py_FdIsInteractive(FILE *fp, const char *filename)[¶](#c.Py_FdIsInteractive)
- Return true (nonzero) if the standard I/O file - *fp*with name- *filename*is deemed interactive. This is the case for files for which- `isatty(fileno(fp))`is true. If the- `PyConfig.interactive`- *filename*pointer is- `NULL`or if the name is equal to one of the strings- `'<stdin>'`or- `'???'`.- This function must not be called before Python is initialized. 

- 
void PyOS_BeforeFork()[¶](#c.PyOS_BeforeFork)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with fork() since version 3.7.- Function to prepare some internal state before a process fork. This should be called before calling - `fork()`or any similar function that clones the current process. Only available on systems where- `fork()`is defined.- Warning - The C - `fork()`call should only be made from the- [“main” thread](threads.html#fork-and-threads)(of the- [“main” interpreter](subinterpreters.html#sub-interpreter-support)). The same is true for- `PyOS_BeforeFork()`.- Added in version 3.7. 

- 
void PyOS_AfterFork_Parent()[¶](#c.PyOS_AfterFork_Parent)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with fork() since version 3.7.- Function to update some internal state after a process fork. This should be called from the parent process after calling - `fork()`or any similar function that clones the current process, regardless of whether process cloning was successful. Only available on systems where- `fork()`is defined.- Warning - The C - `fork()`call should only be made from the- [“main” thread](threads.html#fork-and-threads)(of the- [“main” interpreter](subinterpreters.html#sub-interpreter-support)). The same is true for- `PyOS_AfterFork_Parent()`.- Added in version 3.7. 

- 
void PyOS_AfterFork_Child()[¶](#c.PyOS_AfterFork_Child)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with fork() since version 3.7.- Function to update internal interpreter state after a process fork. This must be called from the child process after calling - `fork()`, or any similar function that clones the current process, if there is any chance the process will call back into the Python interpreter. Only available on systems where- `fork()`is defined.- Warning - The C - `fork()`call should only be made from the- [“main” thread](threads.html#fork-and-threads)(of the- [“main” interpreter](subinterpreters.html#sub-interpreter-support)). The same is true for- `PyOS_AfterFork_Child()`.- Added in version 3.7. - See also - `os.register_at_fork()`- `PyOS_BeforeFork()`- `PyOS_AfterFork_Parent()`- `PyOS_AfterFork_Child()`

- 
void PyOS_AfterFork()[¶](#c.PyOS_AfterFork)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with fork().- Function to update some internal state after a process fork; this should be called in the new process if the Python interpreter will continue to be used. If a new executable is loaded into the new process, this function does not need to be called. - Deprecated since version 3.7: This function is superseded by - `PyOS_AfterFork_Child()`

- 
int PyOS_CheckStack()[¶](#c.PyOS_CheckStack)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with USE_STACKCHECK since version 3.7.- Return true when the interpreter runs out of stack space. This is a reliable check, but is only available when - `USE_STACKCHECK`is defined (currently on certain versions of Windows using the Microsoft Visual C++ compiler).- `USE_STACKCHECK`will be defined automatically; you should never change the definition in your own code.

- 
typedef void (*PyOS_sighandler_t)(int)[¶](#c.PyOS_sighandler_t)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyOS_sighandler_t](#c.PyOS_sighandler_t)PyOS_getsig(int i)[¶](#c.PyOS_getsig)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the current signal handler for signal - *i*. This is a thin wrapper around either- `sigaction()`or- `signal()`. Do not call those functions directly!

- 
[PyOS_sighandler_t](#c.PyOS_sighandler_t)PyOS_setsig(int i,[PyOS_sighandler_t](#c.PyOS_sighandler_t)h)[¶](#c.PyOS_setsig)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the signal handler for signal - *i*to be- *h*; return the old signal handler. This is a thin wrapper around either- `sigaction()`or- `signal()`. Do not call those functions directly!

- 
int PyOS_InterruptOccurred(void)[¶](#c.PyOS_InterruptOccurred)
- *Part of the*- [Stable ABI](stable.html#stable).- Check if a - `SIGINT`signal has been received.- Returns - `1`if a- `SIGINT`has occurred and clears the signal flag, or- `0`otherwise.- In most cases, you should prefer - `PyErr_CheckSignals()`- `PyErr_CheckSignals()`invokes the appropriate signal handlers for all pending signals, allowing Python code to handle the signal properly. This function only detects- `SIGINT`and does not invoke any Python signal handlers.- This function is async-signal-safe and this function cannot fail. The caller must hold an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
wchar_t *Py_DecodeLocale(const char *arg, size_t *size)[¶](#c.Py_DecodeLocale)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Warning - This function should not be called directly: use the - `PyConfig`- `PyConfig_SetBytesString()`- [Python is preinitialized](init_config.html#c-preinit).- This function must not be called before - [Python is preinitialized](init_config.html#c-preinit)and so that the LC_CTYPE locale is properly configured: see the- `Py_PreInitialize()`- Decode a byte string from the - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler). If the error handler is- [surrogateescape error handler](../library/codecs.html#surrogateescape), undecodable bytes are decoded as characters in range U+DC80..U+DCFF; and if a byte sequence can be decoded as a surrogate character, the bytes are escaped using the surrogateescape error handler instead of decoding them.- Return a pointer to a newly allocated wide character string, use - `PyMem_RawFree()`- `NULL`, write the number of wide characters excluding the null character into- `*size`- Return - `NULL`on decoding error or memory allocation error. If- *size*is not- `NULL`,- `*size`is set to- `(size_t)-1`on memory error or set to- `(size_t)-2`on decoding error.- The - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler)are selected by- `PyConfig_Read()`- `filesystem_encoding`- `filesystem_errors`- `PyConfig`- Decoding errors should never happen, unless there is a bug in the C library. - Use the - `Py_EncodeLocale()`- See also - The - `PyUnicode_DecodeFSDefaultAndSize()`- `PyUnicode_DecodeLocaleAndSize()`- Added in version 3.5. - Changed in version 3.7: The function now uses the UTF-8 encoding in the - [Python UTF-8 Mode](../library/os.html#utf8-mode).- Changed in version 3.8: The function now uses the UTF-8 encoding on Windows if - `PyPreConfig.legacy_windows_fs_encoding`

- 
char *Py_EncodeLocale(const wchar_t *text, size_t *error_pos)[¶](#c.Py_EncodeLocale)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Encode a wide character string to the - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler). If the error handler is- [surrogateescape error handler](../library/codecs.html#surrogateescape), surrogate characters in the range U+DC80..U+DCFF are converted to bytes 0x80..0xFF.- Return a pointer to a newly allocated byte string, use - `PyMem_Free()`- `NULL`on encoding error or memory allocation error.- If error_pos is not - `NULL`,- `*error_pos`is set to- `(size_t)-1`on success, or set to the index of the invalid character on encoding error.- The - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler)are selected by- `PyConfig_Read()`- `filesystem_encoding`- `filesystem_errors`- `PyConfig`- Use the - `Py_DecodeLocale()`- Warning - This function must not be called before - [Python is preinitialized](init_config.html#c-preinit)and so that the LC_CTYPE locale is properly configured: see the- `Py_PreInitialize()`- See also - The - `PyUnicode_EncodeFSDefault()`- `PyUnicode_EncodeLocale()`- Added in version 3.5. - Changed in version 3.7: The function now uses the UTF-8 encoding in the - [Python UTF-8 Mode](../library/os.html#utf8-mode).- Changed in version 3.8: The function now uses the UTF-8 encoding on Windows if - `PyPreConfig.legacy_windows_fs_encoding`

- 
FILE *Py_fopen([PyObject](structures.html#c.PyObject)*path, const char *mode)[¶](#c.Py_fopen)
- Similar to - `fopen()`, but- *path*is a Python object and an exception is set on error.- *path*must be a- `str`- `bytes`- [path-like object](../glossary.html#term-path-like-object).- On success, return the new file pointer. On error, set an exception and return - `NULL`.- The file must be closed by - `Py_fclose()`- `fclose()`.- The file descriptor is created non-inheritable ( - **PEP 446**- The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state).- Added in version 3.14. 

- 
int Py_fclose(FILE *file)[¶](#c.Py_fclose)
- Close a file that was opened by - `Py_fopen()`- On success, return - `0`. On error, return- `EOF`and- `errno`is set to indicate the error. In either case, any further access (including another call to- `Py_fclose()`- Added in version 3.14. 

# System Functions[¶](#system-functions)

These are utility functions that make functionality from the [ sys](../library/sys.html#module-sys) module
accessible to C code.  They all work with the current interpreter thread’s

`sys` module’s dict, which is contained in the internal thread state structure.- 
[PyObject](structures.html#c.PyObject)*PySys_GetObject(const char *name)[¶](#c.PySys_GetObject)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the object - *name*from the- `sys`- `NULL`if it does not exist, without setting an exception.

- 
int PySys_SetObject(const char *name, [PyObject](structures.html#c.PyObject)*v)[¶](#c.PySys_SetObject)
- *Part of the*- [Stable ABI](stable.html#stable).- Set - *name*in the- `sys`- *v*unless- *v*is- `NULL`, in which case- *name*is deleted from the sys module. Returns- `0`on success,- `-1`on error.

- 
void PySys_ResetWarnOptions()[¶](#c.PySys_ResetWarnOptions)
- *Part of the*- [Stable ABI](stable.html#stable).- Reset - `sys.warnoptions`- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Clear - `sys.warnoptions`- `warnings.filters`instead.

- 
void PySys_WriteStdout(const char *format, ...)[¶](#c.PySys_WriteStdout)
- *Part of the*- [Stable ABI](stable.html#stable).- Write the output string described by - *format*to- `sys.stdout`- *format*should limit the total size of the formatted output string to 1000 bytes or less – after 1000 bytes, the output string is truncated. In particular, this means that no unrestricted “%s” formats should occur; these should be limited using “%.<N>s” where <N> is a decimal number calculated so that <N> plus the maximum size of other formatted text does not exceed 1000 bytes. Also watch out for “%f”, which can print hundreds of digits for very large numbers.- If a problem occurs, or - `sys.stdout`- *stdout*.

- 
void PySys_WriteStderr(const char *format, ...)[¶](#c.PySys_WriteStderr)
- *Part of the*- [Stable ABI](stable.html#stable).- As - `PySys_WriteStdout()`- `sys.stderr`- *stderr*instead.

- 
void PySys_FormatStdout(const char *format, ...)[¶](#c.PySys_FormatStdout)
- *Part of the*- [Stable ABI](stable.html#stable).- Function similar to PySys_WriteStdout() but format the message using - `PyUnicode_FromFormatV()`- Added in version 3.2. 

- 
void PySys_FormatStderr(const char *format, ...)[¶](#c.PySys_FormatStderr)
- *Part of the*- [Stable ABI](stable.html#stable).- As - `PySys_FormatStdout()`- `sys.stderr`- *stderr*instead.- Added in version 3.2. 

- 
[PyObject](structures.html#c.PyObject)*PySys_GetXOptions()[¶](#c.PySys_GetXOptions)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return the current dictionary of - `-X`- `sys._xoptions`- `NULL`is returned and an exception is set.- Added in version 3.2. 

- 
int PySys_Audit(const char *event, const char *format, ...)[¶](#c.PySys_Audit)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Raise an auditing event with any active hooks. Return zero for success and non-zero with an exception set on failure. - The - *event*string argument must not be- *NULL*.- If any hooks have been added, - *format*and other arguments will be used to construct a tuple to pass. Apart from- `N`, the same format characters as used in- `Py_BuildValue()`- The - `N`format option must not be used. It consumes a reference, but since there is no way to know whether arguments to this function will be consumed, using it may cause reference leaks.- Note that - `#`format characters should always be treated as- `Py_ssize_t`- `PY_SSIZE_T_CLEAN`was defined.- `sys.audit()`- See also - `PySys_AuditTuple()`- Added in version 3.8. - Changed in version 3.8.2: Require - `Py_ssize_t`- `#`format characters. Previously, an unavoidable deprecation warning was raised.

- 
int PySys_AuditTuple(const char *event, [PyObject](structures.html#c.PyObject)*args)[¶](#c.PySys_AuditTuple)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Similar to - `PySys_Audit()`- *args*must be a- `tuple`- *args*can be- *NULL*.- Added in version 3.13. 

- 
int PySys_AddAuditHook([Py_AuditHookFunction](#c.Py_AuditHookFunction)hook, void *userData)[¶](#c.PySys_AddAuditHook)
- Append the callable - *hook*to the list of active auditing hooks. Return zero on success and non-zero on failure. If the runtime has been initialized, also set an error on failure. Hooks added through this API are called for all interpreters created by the runtime.- The - *userData*pointer is passed into the hook function. Since hook functions may be called from different runtimes, this pointer should not refer directly to Python state.- This function is safe to call before - `Py_Initialize()`- `Exception`- The hook function is always called with an - [attached thread state](../glossary.html#term-attached-thread-state)by the Python interpreter that raised the event.- See - **PEP 578**- [audit events table](../library/audit_events.html#audit-events). Details are in each function’s documentation.- If the interpreter is initialized, this function raises an auditing event - `sys.addaudithook`with no arguments. If any existing hooks raise an exception derived from- `Exception`- 
typedef int (*Py_AuditHookFunction)(const char *event, [PyObject](structures.html#c.PyObject)*args, void *userData)[¶](#c.Py_AuditHookFunction)
- The type of the hook function. - *event*is the C string event argument passed to- `PySys_Audit()`- `PySys_AuditTuple()`- *args*is guaranteed to be a- `PyTupleObject`- *userData*is the argument passed to PySys_AddAuditHook().
 - Added in version 3.8. 
- 
typedef int (*Py_AuditHookFunction)(const char *event, 

# Process Control[¶](#process-control)

- 
void Py_FatalError(const char *message)[¶](#c.Py_FatalError)
- *Part of the*- [Stable ABI](stable.html#stable).- Print a fatal error message and kill the process. No cleanup is performed. This function should only be invoked when a condition is detected that would make it dangerous to continue using the Python interpreter; e.g., when the object administration appears to be corrupted. On Unix, the standard C library function - `abort()`is called which will attempt to produce a- `core`file.- The - `Py_FatalError()`function is replaced with a macro which logs automatically the name of the current function, unless the- `Py_LIMITED_API`macro is defined.- Changed in version 3.9: Log the function name automatically. 

- 
void Py_Exit(int status)[¶](#c.Py_Exit)
- *Part of the*- [Stable ABI](stable.html#stable).- Exit the current process. This calls - `Py_FinalizeEx()`- `exit(status)`. If- `Py_FinalizeEx()`indicates an error, the exit status is set to 120.- Changed in version 3.6: Errors from finalization no longer ignored. 

- 
int Py_AtExit(void (*func)())[¶](#c.Py_AtExit)
- *Part of the*- [Stable ABI](stable.html#stable).- Register a cleanup function to be called by - `Py_FinalizeEx()`- `Py_AtExit()`- `0`; on failure, it returns- `-1`. The cleanup function registered last is called first. Each cleanup function will be called at most once. Since Python’s internal finalization will have completed before the cleanup function, no Python APIs should be called by- *func*.- See also - `PyUnstable_AtExit()`- `void *data`argument.