# Exception Handling — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/exceptions.html](https://docs.python.org/c-api/exceptions.html)

---

# Exception Handling[¶](#exception-handling)

The functions described in this chapter will let you handle and raise Python
exceptions.  It is important to understand some of the basics of Python
exception handling.  It works somewhat like the POSIX `errno` variable:
there is a global indicator (per thread) of the last error that occurred.  Most
C API functions don’t clear this on success, but will set it to indicate the
cause of the error on failure.  Most C API functions also return an error
indicator, usually `NULL` if they are supposed to return a pointer, or `-1`
if they return an integer (exception: the `PyArg_*` functions
return `1` for success and `0` for failure).

Concretely, the error indicator consists of three object pointers: the
exception’s type, the exception’s value, and the traceback object.  Any
of those pointers can be `NULL` if non-set (although some combinations are
forbidden, for example you can’t have a non-`NULL` traceback if the exception
type is `NULL`).

When a function must fail because some function it called failed, it generally
doesn’t set the error indicator; the function it called already set it.  It is
responsible for either handling the error and clearing the exception or
returning after cleaning up any resources it holds (such as object references or
memory allocations); it should *not* continue normally if it is not prepared to
handle the error.  If returning due to an error, it is important to indicate to
the caller that an error has been set.  If the error is not handled or carefully
propagated, additional calls into the Python/C API may not behave as intended
and may fail in mysterious ways.

Note

The error indicator is **not** the result of [ sys.exc_info()](../library/sys.html#sys.exc_info).
The former corresponds to an exception that is not yet caught (and is
therefore still propagating), while the latter returns an exception after
it is caught (and has therefore stopped propagating).

## Printing and clearing[¶](#printing-and-clearing)

- 
void PyErr_Clear()[¶](#c.PyErr_Clear)
- *Part of the*- [Stable ABI](stable.html#stable).- Clear the error indicator. If the error indicator is not set, there is no effect. 

- 
void PyErr_PrintEx(int set_sys_last_vars)[¶](#c.PyErr_PrintEx)
- *Part of the*- [Stable ABI](stable.html#stable).- Print a standard traceback to - `sys.stderr`and clear the error indicator.- **Unless**the error is a- `SystemExit`, in that case no traceback is printed and the Python process will exit with the error code specified by the- `SystemExit`instance.- Call this function - **only**when the error indicator is set. Otherwise it will cause a fatal error!- If - *set_sys_last_vars*is nonzero, the variable- `sys.last_exc`- `sys.last_type`- `sys.last_value`- `sys.last_traceback`- Changed in version 3.12: The setting of - `sys.last_exc`

- 
void PyErr_Print()[¶](#c.PyErr_Print)
- *Part of the*- [Stable ABI](stable.html#stable).- Alias for - `PyErr_PrintEx(1)`.

- 
void PyErr_WriteUnraisable([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyErr_WriteUnraisable)
- *Part of the*- [Stable ABI](stable.html#stable).- Call - `sys.unraisablehook()`- *obj*argument.- This utility function prints a warning message to - `sys.stderr`when an exception has been set but it is impossible for the interpreter to actually raise the exception. It is used, for example, when an exception occurs in an- `__del__()`- The function is called with a single argument - *obj*that identifies the context in which the unraisable exception occurred. If possible, the repr of- *obj*will be printed in the warning message. If- *obj*is- `NULL`, only the traceback is printed.- An exception must be set when calling this function. - Changed in version 3.4: Print a traceback. Print only traceback if - *obj*is- `NULL`.- Changed in version 3.8: Use - `sys.unraisablehook()`

- 
void PyErr_FormatUnraisable(const char *format, ...)[¶](#c.PyErr_FormatUnraisable)
- Similar to - `PyErr_WriteUnraisable()`- *format*and subsequent parameters help format the warning message; they have the same meaning and values as in- `PyUnicode_FromFormat()`- `PyErr_WriteUnraisable(obj)`is roughly equivalent to- `PyErr_FormatUnraisable("Exception ignored in: %R", obj)`. If- *format*is- `NULL`, only the traceback is printed.- Added in version 3.13. 

- 
void PyErr_DisplayException([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyErr_DisplayException)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Print the standard traceback display of - `exc`to- `sys.stderr`, including chained exceptions and notes.- Added in version 3.12. 

## Raising exceptions[¶](#raising-exceptions)

These functions help you set the current thread’s error indicator.
For convenience, some of these functions will always return a
`NULL` pointer for use in a `return` statement.

- 
void PyErr_SetString([PyObject](structures.html#c.PyObject)*type, const char *message)[¶](#c.PyErr_SetString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the most common way to set the error indicator. The first argument specifies the exception type; it is normally one of the standard exceptions, e.g. - `PyExc_RuntimeError`- [strong reference](../glossary.html#term-strong-reference)to it (e.g. with- `Py_INCREF()`- `'utf-8'`.

- 
void PyErr_SetObject([PyObject](structures.html#c.PyObject)*type,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyErr_SetObject)
- *Part of the*- [Stable ABI](stable.html#stable).- This function is similar to - `PyErr_SetString()`

- 
[PyObject](structures.html#c.PyObject)*PyErr_Format([PyObject](structures.html#c.PyObject)*exception, const char *format, ...)[¶](#c.PyErr_Format)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable).- This function sets the error indicator and returns - `NULL`.- *exception*should be a Python exception class. The- *format*and subsequent parameters help format the error message; they have the same meaning and values as in- `PyUnicode_FromFormat()`- *format*is an ASCII-encoded string.

- 
[PyObject](structures.html#c.PyObject)*PyErr_FormatV([PyObject](structures.html#c.PyObject)*exception, const char *format, va_list vargs)[¶](#c.PyErr_FormatV)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.5.- Same as - `PyErr_Format()`- `va_list`argument rather than a variable number of arguments.- Added in version 3.5. 

- 
void PyErr_SetNone([PyObject](structures.html#c.PyObject)*type)[¶](#c.PyErr_SetNone)
- *Part of the*- [Stable ABI](stable.html#stable).- This is a shorthand for - `PyErr_SetObject(type, Py_None)`.

- 
int PyErr_BadArgument()[¶](#c.PyErr_BadArgument)
- *Part of the*- [Stable ABI](stable.html#stable).- This is a shorthand for - `PyErr_SetString(PyExc_TypeError, message)`, where- *message*indicates that a built-in operation was invoked with an illegal argument. It is mostly for internal use.

- 
[PyObject](structures.html#c.PyObject)*PyErr_NoMemory()[¶](#c.PyErr_NoMemory)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable).- This is a shorthand for - `PyErr_SetNone(PyExc_MemoryError)`; it returns- `NULL`so an object allocation function can write- `return PyErr_NoMemory();`when it runs out of memory.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetFromErrno([PyObject](structures.html#c.PyObject)*type)[¶](#c.PyErr_SetFromErrno)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable).- This is a convenience function to raise an exception when a C library function has returned an error and set the C variable - `errno`. It constructs a tuple object whose first item is the integer- `errno`value and whose second item is the corresponding error message (gotten from- `strerror()`), and then calls- `PyErr_SetObject(type, object)`. On Unix, when the- `errno`value is- `EINTR`, indicating an interrupted system call, this calls- `PyErr_CheckSignals()`- `NULL`, so a wrapper function around a system call can write- `return PyErr_SetFromErrno(type);`when the system call returns an error.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetFromErrnoWithFilenameObject([PyObject](structures.html#c.PyObject)*type,[PyObject](structures.html#c.PyObject)*filenameObject)[¶](#c.PyErr_SetFromErrnoWithFilenameObject)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyErr_SetFromErrno()`- *filenameObject*is not- `NULL`, it is passed to the constructor of- *type*as a third parameter. In the case of- `OSError`- `filename`attribute of the exception instance.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetFromErrnoWithFilenameObjects([PyObject](structures.html#c.PyObject)*type,[PyObject](structures.html#c.PyObject)*filenameObject,[PyObject](structures.html#c.PyObject)*filenameObject2)[¶](#c.PyErr_SetFromErrnoWithFilenameObjects)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Similar to - `PyErr_SetFromErrnoWithFilenameObject()`- Added in version 3.4. 

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetFromErrnoWithFilename([PyObject](structures.html#c.PyObject)*type, const char *filename)[¶](#c.PyErr_SetFromErrnoWithFilename)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyErr_SetFromErrnoWithFilenameObject()`- *filename*is decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetFromWindowsErr(int ierr)[¶](#c.PyErr_SetFromWindowsErr)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- This is a convenience function to raise - `OSError`- *ierr*of- `0`, the error code returned by a call to- `GetLastError()`is used instead. It calls the Win32 function- `FormatMessage()`to retrieve the Windows description of error code given by- *ierr*or- `GetLastError()`, then it constructs a- `OSError`object with the- `winerror`- `strerror`- `FormatMessage()`), and then calls- `PyErr_SetObject(PyExc_OSError, object)`. This function always returns- `NULL`.- [Availability](../library/intro.html#availability): Windows.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetExcFromWindowsErr([PyObject](structures.html#c.PyObject)*type, int ierr)[¶](#c.PyErr_SetExcFromWindowsErr)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Similar to - `PyErr_SetFromWindowsErr()`- [Availability](../library/intro.html#availability): Windows.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetFromWindowsErrWithFilename(int ierr, const char *filename)[¶](#c.PyErr_SetFromWindowsErrWithFilename)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Similar to - `PyErr_SetFromWindowsErr()`- *filename*is not- `NULL`, it is decoded from the filesystem encoding (- `os.fsdecode()`- `OSError`- `filename`attribute of the exception instance.- [Availability](../library/intro.html#availability): Windows.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetExcFromWindowsErrWithFilenameObject([PyObject](structures.html#c.PyObject)*type, int ierr,[PyObject](structures.html#c.PyObject)*filename)[¶](#c.PyErr_SetExcFromWindowsErrWithFilenameObject)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Similar to - `PyErr_SetExcFromWindowsErr()`- *filename*is not- `NULL`, it is passed to the constructor of- `OSError`- `filename`attribute of the exception instance.- [Availability](../library/intro.html#availability): Windows.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetExcFromWindowsErrWithFilenameObjects([PyObject](structures.html#c.PyObject)*type, int ierr,[PyObject](structures.html#c.PyObject)*filename,[PyObject](structures.html#c.PyObject)*filename2)[¶](#c.PyErr_SetExcFromWindowsErrWithFilenameObjects)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Similar to - `PyErr_SetExcFromWindowsErrWithFilenameObject()`- [Availability](../library/intro.html#availability): Windows.- Added in version 3.4. 

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetExcFromWindowsErrWithFilename([PyObject](structures.html#c.PyObject)*type, int ierr, const char *filename)[¶](#c.PyErr_SetExcFromWindowsErrWithFilename)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)on Windows since version 3.7.- Similar to - `PyErr_SetFromWindowsErrWithFilename()`- [Availability](../library/intro.html#availability): Windows.

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetImportError([PyObject](structures.html#c.PyObject)*msg,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*path)[¶](#c.PyErr_SetImportError)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- This is a convenience function to raise - `ImportError`- *msg*will be set as the exception’s message string.- *name*and- *path*, both of which can be- `NULL`, will be set as the- `ImportError`’s respective- `name`and- `path`attributes.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyErr_SetImportErrorSubclass([PyObject](structures.html#c.PyObject)*exception,[PyObject](structures.html#c.PyObject)*msg,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*path)[¶](#c.PyErr_SetImportErrorSubclass)
- *Return value: Always NULL.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.6.- Much like - `PyErr_SetImportError()`- `ImportError`- Added in version 3.6. 

- 
void PyErr_SyntaxLocationObject([PyObject](structures.html#c.PyObject)*filename, int lineno, int col_offset)[¶](#c.PyErr_SyntaxLocationObject)
- Set file, line, and offset information for the current exception. If the current exception is not a - `SyntaxError`- `SyntaxError`.- Added in version 3.4. 

- 
void PyErr_RangedSyntaxLocationObject([PyObject](structures.html#c.PyObject)*filename, int lineno, int col_offset, int end_lineno, int end_col_offset)[¶](#c.PyErr_RangedSyntaxLocationObject)
- Similar to - `PyErr_SyntaxLocationObject()`- *end_lineno*and- *end_col_offset*information for the current exception.- Added in version 3.10. 

- 
void PyErr_SyntaxLocationEx(const char *filename, int lineno, int col_offset)[¶](#c.PyErr_SyntaxLocationEx)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Like - `PyErr_SyntaxLocationObject()`- *filename*is a byte string decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- Added in version 3.2. 

- 
void PyErr_SyntaxLocation(const char *filename, int lineno)[¶](#c.PyErr_SyntaxLocation)
- *Part of the*- [Stable ABI](stable.html#stable).- Like - `PyErr_SyntaxLocationEx()`- *col_offset*parameter is omitted.

- 
void PyErr_BadInternalCall()[¶](#c.PyErr_BadInternalCall)
- *Part of the*- [Stable ABI](stable.html#stable).- This is a shorthand for - `PyErr_SetString(PyExc_SystemError, message)`, where- *message*indicates that an internal operation (e.g. a Python/C API function) was invoked with an illegal argument. It is mostly for internal use.

- 
[PyObject](structures.html#c.PyObject)*PyErr_ProgramTextObject([PyObject](structures.html#c.PyObject)*filename, int lineno)[¶](#c.PyErr_ProgramTextObject)
- Get the source line in - *filename*at line- *lineno*.- *filename*should be a Python- `str`- On success, this function returns a Python string object with the found line. On failure, this function returns - `NULL`without an exception set.

- 
[PyObject](structures.html#c.PyObject)*PyErr_ProgramText(const char *filename, int lineno)[¶](#c.PyErr_ProgramText)
- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyErr_ProgramTextObject()`- *filename*is a const char*, which is decoded with the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler), instead of a Python object reference.

## Issuing warnings[¶](#issuing-warnings)

Use these functions to issue warnings from C code.  They mirror similar
functions exported by the Python [ warnings](../library/warnings.html#module-warnings) module.  They normally
print a warning message to 

*sys.stderr*; however, it is also possible that the user has specified that warnings are to be turned into errors, and in that case they will raise an exception. It is also possible that the functions raise an exception because of a problem with the warning machinery. The return value is

`0` if no exception is raised, or `-1` if an exception
is raised.  (It is not possible to determine whether a warning message is
actually printed, nor what the reason is for the exception; this is
intentional.)  If an exception is raised, the caller should do its normal
exception handling (for example, [owned references and return an error value).](refcounting.html#c.Py_DECREF)

`Py_DECREF()`- 
int PyErr_WarnEx([PyObject](structures.html#c.PyObject)*category, const char *message,[Py_ssize_t](intro.html#c.Py_ssize_t)stack_level)[¶](#c.PyErr_WarnEx)
- *Part of the*- [Stable ABI](stable.html#stable).- Issue a warning message. The - *category*argument is a warning category (see below) or- `NULL`; the- *message*argument is a UTF-8 encoded string.- *stack_level*is a positive number giving a number of stack frames; the warning will be issued from the currently executing line of code in that stack frame. A- *stack_level*of 1 is the function calling- `PyErr_WarnEx()`- Warning categories must be subclasses of - `PyExc_Warning`- `PyExc_Warning`is a subclass of- `PyExc_Exception`- `PyExc_RuntimeWarning`- [Warning types](#standardwarningcategories).- For information about warning control, see the documentation for the - `warnings`- `-W`

- 
int PyErr_WarnExplicitObject([PyObject](structures.html#c.PyObject)*category,[PyObject](structures.html#c.PyObject)*message,[PyObject](structures.html#c.PyObject)*filename, int lineno,[PyObject](structures.html#c.PyObject)*module,[PyObject](structures.html#c.PyObject)*registry)[¶](#c.PyErr_WarnExplicitObject)
- Issue a warning message with explicit control over all warning attributes. This is a straightforward wrapper around the Python function - `warnings.warn_explicit()`- *module*and- *registry*arguments may be set to- `NULL`to get the default effect described there.- Added in version 3.4. 

- 
int PyErr_WarnExplicit([PyObject](structures.html#c.PyObject)*category, const char *message, const char *filename, int lineno, const char *module,[PyObject](structures.html#c.PyObject)*registry)[¶](#c.PyErr_WarnExplicit)
- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyErr_WarnExplicitObject()`- *message*and- *module*are UTF-8 encoded strings, and- *filename*is decoded from the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).

- 
int PyErr_WarnFormat([PyObject](structures.html#c.PyObject)*category,[Py_ssize_t](intro.html#c.Py_ssize_t)stack_level, const char *format, ...)[¶](#c.PyErr_WarnFormat)
- *Part of the*- [Stable ABI](stable.html#stable).- Function similar to - `PyErr_WarnEx()`- `PyUnicode_FromFormat()`- *format*is an ASCII-encoded string.- Added in version 3.2. 

- 
int PyErr_WarnExplicitFormat([PyObject](structures.html#c.PyObject)*category, const char *filename, int lineno, const char *module,[PyObject](structures.html#c.PyObject)*registry, const char *format, ...)[¶](#c.PyErr_WarnExplicitFormat)
- Similar to - `PyErr_WarnExplicit()`- `PyUnicode_FromFormat()`- *format*is an ASCII-encoded string.- Added in version 3.2. 

- 
int PyErr_ResourceWarning([PyObject](structures.html#c.PyObject)*source,[Py_ssize_t](intro.html#c.Py_ssize_t)stack_level, const char *format, ...)[¶](#c.PyErr_ResourceWarning)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.6.- Function similar to - `PyErr_WarnFormat()`- *category*is- `ResourceWarning`- *source*to- `warnings.WarningMessage`.- Added in version 3.6. 

## Querying the error indicator[¶](#querying-the-error-indicator)

- 
[PyObject](structures.html#c.PyObject)*PyErr_Occurred()[¶](#c.PyErr_Occurred)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Test whether the error indicator is set. If set, return the exception - *type*(the first argument to the last call to one of the- `PyErr_Set*`functions or to- `PyErr_Restore()`- `NULL`. You do not own a reference to the return value, so you do not need to- `Py_DECREF()`- The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state).- Note - Do not compare the return value to a specific exception; use - `PyErr_ExceptionMatches()`

- 
int PyErr_ExceptionMatches([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyErr_ExceptionMatches)
- *Part of the*- [Stable ABI](stable.html#stable).- Equivalent to - `PyErr_GivenExceptionMatches(PyErr_Occurred(), exc)`. This should only be called when an exception is actually set; a memory access violation will occur if no exception has been raised.

- 
int PyErr_GivenExceptionMatches([PyObject](structures.html#c.PyObject)*given,[PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyErr_GivenExceptionMatches)
- *Part of the*- [Stable ABI](stable.html#stable).- Return true if the - *given*exception matches the exception type in- *exc*. If- *exc*is a class object, this also returns true when- *given*is an instance of a subclass. If- *exc*is a tuple, all exception types in the tuple (and recursively in subtuples) are searched for a match.

- 
[PyObject](structures.html#c.PyObject)*PyErr_GetRaisedException(void)[¶](#c.PyErr_GetRaisedException)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Return the exception currently being raised, clearing the error indicator at the same time. Return - `NULL`if the error indicator is not set.- This function is used by code that needs to catch exceptions, or code that needs to save and restore the error indicator temporarily. - For example: - { PyObject *exc = PyErr_GetRaisedException(); /* ... code that might produce other errors ... */ PyErr_SetRaisedException(exc); } - See also - `PyErr_GetHandledException()`- Added in version 3.12. 

- 
void PyErr_SetRaisedException([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyErr_SetRaisedException)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Set - *exc*as the exception currently being raised, clearing the existing exception if one is set.- Warning - This call steals a reference to - *exc*, which must be a valid exception.- Added in version 3.12. 

- 
void PyErr_Fetch([PyObject](structures.html#c.PyObject)**ptype,[PyObject](structures.html#c.PyObject)**pvalue,[PyObject](structures.html#c.PyObject)**ptraceback)[¶](#c.PyErr_Fetch)
- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated since version 3.12: Use - `PyErr_GetRaisedException()`- Retrieve the error indicator into three variables whose addresses are passed. If the error indicator is not set, set all three variables to - `NULL`. If it is set, it will be cleared and you own a reference to each object retrieved. The value and traceback object may be- `NULL`even when the type object is not.- Note - This function is normally only used by legacy code that needs to catch exceptions or save and restore the error indicator temporarily. - For example: - { PyObject *type, *value, *traceback; PyErr_Fetch(&type, &value, &traceback); /* ... code that might produce other errors ... */ PyErr_Restore(type, value, traceback); } 

- 
void PyErr_Restore([PyObject](structures.html#c.PyObject)*type,[PyObject](structures.html#c.PyObject)*value,[PyObject](structures.html#c.PyObject)*traceback)[¶](#c.PyErr_Restore)
- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated since version 3.12: Use - `PyErr_SetRaisedException()`- Set the error indicator from the three objects, - *type*,- *value*, and- *traceback*, clearing the existing exception if one is set. If the objects are- `NULL`, the error indicator is cleared. Do not pass a- `NULL`type and non-- `NULL`value or traceback. The exception type should be a class. Do not pass an invalid exception type or value. (Violating these rules will cause subtle problems later.) This call takes away a reference to each object: you must own a reference to each object before the call and after the call you no longer own these references. (If you don’t understand this, don’t use this function. I warned you.)- Note - This function is normally only used by legacy code that needs to save and restore the error indicator temporarily. Use - `PyErr_Fetch()`

- 
void PyErr_NormalizeException([PyObject](structures.html#c.PyObject)**exc,[PyObject](structures.html#c.PyObject)**val,[PyObject](structures.html#c.PyObject)**tb)[¶](#c.PyErr_NormalizeException)
- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated since version 3.12: Use - `PyErr_GetRaisedException()`- Under certain circumstances, the values returned by - `PyErr_Fetch()`- `*exc`is a class object but- `*val`is not an instance of the same class. This function can be used to instantiate the class in that case. If the values are already normalized, nothing happens. The delayed normalization is implemented to improve performance.- Note - This function - *does not*implicitly set the- `__traceback__`- if (tb != NULL) { PyException_SetTraceback(val, tb); } 

- 
[PyObject](structures.html#c.PyObject)*PyErr_GetHandledException(void)[¶](#c.PyErr_GetHandledException)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Retrieve the active exception instance, as would be returned by - `sys.exception()`- *already caught*, not to an exception that was freshly raised. Returns a new reference to the exception or- `NULL`. Does not modify the interpreter’s exception state.- Note - This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use - `PyErr_SetHandledException()`- Added in version 3.11. 

- 
void PyErr_SetHandledException([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyErr_SetHandledException)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Set the active exception, as known from - `sys.exception()`. This refers to an exception that was- *already caught*, not to an exception that was freshly raised. To clear the exception state, pass- `NULL`.- Note - This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use - `PyErr_GetHandledException()`- Added in version 3.11. 

- 
void PyErr_GetExcInfo([PyObject](structures.html#c.PyObject)**ptype,[PyObject](structures.html#c.PyObject)**pvalue,[PyObject](structures.html#c.PyObject)**ptraceback)[¶](#c.PyErr_GetExcInfo)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Retrieve the old-style representation of the exception info, as known from - `sys.exc_info()`- *already caught*, not to an exception that was freshly raised. Returns new references for the three objects, any of which may be- `NULL`. Does not modify the exception info state. This function is kept for backwards compatibility. Prefer using- `PyErr_GetHandledException()`- Note - This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use - `PyErr_SetExcInfo()`- Added in version 3.3. 

- 
void PyErr_SetExcInfo([PyObject](structures.html#c.PyObject)*type,[PyObject](structures.html#c.PyObject)*value,[PyObject](structures.html#c.PyObject)*traceback)[¶](#c.PyErr_SetExcInfo)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Set the exception info, as known from - `sys.exc_info()`. This refers to an exception that was- *already caught*, not to an exception that was freshly raised. This function steals the references of the arguments. To clear the exception state, pass- `NULL`for all three arguments. This function is kept for backwards compatibility. Prefer using- `PyErr_SetHandledException()`- Note - This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use - `PyErr_GetExcInfo()`- Added in version 3.3. - Changed in version 3.11: The - `type`and- `traceback`arguments are no longer used and can be NULL. The interpreter now derives them from the exception instance (the- `value`argument). The function still steals references of all three arguments.

## Signal Handling[¶](#signal-handling)

- 
int PyErr_CheckSignals()[¶](#c.PyErr_CheckSignals)
- *Part of the*- [Stable ABI](stable.html#stable).- Handle external interruptions, such as signals or activating a debugger, whose processing has been delayed until it is safe to run Python code and/or raise exceptions. - For example, pressing - `Ctrl`-- `C`causes a terminal to send the- `signal.SIGINT`- `KeyboardInterrupt`- `PyErr_CheckSignals()`should be called by long-running C code frequently enough so that the response appears immediate to humans.- Handlers invoked by this function currently include: - Signal handlers, including Python functions registered using the - `signal`- Signal handlers are only run in the main thread of the main interpreter. - (This is where the function got the name: originally, signals were the only way to interrupt the interpreter.) 
- Running the garbage collector, if necessary. 
- Executing a pending - [remote debugger](../howto/remote_debugging.html#remote-debugging)script.
 - If any handler raises an exception, immediately return - `-1`with that exception set. Any remaining interruptions are left to be processed on the next- `PyErr_CheckSignals()`- If all handlers finish successfully, or there are no handlers to run, return - `0`.- Changed in version 3.12: This function may now invoke the garbage collector. - Changed in version 3.14: This function may now execute a remote debugger script, if remote debugging is enabled. 

- 
void PyErr_SetInterrupt()[¶](#c.PyErr_SetInterrupt)
- *Part of the*- [Stable ABI](stable.html#stable).- Simulate the effect of a - `SIGINT`signal arriving. This is equivalent to- `PyErr_SetInterruptEx(SIGINT)`.- Note - This function is async-signal-safe. It can be called without an - [attached thread state](../glossary.html#term-attached-thread-state)and from a C signal handler.

- 
int PyErr_SetInterruptEx(int signum)[¶](#c.PyErr_SetInterruptEx)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Simulate the effect of a signal arriving. The next time - `PyErr_CheckSignals()`- This function can be called by C code that sets up its own signal handling and wants Python signal handlers to be invoked as expected when an interruption is requested (for example when the user presses Ctrl-C to interrupt an operation). - If the given signal isn’t handled by Python (it was set to - `signal.SIG_DFL`- `signal.SIG_IGN`- If - *signum*is outside of the allowed range of signal numbers,- `-1`is returned. Otherwise,- `0`is returned. The error indicator is never changed by this function.- Note - This function is async-signal-safe. It can be called without an - [attached thread state](../glossary.html#term-attached-thread-state)and from a C signal handler.- Added in version 3.10. 

- 
int PySignal_SetWakeupFd(int fd)[¶](#c.PySignal_SetWakeupFd)
- This utility function specifies a file descriptor to which the signal number is written as a single byte whenever a signal is received. - *fd*must be non-blocking. It returns the previous such file descriptor.- The value - `-1`disables the feature; this is the initial state. This is equivalent to- `signal.set_wakeup_fd()`- *fd*should be a valid file descriptor. The function should only be called from the main thread.- Changed in version 3.5: On Windows, the function now also supports socket handles. 

## Exception Classes[¶](#exception-classes)

- 
[PyObject](structures.html#c.PyObject)*PyErr_NewException(const char *name,[PyObject](structures.html#c.PyObject)*base,[PyObject](structures.html#c.PyObject)*dict)[¶](#c.PyErr_NewException)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This utility function creates and returns a new exception class. The - *name*argument must be the name of the new exception, a C string of the form- `module.classname`. The- *base*and- *dict*arguments are normally- `NULL`. This creates a class object derived from- `Exception`- `PyExc_Exception`- The - `__module__`- *name*argument, and the class name is set to the last part (after the last dot). The- *base*argument can be used to specify alternate base classes; it can either be only one class or a tuple of classes. The- *dict*argument can be used to specify a dictionary of class variables and methods.

- 
[PyObject](structures.html#c.PyObject)*PyErr_NewExceptionWithDoc(const char *name, const char *doc,[PyObject](structures.html#c.PyObject)*base,[PyObject](structures.html#c.PyObject)*dict)[¶](#c.PyErr_NewExceptionWithDoc)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Same as - `PyErr_NewException()`- *doc*is non-- `NULL`, it will be used as the docstring for the exception class.- Added in version 3.2. 

- 
int PyExceptionClass_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyExceptionClass_Check)
- Return non-zero if - *ob*is an exception class, zero otherwise. This function always succeeds.

- 
const char *PyExceptionClass_Name([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyExceptionClass_Name)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- Return - `tp_name`- *ob*.

## Exception Objects[¶](#exception-objects)

- 
int PyExceptionInstance_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyExceptionInstance_Check)
- Return true if - *op*is an instance of- `BaseException`

- 
PyExceptionInstance_Class(op)[¶](#c.PyExceptionInstance_Class)
- Equivalent to - `Py_TYPE(op)`

- 
[PyObject](structures.html#c.PyObject)*PyException_GetTraceback([PyObject](structures.html#c.PyObject)*ex)[¶](#c.PyException_GetTraceback)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the traceback associated with the exception as a new reference, as accessible from Python through the - `__traceback__`- `NULL`.

- 
int PyException_SetTraceback([PyObject](structures.html#c.PyObject)*ex,[PyObject](structures.html#c.PyObject)*tb)[¶](#c.PyException_SetTraceback)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the traceback associated with the exception to - *tb*. Use- `Py_None`to clear it.

- 
[PyObject](structures.html#c.PyObject)*PyException_GetContext([PyObject](structures.html#c.PyObject)*ex)[¶](#c.PyException_GetContext)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the context (another exception instance during whose handling - *ex*was raised) associated with the exception as a new reference, as accessible from Python through the- `__context__`- `NULL`.

- 
void PyException_SetContext([PyObject](structures.html#c.PyObject)*ex,[PyObject](structures.html#c.PyObject)*ctx)[¶](#c.PyException_SetContext)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the context associated with the exception to - *ctx*. Use- `NULL`to clear it. There is no type check to make sure that- *ctx*is an exception instance. This steals a reference to- *ctx*.

- 
[PyObject](structures.html#c.PyObject)*PyException_GetCause([PyObject](structures.html#c.PyObject)*ex)[¶](#c.PyException_GetCause)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the cause (either an exception instance, or - `None`, set by- `raise ... from ...`) associated with the exception as a new reference, as accessible from Python through the- `__cause__`

- 
void PyException_SetCause([PyObject](structures.html#c.PyObject)*ex,[PyObject](structures.html#c.PyObject)*cause)[¶](#c.PyException_SetCause)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the cause associated with the exception to - *cause*. Use- `NULL`to clear it. There is no type check to make sure that- *cause*is either an exception instance or- `None`. This steals a reference to- *cause*.- The - `__suppress_context__`- `True`by this function.

- 
[PyObject](structures.html#c.PyObject)*PyException_GetArgs([PyObject](structures.html#c.PyObject)*ex)[¶](#c.PyException_GetArgs)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Return - `args`- *ex*.

- 
void PyException_SetArgs([PyObject](structures.html#c.PyObject)*ex,[PyObject](structures.html#c.PyObject)*args)[¶](#c.PyException_SetArgs)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Set - `args`- *ex*to- *args*.

- 
[PyObject](structures.html#c.PyObject)*PyUnstable_Exc_PrepReraiseStar([PyObject](structures.html#c.PyObject)*orig,[PyObject](structures.html#c.PyObject)*excs)[¶](#c.PyUnstable_Exc_PrepReraiseStar)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Implement part of the interpreter’s implementation of - `except*`.- *orig*is the original exception that was caught, and- *excs*is the list of the exceptions that need to be raised. This list contains the unhandled part of- *orig*, if any, as well as the exceptions that were raised from the- `except*`clauses (so they have a different traceback from- *orig*) and those that were reraised (and have the same traceback as- *orig*). Return the- `ExceptionGroup`- `None`if there is nothing to reraise.- Added in version 3.12. 

## Unicode Exception Objects[¶](#unicode-exception-objects)

The following functions are used to create and modify Unicode exceptions from C.

- 
[PyObject](structures.html#c.PyObject)*PyUnicodeDecodeError_Create(const char *encoding, const char *object,[Py_ssize_t](intro.html#c.Py_ssize_t)length,[Py_ssize_t](intro.html#c.Py_ssize_t)start,[Py_ssize_t](intro.html#c.Py_ssize_t)end, const char *reason)[¶](#c.PyUnicodeDecodeError_Create)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a - `UnicodeDecodeError`- *encoding*,- *object*,- *length*,- *start*,- *end*and- *reason*.- *encoding*and- *reason*are UTF-8 encoded strings.

- 
[PyObject](structures.html#c.PyObject)*PyUnicodeDecodeError_GetEncoding([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeDecodeError_GetEncoding)
- 
[PyObject](structures.html#c.PyObject)*PyUnicodeEncodeError_GetEncoding([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeEncodeError_GetEncoding)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *encoding*attribute of the given exception object.

- 
[PyObject](structures.html#c.PyObject)*PyUnicodeDecodeError_GetObject([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeDecodeError_GetObject)
- 
[PyObject](structures.html#c.PyObject)*PyUnicodeEncodeError_GetObject([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeEncodeError_GetObject)
- 
[PyObject](structures.html#c.PyObject)*PyUnicodeTranslateError_GetObject([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeTranslateError_GetObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *object*attribute of the given exception object.

- 
int PyUnicodeDecodeError_GetStart([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)*start)[¶](#c.PyUnicodeDecodeError_GetStart)
- 
int PyUnicodeEncodeError_GetStart([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)*start)[¶](#c.PyUnicodeEncodeError_GetStart)
- 
int PyUnicodeTranslateError_GetStart([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)*start)[¶](#c.PyUnicodeTranslateError_GetStart)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the - *start*attribute of the given exception object and place it into- **start*.- *start*must not be- `NULL`. Return- `0`on success,- `-1`on failure.- If the - `UnicodeError.object`- *start*is- `0`. Otherwise, it is clipped to- `[0, len(object) - 1]`.- See also 

- 
int PyUnicodeDecodeError_SetStart([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)start)[¶](#c.PyUnicodeDecodeError_SetStart)
- 
int PyUnicodeEncodeError_SetStart([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)start)[¶](#c.PyUnicodeEncodeError_SetStart)
- 
int PyUnicodeTranslateError_SetStart([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)start)[¶](#c.PyUnicodeTranslateError_SetStart)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the - *start*attribute of the given exception object to- *start*. Return- `0`on success,- `-1`on failure.- Note - While passing a negative - *start*does not raise an exception, the corresponding getters will not consider it as a relative offset.

- 
int PyUnicodeDecodeError_GetEnd([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)*end)[¶](#c.PyUnicodeDecodeError_GetEnd)
- 
int PyUnicodeEncodeError_GetEnd([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)*end)[¶](#c.PyUnicodeEncodeError_GetEnd)
- 
int PyUnicodeTranslateError_GetEnd([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)*end)[¶](#c.PyUnicodeTranslateError_GetEnd)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the - *end*attribute of the given exception object and place it into- **end*.- *end*must not be- `NULL`. Return- `0`on success,- `-1`on failure.- If the - `UnicodeError.object`- *end*is- `0`. Otherwise, it is clipped to- `[1, len(object)]`.

- 
int PyUnicodeDecodeError_SetEnd([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)end)[¶](#c.PyUnicodeDecodeError_SetEnd)
- 
int PyUnicodeEncodeError_SetEnd([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)end)[¶](#c.PyUnicodeEncodeError_SetEnd)
- 
int PyUnicodeTranslateError_SetEnd([PyObject](structures.html#c.PyObject)*exc,[Py_ssize_t](intro.html#c.Py_ssize_t)end)[¶](#c.PyUnicodeTranslateError_SetEnd)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the - *end*attribute of the given exception object to- *end*. Return- `0`on success,- `-1`on failure.- See also 

- 
[PyObject](structures.html#c.PyObject)*PyUnicodeDecodeError_GetReason([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeDecodeError_GetReason)
- 
[PyObject](structures.html#c.PyObject)*PyUnicodeEncodeError_GetReason([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeEncodeError_GetReason)
- 
[PyObject](structures.html#c.PyObject)*PyUnicodeTranslateError_GetReason([PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyUnicodeTranslateError_GetReason)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *reason*attribute of the given exception object.

- 
int PyUnicodeDecodeError_SetReason([PyObject](structures.html#c.PyObject)*exc, const char *reason)[¶](#c.PyUnicodeDecodeError_SetReason)
- 
int PyUnicodeEncodeError_SetReason([PyObject](structures.html#c.PyObject)*exc, const char *reason)[¶](#c.PyUnicodeEncodeError_SetReason)
- 
int PyUnicodeTranslateError_SetReason([PyObject](structures.html#c.PyObject)*exc, const char *reason)[¶](#c.PyUnicodeTranslateError_SetReason)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the - *reason*attribute of the given exception object to- *reason*. Return- `0`on success,- `-1`on failure.

## Recursion Control[¶](#recursion-control)

These two functions provide a way to perform safe recursive calls at the C
level, both in the core and in extension modules.  They are needed if the
recursive code does not necessarily invoke Python code (which tracks its
recursion depth automatically).
They are also not needed for *tp_call* implementations
because the [call protocol](call.html#call) takes care of recursion handling.

- 
int Py_EnterRecursiveCall(const char *where)[¶](#c.Py_EnterRecursiveCall)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Marks a point where a recursive C-level call is about to be performed. - The function then checks if the stack limit is reached. If this is the case, a - `RecursionError`- *where*should be a UTF-8 encoded string such as- `" in instance check"`to be concatenated to the- `RecursionError`- See also - The - `PyUnstable_ThreadState_SetStackProtection()`- Changed in version 3.9: This function is now also available in the - [limited API](stable.html#limited-c-api).

- 
void Py_LeaveRecursiveCall(void)[¶](#c.Py_LeaveRecursiveCall)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Ends a - `Py_EnterRecursiveCall()`- *successful*invocation of- `Py_EnterRecursiveCall()`.- Changed in version 3.9: This function is now also available in the - [limited API](stable.html#limited-c-api).

Properly implementing [ tp_repr](typeobj.html#c.PyTypeObject.tp_repr) for container types requires
special recursion handling.  In addition to protecting the stack,

`tp_repr` also needs to track objects to prevent cycles.  The
following two functions facilitate this functionality.  Effectively,
these are the C equivalent to [.](../library/reprlib.html#reprlib.recursive_repr)

`reprlib.recursive_repr()`- 
int Py_ReprEnter([PyObject](structures.html#c.PyObject)*object)[¶](#c.Py_ReprEnter)
- *Part of the*- [Stable ABI](stable.html#stable).- Called at the beginning of the - `tp_repr`- If the object has already been processed, the function returns a positive integer. In that case the - `tp_repr`- `dict`- `{...}`and- `list`- `[...]`.- The function will return a negative integer if the recursion limit is reached. In that case the - `tp_repr`- `NULL`.- Otherwise, the function returns zero and the - `tp_repr`

- 
void Py_ReprLeave([PyObject](structures.html#c.PyObject)*object)[¶](#c.Py_ReprLeave)
- *Part of the*- [Stable ABI](stable.html#stable).- Ends a - `Py_ReprEnter()`- `Py_ReprEnter()`that returns zero.

- 
int Py_GetRecursionLimit(void)[¶](#c.Py_GetRecursionLimit)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the recursion limit for the current interpreter. It can be set with - `Py_SetRecursionLimit()`- This function cannot fail, and the caller must hold an - [attached thread state](../glossary.html#term-attached-thread-state).- See also 

- 
void Py_SetRecursionLimit(int new_limit)[¶](#c.Py_SetRecursionLimit)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the recursion limit for the current interpreter. - This function cannot fail, and the caller must hold an - [attached thread state](../glossary.html#term-attached-thread-state).- See also 

## Exception and warning types[¶](#exception-and-warning-types)

All standard Python exceptions and warning categories are available as global
variables whose names are `PyExc_` followed by the Python exception name.
These have the type [PyObject](structures.html#c.PyObject)*; they are all class objects.

For completeness, here are all the variables:

### Exception types[¶](#exception-types)

| C name | Python name | 
|---|---|
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | 

Added in version 3.3: [ PyExc_BlockingIOError](#c.PyExc_BlockingIOError), 

[,](#c.PyExc_BrokenPipeError)

`PyExc_BrokenPipeError`[,](#c.PyExc_ChildProcessError)

`PyExc_ChildProcessError`[,](#c.PyExc_ConnectionError)

`PyExc_ConnectionError`[,](#c.PyExc_ConnectionAbortedError)

`PyExc_ConnectionAbortedError`[,](#c.PyExc_ConnectionRefusedError)

`PyExc_ConnectionRefusedError`[,](#c.PyExc_ConnectionResetError)

`PyExc_ConnectionResetError`[,](#c.PyExc_FileExistsError)

`PyExc_FileExistsError`[,](#c.PyExc_FileNotFoundError)

`PyExc_FileNotFoundError`[,](#c.PyExc_InterruptedError)

`PyExc_InterruptedError`[,](#c.PyExc_IsADirectoryError)

`PyExc_IsADirectoryError`[,](#c.PyExc_NotADirectoryError)

`PyExc_NotADirectoryError`[,](#c.PyExc_PermissionError)

`PyExc_PermissionError`[and](#c.PyExc_ProcessLookupError)

`PyExc_ProcessLookupError`[were introduced following](#c.PyExc_TimeoutError)

`PyExc_TimeoutError`[.](https://peps.python.org/pep-3151/)

**PEP 3151**Added in version 3.5: [ PyExc_StopAsyncIteration](#c.PyExc_StopAsyncIteration) and 

[.](#c.PyExc_RecursionError)

`PyExc_RecursionError`Added in version 3.6: [ PyExc_ModuleNotFoundError](#c.PyExc_ModuleNotFoundError).

Added in version 3.11: [ PyExc_BaseExceptionGroup](#c.PyExc_BaseExceptionGroup).

### OSError aliases[¶](#oserror-aliases)

The following are a compatibility aliases to [ PyExc_OSError](#c.PyExc_OSError).

Changed in version 3.3: These aliases used to be separate exception types.

| C name | Python name | Notes | 
|---|---|---|
| 
 | ||
| 
 | ||
| 
 | 

Notes:

[win](#id1)]

`PyExc_WindowsError` is only defined on Windows; protect code that
uses this by testing that the preprocessor macro `MS_WINDOWS` is defined.

### Warning types[¶](#warning-types)

| C name | Python name | 
|---|---|
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | 

Added in version 3.2: [ PyExc_ResourceWarning](#c.PyExc_ResourceWarning).

Added in version 3.10: [ PyExc_EncodingWarning](#c.PyExc_EncodingWarning).

## Tracebacks[¶](#tracebacks)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyTraceBack_Type[¶](#c.PyTraceBack_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- Type object for traceback objects. This is available as - `types.TracebackType`

- 
int PyTraceBack_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyTraceBack_Check)
- Return true if - *op*is a traceback object, false otherwise. This function does not account for subtypes.

- 
int PyTraceBack_Here([PyFrameObject](frame.html#c.PyFrameObject)*f)[¶](#c.PyTraceBack_Here)
- *Part of the*- [Stable ABI](stable.html#stable).- Replace the - `__traceback__`- *f*to the existing chain.- Calling this function without an exception set is undefined behavior. - This function returns - `0`on success, and returns- `-1`with an exception set on failure.

- 
int PyTraceBack_Print([PyObject](structures.html#c.PyObject)*tb,[PyObject](structures.html#c.PyObject)*f)[¶](#c.PyTraceBack_Print)
- *Part of the*- [Stable ABI](stable.html#stable).- Write the traceback - *tb*into the file- *f*.- This function returns - `0`on success, and returns- `-1`with an exception set on failure.