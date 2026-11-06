# Python Initialization Configuration — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/init_config.html](https://docs.python.org/c-api/init_config.html)

---

# Python Initialization Configuration[¶](#python-initialization-configuration)

## PyInitConfig C API[¶](#pyinitconfig-c-api)

Added in version 3.14.

Python can be initialized with [ Py_InitializeFromInitConfig()](#c.Py_InitializeFromInitConfig).

The [ Py_RunMain()](interp-lifecycle.html#c.Py_RunMain) function can be used to write a customized Python
program.

See also [Initialization, Finalization, and Threads](interp-lifecycle.html#initialization).

See also

[ PEP 741](https://peps.python.org/pep-0741/) “Python Configuration C API”.

### Example[¶](#example)

Example of customized Python always running with the [Python Development
Mode](../library/devmode.html#devmode) enabled; return `-1` on error:

```
int init_python(void)
{
    PyInitConfig *config = PyInitConfig_Create();
    if (config == NULL) {
        printf("PYTHON INIT ERROR: memory allocation failed\n");
        return -1;
    }
    // Enable the Python Development Mode
    if (PyInitConfig_SetInt(config, "dev_mode", 1) < 0) {
        goto error;
    }
    // Initialize Python with the configuration
    if (Py_InitializeFromInitConfig(config) < 0) {
        goto error;
    }
    PyInitConfig_Free(config);
    return 0;
error:
    {
        // Display the error message.
        //
        // This uncommon braces style is used, because you cannot make
        // goto targets point to variable declarations.
        const char *err_msg;
        (void)PyInitConfig_GetError(config, &err_msg);
        printf("PYTHON INIT ERROR: %s\n", err_msg);
        PyInitConfig_Free(config);
        return -1;
    }
}
```
### Create Config[¶](#create-config)

- 
struct PyInitConfig[¶](#c.PyInitConfig)
- Opaque structure to configure the Python initialization. 

- 
[PyInitConfig](#c.PyInitConfig)*PyInitConfig_Create(void)[¶](#c.PyInitConfig_Create)
- Create a new initialization configuration using - [Isolated Configuration](#init-isolated-conf)default values.- It must be freed by - `PyInitConfig_Free()`- Return - `NULL`on memory allocation failure.

- 
void PyInitConfig_Free([PyInitConfig](#c.PyInitConfig)*config)[¶](#c.PyInitConfig_Free)
- Free memory of the initialization configuration - *config*.- If - *config*is- `NULL`, no operation is performed.

### Error Handling[¶](#error-handling)

- 
int PyInitConfig_GetError([PyInitConfig](#c.PyInitConfig)*config, const char **err_msg)[¶](#c.PyInitConfig_GetError)
- Get the - *config*error message.- Set - **err_msg*and return- `1`if an error is set.
- Set - **err_msg*to- `NULL`and return- `0`otherwise.
 - An error message is a UTF-8 encoded string. - If - *config*has an exit code, format the exit code as an error message.- The error message remains valid until another - `PyInitConfig`function is called with- *config*. The caller doesn’t have to free the error message.

- 
int PyInitConfig_GetExitCode([PyInitConfig](#c.PyInitConfig)*config, int *exitcode)[¶](#c.PyInitConfig_GetExitCode)
- Get the - *config*exit code.- Set - **exitcode*and return- `1`if- *config*has an exit code set.
- Return - `0`if- *config*has no exit code set.
 - Only the - `Py_InitializeFromInitConfig()`function can set an exit code if the- `parse_argv`option is non-zero.- An exit code can be set when parsing the command line failed (exit code - `2`) or when a command line option asks to display the command line help (exit code- `0`).

### Get Options[¶](#get-options)

The configuration option *name* parameter must be a non-NULL null-terminated
UTF-8 encoded string. See [Configuration Options](#pyinitconfig-opts).

- 
int PyInitConfig_HasOption([PyInitConfig](#c.PyInitConfig)*config, const char *name)[¶](#c.PyInitConfig_HasOption)
- Test if the configuration has an option called - *name*.- Return - `1`if the option exists, or return- `0`otherwise.

- 
int PyInitConfig_GetInt([PyInitConfig](#c.PyInitConfig)*config, const char *name, int64_t *value)[¶](#c.PyInitConfig_GetInt)
- Get an integer configuration option. - Set - **value*, and return- `0`on success.
- Set an error in - *config*and return- `-1`on error.
 

- 
int PyInitConfig_GetStr([PyInitConfig](#c.PyInitConfig)*config, const char *name, char **value)[¶](#c.PyInitConfig_GetStr)
- Get a string configuration option as a null-terminated UTF-8 encoded string. - Set - **value*, and return- `0`on success.
- Set an error in - *config*and return- `-1`on error.
 - **value*can be set to- `NULL`if the option is an optional string and the option is unset.- On success, the string must be released with - `free(value)`if it’s not- `NULL`.

- 
int PyInitConfig_GetStrList([PyInitConfig](#c.PyInitConfig)*config, const char *name, size_t *length, char ***items)[¶](#c.PyInitConfig_GetStrList)
- Get a string list configuration option as an array of null-terminated UTF-8 encoded strings. - Set - **length*and- **value*, and return- `0`on success.
- Set an error in - *config*and return- `-1`on error.
 - On success, the string list must be released with - `PyInitConfig_FreeStrList(length, items)`.

- 
void PyInitConfig_FreeStrList(size_t length, char **items)[¶](#c.PyInitConfig_FreeStrList)
- Free memory of a string list created by - `PyInitConfig_GetStrList()`.

### Set Options[¶](#set-options)

The configuration option *name* parameter must be a non-NULL null-terminated
UTF-8 encoded string. See [Configuration Options](#pyinitconfig-opts).

Some configuration options have side effects on other options. This logic is
only implemented when `Py_InitializeFromInitConfig()` is called, not by the
“Set” functions below. For example, setting `dev_mode` to `1` does not set
`faulthandler` to `1`.

- 
int PyInitConfig_SetInt([PyInitConfig](#c.PyInitConfig)*config, const char *name, int64_t value)[¶](#c.PyInitConfig_SetInt)
- Set an integer configuration option. - Return - `0`on success.
- Set an error in - *config*and return- `-1`on error.
 

- 
int PyInitConfig_SetStr([PyInitConfig](#c.PyInitConfig)*config, const char *name, const char *value)[¶](#c.PyInitConfig_SetStr)
- Set a string configuration option from a null-terminated UTF-8 encoded string. The string is copied. - Return - `0`on success.
- Set an error in - *config*and return- `-1`on error.
 

- 
int PyInitConfig_SetStrList([PyInitConfig](#c.PyInitConfig)*config, const char *name, size_t length, char *const *items)[¶](#c.PyInitConfig_SetStrList)
- Set a string list configuration option from an array of null-terminated UTF-8 encoded strings. The string list is copied. - Return - `0`on success.
- Set an error in - *config*and return- `-1`on error.
 

### Module[¶](#module)

- 
int PyInitConfig_AddModule([PyInitConfig](#c.PyInitConfig)*config, const char *name,[PyObject](structures.html#c.PyObject)*(*initfunc)(void))[¶](#c.PyInitConfig_AddModule)
- Add a built-in extension module to the table of built-in modules. - The new module can be imported by the name - *name*, and uses the function- *initfunc*as the initialization function called on the first attempted import.- Return - `0`on success.
- Set an error in - *config*and return- `-1`on error.
 - If Python is initialized multiple times, - `PyInitConfig_AddModule()`must be called at each Python initialization.- Similar to the - `PyImport_AppendInittab()`

### Initialize Python[¶](#initialize-python)

- 
int Py_InitializeFromInitConfig([PyInitConfig](#c.PyInitConfig)*config)[¶](#c.Py_InitializeFromInitConfig)
- Initialize Python from the initialization configuration. - Return - `0`on success.
- Set an error in - *config*and return- `-1`on error.
- Set an exit code in - *config*and return- `-1`if Python wants to exit.
 - See - `PyInitConfig_GetExitcode()`for the exit code case.

## Configuration Options[¶](#configuration-options)

| Option | PyConfig/PyPreConfig member | Type | Visibility | 
|---|---|---|---|
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Public | |
| 
 | 
 | Read-only | 

Visibility:

- Public: Can be retrieved by - `PyConfig_Get()`- `PyConfig_Set()`
- Read-only: Can be retrieved by - `PyConfig_Get()`- `PyConfig_Set()`

## Runtime Python configuration API[¶](#runtime-python-configuration-api)

At runtime, it’s possible to get and set configuration options using
[ PyConfig_Get()](#c.PyConfig_Get) and  

[functions.](#c.PyConfig_Set)

`PyConfig_Set()`The configuration option *name* parameter must be a non-NULL null-terminated
UTF-8 encoded string. See [Configuration Options](#pyinitconfig-opts).

Some options are read from the [ sys](../library/sys.html#module-sys) attributes. For example, the option

`"argv"` is read from [.](../library/sys.html#sys.argv)

`sys.argv`- 
[PyObject](structures.html#c.PyObject)*PyConfig_Get(const char *name)[¶](#c.PyConfig_Get)
- Get the current runtime value of a configuration option as a Python object. - Return a new reference on success. 
- Set an exception and return - `NULL`on error.
 - The object type depends on the configuration option. It can be: - `bool`
- `int`
- `str`
- `list[str]`
- `dict[str, str]`
 - The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state). The function cannot be called before Python initialization nor after Python finalization.- Added in version 3.14. 

- 
int PyConfig_GetInt(const char *name, int *value)[¶](#c.PyConfig_GetInt)
- Similar to - `PyConfig_Get()`- Return - `0`on success.
- Set an exception and return - `-1`on error.
 - Added in version 3.14. 

- 
[PyObject](structures.html#c.PyObject)*PyConfig_Names(void)[¶](#c.PyConfig_Names)
- Get all configuration option names as a - `frozenset`.- Return a new reference on success. 
- Set an exception and return - `NULL`on error.
 - The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state). The function cannot be called before Python initialization nor after Python finalization.- Added in version 3.14. 

- 
int PyConfig_Set(const char *name, [PyObject](structures.html#c.PyObject)*value)[¶](#c.PyConfig_Set)
- Set the current runtime value of a configuration option. - Raise a - `ValueError`- *name*.
- Raise a - `ValueError`- *value*is an invalid value.
- Raise a - `ValueError`
- Raise a - `TypeError`- *value*has not the proper type.
 - The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state). The function cannot be called before Python initialization nor after Python finalization.- Raises an - [auditing event](../library/sys.html#auditing)- `cpython.PyConfig_Set`with arguments- `name`,- `value`.- Added in version 3.14. 

## PyConfig C API[¶](#pyconfig-c-api)

Added in version 3.8.

Python can be initialized with [ Py_InitializeFromConfig()](interp-lifecycle.html#c.Py_InitializeFromConfig) and the

[structure. It can be preinitialized with](#c.PyConfig)

`PyConfig`[and the](#c.Py_PreInitialize)

`Py_PreInitialize()`[structure.](#c.PyPreConfig)

`PyPreConfig`There are two kinds of configuration:

- The - [Python Configuration](#init-python-config)can be used to build a customized Python which behaves as the regular Python. For example, environment variables and command line arguments are used to configure Python.
- The - [Isolated Configuration](#init-isolated-conf)can be used to embed Python into an application. It isolates Python from the system. For example, environment variables are ignored, the LC_CTYPE locale is left unchanged and no signal handler is registered.

The [ Py_RunMain()](interp-lifecycle.html#c.Py_RunMain) function can be used to write a customized Python
program.

See also [Initialization, Finalization, and Threads](interp-lifecycle.html#initialization).

See also

[ PEP 587](https://peps.python.org/pep-0587/) “Python Initialization Configuration”.

### Example[¶](#id1)

Example of customized Python always running in isolated mode:

```
int main(int argc, char **argv)
{
    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);
    config.isolated = 1;
    /* Decode command line arguments.
       Implicitly preinitialize Python (in isolated mode). */
    status = PyConfig_SetBytesArgv(&config, argc, argv);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    PyConfig_Clear(&config);
    return Py_RunMain();
exception:
    PyConfig_Clear(&config);
    if (PyStatus_IsExit(status)) {
        return status.exitcode;
    }
    /* Display the error message and exit the process with
       non-zero exit code */
    Py_ExitStatusException(status);
}
```
### PyWideStringList[¶](#pywidestringlist)

- 
type PyWideStringList[¶](#c.PyWideStringList)
- List of - `wchar_t*`strings.- If - *length*is non-zero,- *items*must be non-- `NULL`and all strings must be non-- `NULL`.- Methods: - 
[PyStatus](#c.PyStatus)PyWideStringList_Append([PyWideStringList](#c.PyWideStringList)*list, const wchar_t *item)[¶](#c.PyWideStringList_Append)
- Append - *item*to- *list*.- Python must be preinitialized to call this function. 
 - 
[PyStatus](#c.PyStatus)PyWideStringList_Insert([PyWideStringList](#c.PyWideStringList)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)index, const wchar_t *item)[¶](#c.PyWideStringList_Insert)
- Insert - *item*into- *list*at- *index*.- If - *index*is greater than or equal to- *list*length, append- *item*to- *list*.- *index*must be greater than or equal to- `0`.- Python must be preinitialized to call this function. 
 - Structure fields: - 
[Py_ssize_t](intro.html#c.Py_ssize_t)length[¶](#c.PyWideStringList.length)
- List length. 
 - 
wchar_t **items[¶](#c.PyWideStringList.items)
- List items. 
 
- 

### PyStatus[¶](#pystatus)

- 
type PyStatus[¶](#c.PyStatus)
- Structure to store an initialization function status: success, error or exit. - For an error, it can store the C function name which created the error. - Structure fields: - 
int exitcode[¶](#c.PyStatus.exitcode)
- Exit code. Argument passed to - `exit()`.
 - 
const char *err_msg[¶](#c.PyStatus.err_msg)
- Error message. 
 - 
const char *func[¶](#c.PyStatus.func)
- Name of the function which created an error, can be - `NULL`.
 - Functions to create a status: - 
[PyStatus](#c.PyStatus)PyStatus_Error(const char *err_msg)[¶](#c.PyStatus_Error)
- Initialization error with a message. - *err_msg*must not be- `NULL`.
 - Functions to handle a status: - 
int PyStatus_Exception([PyStatus](#c.PyStatus)status)[¶](#c.PyStatus_Exception)
- Is the status an error or an exit? If true, the exception must be handled; by calling - `Py_ExitStatusException()`
 
- 
int exitcode

Note

Internally, Python uses macros which set `PyStatus.func`,
whereas functions to create a status set `func` to `NULL`.

Example:

```
PyStatus alloc(void **ptr, size_t size)
{
    *ptr = PyMem_RawMalloc(size);
    if (*ptr == NULL) {
        return PyStatus_NoMemory();
    }
    return PyStatus_Ok();
}
int main(int argc, char **argv)
{
    void *ptr;
    PyStatus status = alloc(&ptr, 16);
    if (PyStatus_Exception(status)) {
        Py_ExitStatusException(status);
    }
    PyMem_Free(ptr);
    return 0;
}
```
### PyPreConfig[¶](#pypreconfig)

- 
type PyPreConfig[¶](#c.PyPreConfig)
- Structure used to preinitialize Python. - Function to initialize a preconfiguration: - 
void PyPreConfig_InitPythonConfig([PyPreConfig](#c.PyPreConfig)*preconfig)[¶](#c.PyPreConfig_InitPythonConfig)
- Initialize the preconfiguration with - [Python Configuration](#init-python-config).
 - 
void PyPreConfig_InitIsolatedConfig([PyPreConfig](#c.PyPreConfig)*preconfig)[¶](#c.PyPreConfig_InitIsolatedConfig)
- Initialize the preconfiguration with - [Isolated Configuration](#init-isolated-conf).
 - Structure fields: - 
int allocator[¶](#c.PyPreConfig.allocator)
- Name of the Python memory allocators: - `PYMEM_ALLOCATOR_NOT_SET`(- `0`): don’t change memory allocators (use defaults).
- `PYMEM_ALLOCATOR_DEFAULT`(- `1`):- [default memory allocators](memory.html#default-memory-allocators).
- `PYMEM_ALLOCATOR_DEBUG`(- `2`):- [default memory allocators](memory.html#default-memory-allocators)with- [debug hooks](memory.html#pymem-debug-hooks).
- `PYMEM_ALLOCATOR_MALLOC`(- `3`): use- `malloc()`of the C library.
- `PYMEM_ALLOCATOR_MALLOC_DEBUG`(- `4`): force usage of- `malloc()`with- [debug hooks](memory.html#pymem-debug-hooks).
- `PYMEM_ALLOCATOR_PYMALLOC`(- `5`):- [Python pymalloc memory allocator](memory.html#pymalloc).
- `PYMEM_ALLOCATOR_PYMALLOC_DEBUG`(- `6`):- [Python pymalloc memory allocator](memory.html#pymalloc)with- [debug hooks](memory.html#pymem-debug-hooks).
- `PYMEM_ALLOCATOR_MIMALLOC`(- `6`): use- `mimalloc`, a fast malloc replacement.
- `PYMEM_ALLOCATOR_MIMALLOC_DEBUG`(- `7`): use- `mimalloc`, a fast malloc replacement with- [debug hooks](memory.html#pymem-debug-hooks).
 - `PYMEM_ALLOCATOR_PYMALLOC`and- `PYMEM_ALLOCATOR_PYMALLOC_DEBUG`are not supported if Python is- `configured using --without-pymalloc`- `PYMEM_ALLOCATOR_MIMALLOC`and- `PYMEM_ALLOCATOR_MIMALLOC_DEBUG`are not supported if Python is- `configured using --without-mimalloc`- See - [Memory Management](memory.html#memory).- Default: - `PYMEM_ALLOCATOR_NOT_SET`.
 - 
int configure_locale[¶](#c.PyPreConfig.configure_locale)
- Set the LC_CTYPE locale to the user preferred locale. - If equals to - `0`, set- `coerce_c_locale`- `coerce_c_locale_warn`- `0`.- See the - [locale encoding](../glossary.html#term-locale-encoding).- Default: - `1`in Python config,- `0`in isolated config.
 - 
int coerce_c_locale[¶](#c.PyPreConfig.coerce_c_locale)
- If equals to - `2`, coerce the C locale.- If equals to - `1`, read the LC_CTYPE locale to decide if it should be coerced.- See the - [locale encoding](../glossary.html#term-locale-encoding).- Default: - `-1`in Python config,- `0`in isolated config.
 - 
int coerce_c_locale_warn[¶](#c.PyPreConfig.coerce_c_locale_warn)
- If non-zero, emit a warning if the C locale is coerced. - Default: - `-1`in Python config,- `0`in isolated config.
 - 
int dev_mode[¶](#c.PyPreConfig.dev_mode)
- [Python Development Mode](../library/devmode.html#devmode): see- `PyConfig.dev_mode`- Default: - `-1`in Python mode,- `0`in isolated mode.
 - 
int isolated[¶](#c.PyPreConfig.isolated)
- Isolated mode: see - `PyConfig.isolated`- Default: - `0`in Python mode,- `1`in isolated mode.
 - 
int legacy_windows_fs_encoding[¶](#c.PyPreConfig.legacy_windows_fs_encoding)
- If non-zero: - Set - `PyPreConfig.utf8_mode`- `0`,
- Set - `PyConfig.filesystem_encoding`- `"mbcs"`,
- Set - `PyConfig.filesystem_errors`- `"replace"`.
 - Initialized from the - `PYTHONLEGACYWINDOWSFSENCODING`- Only available on Windows. - `#ifdef MS_WINDOWS`macro can be used for Windows specific code.- Default: - `0`.
 - 
int parse_argv[¶](#c.PyPreConfig.parse_argv)
- If non-zero, - `Py_PreInitializeFromArgs()`- `Py_PreInitializeFromBytesArgs()`- `argv`argument the same way the regular Python parses command line arguments: see- [Command Line Arguments](../using/cmdline.html#using-on-cmdline).- Default: - `1`in Python config,- `0`in isolated config.
 - 
int use_environment[¶](#c.PyPreConfig.use_environment)
- Use - [environment variables](../using/cmdline.html#using-on-envvars)? See- `PyConfig.use_environment`- Default: - `1`in Python config and- `0`in isolated config.
 - 
int utf8_mode[¶](#c.PyPreConfig.utf8_mode)
- If non-zero, enable the - [Python UTF-8 Mode](../library/os.html#utf8-mode).- Set to - `0`or- `1`by the- `-X utf8`- `PYTHONUTF8`- Also set to - `1`if the- `LC_CTYPE`locale is- `C`or- `POSIX`.- Default: - `-1`in Python config and- `0`in isolated config.
 
- 
void PyPreConfig_InitPythonConfig(

### Preinitialize Python with PyPreConfig[¶](#preinitialize-python-with-pypreconfig)

The preinitialization of Python:

- Set the Python memory allocators ( - `PyPreConfig.allocator`
- Configure the LC_CTYPE locale ( - [locale encoding](../glossary.html#term-locale-encoding))
- Set the - [Python UTF-8 Mode](../library/os.html#utf8-mode)(- `PyPreConfig.utf8_mode`

The current preconfiguration (`PyPreConfig` type) is stored in
`_PyRuntime.preconfig`.

Functions to preinitialize Python:

- 
[PyStatus](#c.PyStatus)Py_PreInitialize(const[PyPreConfig](#c.PyPreConfig)*preconfig)[¶](#c.Py_PreInitialize)
- Preinitialize Python from - *preconfig*preconfiguration.- *preconfig*must not be- `NULL`.

- 
[PyStatus](#c.PyStatus)Py_PreInitializeFromBytesArgs(const[PyPreConfig](#c.PyPreConfig)*preconfig, int argc, char *const *argv)[¶](#c.Py_PreInitializeFromBytesArgs)
- Preinitialize Python from - *preconfig*preconfiguration.- Parse - *argv*command line arguments (bytes strings) if- `parse_argv`- *preconfig*is non-zero.- *preconfig*must not be- `NULL`.

- 
[PyStatus](#c.PyStatus)Py_PreInitializeFromArgs(const[PyPreConfig](#c.PyPreConfig)*preconfig, int argc, wchar_t *const *argv)[¶](#c.Py_PreInitializeFromArgs)
- Preinitialize Python from - *preconfig*preconfiguration.- Parse - *argv*command line arguments (wide strings) if- `parse_argv`- *preconfig*is non-zero.- *preconfig*must not be- `NULL`.

The caller is responsible to handle exceptions (error or exit) using
[ PyStatus_Exception()](#c.PyStatus_Exception) and 

[.](#c.Py_ExitStatusException)

`Py_ExitStatusException()`For [Python Configuration](#init-python-config)
([ PyPreConfig_InitPythonConfig()](#c.PyPreConfig_InitPythonConfig)), if Python is initialized with
command line arguments, the command line arguments must also be passed to
preinitialize Python, since they have an effect on the pre-configuration
like encodings. For example, the 

[command line option enables the](../using/cmdline.html#cmdoption-X)

`-X utf8`[Python UTF-8 Mode](../library/os.html#utf8-mode).

`PyMem_SetAllocator()` can be called after [ Py_PreInitialize()](#c.Py_PreInitialize) and
before 

[to install a custom memory allocator. It can be called before](interp-lifecycle.html#c.Py_InitializeFromConfig)

`Py_InitializeFromConfig()``Py_PreInitialize()` if
[is set to](#c.PyPreConfig.allocator)

`PyPreConfig.allocator``PYMEM_ALLOCATOR_NOT_SET`.Python memory allocation functions like [ PyMem_RawMalloc()](memory.html#c.PyMem_RawMalloc) must not be
used before the Python preinitialization, whereas calling directly 

`malloc()`
and `free()` is always safe. [must not be called before the Python preinitialization.](sys.html#c.Py_DecodeLocale)

`Py_DecodeLocale()`Example using the preinitialization to enable
the [Python UTF-8 Mode](../library/os.html#utf8-mode):

```
PyStatus status;
PyPreConfig preconfig;
PyPreConfig_InitPythonConfig(&preconfig);
preconfig.utf8_mode = 1;
status = Py_PreInitialize(&preconfig);
if (PyStatus_Exception(status)) {
    Py_ExitStatusException(status);
}
/* at this point, Python speaks UTF-8 */
Py_Initialize();
/* ... use Python API here ... */
Py_Finalize();
```
### PyConfig[¶](#pyconfig)

- 
type PyConfig[¶](#c.PyConfig)
- Structure containing most parameters to configure Python. - When done, the - `PyConfig_Clear()`- Structure methods: - 
void PyConfig_InitPythonConfig([PyConfig](#c.PyConfig)*config)[¶](#c.PyConfig_InitPythonConfig)
- Initialize configuration with the - [Python Configuration](#init-python-config).
 - 
void PyConfig_InitIsolatedConfig([PyConfig](#c.PyConfig)*config)[¶](#c.PyConfig_InitIsolatedConfig)
- Initialize configuration with the - [Isolated Configuration](#init-isolated-conf).
 - 
[PyStatus](#c.PyStatus)PyConfig_SetString([PyConfig](#c.PyConfig)*config, wchar_t *const *config_str, const wchar_t *str)[¶](#c.PyConfig_SetString)
- Copy the wide character string - *str*into- `*config_str`.- [Preinitialize Python](#c-preinit)if needed.
 - 
[PyStatus](#c.PyStatus)PyConfig_SetBytesString([PyConfig](#c.PyConfig)*config, wchar_t *const *config_str, const char *str)[¶](#c.PyConfig_SetBytesString)
- Decode - *str*using- `Py_DecodeLocale()`- `*config_str`.- [Preinitialize Python](#c-preinit)if needed.
 - 
[PyStatus](#c.PyStatus)PyConfig_SetArgv([PyConfig](#c.PyConfig)*config, int argc, wchar_t *const *argv)[¶](#c.PyConfig_SetArgv)
- Set command line arguments ( - `argv`- *config*) from the- *argv*list of wide character strings.- [Preinitialize Python](#c-preinit)if needed.
 - 
[PyStatus](#c.PyStatus)PyConfig_SetBytesArgv([PyConfig](#c.PyConfig)*config, int argc, char *const *argv)[¶](#c.PyConfig_SetBytesArgv)
- Set command line arguments ( - `argv`- *config*) from the- *argv*list of bytes strings. Decode bytes using- `Py_DecodeLocale()`- [Preinitialize Python](#c-preinit)if needed.
 - 
[PyStatus](#c.PyStatus)PyConfig_SetWideStringList([PyConfig](#c.PyConfig)*config,[PyWideStringList](#c.PyWideStringList)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)length, wchar_t **items)[¶](#c.PyConfig_SetWideStringList)
- Set the list of wide strings - *list*to- *length*and- *items*.- [Preinitialize Python](#c-preinit)if needed.
 - 
[PyStatus](#c.PyStatus)PyConfig_Read([PyConfig](#c.PyConfig)*config)[¶](#c.PyConfig_Read)
- Read all Python configuration. - Fields which are already initialized are left unchanged. - Fields for - [path configuration](#init-path-config)are no longer calculated or modified when calling this function, as of Python 3.11.- The - `PyConfig_Read()`- `PyConfig.argv`- `PyConfig.parse_argv`- `2`after arguments are parsed. Since Python arguments are stripped from- `PyConfig.argv`, parsing arguments twice would parse the application options as Python options.- [Preinitialize Python](#c-preinit)if needed.- Changed in version 3.10: The - `PyConfig.argv`- `PyConfig.parse_argv`- `2`after arguments are parsed, and arguments are only parsed if- `PyConfig.parse_argv`equals- `1`.- Changed in version 3.11: - `PyConfig_Read()`- [Python Path Configuration](#init-path-config)may no longer be updated until- `Py_InitializeFromConfig()`
 - Most - `PyConfig`methods- [preinitialize Python](#c-preinit)if needed. In that case, the Python preinitialization configuration (- `PyPreConfig`- `PyConfig`- `PyPreConfig`are tuned, they must be set before calling a- `PyConfig`method:- Moreover, if - `PyConfig_SetArgv()`- `PyConfig_SetBytesArgv()`- `parse_argv`- The caller of these methods is responsible to handle exceptions (error or exit) using - `PyStatus_Exception()`and- `Py_ExitStatusException()`.- Structure fields: - 
[PyWideStringList](#c.PyWideStringList)argv[¶](#c.PyConfig.argv)
- Set - `sys.argv`- `argv`- `main()`function with the difference that the first entry should refer to the script file to be executed rather than the executable hosting the Python interpreter. If there isn’t a script that will be run, the first entry in- `argv`can be an empty string.- Set - `parse_argv`- `1`to parse- `argv`- `argv`.- If - `argv`- `sys.argv`- Default: - `NULL`.- See also the - `orig_argv`
 - 
int safe_path[¶](#c.PyConfig.safe_path)
- If equals to zero, - `Py_RunMain()`prepends a potentially unsafe path to- `sys.path`- If - `argv[0]`- `L"-m"`(- `python -m module`), prepend the current working directory.
- If running a script ( - `python script.py`), prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
- Otherwise ( - `python -c code`and- `python`), prepend an empty string, which means the current working directory.
 - Set to - `1`by the- `-P`- `PYTHONSAFEPATH`- Default: - `0`in Python config,- `1`in isolated config.- Added in version 3.11. 
 - 
wchar_t *base_exec_prefix[¶](#c.PyConfig.base_exec_prefix)
- 
Default: `NULL`.Part of the [Python Path Configuration](#init-path-config)output.See also `PyConfig.exec_prefix`
 - 
wchar_t *base_executable[¶](#c.PyConfig.base_executable)
- Python base executable: - `sys._base_executable`.- Set by the - `__PYVENV_LAUNCHER__`environment variable.- Set from - `PyConfig.executable`- `NULL`.- Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)output.- See also - `PyConfig.executable`
 - 
wchar_t *base_prefix[¶](#c.PyConfig.base_prefix)
- 
Default: `NULL`.Part of the [Python Path Configuration](#init-path-config)output.See also `PyConfig.prefix`
 - 
int buffered_stdio[¶](#c.PyConfig.buffered_stdio)
- If equals to - `0`and- `configure_c_stdio`- Set to - `0`by the- `-u`- `PYTHONUNBUFFERED`- stdin is always opened in buffered mode. - Default: - `1`.
 - 
int bytes_warning[¶](#c.PyConfig.bytes_warning)
- If equals to - `1`, issue a warning when comparing- `bytes`- `bytearray`- `str`- `bytes`with- `int`- If equal or greater to - `2`, raise a- `BytesWarning`- Incremented by the - `-b`- Default: - `0`.
 - 
int warn_default_encoding[¶](#c.PyConfig.warn_default_encoding)
- If non-zero, emit a - `EncodingWarning`- `io.TextIOWrapper`- [Opt-in EncodingWarning](../library/io.html#io-encoding-warning)for details.- Default: - `0`.- Added in version 3.10. 
 - 
int code_debug_ranges[¶](#c.PyConfig.code_debug_ranges)
- If equals to - `0`, disables the inclusion of the end line and column mappings in code objects. Also disables traceback printing carets to specific error locations.- Set to - `0`by the- `PYTHONNODEBUGRANGES`- `-X no_debug_ranges`- Default: - `1`.- Added in version 3.11. 
 - 
wchar_t *check_hash_pycs_mode[¶](#c.PyConfig.check_hash_pycs_mode)
- Control the validation behavior of hash-based - `.pyc`files: value of the- `--check-hash-based-pycs`- Valid values: - `L"always"`: Hash the source file for invalidation regardless of value of the ‘check_source’ flag.
- `L"never"`: Assume that hash-based pycs always are valid.
- `L"default"`: The ‘check_source’ flag in hash-based pycs determines invalidation.
 - Default: - `L"default"`.- See also - **PEP 552**
 - 
int configure_c_stdio[¶](#c.PyConfig.configure_c_stdio)
- If non-zero, configure C standard streams: - On Windows, set the binary mode ( - `O_BINARY`) on stdin, stdout and stderr.
- If - `buffered_stdio`
- If - `interactive`
 - Default: - `1`in Python config,- `0`in isolated config.
 - 
int dev_mode[¶](#c.PyConfig.dev_mode)
- If non-zero, enable the - [Python Development Mode](../library/devmode.html#devmode).- Set to - `1`by the- `-X dev`- `PYTHONDEVMODE`- Default: - `-1`in Python mode,- `0`in isolated mode.
 - 
int dump_refs[¶](#c.PyConfig.dump_refs)
- Dump Python references? - If non-zero, dump all objects which are still alive at exit. - Set to - `1`by the- `PYTHONDUMPREFS`- Needs a special build of Python with the - `Py_TRACE_REFS`macro defined: see the- `configure --with-trace-refs option`- Default: - `0`.
 - 
wchar_t *dump_refs_file[¶](#c.PyConfig.dump_refs_file)
- Filename where to dump Python references. - Set by the - `PYTHONDUMPREFSFILE`- Default: - `NULL`.- Added in version 3.11. 
 - 
wchar_t *exec_prefix[¶](#c.PyConfig.exec_prefix)
- The site-specific directory prefix where the platform-dependent Python files are installed: - `sys.exec_prefix`- Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)output.- See also - `PyConfig.base_exec_prefix`
 - 
wchar_t *executable[¶](#c.PyConfig.executable)
- The absolute path of the executable binary for the Python interpreter: - `sys.executable`- Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)output.- See also - `PyConfig.base_executable`
 - 
int faulthandler[¶](#c.PyConfig.faulthandler)
- Enable faulthandler? - If non-zero, call - `faulthandler.enable()`- Set to - `1`by- `-X faulthandler`- `PYTHONFAULTHANDLER`- Default: - `-1`in Python mode,- `0`in isolated mode.
 - 
wchar_t *filesystem_encoding[¶](#c.PyConfig.filesystem_encoding)
- [Filesystem encoding](../glossary.html#term-filesystem-encoding-and-error-handler):- `sys.getfilesystemencoding()`- On macOS, Android and VxWorks: use - `"utf-8"`by default.- On Windows: use - `"utf-8"`by default, or- `"mbcs"`if- `legacy_windows_fs_encoding`- `PyPreConfig`- Default encoding on other platforms: - `"utf-8"`if- `PyPreConfig.utf8_mode`
- `"ascii"`if Python detects that- `nl_langinfo(CODESET)`announces the ASCII encoding, whereas the- `mbstowcs()`function decodes from a different encoding (usually Latin1).
- `"utf-8"`if- `nl_langinfo(CODESET)`returns an empty string.
- Otherwise, use the - [locale encoding](../glossary.html#term-locale-encoding):- `nl_langinfo(CODESET)`result.
 - At Python startup, the encoding name is normalized to the Python codec name. For example, - `"ANSI_X3.4-1968"`is replaced with- `"ascii"`.- See also the - `filesystem_errors`
 - 
wchar_t *filesystem_errors[¶](#c.PyConfig.filesystem_errors)
- [Filesystem error handler](../glossary.html#term-filesystem-encoding-and-error-handler):- `sys.getfilesystemencodeerrors()`- On Windows: use - `"surrogatepass"`by default, or- `"replace"`if- `legacy_windows_fs_encoding`- `PyPreConfig`- On other platforms: use - `"surrogateescape"`by default.- Supported error handlers: - `"strict"`
- `"surrogateescape"`
- `"surrogatepass"`(only supported with the UTF-8 encoding)
 - See also the - `filesystem_encoding`
 - 
int use_frozen_modules[¶](#c.PyConfig.use_frozen_modules)
- If non-zero, use frozen modules. - Set by the - `PYTHON_FROZEN_MODULES`- Default: - `1`in a release build, or- `0`in a- [debug build](../using/configure.html#debug-build).
 - 
unsigned long hash_seed[¶](#c.PyConfig.hash_seed)
 - 
int use_hash_seed[¶](#c.PyConfig.use_hash_seed)
- Randomized hash function seed. - If - `use_hash_seed`- `hash_seed`- Set by the - `PYTHONHASHSEED`- Default - *use_hash_seed*value:- `-1`in Python mode,- `0`in isolated mode.
 - 
wchar_t *home[¶](#c.PyConfig.home)
- Set the default Python “home” directory, that is, the location of the standard Python libraries (see - `PYTHONHOME`- Set by the - `PYTHONHOME`- Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)input.
 - 
int import_time[¶](#c.PyConfig.import_time)
- If - `1`, profile import time. If- `2`, include additional output that indicates when an imported module has already been loaded.- Set by the - `-X importtime`- `PYTHONPROFILEIMPORTTIME`- Default: - `0`.- Changed in version 3.14: Added support for - `import_time = 2`
 - 
int inspect[¶](#c.PyConfig.inspect)
- Enter interactive mode after executing a script or a command. - If greater than - `0`, enable inspect: when a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command, even when- `sys.stdin`- Incremented by the - `-i`- `1`if the- `PYTHONINSPECT`- Default: - `0`.
 - 
int install_signal_handlers[¶](#c.PyConfig.install_signal_handlers)
- Install Python signal handlers? - Default: - `1`in Python mode,- `0`in isolated mode.
 - 
int interactive[¶](#c.PyConfig.interactive)
- If greater than - `0`, enable the interactive mode (REPL).- Incremented by the - `-i`- Default: - `0`.
 - 
int int_max_str_digits[¶](#c.PyConfig.int_max_str_digits)
- Configures the - [integer string conversion length limitation](../library/stdtypes.html#int-max-str-digits). An initial value of- `-1`means the value will be taken from the command line or environment or otherwise default to 4300 (- `sys.int_info.default_max_str_digits`- `0`disables the limitation. Values greater than zero but less than 640 (- `sys.int_info.str_digits_check_threshold`- Configured by the - `-X int_max_str_digits`- `PYTHONINTMAXSTRDIGITS`- Default: - `-1`in Python mode. 4300 (- `sys.int_info.default_max_str_digits`- Added in version 3.12. 
 - 
int cpu_count[¶](#c.PyConfig.cpu_count)
- If the value of - `cpu_count`- `-1`then it will override the return values of- `os.cpu_count()`- `os.process_cpu_count()`- `multiprocessing.cpu_count()`- Configured by the - `-X cpu_count=`command line flag or the- *n|default*- `PYTHON_CPU_COUNT`- Default: - `-1`.- Added in version 3.13. 
 - 
int isolated[¶](#c.PyConfig.isolated)
- If greater than - `0`, enable isolated mode:- Set - `safe_path`- `1`: don’t prepend a potentially unsafe path to- `sys.path`
- Set - `use_environment`- `0`: ignore- `PYTHON`environment variables.
- Set - `user_site_directory`- `0`: don’t add the user site directory to- `sys.path`
- Python REPL doesn’t import - `readline`
 - Set to - `1`by the- `-I`- Default: - `0`in Python mode,- `1`in isolated mode.- See also the - [Isolated Configuration](#init-isolated-conf)and- `PyPreConfig.isolated`
 - 
int legacy_windows_stdio[¶](#c.PyConfig.legacy_windows_stdio)
- If non-zero, use - `io.FileIO`- `io._WindowsConsoleIO`for- `sys.stdin`- `sys.stdout`- `sys.stderr`- Set to - `1`if the- `PYTHONLEGACYWINDOWSSTDIO`- Only available on Windows. - `#ifdef MS_WINDOWS`macro can be used for Windows specific code.- Default: - `0`.- See also the - **PEP 528**
 - 
int malloc_stats[¶](#c.PyConfig.malloc_stats)
- If non-zero, dump statistics on - [Python pymalloc memory allocator](memory.html#pymalloc)at exit.- Set to - `1`by the- `PYTHONMALLOCSTATS`- The option is ignored if Python is - `configured using the --without-pymalloc option`- Default: - `0`.
 - 
wchar_t *platlibdir[¶](#c.PyConfig.platlibdir)
- Platform library directory name: - `sys.platlibdir`- Set by the - `PYTHONPLATLIBDIR`- Default: value of the - `PLATLIBDIR`macro which is set by the- `configure --with-platlibdir option`- `"lib"`, or- `"DLLs"`on Windows).- Part of the - [Python Path Configuration](#init-path-config)input.- Added in version 3.9. - Changed in version 3.11: This macro is now used on Windows to locate the standard library extension modules, typically under - `DLLs`. However, for compatibility, note that this value is ignored for any non-standard layouts, including in-tree builds and virtual environments.
 - 
wchar_t *pythonpath_env[¶](#c.PyConfig.pythonpath_env)
- Module search paths ( - `sys.path`- `DELIM`(- `os.pathsep`- Set by the - `PYTHONPATH`- Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)input.
 - 
[PyWideStringList](#c.PyWideStringList)module_search_paths[¶](#c.PyConfig.module_search_paths)
 - 
int module_search_paths_set[¶](#c.PyConfig.module_search_paths_set)
- Module search paths: - `sys.path`- If - `module_search_paths_set`- `0`,- `Py_InitializeFromConfig()`- `module_search_paths`- `module_search_paths_set`to- `1`.- Default: empty list ( - `module_search_paths`) and- `0`(- `module_search_paths_set`).- Part of the - [Python Path Configuration](#init-path-config)output.
 - 
int optimization_level[¶](#c.PyConfig.optimization_level)
- Compilation optimization level: - `0`: Peephole optimizer, set- `__debug__`to- `True`.
- `1`: Level 0, remove assertions, set- `__debug__`to- `False`.
- `2`: Level 1, strip docstrings.
 - Incremented by the - `-O`- `PYTHONOPTIMIZE`- Default: - `0`.
 - 
[PyWideStringList](#c.PyWideStringList)orig_argv[¶](#c.PyConfig.orig_argv)
- The list of the original command line arguments passed to the Python executable: - `sys.orig_argv`- If - `orig_argv`- `argv`- `PyConfig_Read()`- `argv`into- `orig_argv`before modifying- `argv`(if- `parse_argv`- See also the - `argv`- `Py_GetArgcArgv()`- Default: empty list. - Added in version 3.10. 
 - 
int parse_argv[¶](#c.PyConfig.parse_argv)
- Parse command line arguments? - If equals to - `1`, parse- `argv`- [command line arguments](../using/cmdline.html#using-on-cmdline), and strip Python arguments from- `argv`.- The - `PyConfig_Read()`- `PyConfig.argv`- `PyConfig.parse_argv`- `2`after arguments are parsed. Since Python arguments are stripped from- `PyConfig.argv`, parsing arguments twice would parse the application options as Python options.- Default: - `1`in Python mode,- `0`in isolated mode.- Changed in version 3.10: The - `PyConfig.argv`- `PyConfig.parse_argv`- `1`.
 - 
int parser_debug[¶](#c.PyConfig.parser_debug)
- Parser debug mode. If greater than - `0`, turn on parser debugging output (for expert only, depending on compilation options).- Incremented by the - `-d`- `PYTHONDEBUG`- Needs a - [debug build of Python](../using/configure.html#debug-build)(the- `Py_DEBUG`macro must be defined).- Default: - `0`.
 - 
int pathconfig_warnings[¶](#c.PyConfig.pathconfig_warnings)
- If non-zero, calculation of path configuration is allowed to log warnings into - `stderr`. If equals to- `0`, suppress these warnings.- Default: - `1`in Python mode,- `0`in isolated mode.- Part of the - [Python Path Configuration](#init-path-config)input.- Changed in version 3.11: Now also applies on Windows. 
 - 
wchar_t *prefix[¶](#c.PyConfig.prefix)
- The site-specific directory prefix where the platform independent Python files are installed: - `sys.prefix`- Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)output.- See also - `PyConfig.base_prefix`
 - 
wchar_t *program_name[¶](#c.PyConfig.program_name)
- Program name used to initialize - `executable`- On macOS, use - `PYTHONEXECUTABLE`
- If the - `WITH_NEXT_FRAMEWORK`macro is defined, use- `__PYVENV_LAUNCHER__`environment variable if set.
- Use - `argv[0]`of- `argv`
- Otherwise, use - `L"python"`on Windows, or- `L"python3"`on other platforms.
 - Default: - `NULL`.- Part of the - [Python Path Configuration](#init-path-config)input.
 - 
wchar_t *pycache_prefix[¶](#c.PyConfig.pycache_prefix)
- Directory where cached - `.pyc`files are written:- `sys.pycache_prefix`- Set by the - `-X pycache_prefix=PATH`- `PYTHONPYCACHEPREFIX`- If - `NULL`,- `sys.pycache_prefix`- `None`.- Default: - `NULL`.
 - 
int quiet[¶](#c.PyConfig.quiet)
- Quiet mode. If greater than - `0`, don’t display the copyright and version at Python startup in interactive mode.- Incremented by the - `-q`- Default: - `0`.
 - 
wchar_t *run_command[¶](#c.PyConfig.run_command)
- Value of the - `-c`- Used by - `Py_RunMain()`- Default: - `NULL`.
 - 
wchar_t *run_filename[¶](#c.PyConfig.run_filename)
- Filename passed on the command line: trailing command line argument without - `-c`- `-m`- `Py_RunMain()`- For example, it is set to - `script.py`by the- `python3 script.py arg`command line.- See also the - `PyConfig.skip_source_first_line`- Default: - `NULL`.
 - 
wchar_t *run_module[¶](#c.PyConfig.run_module)
- Value of the - `-m`- Used by - `Py_RunMain()`- Default: - `NULL`.
 - 
wchar_t *run_presite[¶](#c.PyConfig.run_presite)
- `package.module`path to module that should be imported before- `site.py`is run.- Set by the - `-X presite=package.module`- `PYTHON_PRESITE`- Needs a - [debug build of Python](../using/configure.html#debug-build)(the- `Py_DEBUG`macro must be defined).- Default: - `NULL`.
 - 
int show_ref_count[¶](#c.PyConfig.show_ref_count)
- Show total reference count at exit (excluding - [immortal](../glossary.html#term-immortal)objects)?- Set to - `1`by- `-X showrefcount`- Needs a - [debug build of Python](../using/configure.html#debug-build)(the- `Py_REF_DEBUG`macro must be defined).- Default: - `0`.
 - 
int site_import[¶](#c.PyConfig.site_import)
- Import the - `site`- If equal to zero, disable the import of the module site and the site-dependent manipulations of - `sys.path`- Also disable these manipulations if the - `site`- `site.main()`- Set to - `0`by the- `-S`- `sys.flags.no_site`- `site_import`- Default: - `1`.
 - 
int skip_source_first_line[¶](#c.PyConfig.skip_source_first_line)
- If non-zero, skip the first line of the - `PyConfig.run_filename`- It allows the usage of non-Unix forms of - `#!cmd`. This is intended for a DOS specific hack only.- Set to - `1`by the- `-x`- Default: - `0`.
 - 
wchar_t *stdio_encoding[¶](#c.PyConfig.stdio_encoding)
 - 
wchar_t *stdio_errors[¶](#c.PyConfig.stdio_errors)
- Encoding and encoding errors of - `sys.stdin`- `sys.stdout`- `sys.stderr`- `sys.stderr`always uses- `"backslashreplace"`error handler).- Use the - `PYTHONIOENCODING`- Default encoding: - `"UTF-8"`if- `PyPreConfig.utf8_mode`
- Otherwise, use the - [locale encoding](../glossary.html#term-locale-encoding).
 - Default error handler: - On Windows: use - `"surrogateescape"`.
- `"surrogateescape"`if- `PyPreConfig.utf8_mode`
- `"strict"`otherwise.
 - See also - `PyConfig.legacy_windows_stdio`
 - 
int tracemalloc[¶](#c.PyConfig.tracemalloc)
- Enable tracemalloc? - If non-zero, call - `tracemalloc.start()`- Set by - `-X tracemalloc=N`- `PYTHONTRACEMALLOC`- Default: - `-1`in Python mode,- `0`in isolated mode.
 - 
int perf_profiling[¶](#c.PyConfig.perf_profiling)
- Enable the Linux - `perf`profiler support?- If equals to - `1`, enable support for the Linux- `perf`profiler.- If equals to - `2`, enable support for the Linux- `perf`profiler with DWARF JIT support.- Set to - `1`by- `-X perf`- `PYTHONPERFSUPPORT`- Set to - `2`by the- `-X perf_jit`- `PYTHON_PERF_JIT_SUPPORT`- Default: - `-1`.- See also - See - [Python support for the Linux perf profiler](../howto/perf_profiling.html#perf-profiling)for more information.- Added in version 3.12. 
 - 
wchar_t *stdlib_dir[¶](#c.PyConfig.stdlib_dir)
- Directory of the Python standard library. - Default: - `NULL`.- Added in version 3.11. 
 - 
int use_environment[¶](#c.PyConfig.use_environment)
- 
If equals to zero, ignore the [environment variables](../using/cmdline.html#using-on-envvars).Set to `0`by the`-E`Default: `1`in Python config and`0`in isolated config.
 - 
int use_system_logger[¶](#c.PyConfig.use_system_logger)
- If non-zero, - `stdout`and- `stderr`will be redirected to the system log.- Only available on macOS 10.12 and later, and on iOS. - Default: - `0`(don’t use the system log) on macOS;- `1`on iOS (use the system log).- Added in version 3.14. 
 - 
int user_site_directory[¶](#c.PyConfig.user_site_directory)
- If non-zero, add the user site directory to - `sys.path`- Set to - `0`by the- `-s`- `-I`- Set to - `0`by the- `PYTHONNOUSERSITE`- Default: - `1`in Python mode,- `0`in isolated mode.
 - 
int verbose[¶](#c.PyConfig.verbose)
- Verbose mode. If greater than - `0`, print a message each time a module is imported, showing the place (filename or built-in module) from which it is loaded.- If greater than or equal to - `2`, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.- Incremented by the - `-v`- Set by the - `PYTHONVERBOSE`- Default: - `0`.
 - 
[PyWideStringList](#c.PyWideStringList)warnoptions[¶](#c.PyConfig.warnoptions)
- Options of the - `warnings`- `sys.warnoptions`- The - `warnings`- `sys.warnoptions`- `PyConfig.warnoptions`- `warnings.filters`which is checked first (highest priority).- The - `-W`- `warnoptions`- The - `PYTHONWARNINGS`- `,`).- Default: empty list. 
 - 
int write_bytecode[¶](#c.PyConfig.write_bytecode)
- If equal to - `0`, Python won’t try to write- `.pyc`files on the import of source modules.- Set to - `0`by the- `-B`- `PYTHONDONTWRITEBYTECODE`- `sys.dont_write_bytecode`- `write_bytecode`- Default: - `1`.
 - 
[PyWideStringList](#c.PyWideStringList)xoptions[¶](#c.PyConfig.xoptions)
- Values of the - `-X`- `sys._xoptions`- Default: empty list. 
 - 
int _pystats[¶](#c.PyConfig._pystats)
- If non-zero, write performance statistics at Python exit. - Need a special build with the - `Py_STATS`macro: see- `--enable-pystats`- Default: - `0`.
 
- 
void PyConfig_InitPythonConfig(

If [ parse_argv](#c.PyConfig.parse_argv) is non-zero, 

[arguments are parsed the same way the regular Python parses](#c.PyConfig.argv)

`argv`[command line arguments](../using/cmdline.html#using-on-cmdline), and Python arguments are stripped from

`argv`.The [ xoptions](#c.PyConfig.xoptions) options are parsed to set other options: see
the 

[command line option.](../using/cmdline.html#cmdoption-X)

`-X`Changed in version 3.9: The `show_alloc_count` field has been removed.

### Initialization with PyConfig[¶](#initialization-with-pyconfig)

Initializing the interpreter from a populated configuration struct is handled
by calling [ Py_InitializeFromConfig()](interp-lifecycle.html#c.Py_InitializeFromConfig).

The caller is responsible to handle exceptions (error or exit) using
[ PyStatus_Exception()](#c.PyStatus_Exception) and 

[.](#c.Py_ExitStatusException)

`Py_ExitStatusException()`If [ PyImport_FrozenModules()](import.html#c.PyImport_FrozenModules), 

[or](import.html#c.PyImport_AppendInittab)

`PyImport_AppendInittab()`[are used, they must be set or called after Python preinitialization and before the Python initialization. If Python is initialized multiple times,](import.html#c.PyImport_ExtendInittab)

`PyImport_ExtendInittab()``PyImport_AppendInittab()` or
`PyImport_ExtendInittab()` must be called before each Python
initialization.The current configuration (`PyConfig` type) is stored in
`PyInterpreterState.config`.

Example setting the program name:

```
void init_python(void)
{
    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);
    /* Set the program name. Implicitly preinitialize Python. */
    status = PyConfig_SetString(&config, &config.program_name,
                                L"/path/to/my_program");
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        goto exception;
    }
    PyConfig_Clear(&config);
    return;
exception:
    PyConfig_Clear(&config);
    Py_ExitStatusException(status);
}
```
More complete example modifying the default configuration, read the configuration, and then override some parameters. Note that since 3.11, many parameters are not calculated until initialization, and so values cannot be read from the configuration structure. Any values set before initialize is called will be left unchanged by initialization:

```
PyStatus init_python(const char *program_name)
{
    PyStatus status;
    PyConfig config;
    PyConfig_InitPythonConfig(&config);
    /* Set the program name before reading the configuration
       (decode byte string from the locale encoding).
       Implicitly preinitialize Python. */
    status = PyConfig_SetBytesString(&config, &config.program_name,
                                     program_name);
    if (PyStatus_Exception(status)) {
        goto done;
    }
    /* Read all configuration at once */
    status = PyConfig_Read(&config);
    if (PyStatus_Exception(status)) {
        goto done;
    }
    /* Specify sys.path explicitly */
    /* If you want to modify the default set of paths, finish
       initialization first and then use PySys_GetObject("path") */
    config.module_search_paths_set = 1;
    status = PyWideStringList_Append(&config.module_search_paths,
                                     L"/path/to/stdlib");
    if (PyStatus_Exception(status)) {
        goto done;
    }
    status = PyWideStringList_Append(&config.module_search_paths,
                                     L"/path/to/more/modules");
    if (PyStatus_Exception(status)) {
        goto done;
    }
    /* Override executable computed by PyConfig_Read() */
    status = PyConfig_SetString(&config, &config.executable,
                                L"/path/to/my_executable");
    if (PyStatus_Exception(status)) {
        goto done;
    }
    status = Py_InitializeFromConfig(&config);
done:
    PyConfig_Clear(&config);
    return status;
}
```
### Isolated Configuration[¶](#isolated-configuration)

[ PyPreConfig_InitIsolatedConfig()](#c.PyPreConfig_InitIsolatedConfig) and

[functions create a configuration to isolate Python from the system. For example, to embed Python into an application.](#c.PyConfig_InitIsolatedConfig)

`PyConfig_InitIsolatedConfig()`This configuration ignores global configuration variables, environment
variables, command line arguments ([ PyConfig.argv](#c.PyConfig.argv) is not parsed)
and user site directory. The C standard streams (ex: 

`stdout`) and the
LC_CTYPE locale are left unchanged. Signal handlers are not installed.Configuration files are still used with this configuration to determine
paths that are unspecified. Ensure [ PyConfig.home](#c.PyConfig.home) is specified
to avoid computing the default path configuration.

### Python Configuration[¶](#python-configuration)

[ PyPreConfig_InitPythonConfig()](#c.PyPreConfig_InitPythonConfig) and 

[functions create a configuration to build a customized Python which behaves as the regular Python.](#c.PyConfig_InitPythonConfig)

`PyConfig_InitPythonConfig()`Environments variables and command line arguments are used to configure Python, whereas global configuration variables are ignored.

This function enables C locale coercion ([ PEP 538](https://peps.python.org/pep-0538/))
and 

[Python UTF-8 Mode](../library/os.html#utf8-mode)(

[) depending on the LC_CTYPE locale,](https://peps.python.org/pep-0540/)

**PEP 540**[and](../using/cmdline.html#envvar-PYTHONUTF8)

`PYTHONUTF8`[environment variables.](../using/cmdline.html#envvar-PYTHONCOERCECLOCALE)

`PYTHONCOERCECLOCALE`### Python Path Configuration[¶](#python-path-configuration)

[ PyConfig](#c.PyConfig) contains multiple fields for the path configuration:

- Path configuration inputs: 
- current working directory: to get absolute paths 
- `PATH`environment variable to get the program full path (from- `PyConfig.program_name`
- `__PYVENV_LAUNCHER__`environment variable
- (Windows only) Application paths in the registry under “SoftwarePythonPythonCoreX.YPythonPath” of HKEY_CURRENT_USER and HKEY_LOCAL_MACHINE (where X.Y is the Python version). 
 
- Path configuration output fields: 

If at least one “output field” is not set, Python calculates the path
configuration to fill unset fields. If
[ module_search_paths_set](#c.PyConfig.module_search_paths_set) is equal to 

`0`,
[is overridden and](#c.PyConfig.module_search_paths)

`module_search_paths``module_search_paths_set` is set to `1`.It is possible to completely ignore the function calculating the default
path configuration by setting explicitly all path configuration output
fields listed above. A string is considered as set even if it is non-empty.
`module_search_paths` is considered as set if
`module_search_paths_set` is set to `1`. In this case,
`module_search_paths` will be used without modification.

Set [ pathconfig_warnings](#c.PyConfig.pathconfig_warnings) to 

`0` to suppress warnings when
calculating the path configuration (Unix only, Windows does not log any warning).If [ base_prefix](#c.PyConfig.base_prefix) or 

[fields are not set, they inherit their value from](#c.PyConfig.base_exec_prefix)

`base_exec_prefix`[and](#c.PyConfig.prefix)

`prefix`[respectively.](#c.PyConfig.exec_prefix)

`exec_prefix`[ Py_RunMain()](interp-lifecycle.html#c.Py_RunMain) and 

[modify](interp-lifecycle.html#c.Py_Main)

`Py_Main()`[:](../library/sys.html#sys.path)

`sys.path`- If - `run_filename`- `__main__.py`script, prepend- `run_filename`to- `sys.path`
- If - `isolated`- If - `run_module`- `sys.path`
- If - `run_filename`- `sys.path`
- Otherwise, prepend an empty string to - `sys.path`
 

If [ site_import](#c.PyConfig.site_import) is non-zero, 

[can be modified by the](../library/sys.html#sys.path)

`sys.path`[module. If](../library/site.html#module-site)

`site`[is non-zero and the user’s site-package directory exists, the](#c.PyConfig.user_site_directory)

`user_site_directory``site` module appends the user’s
site-package directory to `sys.path`.The following configuration files are used by the path configuration:

- `pyvenv.cfg`
- `._pth`file (ex:- `python._pth`)
- `pybuilddir.txt`(Unix only)

If a `._pth` file is present:

- Set - `isolated`- `1`.
- Set - `use_environment`- `0`.
- Set - `site_import`- `0`.
- Set - `safe_path`- `1`.

If [ home](#c.PyConfig.home) is not set and a 

`pyvenv.cfg` file is present in
the same directory as [, or its parent,](#c.PyConfig.executable)

`executable`[and](#c.PyConfig.prefix)

`prefix`[are set that location. When this happens,](#c.PyConfig.exec_prefix)

`exec_prefix`[and](#c.PyConfig.base_prefix)

`base_prefix`[still keep their value, pointing to the base installation. See](#c.PyConfig.base_exec_prefix)

`base_exec_prefix`[Virtual Environments](../library/sys_path_init.html#sys-path-init-virtual-environments)for more information.

The `__PYVENV_LAUNCHER__` environment variable is used to set
[ PyConfig.base_executable](#c.PyConfig.base_executable).

Changed in version 3.14: [ prefix](#c.PyConfig.prefix), and 

[, are now set to the](#c.PyConfig.exec_prefix)

`exec_prefix``pyvenv.cfg` directory. This was previously done by [, therefore affected by](../library/site.html#module-site)

`site`[.](../using/cmdline.html#cmdoption-S)

`-S`## Py_GetArgcArgv()[¶](#py-getargcargv)

- 
void Py_GetArgcArgv(int *argc, wchar_t ***argv)[¶](#c.Py_GetArgcArgv)
- Get the original command line arguments, before Python modified them. - See also - `PyConfig.orig_argv`

## Delaying main module execution[¶](#delaying-main-module-execution)

In some embedding use cases, it may be desirable to separate interpreter initialization from the execution of the main module.

This separation can be achieved by setting `PyConfig.run_command` to the empty
string during initialization (to prevent the interpreter from dropping into the
interactive prompt), and then subsequently executing the desired main module
code using `__main__.__dict__` as the global namespace.