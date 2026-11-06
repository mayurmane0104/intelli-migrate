# Initialization, Finalization, and Threads — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/init.html](https://docs.python.org/3.13/c-api/init.html)

---

# Initialization, Finalization, and Threads[¶](#initialization-finalization-and-threads)

See [Python Initialization Configuration](init_config.html#init-config) for details
on how to configure the interpreter prior to initialization.

## Before Python Initialization[¶](#before-python-initialization)

In an application embedding  Python, the [ Py_Initialize()](#c.Py_Initialize) function must
be called before using any other Python/C API functions; with the exception of
a few functions and the 

[global configuration variables](#global-conf-vars).

The following functions can be safely called before Python is initialized:

- Functions that initialize the interpreter: 
- the runtime pre-initialization functions covered in - [Python Initialization Configuration](init_config.html#init-config)
 
- Configuration functions: 
- `PyInitFrozenExtensions()`
- the configuration functions covered in - [Python Initialization Configuration](init_config.html#init-config)
 
- Informative functions: 
- Utilities: 
- the status reporting and utility functions covered in - [Python Initialization Configuration](init_config.html#init-config)
 
- Memory allocators: 
- Synchronization: 

Note

Despite their apparent similarity to some of the functions listed above,
the following functions **should not be called** before the interpreter has
been initialized: [ Py_EncodeLocale()](sys.html#c.Py_EncodeLocale), 

[,](#c.Py_GetPath)

`Py_GetPath()`[,](#c.Py_GetPrefix)

`Py_GetPrefix()`[,](#c.Py_GetExecPrefix)

`Py_GetExecPrefix()`[,](#c.Py_GetProgramFullPath)

`Py_GetProgramFullPath()`[,](#c.Py_GetPythonHome)

`Py_GetPythonHome()`[,](#c.Py_GetProgramName)

`Py_GetProgramName()`[, and](#c.PyEval_InitThreads)

`PyEval_InitThreads()`[.](#c.Py_RunMain)

`Py_RunMain()`## Global configuration variables[¶](#global-configuration-variables)

Python has variables for the global configuration to control different features
and options. By default, these flags are controlled by [command line
options](../using/cmdline.html#using-on-interface-options).

When a flag is set by an option, the value of the flag is the number of times
that the option was set. For example, `-b` sets [ Py_BytesWarningFlag](#c.Py_BytesWarningFlag)
to 1 and 

`-bb` sets `Py_BytesWarningFlag` to 2.- 
int Py_BytesWarningFlag[¶](#c.Py_BytesWarningFlag)
- This API is kept for backward compatibility: setting - `PyConfig.bytes_warning`- [Python Initialization Configuration](init_config.html#init-config).- Issue a warning when comparing - `bytes`- `bytearray`- `str`- `bytes`with- `int`- `2`.- Set by the - `-b`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_DebugFlag[¶](#c.Py_DebugFlag)
- This API is kept for backward compatibility: setting - `PyConfig.parser_debug`- [Python Initialization Configuration](init_config.html#init-config).- Turn on parser debugging output (for expert only, depending on compilation options). - Set by the - `-d`- `PYTHONDEBUG`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_DontWriteBytecodeFlag[¶](#c.Py_DontWriteBytecodeFlag)
- This API is kept for backward compatibility: setting - `PyConfig.write_bytecode`- [Python Initialization Configuration](init_config.html#init-config).- If set to non-zero, Python won’t try to write - `.pyc`files on the import of source modules.- Set by the - `-B`- `PYTHONDONTWRITEBYTECODE`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_FrozenFlag[¶](#c.Py_FrozenFlag)
- This API is kept for backward compatibility: setting - `PyConfig.pathconfig_warnings`- [Python Initialization Configuration](init_config.html#init-config).- Suppress error messages when calculating the module search path in - `Py_GetPath()`- Private flag used by - `_freeze_module`and- `frozenmain`programs.- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_HashRandomizationFlag[¶](#c.Py_HashRandomizationFlag)
- This API is kept for backward compatibility: setting - `PyConfig.hash_seed`- `PyConfig.use_hash_seed`- [Python Initialization Configuration](init_config.html#init-config).- Set to - `1`if the- `PYTHONHASHSEED`- If the flag is non-zero, read the - `PYTHONHASHSEED`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_IgnoreEnvironmentFlag[¶](#c.Py_IgnoreEnvironmentFlag)
- This API is kept for backward compatibility: setting - `PyConfig.use_environment`- [Python Initialization Configuration](init_config.html#init-config).- Ignore all - `PYTHON*`environment variables, e.g.- `PYTHONPATH`- `PYTHONHOME`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_InspectFlag[¶](#c.Py_InspectFlag)
- This API is kept for backward compatibility: setting - `PyConfig.inspect`- [Python Initialization Configuration](init_config.html#init-config).- When a script is passed as first argument or the - `-c`- `sys.stdin`- Set by the - `-i`- `PYTHONINSPECT`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_InteractiveFlag[¶](#c.Py_InteractiveFlag)
- This API is kept for backward compatibility: setting - `PyConfig.interactive`- [Python Initialization Configuration](init_config.html#init-config).- Set by the - `-i`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_IsolatedFlag[¶](#c.Py_IsolatedFlag)
- This API is kept for backward compatibility: setting - `PyConfig.isolated`- [Python Initialization Configuration](init_config.html#init-config).- Run Python in isolated mode. In isolated mode - `sys.path`- Set by the - `-I`- Added in version 3.4. - Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_LegacyWindowsFSEncodingFlag[¶](#c.Py_LegacyWindowsFSEncodingFlag)
- This API is kept for backward compatibility: setting - `PyPreConfig.legacy_windows_fs_encoding`- [Python Initialization Configuration](init_config.html#init-config).- If the flag is non-zero, use the - `mbcs`encoding with- `replace`error handler, instead of the UTF-8 encoding with- `surrogatepass`error handler, for the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- Set to - `1`if the- `PYTHONLEGACYWINDOWSFSENCODING`- See - **PEP 529**- [Availability](../library/intro.html#availability): Windows.- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_LegacyWindowsStdioFlag[¶](#c.Py_LegacyWindowsStdioFlag)
- This API is kept for backward compatibility: setting - `PyConfig.legacy_windows_stdio`- [Python Initialization Configuration](init_config.html#init-config).- If the flag is non-zero, use - `io.FileIO`- `io._WindowsConsoleIO`for- `sys`- Set to - `1`if the- `PYTHONLEGACYWINDOWSSTDIO`- See - **PEP 528**- [Availability](../library/intro.html#availability): Windows.- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_NoSiteFlag[¶](#c.Py_NoSiteFlag)
- This API is kept for backward compatibility: setting - `PyConfig.site_import`- [Python Initialization Configuration](init_config.html#init-config).- Disable the import of the module - `site`- `sys.path`- `site`is explicitly imported later (call- `site.main()`- Set by the - `-S`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_NoUserSiteDirectory[¶](#c.Py_NoUserSiteDirectory)
- This API is kept for backward compatibility: setting - `PyConfig.user_site_directory`- [Python Initialization Configuration](init_config.html#init-config).- Don’t add the - `user site-packages directory`- `sys.path`- Set by the - `-s`- `-I`- `PYTHONNOUSERSITE`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_OptimizeFlag[¶](#c.Py_OptimizeFlag)
- This API is kept for backward compatibility: setting - `PyConfig.optimization_level`- [Python Initialization Configuration](init_config.html#init-config).- Set by the - `-O`- `PYTHONOPTIMIZE`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_QuietFlag[¶](#c.Py_QuietFlag)
- This API is kept for backward compatibility: setting - `PyConfig.quiet`- [Python Initialization Configuration](init_config.html#init-config).- Don’t display the copyright and version messages even in interactive mode. - Set by the - `-q`- Added in version 3.2. - Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_UnbufferedStdioFlag[¶](#c.Py_UnbufferedStdioFlag)
- This API is kept for backward compatibility: setting - `PyConfig.buffered_stdio`- [Python Initialization Configuration](init_config.html#init-config).- Force the stdout and stderr streams to be unbuffered. - Set by the - `-u`- `PYTHONUNBUFFERED`- Deprecated since version 3.12, will be removed in version 3.14. 

- 
int Py_VerboseFlag[¶](#c.Py_VerboseFlag)
- This API is kept for backward compatibility: setting - `PyConfig.verbose`- [Python Initialization Configuration](init_config.html#init-config).- Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. If greater or equal to - `2`, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.- Set by the - `-v`- `PYTHONVERBOSE`- Deprecated since version 3.12, will be removed in version 3.14. 

## Initializing and finalizing the interpreter[¶](#initializing-and-finalizing-the-interpreter)

- 
void Py_Initialize()[¶](#c.Py_Initialize)
- *Part of the*- [Stable ABI](stable.html#stable).- Initialize the Python interpreter. In an application embedding Python, this should be called before using any other Python/C API functions; see - [Before Python Initialization](#pre-init-safe)for the few exceptions.- This initializes the table of loaded modules ( - `sys.modules`), and creates the fundamental modules- `builtins`- `__main__`- `sys`- `sys.path`). It does not set- `sys.argv`; use the- [Python Initialization Configuration](init_config.html#init-config)API for that. This is a no-op when called for a second time (without calling- `Py_FinalizeEx()`- Use - `Py_InitializeFromConfig()`- [Python Initialization Configuration](init_config.html#init-config).- Note - On Windows, changes the console mode from - `O_TEXT`to- `O_BINARY`, which will also affect non-Python uses of the console using the C Runtime.

- 
void Py_InitializeEx(int initsigs)[¶](#c.Py_InitializeEx)
- *Part of the*- [Stable ABI](stable.html#stable).- This function works like - `Py_Initialize()`- *initsigs*is- `1`. If- *initsigs*is- `0`, it skips initialization registration of signal handlers, which may be useful when CPython is embedded as part of a larger application.- Use - `Py_InitializeFromConfig()`- [Python Initialization Configuration](init_config.html#init-config).

- 
[PyStatus](init_config.html#c.PyStatus)Py_InitializeFromConfig(const[PyConfig](init_config.html#c.PyConfig)*config)[¶](#c.Py_InitializeFromConfig)
- Initialize Python from - *config*configuration, as described in- [Initialization with PyConfig](init_config.html#init-from-config).- See the - [Python Initialization Configuration](init_config.html#init-config)section for details on pre-initializing the interpreter, populating the runtime configuration structure, and querying the returned status structure.

- 
int Py_IsInitialized()[¶](#c.Py_IsInitialized)
- *Part of the*- [Stable ABI](stable.html#stable).- Return true (nonzero) when the Python interpreter has been initialized, false (zero) if not. After - `Py_FinalizeEx()`- `Py_Initialize()`

- 
int Py_IsFinalizing()[¶](#c.Py_IsFinalizing)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return true (non-zero) if the main Python interpreter is - [shutting down](../glossary.html#term-interpreter-shutdown). Return false (zero) otherwise.- Added in version 3.13. 

- 
int Py_FinalizeEx()[¶](#c.Py_FinalizeEx)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.6.- Undo all initializations made by - `Py_Initialize()`- `Py_NewInterpreter()`- `Py_Initialize()`. Ideally, this frees all memory allocated by the Python interpreter. This is a no-op when called for a second time (without calling- `Py_Initialize()`again first).- Since this is the reverse of - `Py_Initialize()`- `Py_RunMain()`- Normally the return value is - `0`. If there were errors during finalization (flushing buffered data),- `-1`is returned.- This function is provided for a number of reasons. An embedding application might want to restart Python without having to restart the application itself. An application that has loaded the Python interpreter from a dynamically loadable library (or DLL) might want to free all memory allocated by Python before unloading the DLL. During a hunt for memory leaks in an application a developer might want to free all memory allocated by Python before exiting from the application. - **Bugs and caveats:**The destruction of modules and objects in modules is done in random order; this may cause destructors (- `__del__()`- `Py_Initialize()`- `Py_FinalizeEx()`- `Py_FinalizeEx()`must not be called recursively from within itself. Therefore, it must not be called by any code that may be run as part of the interpreter shutdown process, such as- `atexit`- Raises an - [auditing event](../library/sys.html#auditing)- `cpython._PySys_ClearAuditHooks`with no arguments.- Added in version 3.6. 

- 
void Py_Finalize()[¶](#c.Py_Finalize)
- *Part of the*- [Stable ABI](stable.html#stable).- This is a backwards-compatible version of - `Py_FinalizeEx()`

- 
int Py_BytesMain(int argc, char **argv)[¶](#c.Py_BytesMain)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- Similar to - `Py_Main()`- *argv*is an array of bytes strings, allowing the calling application to delegate the text decoding step to the CPython runtime.- Added in version 3.8. 

- 
int Py_Main(int argc, wchar_t **argv)[¶](#c.Py_Main)
- *Part of the*- [Stable ABI](stable.html#stable).- The main program for the standard interpreter, encapsulating a full initialization/finalization cycle, as well as additional behaviour to implement reading configurations settings from the environment and command line, and then executing - `__main__`in accordance with- [Command line](../using/cmdline.html#using-on-cmdline).- This is made available for programs which wish to support the full CPython command line interface, rather than just embedding a Python runtime in a larger application. - The - *argc*and- *argv*parameters are similar to those which are passed to a C program’s- `main()`function, except that the- *argv*entries are first converted to- `wchar_t`using- `Py_DecodeLocale()`- The return value is - `2`if the argument list does not represent a valid Python command line, and otherwise the same as- `Py_RunMain()`- In terms of the CPython runtime configuration APIs documented in the - [runtime configuration](init_config.html#init-config)section (and without accounting for error handling),- `Py_Main`is approximately equivalent to:- PyConfig config; PyConfig_InitPythonConfig(&config); PyConfig_SetArgv(&config, argc, argv); Py_InitializeFromConfig(&config); PyConfig_Clear(&config); Py_RunMain(); - In normal usage, an embedding application will call this function - *instead*of calling- `Py_Initialize()`- `Py_InitializeEx()`- `Py_InitializeFromConfig()`- *after*a preceding runtime initialization API call, then exactly which environmental and command line configuration settings will be updated is version dependent (as it depends on which settings correctly support being modified after they have already been set once when the runtime was first initialized).

- 
int Py_RunMain(void)[¶](#c.Py_RunMain)
- Executes the main module in a fully configured CPython runtime. - Executes the command ( - `PyConfig.run_command`- `PyConfig.run_filename`- `PyConfig.run_module`- `__main__`module’s global namespace.- If - `PyConfig.inspect`- `0`if the interpreter exits normally (that is, without raising an exception), the exit status of an unhandled- `SystemExit`- `1`for any other unhandled exception.- If - `PyConfig.inspect`- `-i`- `__main__`module’s global namespace. If the interpreter exited with an exception, it is immediately raised in the REPL session. The function return value is then determined by the way the- *REPL session*terminates:- `0`,- `1`, or the status of a- `SystemExit`- This function always finalizes the Python interpreter before it returns. - See - [Python Configuration](init_config.html#init-python-config)for an example of a customized Python that always runs in isolated mode using- `Py_RunMain()`

- 
int PyUnstable_AtExit([PyInterpreterState](#c.PyInterpreterState)*interp, void (*func)(void*), void *data)[¶](#c.PyUnstable_AtExit)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Register an - `atexit`- *interp*. This is similar to- `Py_AtExit()`- The - [GIL](../glossary.html#term-GIL)must be held for- *interp*.- Added in version 3.13. 

## Process-wide parameters[¶](#process-wide-parameters)

- 
void Py_SetProgramName(const wchar_t *name)[¶](#c.Py_SetProgramName)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.program_name`- [Python Initialization Configuration](init_config.html#init-config).- This function should be called before - `Py_Initialize()`- `argv[0]`argument to the- `main()`function of the program (converted to wide characters). This is used by- `Py_GetPath()`- `'python'`. The argument should point to a zero-terminated wide character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.- Use - `Py_DecodeLocale()`- Deprecated since version 3.11. 

- 
wchar_t *Py_GetProgramName()[¶](#c.Py_GetProgramName)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the program name set with - `PyConfig.program_name`- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Get - `sys.executable`

- 
wchar_t *Py_GetPrefix()[¶](#c.Py_GetPrefix)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *prefix*for installed platform-independent files. This is derived through a number of complicated rules from the program name set with- `PyConfig.program_name`- `'/usr/local/bin/python'`, the prefix is- `'/usr/local'`. The returned string points into static storage; the caller should not modify its value. This corresponds to the- **prefix**variable in the top-level- `Makefile`and the- `--prefix`- **configure**script at build time. The value is available to Python code as- `sys.base_prefix`. It is only useful on Unix. See also the next function.- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Get - `sys.base_prefix`- `sys.prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.

- 
wchar_t *Py_GetExecPrefix()[¶](#c.Py_GetExecPrefix)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *exec-prefix*for installed platform-- *dependent*files. This is derived through a number of complicated rules from the program name set with- `PyConfig.program_name`- `'/usr/local/bin/python'`, the exec-prefix is- `'/usr/local'`. The returned string points into static storage; the caller should not modify its value. This corresponds to the- **exec_prefix**variable in the top-level- `Makefile`and the- `--exec-prefix`argument to the- **configure**script at build time. The value is available to Python code as- `sys.base_exec_prefix`. It is only useful on Unix.- Background: The exec-prefix differs from the prefix when platform dependent files (such as executables and shared libraries) are installed in a different directory tree. In a typical installation, platform dependent files may be installed in the - `/usr/local/plat`subtree while platform independent may be installed in- `/usr/local`.- Generally speaking, a platform is a combination of hardware and software families, e.g. Sparc machines running the Solaris 2.x operating system are considered the same platform, but Intel machines running Solaris 2.x are another platform, and Intel machines running Linux are yet another platform. Different major revisions of the same operating system generally also form different platforms. Non-Unix operating systems are a different story; the installation strategies on those systems are so different that the prefix and exec-prefix are meaningless, and set to the empty string. Note that compiled Python bytecode files are platform independent (but not independent from the Python version by which they were compiled!). - System administrators will know how to configure the - **mount**or- **automount**programs to share- `/usr/local`between platforms while having- `/usr/local/plat`be a different filesystem for each platform.- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Get - `sys.base_exec_prefix`- `sys.exec_prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.

- 
wchar_t *Py_GetProgramFullPath()[¶](#c.Py_GetProgramFullPath)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the full program name of the Python executable; this is computed as a side-effect of deriving the default module search path from the program name (set by - `PyConfig.program_name`- `sys.executable`.- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Get - `sys.executable`

- 
wchar_t *Py_GetPath()[¶](#c.Py_GetPath)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the default module search path; this is computed from the program name (set by - `PyConfig.program_name`- `':'`on Unix and macOS,- `';'`on Windows. The returned string points into static storage; the caller should not modify its value. The list- `sys.path`- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Get - `sys.path`

- 
const char *Py_GetVersion()[¶](#c.Py_GetVersion)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the version of this Python interpreter. This is a string that looks something like - "3.0a5+ (py3k:63103M, May 12 2008, 00:53:55) \n[GCC 4.2.3]" - The first word (up to the first space character) is the current Python version; the first characters are the major and minor version separated by a period. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as - `sys.version`- See also the - `Py_Version`

- 
const char *Py_GetPlatform()[¶](#c.Py_GetPlatform)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the platform identifier for the current platform. On Unix, this is formed from the “official” name of the operating system, converted to lower case, followed by the major revision number; e.g., for Solaris 2.x, which is also known as SunOS 5.x, the value is - `'sunos5'`. On macOS, it is- `'darwin'`. On Windows, it is- `'win'`. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as- `sys.platform`.

- 
const char *Py_GetCopyright()[¶](#c.Py_GetCopyright)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the official copyright string for the current Python version, for example - `'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'`- The returned string points into static storage; the caller should not modify its value. The value is available to Python code as - `sys.copyright`.

- 
const char *Py_GetCompiler()[¶](#c.Py_GetCompiler)
- *Part of the*- [Stable ABI](stable.html#stable).- Return an indication of the compiler used to build the current Python version, in square brackets, for example: - `"[GCC 2.7.2.2]"`- The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable - `sys.version`.

- 
const char *Py_GetBuildInfo()[¶](#c.Py_GetBuildInfo)
- *Part of the*- [Stable ABI](stable.html#stable).- Return information about the sequence number and build date and time of the current Python interpreter instance, for example - `"#67, Aug 1 1997, 22:34:28"`- The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable - `sys.version`.

- 
void PySys_SetArgvEx(int argc, wchar_t **argv, int updatepath)[¶](#c.PySys_SetArgvEx)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.argv`- `PyConfig.parse_argv`- `PyConfig.safe_path`- [Python Initialization Configuration](init_config.html#init-config).- Set - `sys.argv`- *argc*and- *argv*. These parameters are similar to those passed to the program’s- `main()`function with the difference that the first entry should refer to the script file to be executed rather than the executable hosting the Python interpreter. If there isn’t a script that will be run, the first entry in- *argv*can be an empty string. If this function fails to initialize- `sys.argv`, a fatal condition is signalled using- `Py_FatalError()`- If - *updatepath*is zero, this is all the function does. If- *updatepath*is non-zero, the function also modifies- `sys.path`- If the name of an existing script is passed in - `argv[0]`, the absolute path of the directory where the script is located is prepended to- `sys.path`
- Otherwise (that is, if - *argc*is- `0`or- `argv[0]`doesn’t point to an existing file name), an empty string is prepended to- `sys.path`- `"."`).
 - Use - `Py_DecodeLocale()`- See also - `PyConfig.orig_argv`- `PyConfig.argv`- [Python Initialization Configuration](init_config.html#init-config).- Note - It is recommended that applications embedding the Python interpreter for purposes other than executing a single script pass - `0`as- *updatepath*, and update- `sys.path`- **CVE 2008-5983**- On versions before 3.1.3, you can achieve the same effect by manually popping the first - `sys.path`- `PySys_SetArgv()`- PyRun_SimpleString("import sys; sys.path.pop(0)\n"); - Added in version 3.1.3. - Deprecated since version 3.11. 

- 
void PySys_SetArgv(int argc, wchar_t **argv)[¶](#c.PySys_SetArgv)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.argv`- `PyConfig.parse_argv`- [Python Initialization Configuration](init_config.html#init-config).- This function works like - `PySys_SetArgvEx()`- *updatepath*set to- `1`unless the- **python**interpreter was started with the- `-I`- Use - `Py_DecodeLocale()`- See also - `PyConfig.orig_argv`- `PyConfig.argv`- [Python Initialization Configuration](init_config.html#init-config).- Changed in version 3.4: The - *updatepath*value depends on- `-I`- Deprecated since version 3.11. 

- 
void Py_SetPythonHome(const wchar_t *home)[¶](#c.Py_SetPythonHome)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.home`- [Python Initialization Configuration](init_config.html#init-config).- Set the default “home” directory, that is, the location of the standard Python libraries. See - `PYTHONHOME`- The argument should point to a zero-terminated character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage. - Use - `Py_DecodeLocale()`- Deprecated since version 3.11. 

- 
wchar_t *Py_GetPythonHome()[¶](#c.Py_GetPythonHome)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the default “home”, that is, the value set by - `PyConfig.home`- `PYTHONHOME`- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Get - `PyConfig.home`- `PYTHONHOME`

## Thread State and the Global Interpreter Lock[¶](#thread-state-and-the-global-interpreter-lock)

The Python interpreter is not fully thread-safe.  In order to support
multi-threaded Python programs, there’s a global lock, called the [global
interpreter lock](../glossary.html#term-global-interpreter-lock) or [GIL](../glossary.html#term-GIL), that must be held by the current thread before
it can safely access Python objects. Without the lock, even the simplest
operations could cause problems in a multi-threaded program: for example, when
two threads simultaneously increment the reference count of the same object, the
reference count could end up being incremented only once instead of twice.

Therefore, the rule exists that only the thread that has acquired the
[GIL](../glossary.html#term-GIL) may operate on Python objects or call Python/C API functions.
In order to emulate concurrency of execution, the interpreter regularly
tries to switch threads (see [ sys.setswitchinterval()](../library/sys.html#sys.setswitchinterval)).  The lock is also
released around potentially blocking I/O operations like reading or writing
a file, so that other Python threads can run in the meantime.

The Python interpreter keeps some thread-specific bookkeeping information
inside a data structure called [ PyThreadState](#c.PyThreadState).  There’s also one
global variable pointing to the current 

`PyThreadState`: it can
be retrieved using [.](#c.PyThreadState_Get)

`PyThreadState_Get()`### Releasing the GIL from extension code[¶](#releasing-the-gil-from-extension-code)

Most extension code manipulating the [GIL](../glossary.html#term-GIL) has the following simple
structure:

```
Save the thread state in a local variable.
Release the global interpreter lock.
... Do some blocking I/O operation ...
Reacquire the global interpreter lock.
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
Here is how these functions work: the global interpreter lock is used to protect the pointer to the current thread state. When releasing the lock and saving the thread state, the current thread state pointer must be retrieved before the lock is released (since another thread could immediately acquire the lock and store its own thread state in the global variable). Conversely, when acquiring the lock and restoring the thread state, the lock must be acquired before storing the thread state pointer.

Note

Calling system I/O functions is the most common use case for releasing
the GIL, but it can also be useful before calling long-running computations
which don’t need access to Python objects, such as compression or
cryptographic functions operating over memory buffers.  For example, the
standard [ zlib](../library/zlib.html#module-zlib) and 

[modules release the GIL when compressing or hashing data.](../library/hashlib.html#module-hashlib)

`hashlib`### Non-Python created threads[¶](#non-python-created-threads)

When threads are created using the dedicated Python APIs (such as the
[ threading](../library/threading.html#module-threading) module), a thread state is automatically associated to them
and the code showed above is therefore correct.  However, when threads are
created from C (for example by a third-party library with its own thread
management), they don’t hold the GIL, nor is there a thread state structure
for them.

If you need to call Python code from these threads (often this will be part of a callback API provided by the aforementioned third-party library), you must first register these threads with the interpreter by creating a thread state data structure, then acquiring the GIL, and finally storing their thread state pointer, before you can start using the Python/C API. When you are done, you should reset the thread state pointer, release the GIL, and finally free the thread state data structure.

The [ PyGILState_Ensure()](#c.PyGILState_Ensure) and 

[functions do all of the above automatically. The typical idiom for calling into Python from a C thread is:](#c.PyGILState_Release)

`PyGILState_Release()````
PyGILState_STATE gstate;
gstate = PyGILState_Ensure();
/* Perform Python actions here. */
result = CallSomeFunction();
/* evaluate result or handle exception */
/* Release the thread. No Python API allowed beyond this point. */
PyGILState_Release(gstate);
```
Note that the `PyGILState_*` functions assume there is only one global
interpreter (created automatically by [ Py_Initialize()](#c.Py_Initialize)).  Python
supports the creation of additional interpreters (using

[), but mixing multiple interpreters and the](#c.Py_NewInterpreter)

`Py_NewInterpreter()``PyGILState_*` API is unsupported.### Cautions about fork()[¶](#cautions-about-fork)

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

`PyThreadState`[objects. Due to this and the special nature of the](#c.PyInterpreterState)

`PyInterpreterState`[“main” interpreter](#sub-interpreter-support),

`fork()` should only be called in that interpreter’s “main”
thread, where the CPython global runtime was originally initialized.
The only exception is if `exec()` will be called immediately
after.### Cautions regarding runtime finalization[¶](#cautions-regarding-runtime-finalization)

In the late stage of [interpreter shutdown](../glossary.html#term-interpreter-shutdown), after attempting to wait for
non-daemon threads to exit (though this can be interrupted by
[ KeyboardInterrupt](../library/exceptions.html#KeyboardInterrupt)) and running the 

[functions, the runtime is marked as](../library/atexit.html#module-atexit)

`atexit`*finalizing*:

[and](#c.Py_IsFinalizing)

`Py_IsFinalizing()`[return true. At this point, only the](../library/sys.html#sys.is_finalizing)

`sys.is_finalizing()`*finalization thread*that initiated finalization (typically the main thread) is allowed to acquire the

[GIL](../glossary.html#term-GIL).

If any thread, other than the finalization thread, attempts to acquire the GIL
during finalization, either explicitly via [ PyGILState_Ensure()](#c.PyGILState_Ensure),

[,](#c.Py_END_ALLOW_THREADS)

`Py_END_ALLOW_THREADS`[, or](#c.PyEval_AcquireThread)

`PyEval_AcquireThread()``PyEval_AcquireLock()`, or implicitly when the interpreter attempts to
reacquire it after having yielded it, the thread enters **a permanently blocked state**where it remains until the program exits. In most cases this is harmless, but this can result in deadlock if a later stage of finalization attempts to acquire a lock owned by the blocked thread, or otherwise waits on the blocked thread.

Gross? Yes. This prevents random crashes and/or unexpectedly skipped C++ finalizations further up the call stack when such threads were forcibly exited here in CPython 3.13.7 and earlier. The CPython runtime GIL acquiring C APIs have never had any error reporting or handling expectations at GIL acquisition time that would’ve allowed for graceful exit from this situation. Changing that would require new stable C APIs and rewriting the majority of C code in the CPython ecosystem to use those with error handling.

### High-level API[¶](#high-level-api)

These are the most commonly used types and functions when writing C extension code, or when embedding the Python interpreter:

- 
type PyInterpreterState[¶](#c.PyInterpreterState)
- *Part of the*- [Limited API](stable.html#stable)(as an opaque struct).- This data structure represents the state shared by a number of cooperating threads. Threads belonging to the same interpreter share their module administration and a few other internal items. There are no public members in this structure. - Threads belonging to different interpreters initially share nothing, except process state like available memory, open file descriptors and such. The global interpreter lock is also shared by all threads, regardless of to which interpreter they belong. - Changed in version 3.12: - **PEP 684**- [per-interpreter GIL](#per-interpreter-gil). See- `Py_NewInterpreterFromConfig()`

- 
type PyThreadState[¶](#c.PyThreadState)
- *Part of the*- [Limited API](stable.html#stable)(as an opaque struct).- This data structure represents the state of a single thread. The only public data member is: - 
[PyInterpreterState](#c.PyInterpreterState)*interp[¶](#c.PyThreadState.interp)
- This thread’s interpreter state. 
 
- 

- 
void PyEval_InitThreads()[¶](#c.PyEval_InitThreads)
- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated function which does nothing. - In Python 3.6 and older, this function created the GIL if it didn’t exist. - Changed in version 3.9: The function now does nothing. - Changed in version 3.7: This function is now called by - `Py_Initialize()`- Changed in version 3.2: This function cannot be called before - `Py_Initialize()`- Deprecated since version 3.9. 

- 
[PyThreadState](#c.PyThreadState)*PyEval_SaveThread()[¶](#c.PyEval_SaveThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Release the global interpreter lock (if it has been created) and reset the thread state to - `NULL`, returning the previous thread state (which is not- `NULL`). If the lock has been created, the current thread must have acquired it.

- 
void PyEval_RestoreThread([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyEval_RestoreThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Acquire the global interpreter lock (if it has been created) and set the thread state to - *tstate*, which must not be- `NULL`. If the lock has been created, the current thread must not have acquired it, otherwise deadlock ensues.- Note - Calling this function from a thread when the runtime is finalizing will hang the thread until the program exits, even if the thread was not created by Python. Refer to - [Cautions regarding runtime finalization](#cautions-regarding-runtime-finalization)for more details.- Changed in version 3.13.8: Hangs the current thread, rather than terminating it, if called while the interpreter is finalizing. 

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_Get()[¶](#c.PyThreadState_Get)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the current thread state. The global interpreter lock must be held. When the current thread state is - `NULL`, this issues a fatal error (so that the caller needn’t check for- `NULL`).- See also - `PyThreadState_GetUnchecked()`

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_GetUnchecked()[¶](#c.PyThreadState_GetUnchecked)
- Similar to - `PyThreadState_Get()`- Added in version 3.13: In Python 3.5 to 3.12, the function was private and known as - `_PyThreadState_UncheckedGet()`.

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_Swap([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Swap)
- *Part of the*- [Stable ABI](stable.html#stable).- Swap the current thread state with the thread state given by the argument - *tstate*, which may be- `NULL`.- The - [GIL](../glossary.html#term-GIL)does not need to be held, but will be held upon returning if- *tstate*is non-- `NULL`.

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
- *Part of the*- [Stable ABI](stable.html#stable).- Ensure that the current thread is ready to call the Python C API regardless of the current state of Python, or of the global interpreter lock. This may be called as many times as desired by a thread as long as each call is matched with a call to - `PyGILState_Release()`- `PyGILState_Ensure()`- `PyGILState_Release()`calls as long as the thread state is restored to its previous state before the Release(). For example, normal usage of the- `Py_BEGIN_ALLOW_THREADS`- `Py_END_ALLOW_THREADS`- The return value is an opaque “handle” to the thread state when - `PyGILState_Ensure()`- `PyGILState_Release()`- *cannot*be shared - each unique call to- `PyGILState_Ensure()`must save the handle for its call to- `PyGILState_Release()`.- When the function returns, the current thread will hold the GIL and be able to call arbitrary Python code. Failure is a fatal error. - Note - Calling this function from a thread when the runtime is finalizing will hang the thread until the program exits, even if the thread was not created by Python. Refer to - [Cautions regarding runtime finalization](#cautions-regarding-runtime-finalization)for more details.- Changed in version 3.13.8: Hangs the current thread, rather than terminating it, if called while the interpreter is finalizing. 

- 
void PyGILState_Release([PyGILState_STATE](#c.PyGILState_STATE))[¶](#c.PyGILState_Release)
- *Part of the*- [Stable ABI](stable.html#stable).- Release any resources previously acquired. After this call, Python’s state will be the same as it was prior to the corresponding - `PyGILState_Ensure()`- Every call to - `PyGILState_Ensure()`- `PyGILState_Release()`

- 
[PyThreadState](#c.PyThreadState)*PyGILState_GetThisThreadState()[¶](#c.PyGILState_GetThisThreadState)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the current thread state for this thread. May return - `NULL`if no GILState API has been used on the current thread. Note that the main thread always has such a thread-state, even if no auto-thread-state call has been made on the main thread. This is mainly a helper/diagnostic function.

- 
int PyGILState_Check()[¶](#c.PyGILState_Check)
- Return - `1`if the current thread is holding the GIL and- `0`otherwise. This function can be called from any thread at any time. Only if it has had its Python thread state initialized and currently is holding the GIL will it return- `1`. This is mainly a helper/diagnostic function. It can be useful for example in callback contexts or memory allocation functions when knowing that the GIL is locked can allow the caller to perform sensitive actions or otherwise behave differently.- Added in version 3.4. 

The following macros are normally used without a trailing semicolon; look for example usage in the Python source distribution.

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

### Low-level API[¶](#low-level-api)

All of the following functions must be called after [ Py_Initialize()](#c.Py_Initialize).

Changed in version 3.7: [ Py_Initialize()](#c.Py_Initialize) now initializes the 

[GIL](../glossary.html#term-GIL).

- 
[PyInterpreterState](#c.PyInterpreterState)*PyInterpreterState_New()[¶](#c.PyInterpreterState_New)
- *Part of the*- [Stable ABI](stable.html#stable).- Create a new interpreter state object. The global interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function. - Raises an - [auditing event](../library/sys.html#auditing)- `cpython.PyInterpreterState_New`with no arguments.

- 
void PyInterpreterState_Clear([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyInterpreterState_Clear)
- *Part of the*- [Stable ABI](stable.html#stable).- Reset all information in an interpreter state object. The global interpreter lock must be held. - Raises an - [auditing event](../library/sys.html#auditing)- `cpython.PyInterpreterState_Clear`with no arguments.

- 
void PyInterpreterState_Delete([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyInterpreterState_Delete)
- *Part of the*- [Stable ABI](stable.html#stable).- Destroy an interpreter state object. The global interpreter lock need not be held. The interpreter state must have been reset with a previous call to - `PyInterpreterState_Clear()`

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_New([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyThreadState_New)
- *Part of the*- [Stable ABI](stable.html#stable).- Create a new thread state object belonging to the given interpreter object. The global interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function. 

- 
void PyThreadState_Clear([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Clear)
- *Part of the*- [Stable ABI](stable.html#stable).- Reset all information in a thread state object. The global interpreter lock must be held. - Changed in version 3.9: This function now calls the - `PyThreadState.on_delete`callback. Previously, that happened in- `PyThreadState_Delete()`- Changed in version 3.13: The - `PyThreadState.on_delete`callback was removed.

- 
void PyThreadState_Delete([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Delete)
- *Part of the*- [Stable ABI](stable.html#stable).- Destroy a thread state object. The global interpreter lock need not be held. The thread state must have been reset with a previous call to - `PyThreadState_Clear()`

- 
void PyThreadState_DeleteCurrent(void)[¶](#c.PyThreadState_DeleteCurrent)
- Destroy the current thread state and release the global interpreter lock. Like - `PyThreadState_Delete()`- `PyThreadState_Clear()`

- 
[PyFrameObject](frame.html#c.PyFrameObject)*PyThreadState_GetFrame([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_GetFrame)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the current frame of the Python thread state - *tstate*.- Return a - [strong reference](../glossary.html#term-strong-reference). Return- `NULL`if no frame is currently executing.- See also - `PyEval_GetFrame()`- *tstate*must not be- `NULL`.- Added in version 3.9. 

- 
uint64_t PyThreadState_GetID([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_GetID)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the unique thread state identifier of the Python thread state - *tstate*.- *tstate*must not be- `NULL`.- Added in version 3.9. 

- 
[PyInterpreterState](#c.PyInterpreterState)*PyThreadState_GetInterpreter([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_GetInterpreter)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the interpreter of the Python thread state - *tstate*.- *tstate*must not be- `NULL`.- Added in version 3.9. 

- 
void PyThreadState_EnterTracing([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_EnterTracing)
- Suspend tracing and profiling in the Python thread state - *tstate*.- Resume them using the - `PyThreadState_LeaveTracing()`- Added in version 3.11. 

- 
void PyThreadState_LeaveTracing([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_LeaveTracing)
- Resume tracing and profiling in the Python thread state - *tstate*suspended by the- `PyThreadState_EnterTracing()`- See also - `PyEval_SetTrace()`- `PyEval_SetProfile()`- Added in version 3.11. 

- 
[PyInterpreterState](#c.PyInterpreterState)*PyInterpreterState_Get(void)[¶](#c.PyInterpreterState_Get)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Get the current interpreter. - Issue a fatal error if there is no current Python thread state or no current interpreter. It cannot return NULL. - The caller must hold the GIL. - Added in version 3.9. 

- 
int64_t PyInterpreterState_GetID([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyInterpreterState_GetID)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return the interpreter’s unique ID. If there was any error in doing so then - `-1`is returned and an error is set.- The caller must hold the GIL. - Added in version 3.7. 

- 
[PyObject](structures.html#c.PyObject)*PyInterpreterState_GetDict([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyInterpreterState_GetDict)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- Return a dictionary in which interpreter-specific data may be stored. If this function returns - `NULL`then no exception has been raised and the caller should assume no interpreter-specific dict is available.- This is not a replacement for - `PyModule_GetState()`- The returned dictionary is borrowed from the interpreter and is valid until interpreter shutdown. - Added in version 3.8. 

- 
[PyObject](structures.html#c.PyObject)*PyUnstable_InterpreterState_GetMainModule([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyUnstable_InterpreterState_GetMainModule)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return a - [strong reference](../glossary.html#term-strong-reference)to the- `__main__`- [module object](module.html#moduleobjects)for the given interpreter.- The caller must hold the GIL. - Added in version 3.13. 

- 
typedef [PyObject](structures.html#c.PyObject)*(*_PyFrameEvalFunction)([PyThreadState](#c.PyThreadState)*tstate,[_PyInterpreterFrame](frame.html#c._PyInterpreterFrame)*frame, int throwflag)[¶](#c._PyFrameEvalFunction)
- Type of a frame evaluation function. - The - *throwflag*parameter is used by the- `throw()`method of generators: if non-zero, handle the current exception.- Changed in version 3.9: The function now takes a - *tstate*parameter.- Changed in version 3.11: The - *frame*parameter changed from- `PyFrameObject*`to- `_PyInterpreterFrame*`.

- 
[_PyFrameEvalFunction](#c._PyFrameEvalFunction)_PyInterpreterState_GetEvalFrameFunc([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c._PyInterpreterState_GetEvalFrameFunc)
- Get the frame evaluation function. - See the - **PEP 523**- Added in version 3.9. 

- 
void _PyInterpreterState_SetEvalFrameFunc([PyInterpreterState](#c.PyInterpreterState)*interp,[_PyFrameEvalFunction](#c._PyFrameEvalFunction)eval_frame)[¶](#c._PyInterpreterState_SetEvalFrameFunc)
- Set the frame evaluation function. - See the - **PEP 523**- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyThreadState_GetDict()[¶](#c.PyThreadState_GetDict)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a dictionary in which extensions can store thread-specific state information. Each extension should use a unique key to use to store state in the dictionary. It is okay to call this function when no current thread state is available. If this function returns - `NULL`, no exception has been raised and the caller should assume no current thread state is available.

- 
int PyThreadState_SetAsyncExc(unsigned long id, [PyObject](structures.html#c.PyObject)*exc)[¶](#c.PyThreadState_SetAsyncExc)
- *Part of the*- [Stable ABI](stable.html#stable).- Asynchronously raise an exception in a thread. The - *id*argument is the thread id of the target thread;- *exc*is the exception object to be raised. This function does not steal any references to- *exc*. To prevent naive misuse, you must write your own C extension to call this. Must be called with the GIL held. Returns the number of thread states modified; this is normally one, but will be zero if the thread id isn’t found. If- *exc*is- `NULL`, the pending exception (if any) for the thread is cleared. This raises no exceptions.- Changed in version 3.7: The type of the - *id*parameter changed from long to unsigned long.

- 
void PyEval_AcquireThread([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyEval_AcquireThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Acquire the global interpreter lock and set the current thread state to - *tstate*, which must not be- `NULL`. The lock must have been created earlier. If this thread already has the lock, deadlock ensues.- Note - Calling this function from a thread when the runtime is finalizing will hang the thread until the program exits, even if the thread was not created by Python. Refer to - [Cautions regarding runtime finalization](#cautions-regarding-runtime-finalization)for more details.- Changed in version 3.8: Updated to be consistent with - `PyEval_RestoreThread()`- `Py_END_ALLOW_THREADS()`- `PyGILState_Ensure()`- Changed in version 3.13.8: Hangs the current thread, rather than terminating it, if called while the interpreter is finalizing. - `PyEval_RestoreThread()`

- 
void PyEval_ReleaseThread([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyEval_ReleaseThread)
- *Part of the*- [Stable ABI](stable.html#stable).- Reset the current thread state to - `NULL`and release the global interpreter lock. The lock must have been created earlier and must be held by the current thread. The- *tstate*argument, which must not be- `NULL`, is only used to check that it represents the current thread state — if it isn’t, a fatal error is reported.- `PyEval_SaveThread()`

## Sub-interpreter support[¶](#sub-interpreter-support)

While in most uses, you will only embed a single Python interpreter, there are cases where you need to create several independent interpreters in the same process and perhaps even in the same thread. Sub-interpreters allow you to do that.

The “main” interpreter is the first one created when the runtime initializes.
It is usually the only Python interpreter in a process.  Unlike sub-interpreters,
the main interpreter has unique process-global responsibilities like signal
handling.  It is also responsible for execution during runtime initialization and
is usually the active interpreter during runtime finalization.  The
[ PyInterpreterState_Main()](#c.PyInterpreterState_Main) function returns a pointer to its state.

You can switch between sub-interpreters using the [ PyThreadState_Swap()](#c.PyThreadState_Swap)
function. You can create and destroy them using the following functions:

- 
type PyInterpreterConfig[¶](#c.PyInterpreterConfig)
- Structure containing most parameters to configure a sub-interpreter. Its values are used only in - `Py_NewInterpreterFromConfig()`- Added in version 3.12. - Structure fields: - 
int use_main_obmalloc[¶](#c.PyInterpreterConfig.use_main_obmalloc)
- If this is - `0`then the sub-interpreter will use its own “object” allocator state. Otherwise it will use (share) the main interpreter’s.- If this is - `0`then- `check_multi_interp_extensions`- `1`(non-zero). If this is- `1`then- `gil`- `PyInterpreterConfig_OWN_GIL`
 - 
int allow_fork[¶](#c.PyInterpreterConfig.allow_fork)
- If this is - `0`then the runtime will not support forking the process in any thread where the sub-interpreter is currently active. Otherwise fork is unrestricted.- Note that the - `subprocess`
 - 
int allow_exec[¶](#c.PyInterpreterConfig.allow_exec)
- If this is - `0`then the runtime will not support replacing the current process via exec (e.g.- `os.execv()`- Note that the - `subprocess`
 - 
int allow_threads[¶](#c.PyInterpreterConfig.allow_threads)
- If this is - `0`then the sub-interpreter’s- `threading`
 - 
int allow_daemon_threads[¶](#c.PyInterpreterConfig.allow_daemon_threads)
- If this is - `0`then the sub-interpreter’s- `threading`- `allow_threads`
 - 
int check_multi_interp_extensions[¶](#c.PyInterpreterConfig.check_multi_interp_extensions)
- If this is - `0`then all extension modules may be imported, including legacy (single-phase init) modules, in any thread where the sub-interpreter is currently active. Otherwise only multi-phase init extension modules (see- **PEP 489**- `Py_mod_multiple_interpreters`- This must be - `1`(non-zero) if- `use_main_obmalloc`- `0`.
 - 
int gil[¶](#c.PyInterpreterConfig.gil)
- This determines the operation of the GIL for the sub-interpreter. It may be one of the following: - 
PyInterpreterConfig_DEFAULT_GIL[¶](#c.PyInterpreterConfig_DEFAULT_GIL)
- Use the default selection ( - `PyInterpreterConfig_SHARED_GIL`
 - 
PyInterpreterConfig_SHARED_GIL[¶](#c.PyInterpreterConfig_SHARED_GIL)
- Use (share) the main interpreter’s GIL. 
 - 
PyInterpreterConfig_OWN_GIL[¶](#c.PyInterpreterConfig_OWN_GIL)
- Use the sub-interpreter’s own GIL. 
 - If this is - `PyInterpreterConfig_OWN_GIL`- `PyInterpreterConfig.use_main_obmalloc`- `0`.
- 
PyInterpreterConfig_DEFAULT_GIL
 
- 
int use_main_obmalloc

- 
[PyStatus](init_config.html#c.PyStatus)Py_NewInterpreterFromConfig([PyThreadState](#c.PyThreadState)**tstate_p, const[PyInterpreterConfig](#c.PyInterpreterConfig)*config)[¶](#c.Py_NewInterpreterFromConfig)
- Create a new sub-interpreter. This is an (almost) totally separate environment for the execution of Python code. In particular, the new interpreter has separate, independent versions of all imported modules, including the fundamental modules - `builtins`- `__main__`- `sys`- `sys.modules`) and the module search path (- `sys.path`) are also separate. The new environment has no- `sys.argv`variable. It has new standard I/O stream file objects- `sys.stdin`,- `sys.stdout`and- `sys.stderr`(however these refer to the same underlying file descriptors).- The given - *config*controls the options with which the interpreter is initialized.- Upon success, - *tstate_p*will be set to the first thread state created in the new sub-interpreter. This thread state is made in the current thread state. Note that no actual thread is created; see the discussion of thread states below. If creation of the new interpreter is unsuccessful,- *tstate_p*is set to- `NULL`; no exception is set since the exception state is stored in the current thread state and there may not be a current thread state.- Like all other Python/C API functions, the global interpreter lock must be held before calling this function and is still held when it returns. Likewise a current thread state must be set on entry. On success, the returned thread state will be set as current. If the sub-interpreter is created with its own GIL then the GIL of the calling interpreter will be released. When the function returns, the new interpreter’s GIL will be held by the current thread and the previously interpreter’s GIL will remain released here. - Added in version 3.12. - Sub-interpreters are most effective when isolated from each other, with certain functionality restricted: - PyInterpreterConfig config = { .use_main_obmalloc = 0, .allow_fork = 0, .allow_exec = 0, .allow_threads = 1, .allow_daemon_threads = 0, .check_multi_interp_extensions = 1, .gil = PyInterpreterConfig_OWN_GIL, }; PyThreadState *tstate = NULL; PyStatus status = Py_NewInterpreterFromConfig(&tstate, &config); if (PyStatus_Exception(status)) { Py_ExitStatusException(status); } - Note that the config is used only briefly and does not get modified. During initialization the config’s values are converted into various - `PyInterpreterState`- `PyInterpreterState`.- Extension modules are shared between (sub-)interpreters as follows: - For modules using multi-phase initialization, e.g. - `PyModule_FromDefAndSpec()`
- For modules using single-phase initialization, e.g. - `PyModule_Create()`- `init`function is not called. Objects in the module’s dictionary thus end up shared across (sub-)interpreters, which might cause unwanted behavior (see- [Bugs and caveats](#bugs-and-caveats)below).- Note that this is different from what happens when an extension is imported after the interpreter has been completely re-initialized by calling - `Py_FinalizeEx()`- `Py_Initialize()`- `initmodule`function- *is*called again. As with multi-phase initialization, this means that only C-level static and global variables are shared between these modules.
 

- 
[PyThreadState](#c.PyThreadState)*Py_NewInterpreter(void)[¶](#c.Py_NewInterpreter)
- *Part of the*- [Stable ABI](stable.html#stable).- Create a new sub-interpreter. This is essentially just a wrapper around - `Py_NewInterpreterFromConfig()`

- 
void Py_EndInterpreter([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.Py_EndInterpreter)
- *Part of the*- [Stable ABI](stable.html#stable).- Destroy the (sub-)interpreter represented by the given thread state. The given thread state must be the current thread state. See the discussion of thread states below. When the call returns, the current thread state is - `NULL`. All thread states associated with this interpreter are destroyed. The global interpreter lock used by the target interpreter must be held before calling this function. No GIL is held when it returns.- `Py_FinalizeEx()`

### A Per-Interpreter GIL[¶](#a-per-interpreter-gil)

Using [ Py_NewInterpreterFromConfig()](#c.Py_NewInterpreterFromConfig) you can create
a sub-interpreter that is completely isolated from other interpreters,
including having its own GIL.  The most important benefit of this
isolation is that such an interpreter can execute Python code without
being blocked by other interpreters or blocking any others.  Thus a
single Python process can truly take advantage of multiple CPU cores
when running Python code.  The isolation also encourages a different
approach to concurrency than that of just using threads.
(See 

[and](https://peps.python.org/pep-0554/)

**PEP 554**[.)](https://peps.python.org/pep-0684/)

**PEP 684**Using an isolated interpreter requires vigilance in preserving that
isolation.  That especially means not sharing any objects or mutable
state without guarantees about thread-safety.  Even objects that are
otherwise immutable (e.g. `None`, `(1, 5)`) can’t normally be shared
because of the refcount.  One simple but less-efficient approach around
this is to use a global lock around all use of some state (or object).
Alternately, effectively immutable objects (like integers or strings)
can be made safe in spite of their refcounts by making them [immortal](../glossary.html#term-immortal).
In fact, this has been done for the builtin singletons, small integers,
and a number of other builtin objects.

If you preserve isolation then you will have access to proper multi-core computing without the complications that come with free-threading. Failure to preserve isolation will expose you to the full consequences of free-threading, including races and hard-to-debug crashes.

Aside from that, one of the main challenges of using multiple isolated interpreters is how to communicate between them safely (not break isolation) and efficiently. The runtime and stdlib do not provide any standard approach to this yet. A future stdlib module would help mitigate the effort of preserving isolation and expose effective tools for communicating (and sharing) data between interpreters.

Added in version 3.12.

### Bugs and caveats[¶](#bugs-and-caveats)

Because sub-interpreters (and the main interpreter) are part of the same
process, the insulation between them isn’t perfect — for example, using
low-level file operations like  [ os.close()](../library/os.html#os.close) they can
(accidentally or maliciously) affect each other’s open files.  Because of the
way extensions are shared between (sub-)interpreters, some extensions may not
work properly; this is especially likely when using single-phase initialization
or (static) global variables.
It is possible to insert objects created in one sub-interpreter into
a namespace of another (sub-)interpreter; this should be avoided if possible.

Special care should be taken to avoid sharing user-defined functions, methods, instances or classes between sub-interpreters, since import operations executed by such objects may affect the wrong (sub-)interpreter’s dictionary of loaded modules. It is equally important to avoid sharing objects from which the above are reachable.

Also note that combining this functionality with `PyGILState_*` APIs
is delicate, because these APIs assume a bijection between Python thread states
and OS-level threads, an assumption broken by the presence of sub-interpreters.
It is highly recommended that you don’t switch sub-interpreters between a pair
of matching [ PyGILState_Ensure()](#c.PyGILState_Ensure) and 

[calls. Furthermore, extensions (such as](#c.PyGILState_Release)

`PyGILState_Release()`[) using these APIs to allow calling of Python code from non-Python created threads will probably be broken when using sub-interpreters.](../library/ctypes.html#module-ctypes)

`ctypes`## Asynchronous Notifications[¶](#asynchronous-notifications)

A mechanism is provided to make asynchronous notifications to the main interpreter thread. These notifications take the form of a function pointer and a void pointer argument.

- 
int Py_AddPendingCall(int (*func)(void*), void *arg)[¶](#c.Py_AddPendingCall)
- *Part of the*- [Stable ABI](stable.html#stable).- Schedule a function to be called from the main interpreter thread. On success, - `0`is returned and- *func*is queued for being called in the main thread. On failure,- `-1`is returned without setting any exception.- When successfully queued, - *func*will be- *eventually*called from the main interpreter thread with the argument- *arg*. It will be called asynchronously with respect to normally running Python code, but with both these conditions met:- on a - [bytecode](../glossary.html#term-bytecode)boundary;
- with the main thread holding the - [global interpreter lock](../glossary.html#term-global-interpreter-lock)(- *func*can therefore use the full C API).
 - *func*must return- `0`on success, or- `-1`on failure with an exception set.- *func*won’t be interrupted to perform another asynchronous notification recursively, but it can still be interrupted to switch threads if the global interpreter lock is released.- This function doesn’t need a current thread state to run, and it doesn’t need the global interpreter lock. - To call this function in a subinterpreter, the caller must hold the GIL. Otherwise, the function - *func*can be scheduled to be called from the wrong interpreter.- Warning - This is a low-level function, only useful for very special cases. There is no guarantee that - *func*will be called as quick as possible. If the main thread is busy executing a system call,- *func*won’t be called before the system call returns. This function is generally- **not**suitable for calling Python code from arbitrary C threads. Instead, use the- [PyGILState API](#gilstate).- Added in version 3.1. - Changed in version 3.9: If this function is called in a subinterpreter, the function - *func*is now scheduled to be called from the subinterpreter, rather than being called from the main interpreter. Each subinterpreter now has its own list of scheduled calls.- Changed in version 3.12: This function now always schedules - *func*to be run in the main interpreter.

- 
int Py_MakePendingCalls(void)[¶](#c.Py_MakePendingCalls)
- *Part of the*- [Stable ABI](stable.html#stable).- Execute all pending calls. This is usually executed automatically by the interpreter. - This function returns - `0`on success, and returns- `-1`with an exception set on failure.- If this is not called in the main thread of the main interpreter, this function does nothing and returns - `0`. The caller must hold the- [GIL](../glossary.html#term-GIL).- Added in version 3.1. - Changed in version 3.12: This function only runs pending calls in the main interpreter. 

## Profiling and Tracing[¶](#profiling-and-tracing)

The Python interpreter provides some low-level support for attaching profiling and execution tracing facilities. These are used for profiling, debugging, and coverage analysis tools.

This C interface allows the profiling or tracing code to avoid the overhead of calling through Python-level callable objects, making a direct C function call instead. The essential attributes of the facility have not changed; the interface allows trace functions to be installed per-thread, and the basic events reported to the trace function are the same as had been reported to the Python-level trace functions in previous versions.

- 
typedef int (*Py_tracefunc)([PyObject](structures.html#c.PyObject)*obj,[PyFrameObject](frame.html#c.PyFrameObject)*frame, int what,[PyObject](structures.html#c.PyObject)*arg)[¶](#c.Py_tracefunc)
- The type of the trace function registered using - `PyEval_SetProfile()`- `PyEval_SetTrace()`- *obj*,- *frame*is the frame object to which the event pertains,- *what*is one of the constants- `PyTrace_CALL`- `PyTrace_EXCEPTION`- `PyTrace_LINE`- `PyTrace_RETURN`- `PyTrace_C_CALL`- `PyTrace_C_EXCEPTION`- `PyTrace_C_RETURN`- `PyTrace_OPCODE`- *arg*depends on the value of- *what*:- Value of - *what*- Meaning of - *arg*- Always - `Py_None`- Exception information as returned by - `sys.exc_info()`- Always - `Py_None`- Value being returned to the caller, or - `NULL`if caused by an exception.- Function object being called. - Function object being called. - Function object being called. - Always - `Py_None`

- 
int PyTrace_CALL[¶](#c.PyTrace_CALL)
- The value of the - *what*parameter to a- `Py_tracefunc`

- 
int PyTrace_EXCEPTION[¶](#c.PyTrace_EXCEPTION)
- The value of the - *what*parameter to a- `Py_tracefunc`- *what*when after any bytecode is processed after which the exception becomes set within the frame being executed. The effect of this is that as exception propagation causes the Python stack to unwind, the callback is called upon return to each frame as the exception propagates. Only trace functions receive these events; they are not needed by the profiler.

- 
int PyTrace_LINE[¶](#c.PyTrace_LINE)
- The value passed as the - *what*parameter to a- `Py_tracefunc`- `f_trace_lines`- *0*on that frame.

- 
int PyTrace_RETURN[¶](#c.PyTrace_RETURN)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_C_CALL[¶](#c.PyTrace_C_CALL)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_C_EXCEPTION[¶](#c.PyTrace_C_EXCEPTION)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_C_RETURN[¶](#c.PyTrace_C_RETURN)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_OPCODE[¶](#c.PyTrace_OPCODE)
- The value for the - *what*parameter to- `Py_tracefunc`- `f_trace_opcodes`- *1*on the frame.

- 
void PyEval_SetProfile([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetProfile)
- Set the profiler function to - *func*. The- *obj*parameter is passed to the function as its first parameter, and may be any Python object, or- `NULL`. If the profile function needs to maintain state, using a different value for- *obj*for each thread provides a convenient and thread-safe place to store it. The profile function is called for all monitored events except- `PyTrace_LINE`- `PyTrace_OPCODE`- `PyTrace_EXCEPTION`- See also the - `sys.setprofile()`- The caller must hold the - [GIL](../glossary.html#term-GIL).

- 
void PyEval_SetProfileAllThreads([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetProfileAllThreads)
- Like - `PyEval_SetProfile()`- The caller must hold the - [GIL](../glossary.html#term-GIL).- As - `PyEval_SetProfile()`

Added in version 3.12.

- 
void PyEval_SetTrace([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetTrace)
- Set the tracing function to - *func*. This is similar to- `PyEval_SetProfile()`- `PyEval_SetTrace()`- `PyTrace_C_CALL`- `PyTrace_C_EXCEPTION`- `PyTrace_C_RETURN`- *what*parameter.- See also the - `sys.settrace()`- The caller must hold the - [GIL](../glossary.html#term-GIL).

- 
void PyEval_SetTraceAllThreads([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetTraceAllThreads)
- Like - `PyEval_SetTrace()`- The caller must hold the - [GIL](../glossary.html#term-GIL).- As - `PyEval_SetTrace()`

Added in version 3.12.

## Reference tracing[¶](#reference-tracing)

Added in version 3.13.

- 
typedef int (*PyRefTracer)([PyObject](structures.html#c.PyObject)*, int event, void *data)[¶](#c.PyRefTracer)
- The type of the trace function registered using - `PyRefTracer_SetTracer()`- **event**is set to- `PyRefTracer_CREATE`- **event**is set to- `PyRefTracer_DESTROY`- **data**argument is the opaque pointer that was provided when- `PyRefTracer_SetTracer()`was called.

Added in version 3.13.

- 
int PyRefTracer_CREATE[¶](#c.PyRefTracer_CREATE)
- The value for the - *event*parameter to- `PyRefTracer`

- 
int PyRefTracer_DESTROY[¶](#c.PyRefTracer_DESTROY)
- The value for the - *event*parameter to- `PyRefTracer`

- 
int PyRefTracer_SetTracer([PyRefTracer](#c.PyRefTracer)tracer, void *data)[¶](#c.PyRefTracer_SetTracer)
- Register a reference tracer function. The function will be called when a new Python has been created or when an object is going to be destroyed. If - **data**is provided it must be an opaque pointer that will be provided when the tracer function is called. Return- `0`on success. Set an exception and return- `-1`on error.- Note that tracer functions - **must not**create Python objects inside or otherwise the call will be re-entrant. The tracer also- **must not**clear any existing exception or set an exception. The GIL will be held every time the tracer function is called.- The GIL must be held when calling this function. 

Added in version 3.13.

- 
[PyRefTracer](#c.PyRefTracer)PyRefTracer_GetTracer(void **data)[¶](#c.PyRefTracer_GetTracer)
- Get the registered reference tracer function and the value of the opaque data pointer that was registered when - `PyRefTracer_SetTracer()`- **data**pointer to NULL.- The GIL must be held when calling this function. 

Added in version 3.13.

## Advanced Debugger Support[¶](#advanced-debugger-support)

These functions are only intended to be used by advanced debugging tools.

- 
[PyInterpreterState](#c.PyInterpreterState)*PyInterpreterState_Head()[¶](#c.PyInterpreterState_Head)
- Return the interpreter state object at the head of the list of all such objects. 

- 
[PyInterpreterState](#c.PyInterpreterState)*PyInterpreterState_Main()[¶](#c.PyInterpreterState_Main)
- Return the main interpreter state object. 

- 
[PyInterpreterState](#c.PyInterpreterState)*PyInterpreterState_Next([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyInterpreterState_Next)
- Return the next interpreter state object after - *interp*from the list of all such objects.

- 
[PyThreadState](#c.PyThreadState)*PyInterpreterState_ThreadHead([PyInterpreterState](#c.PyInterpreterState)*interp)[¶](#c.PyInterpreterState_ThreadHead)
- Return the pointer to the first - `PyThreadState`- *interp*.

- 
[PyThreadState](#c.PyThreadState)*PyThreadState_Next([PyThreadState](#c.PyThreadState)*tstate)[¶](#c.PyThreadState_Next)
- Return the next thread state object after - *tstate*from the list of all such objects belonging to the same- `PyInterpreterState`

## Thread Local Storage Support[¶](#thread-local-storage-support)

The Python interpreter provides low-level support for thread-local storage
(TLS) which wraps the underlying native TLS implementation to support the
Python-level thread local storage API ([ threading.local](../library/threading.html#threading.local)).  The
CPython C level APIs are similar to those offered by pthreads and Windows:
use a thread key and functions to associate a void* value per
thread.

The GIL does *not* need to be held when calling these functions; they supply
their own locking.

Note that `Python.h` does not include the declaration of the TLS APIs,
you need to include `pythread.h` to use thread-local storage.

Note

None of these API functions handle memory management on behalf of the
void* values.  You need to allocate and deallocate them yourself.
If the void* values happen to be [PyObject](structures.html#c.PyObject)*, these
functions don’t do refcount operations on them either.

### Thread Specific Storage (TSS) API[¶](#thread-specific-storage-tss-api)

TSS API is introduced to supersede the use of the existing TLS API within the
CPython interpreter.  This API uses a new type [ Py_tss_t](#c.Py_tss_t) instead of
int to represent thread keys.

Added in version 3.7.

See also

“A New C-API for Thread-Local Storage in CPython” ([ PEP 539](https://peps.python.org/pep-0539/))

- 
type Py_tss_t[¶](#c.Py_tss_t)
- This data structure represents the state of a thread key, the definition of which may depend on the underlying TLS implementation, and it has an internal field representing the key’s initialization state. There are no public members in this structure. - When - [Py_LIMITED_API](stable.html#stable)is not defined, static allocation of this type by- `Py_tss_NEEDS_INIT`

- 
Py_tss_NEEDS_INIT[¶](#c.Py_tss_NEEDS_INIT)
- This macro expands to the initializer for - `Py_tss_t`- [Py_LIMITED_API](stable.html#stable).

#### Dynamic Allocation[¶](#dynamic-allocation)

Dynamic allocation of the [ Py_tss_t](#c.Py_tss_t), required in extension modules
built with 

[Py_LIMITED_API](stable.html#stable), where static allocation of this type is not possible due to its implementation being opaque at build time.

- 
[Py_tss_t](#c.Py_tss_t)*PyThread_tss_alloc()[¶](#c.PyThread_tss_alloc)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return a value which is the same state as a value initialized with - `Py_tss_NEEDS_INIT`- `NULL`in the case of dynamic allocation failure.

- 
void PyThread_tss_free([Py_tss_t](#c.Py_tss_t)*key)[¶](#c.PyThread_tss_free)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Free the given - *key*allocated by- `PyThread_tss_alloc()`- `PyThread_tss_delete()`- *key*argument is- `NULL`.- Note - A freed key becomes a dangling pointer. You should reset the key to - `NULL`.

#### Methods[¶](#methods)

The parameter *key* of these functions must not be `NULL`.  Moreover, the
behaviors of [ PyThread_tss_set()](#c.PyThread_tss_set) and 

[are undefined if the given](#c.PyThread_tss_get)

`PyThread_tss_get()`[has not been initialized by](#c.Py_tss_t)

`Py_tss_t`[.](#c.PyThread_tss_create)

`PyThread_tss_create()`- 
int PyThread_tss_is_created([Py_tss_t](#c.Py_tss_t)*key)[¶](#c.PyThread_tss_is_created)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return a non-zero value if the given - `Py_tss_t`- `PyThread_tss_create()`

- 
int PyThread_tss_create([Py_tss_t](#c.Py_tss_t)*key)[¶](#c.PyThread_tss_create)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return a zero value on successful initialization of a TSS key. The behavior is undefined if the value pointed to by the - *key*argument is not initialized by- `Py_tss_NEEDS_INIT`

- 
void PyThread_tss_delete([Py_tss_t](#c.Py_tss_t)*key)[¶](#c.PyThread_tss_delete)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Destroy a TSS key to forget the values associated with the key across all threads, and change the key’s initialization state to uninitialized. A destroyed key is able to be initialized again by - `PyThread_tss_create()`

- 
int PyThread_tss_set([Py_tss_t](#c.Py_tss_t)*key, void *value)[¶](#c.PyThread_tss_set)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return a zero value to indicate successfully associating a void* value with a TSS key in the current thread. Each thread has a distinct mapping of the key to a void* value. 

- 
void *PyThread_tss_get([Py_tss_t](#c.Py_tss_t)*key)[¶](#c.PyThread_tss_get)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Return the void* value associated with a TSS key in the current thread. This returns - `NULL`if no value is associated with the key in the current thread.

### Thread Local Storage (TLS) API[¶](#thread-local-storage-tls-api)

Deprecated since version 3.7: This API is superseded by
[Thread Specific Storage (TSS) API](#thread-specific-storage-api).

Note

This version of the API does not support platforms where the native TLS key
is defined in a way that cannot be safely cast to `int`.  On such platforms,
[ PyThread_create_key()](#c.PyThread_create_key) will return immediately with a failure status,
and the other TLS functions will all be no-ops on such platforms.

Due to the compatibility problem noted above, this version of the API should not be used in new code.

- 
int PyThread_create_key()[¶](#c.PyThread_create_key)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
void PyThread_delete_key(int key)[¶](#c.PyThread_delete_key)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
int PyThread_set_key_value(int key, void *value)[¶](#c.PyThread_set_key_value)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
void *PyThread_get_key_value(int key)[¶](#c.PyThread_get_key_value)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
void PyThread_delete_key_value(int key)[¶](#c.PyThread_delete_key_value)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
void PyThread_ReInitTLS()[¶](#c.PyThread_ReInitTLS)
- *Part of the*- [Stable ABI](stable.html#stable).

## Synchronization Primitives[¶](#synchronization-primitives)

The C-API provides a basic mutual exclusion lock.

- 
type PyMutex[¶](#c.PyMutex)
- A mutual exclusion lock. The - `PyMutex`should be initialized to zero to represent the unlocked state. For example:- PyMutex mutex = {0}; - Instances of - `PyMutex`should not be copied or moved. Both the contents and address of a- `PyMutex`are meaningful, and it must remain at a fixed, writable location in memory.- Note - A - `PyMutex`currently occupies one byte, but the size should be considered unstable. The size may change in future Python releases without a deprecation period.- Added in version 3.13. 

- 
void PyMutex_Lock([PyMutex](#c.PyMutex)*m)[¶](#c.PyMutex_Lock)
- Lock mutex - *m*. If another thread has already locked it, the calling thread will block until the mutex is unlocked. While blocked, the thread will temporarily release the- [GIL](../glossary.html#term-GIL)if it is held.- Added in version 3.13. 

- 
void PyMutex_Unlock([PyMutex](#c.PyMutex)*m)[¶](#c.PyMutex_Unlock)
- Unlock mutex - *m*. The mutex must be locked — otherwise, the function will issue a fatal error.- Added in version 3.13. 

### Python Critical Section API[¶](#python-critical-section-api)

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

The functions and structs used by the macros are exposed for cases where C macros are not available. They should only be used as in the given macro expansions. Note that the sizes and contents of the structures may change in future Python versions.

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

`Py_DECREF`[.](#c.PyEval_SaveThread)

`PyEval_SaveThread()`- 
Py_BEGIN_CRITICAL_SECTION(op)[¶](#c.Py_BEGIN_CRITICAL_SECTION)
- Acquires the per-object lock for the object - *op*and begins a critical section.- In the free-threaded build, this macro expands to: - { PyCriticalSection _py_cs; PyCriticalSection_Begin(&_py_cs, (PyObject*)(op)) - In the default build, this macro expands to - `{`.- Added in version 3.13. 

- 
Py_END_CRITICAL_SECTION()[¶](#c.Py_END_CRITICAL_SECTION)
- Ends the critical section and releases the per-object lock. - In the free-threaded build, this macro expands to: - PyCriticalSection_End(&_py_cs); } - In the default build, this macro expands to - `}`.- Added in version 3.13. 

- 
Py_BEGIN_CRITICAL_SECTION2(a, b)[¶](#c.Py_BEGIN_CRITICAL_SECTION2)
- Acquires the per-objects locks for the objects - *a*and- *b*and begins a critical section. The locks are acquired in a consistent order (lowest address first) to avoid lock ordering deadlocks.- In the free-threaded build, this macro expands to: - { PyCriticalSection2 _py_cs2; PyCriticalSection2_Begin(&_py_cs2, (PyObject*)(a), (PyObject*)(b)) - In the default build, this macro expands to - `{`.- Added in version 3.13. 

- 
Py_END_CRITICAL_SECTION2()[¶](#c.Py_END_CRITICAL_SECTION2)
- Ends the critical section and releases the per-object locks. - In the free-threaded build, this macro expands to: - PyCriticalSection2_End(&_py_cs2); } - In the default build, this macro expands to - `}`.- Added in version 3.13. 

### Legacy Locking APIs[¶](#legacy-locking-apis)

These APIs are obsolete since Python 3.13 with the introduction of
[ PyMutex](#c.PyMutex).

Changed in version 3.15: These APIs are now a simple wrapper around `PyMutex`.

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
- *Part of the*- [Stable ABI](stable.html#stable).- Allocate a new lock. - On success, this function returns a lock; on failure, this function returns - `0`without an exception set.- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).- Changed in version 3.15: This function now always uses - `PyMutex`

- 
void PyThread_free_lock([PyThread_type_lock](#c.PyThread_type_lock)lock)[¶](#c.PyThread_free_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Destroy - *lock*. The lock should not be held by any thread when calling this.- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).

- 
[PyLockStatus](#c.PyLockStatus)PyThread_acquire_lock_timed([PyThread_type_lock](#c.PyThread_type_lock)lock, long long microseconds, int intr_flag)[¶](#c.PyThread_acquire_lock_timed)
- *Part of the*- [Stable ABI](stable.html#stable).- Acquire - *lock*with a timeout.- This will wait for - *microseconds*microseconds to acquire the lock. If the timeout expires, this function returns- `PY_LOCK_FAILURE`- *microseconds*is- `-1`, this will wait indefinitely until the lock has been released.- If - *intr_flag*is- `1`, acquiring the lock may be interrupted by a signal, in which case this function returns- `PY_LOCK_INTR`- `Py_MakePendingCalls()`- If the lock is successfully acquired, this function returns - `PY_LOCK_ACQUIRED`- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).

- 
int PyThread_acquire_lock([PyThread_type_lock](#c.PyThread_type_lock)lock, int waitflag)[¶](#c.PyThread_acquire_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Acquire - *lock*.- If - *waitflag*is- `1`and another thread currently holds the lock, this function will wait until the lock can be acquired and will always return- `1`.- If - *waitflag*is- `0`and another thread holds the lock, this function will not wait and instead return- `0`. If the lock is not held by any other thread, then this function will acquire it and return- `1`.- Unlike - `PyThread_acquire_lock_timed()`- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).

- 
int PyThread_release_lock([PyThread_type_lock](#c.PyThread_type_lock)lock)[¶](#c.PyThread_release_lock)
- *Part of the*- [Stable ABI](stable.html#stable).- Release - *lock*. If- *lock*is not held, then this function issues a fatal error.- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).

## Operating System Thread APIs[¶](#operating-system-thread-apis)

- 
PYTHREAD_INVALID_THREAD_ID[¶](#c.PYTHREAD_INVALID_THREAD_ID)
- Sentinel value for an invalid thread ID. - This is currently equivalent to - `(unsigned long)-1`.

- 
unsigned long PyThread_start_new_thread(void (*func)(void*), void *arg)[¶](#c.PyThread_start_new_thread)
- *Part of the*- [Stable ABI](stable.html#stable).- Start function - *func*in a new thread with argument- *arg*. The resulting thread is not intended to be joined.- *func*must not be- `NULL`, but- *arg*may be- `NULL`.- On success, this function returns the identifier of the new thread; on failure, this returns - `PYTHREAD_INVALID_THREAD_ID`- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).

- 
unsigned long PyThread_get_thread_ident(void)[¶](#c.PyThread_get_thread_ident)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the identifier of the current thread, which will never be zero. - This function cannot fail, and the caller does not need to hold the - [GIL](../glossary.html#term-GIL).- See also 

- 
[PyObject](structures.html#c.PyObject)*PyThread_GetInfo(void)[¶](#c.PyThread_GetInfo)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.3.- Get general information about the current thread in the form of a - [struct sequence](tuple.html#struct-sequence-objects)object. This information is accessible as- `sys.thread_info`- On success, this returns a new - [strong reference](../glossary.html#term-strong-reference)to the thread information; on failure, this returns- `NULL`with an exception set.- The caller must hold the - [GIL](../glossary.html#term-GIL).

- 
PY_HAVE_THREAD_NATIVE_ID[¶](#c.PY_HAVE_THREAD_NATIVE_ID)
- This macro is defined when the system supports native thread IDs. 

- 
unsigned long PyThread_get_thread_native_id(void)[¶](#c.PyThread_get_thread_native_id)
- *Part of the*- [Stable ABI](stable.html#stable)on platforms with native thread IDs.- Get the native identifier of the current thread as it was assigned by the operating system’s kernel, which will never be less than zero. - This function is only available when - `PY_HAVE_THREAD_NATIVE_ID`- This function cannot fail, and the caller does not need to hold the - [GIL](../glossary.html#term-GIL).- See also 

- 
void PyThread_exit_thread(void)[¶](#c.PyThread_exit_thread)
- *Part of the*- [Stable ABI](stable.html#stable).- Terminate the current thread. This function is generally considered unsafe and should be avoided. It is kept solely for backwards compatibility. - This function is only safe to call if all functions in the full call stack are written to safely allow it. - Warning - If the current system uses POSIX threads (also known as “pthreads”), this calls - [pthread_exit(3)](https://manpages.debian.org/pthread_exit(3))- `noexcept`function is reached, it may terminate the process. Other systems, such as macOS, do unwinding.- On Windows, this function calls - `_endthreadex()`, which kills the thread without calling C++ destructors.- In any case, there is a risk of corruption on the thread’s stack. 

- 
void PyThread_init_thread(void)[¶](#c.PyThread_init_thread)
- *Part of the*- [Stable ABI](stable.html#stable).- Initialize - `PyThread*`APIs. Python executes this function automatically, so there’s little need to call it from an extension module.

- 
int PyThread_set_stacksize(size_t size)[¶](#c.PyThread_set_stacksize)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the stack size of the current thread to - *size*bytes.- This function returns - `0`on success,- `-1`if- *size*is invalid, or- `-2`if the system does not support changing the stack size. This function does not set exceptions.- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).

- 
size_t PyThread_get_stacksize(void)[¶](#c.PyThread_get_stacksize)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the stack size of the current thread in bytes, or - `0`if the system’s default stack size is in use.- The caller does not need to hold the - [GIL](../glossary.html#term-GIL).