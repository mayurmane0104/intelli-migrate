# Interpreter initialization and finalization — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/interp-lifecycle.html](https://docs.python.org/c-api/interp-lifecycle.html)

---

# Interpreter initialization and finalization[¶](#interpreter-initialization-and-finalization)

See [Python Initialization Configuration](init_config.html#init-config) for details
on how to configure the interpreter prior to initialization.

## Before Python initialization[¶](#before-python-initialization)

In an application embedding Python, the [ Py_Initialize()](#c.Py_Initialize) function must
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

[, and](threads.html#c.PyEval_InitThreads)

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
- This API is kept for backward compatibility: setting - `PyConfig.bytes_warning`- [Python Initialization Configuration](init_config.html#init-config).- Issue a warning when comparing - `bytes`- `bytearray`- `str`- `bytes`with- `int`- `2`.- Set by the - `-b`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_DebugFlag[¶](#c.Py_DebugFlag)
- This API is kept for backward compatibility: setting - `PyConfig.parser_debug`- [Python Initialization Configuration](init_config.html#init-config).- Turn on parser debugging output (for expert only, depending on compilation options). - Set by the - `-d`- `PYTHONDEBUG`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_DontWriteBytecodeFlag[¶](#c.Py_DontWriteBytecodeFlag)
- This API is kept for backward compatibility: setting - `PyConfig.write_bytecode`- [Python Initialization Configuration](init_config.html#init-config).- If set to non-zero, Python won’t try to write - `.pyc`files on the import of source modules.- Set by the - `-B`- `PYTHONDONTWRITEBYTECODE`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_FrozenFlag[¶](#c.Py_FrozenFlag)
- This API is kept for backward compatibility: setting - `PyConfig.pathconfig_warnings`- [Python Initialization Configuration](init_config.html#init-config).- Private flag used by - `_freeze_module`and- `frozenmain`programs.- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_HashRandomizationFlag[¶](#c.Py_HashRandomizationFlag)
- This API is kept for backward compatibility: setting - `PyConfig.hash_seed`- `PyConfig.use_hash_seed`- [Python Initialization Configuration](init_config.html#init-config).- Set to - `1`if the- `PYTHONHASHSEED`- If the flag is non-zero, read the - `PYTHONHASHSEED`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_IgnoreEnvironmentFlag[¶](#c.Py_IgnoreEnvironmentFlag)
- This API is kept for backward compatibility: setting - `PyConfig.use_environment`- [Python Initialization Configuration](init_config.html#init-config).- Ignore all - `PYTHON*`environment variables, e.g.- `PYTHONPATH`- `PYTHONHOME`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_InspectFlag[¶](#c.Py_InspectFlag)
- This API is kept for backward compatibility: setting - `PyConfig.inspect`- [Python Initialization Configuration](init_config.html#init-config).- When a script is passed as first argument or the - `-c`- `sys.stdin`- Set by the - `-i`- `PYTHONINSPECT`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_InteractiveFlag[¶](#c.Py_InteractiveFlag)
- This API is kept for backward compatibility: setting - `PyConfig.interactive`- [Python Initialization Configuration](init_config.html#init-config).- Set by the - `-i`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_IsolatedFlag[¶](#c.Py_IsolatedFlag)
- This API is kept for backward compatibility: setting - `PyConfig.isolated`- [Python Initialization Configuration](init_config.html#init-config).- Run Python in isolated mode. In isolated mode - `sys.path`- Set by the - `-I`- Added in version 3.4. - Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_LegacyWindowsFSEncodingFlag[¶](#c.Py_LegacyWindowsFSEncodingFlag)
- This API is kept for backward compatibility: setting - `PyPreConfig.legacy_windows_fs_encoding`- [Python Initialization Configuration](init_config.html#init-config).- If the flag is non-zero, use the - `mbcs`encoding with- `replace`error handler, instead of the UTF-8 encoding with- `surrogatepass`error handler, for the- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).- Set to - `1`if the- `PYTHONLEGACYWINDOWSFSENCODING`- See - **PEP 529**- [Availability](../library/intro.html#availability): Windows.- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_LegacyWindowsStdioFlag[¶](#c.Py_LegacyWindowsStdioFlag)
- This API is kept for backward compatibility: setting - `PyConfig.legacy_windows_stdio`- [Python Initialization Configuration](init_config.html#init-config).- If the flag is non-zero, use - `io.FileIO`- `io._WindowsConsoleIO`for- `sys`- Set to - `1`if the- `PYTHONLEGACYWINDOWSSTDIO`- See - **PEP 528**- [Availability](../library/intro.html#availability): Windows.- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_NoSiteFlag[¶](#c.Py_NoSiteFlag)
- This API is kept for backward compatibility: setting - `PyConfig.site_import`- [Python Initialization Configuration](init_config.html#init-config).- Disable the import of the module - `site`- `sys.path`- `site`is explicitly imported later (call- `site.main()`- Set by the - `-S`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_NoUserSiteDirectory[¶](#c.Py_NoUserSiteDirectory)
- This API is kept for backward compatibility: setting - `PyConfig.user_site_directory`- [Python Initialization Configuration](init_config.html#init-config).- Don’t add the - `user site-packages directory`- `sys.path`- Set by the - `-s`- `-I`- `PYTHONNOUSERSITE`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_OptimizeFlag[¶](#c.Py_OptimizeFlag)
- This API is kept for backward compatibility: setting - `PyConfig.optimization_level`- [Python Initialization Configuration](init_config.html#init-config).- Set by the - `-O`- `PYTHONOPTIMIZE`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_QuietFlag[¶](#c.Py_QuietFlag)
- This API is kept for backward compatibility: setting - `PyConfig.quiet`- [Python Initialization Configuration](init_config.html#init-config).- Don’t display the copyright and version messages even in interactive mode. - Set by the - `-q`- Added in version 3.2. - Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_UnbufferedStdioFlag[¶](#c.Py_UnbufferedStdioFlag)
- This API is kept for backward compatibility: setting - `PyConfig.buffered_stdio`- [Python Initialization Configuration](init_config.html#init-config).- Force the stdout and stderr streams to be unbuffered. - Set by the - `-u`- `PYTHONUNBUFFERED`- Deprecated since version 3.12, will be removed in version 3.15. 

- 
int Py_VerboseFlag[¶](#c.Py_VerboseFlag)
- This API is kept for backward compatibility: setting - `PyConfig.verbose`- [Python Initialization Configuration](init_config.html#init-config).- Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. If greater or equal to - `2`, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.- Set by the - `-v`- `PYTHONVERBOSE`- Deprecated since version 3.12, will be removed in version 3.15. 

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
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.6.- Undo all initializations made by - `Py_Initialize()`- `Py_NewInterpreter()`- `Py_Initialize()`. This is a no-op when called for a second time (without calling- `Py_Initialize()`again first).- Since this is the reverse of - `Py_Initialize()`- `Py_RunMain()`- Normally the return value is - `0`. If there were errors during finalization (flushing buffered data),- `-1`is returned.- Note that Python will do a best effort at freeing all memory allocated by the Python interpreter. Therefore, any C-Extension should make sure to correctly clean up all of the previously allocated PyObjects before using them in subsequent calls to - `Py_Initialize()`- This function is provided for a number of reasons. An embedding application might want to restart Python without having to restart the application itself. An application that has loaded the Python interpreter from a dynamically loadable library (or DLL) might want to free all memory allocated by Python before unloading the DLL. During a hunt for memory leaks in an application a developer might want to free all memory allocated by Python before exiting from the application. - **Bugs and caveats:**The destruction of modules and objects in modules is done in random order; this may cause destructors (- `__del__()`- `Py_Initialize()`- `Py_FinalizeEx()`- `Py_FinalizeEx()`must not be called recursively from within itself. Therefore, it must not be called by any code that may be run as part of the interpreter shutdown process, such as- `atexit`- Raises an - [auditing event](../library/sys.html#auditing)- `cpython._PySys_ClearAuditHooks`with no arguments.- Added in version 3.6. 

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
int PyUnstable_AtExit([PyInterpreterState](subinterpreters.html#c.PyInterpreterState)*interp, void (*func)(void*), void *data)[¶](#c.PyUnstable_AtExit)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Register an - `atexit`- *interp*. This is similar to- `Py_AtExit()`- There must be an - [attached thread state](../glossary.html#term-attached-thread-state)for- *interp*.- Added in version 3.13. 

## Cautions regarding runtime finalization[¶](#cautions-regarding-runtime-finalization)

In the late stage of [interpreter shutdown](../glossary.html#term-interpreter-shutdown), after attempting to wait for
non-daemon threads to exit (though this can be interrupted by
[ KeyboardInterrupt](../library/exceptions.html#KeyboardInterrupt)) and running the 

[functions, the runtime is marked as](../library/atexit.html#module-atexit)

`atexit`*finalizing*:

[and](#c.Py_IsFinalizing)

`Py_IsFinalizing()`[return true. At this point, only the](../library/sys.html#sys.is_finalizing)

`sys.is_finalizing()`*finalization thread*that initiated finalization (typically the main thread) is allowed to acquire the

[GIL](../glossary.html#term-GIL).

If any thread, other than the finalization thread, attempts to attach a [thread state](../glossary.html#term-thread-state)
during finalization, either explicitly or
implicitly, the thread enters **a permanently blocked state**
where it remains until the program exits.  In most cases this is harmless, but this can result
in deadlock if a later stage of finalization attempts to acquire a lock owned by the
blocked thread, or otherwise waits on the blocked thread.

Gross? Yes. This prevents random crashes and/or unexpectedly skipped C++
finalizations further up the call stack when such threads were forcibly exited
here in CPython 3.13 and earlier. The CPython runtime [thread state](../glossary.html#term-thread-state) C APIs
have never had any error reporting or handling expectations at thread state
attachment time that would’ve allowed for graceful exit from this situation. Changing that
would require new stable C APIs and rewriting the majority of C code in the
CPython ecosystem to use those with error handling.

## Process-wide parameters[¶](#process-wide-parameters)

- 
void Py_SetProgramName(const wchar_t *name)[¶](#c.Py_SetProgramName)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.program_name`- [Python Initialization Configuration](init_config.html#init-config).- This function should be called before - `Py_Initialize()`- `argv[0]`argument to the- `main()`function of the program (converted to wide characters). This is used by- `Py_GetPath()`- `'python'`. The argument should point to a zero-terminated wide character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.- Use - `Py_DecodeLocale()`- Deprecated since version 3.11, will be removed in version 3.15. 

- 
wchar_t *Py_GetProgramName()[¶](#c.Py_GetProgramName)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the program name set with - `PyConfig.program_name`- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyConfig_Get("executable")`- `sys.executable`

- 
wchar_t *Py_GetPrefix()[¶](#c.Py_GetPrefix)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *prefix*for installed platform-independent files. This is derived through a number of complicated rules from the program name set with- `PyConfig.program_name`- `'/usr/local/bin/python'`, the prefix is- `'/usr/local'`. The returned string points into static storage; the caller should not modify its value. This corresponds to the- **prefix**variable in the top-level- `Makefile`and the- `--prefix`- **configure**script at build time. The value is available to Python code as- `sys.base_prefix`. It is only useful on Unix. See also the next function.- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyConfig_Get("base_prefix")`- `sys.base_prefix`- `PyConfig_Get("prefix")`(- `sys.prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.

- 
wchar_t *Py_GetExecPrefix()[¶](#c.Py_GetExecPrefix)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *exec-prefix*for installed platform-- *dependent*files. This is derived through a number of complicated rules from the program name set with- `PyConfig.program_name`- `'/usr/local/bin/python'`, the exec-prefix is- `'/usr/local'`. The returned string points into static storage; the caller should not modify its value. This corresponds to the- **exec_prefix**variable in the top-level- `Makefile`and the- `--exec-prefix`argument to the- **configure**script at build time. The value is available to Python code as- `sys.base_exec_prefix`. It is only useful on Unix.- Background: The exec-prefix differs from the prefix when platform dependent files (such as executables and shared libraries) are installed in a different directory tree. In a typical installation, platform dependent files may be installed in the - `/usr/local/plat`subtree while platform independent may be installed in- `/usr/local`.- Generally speaking, a platform is a combination of hardware and software families, e.g. Sparc machines running the Solaris 2.x operating system are considered the same platform, but Intel machines running Solaris 2.x are another platform, and Intel machines running Linux are yet another platform. Different major revisions of the same operating system generally also form different platforms. Non-Unix operating systems are a different story; the installation strategies on those systems are so different that the prefix and exec-prefix are meaningless, and set to the empty string. Note that compiled Python bytecode files are platform independent (but not independent from the Python version by which they were compiled!). - System administrators will know how to configure the - **mount**or- **automount**programs to share- `/usr/local`between platforms while having- `/usr/local/plat`be a different filesystem for each platform.- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyConfig_Get("base_exec_prefix")`- `sys.base_exec_prefix`- `PyConfig_Get("exec_prefix")`(- `sys.exec_prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.

- 
wchar_t *Py_GetProgramFullPath()[¶](#c.Py_GetProgramFullPath)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the full program name of the Python executable; this is computed as a side-effect of deriving the default module search path from the program name (set by - `PyConfig.program_name`- `sys.executable`.- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyConfig_Get("executable")`- `sys.executable`

- 
wchar_t *Py_GetPath()[¶](#c.Py_GetPath)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the default module search path; this is computed from the program name (set by - `PyConfig.program_name`- `':'`on Unix and macOS,- `';'`on Windows. The returned string points into static storage; the caller should not modify its value. The list- `sys.path`- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyConfig_Get("module_search_paths")`- `sys.path`

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
 - Use - `Py_DecodeLocale()`- See also - `PyConfig.orig_argv`- `PyConfig.argv`- [Python Initialization Configuration](init_config.html#init-config).- Note - It is recommended that applications embedding the Python interpreter for purposes other than executing a single script pass - `0`as- *updatepath*, and update- `sys.path`- **CVE 2008-5983**- On versions before 3.1.3, you can achieve the same effect by manually popping the first - `sys.path`- `PySys_SetArgv()`- PyRun_SimpleString("import sys; sys.path.pop(0)\n"); - Added in version 3.1.3. - Deprecated since version 3.11, will be removed in version 3.15. 

- 
void PySys_SetArgv(int argc, wchar_t **argv)[¶](#c.PySys_SetArgv)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.argv`- `PyConfig.parse_argv`- [Python Initialization Configuration](init_config.html#init-config).- This function works like - `PySys_SetArgvEx()`- *updatepath*set to- `1`unless the- **python**interpreter was started with the- `-I`- Use - `Py_DecodeLocale()`- See also - `PyConfig.orig_argv`- `PyConfig.argv`- [Python Initialization Configuration](init_config.html#init-config).- Changed in version 3.4: The - *updatepath*value depends on- `-I`- Deprecated since version 3.11, will be removed in version 3.15. 

- 
void Py_SetPythonHome(const wchar_t *home)[¶](#c.Py_SetPythonHome)
- *Part of the*- [Stable ABI](stable.html#stable).- This API is kept for backward compatibility: setting - `PyConfig.home`- [Python Initialization Configuration](init_config.html#init-config).- Set the default “home” directory, that is, the location of the standard Python libraries. See - `PYTHONHOME`- The argument should point to a zero-terminated character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage. - Use - `Py_DecodeLocale()`- Deprecated since version 3.11, will be removed in version 3.15. 

- 
wchar_t *Py_GetPythonHome()[¶](#c.Py_GetPythonHome)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the default “home”, that is, the value set by - `PyConfig.home`- `PYTHONHOME`- This function should not be called before - `Py_Initialize()`- `NULL`.- Changed in version 3.10: It now returns - `NULL`if called before- `Py_Initialize()`- Deprecated since version 3.13, will be removed in version 3.15: Use - `PyConfig_Get("home")`- `PYTHONHOME`