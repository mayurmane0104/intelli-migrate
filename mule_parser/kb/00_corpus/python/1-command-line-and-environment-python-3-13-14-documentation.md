# 1. Command line and environment — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/using/cmdline.html](https://docs.python.org/3.13/using/cmdline.html)

---

# 1. Command line and environment[¶](#command-line-and-environment)

The CPython interpreter scans the command line and the environment for various settings.

**CPython implementation detail:** Other implementations’ command line schemes may differ.  See
[Alternate Implementations](../reference/introduction.html#implementations) for further resources.

## 1.1. Command line[¶](#command-line)

When invoking Python, you may specify any of these options:

```
python [-bBdEhiIOPqRsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```
The most common use case is, of course, a simple invocation of a script:

```
python myscript.py
```
### 1.1.1. Interface options[¶](#interface-options)

The interpreter interface resembles that of the UNIX shell, but provides some additional methods of invocation:

- When called with standard input connected to a tty device, it prompts for commands and executes them until an EOF (an end-of-file character, you can produce that with - `Ctrl`-- `D`on UNIX or- `Ctrl`-- `Z,`- `Enter`on Windows) is read. For more on interactive mode, see- [Interactive Mode](../tutorial/appendix.html#tut-interac).
- When called with a file name argument or with a file as standard input, it reads and executes a script from that file. 
- When called with a directory name argument, it reads and executes an appropriately named script from that directory. 
- When called with - `-c command`, it executes the Python statement(s) given as- *command*. Here- *command*may contain multiple statements separated by newlines. Leading whitespace is significant in Python statements!
- When called with - `-m module-name`, the given module is located using the standard import mechanism and executed as a script.

In non-interactive mode, the entire input is parsed before it is executed.

An interface option terminates the list of options consumed by the interpreter,
all consecutive arguments will end up in [ sys.argv](../library/sys.html#sys.argv) – note that the first
element, subscript zero (

`sys.argv[0]`), is a string reflecting the program’s
source.- 
-c <command>[¶](#cmdoption-c)
- Execute the Python code in - *command*.- *command*can be one or more statements separated by newlines, with significant leading whitespace as in normal module code.- If this option is given, the first element of - `sys.argv`- `"-c"`and the current directory will be added to the start of- `sys.path`- Raises an - [auditing event](../library/sys.html#auditing)- `cpython.run_command`with argument- `command`.

- 
-m <module-name>[¶](#cmdoption-m)
- Locate the module using the standard import mechanism and execute its contents as the - `__main__`- Since the argument is a - *module*name, you must not give a file extension (- `.py`). The module name should be a valid absolute Python module name, but the implementation may not always enforce this (e.g. it may allow you to use a name that includes a hyphen).- Package names (including namespace packages) are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute - `<pkg>.__main__`as the main module. This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script argument.- Note - This option cannot be used with built-in modules and extension modules written in C, since they do not have Python module files. However, it can still be used for precompiled modules, even if the original source file is not available. - If this option is given, the first element of - `sys.argv`- `"-m"`). As with the- `-c`- `sys.path`- `-I`- `sys.path`- `PYTHON*`environment variables are ignored, too.- Many standard library modules contain code that is invoked on their execution as a script. An example is the - `timeit`- python -m timeit -s "setup here" "benchmarked code here" python -m timeit -h # for details - Raises an - [auditing event](../library/sys.html#auditing)- `cpython.run_module`with argument- `module-name`.- See also - `runpy.run_module()`
- Equivalent functionality directly available to Python code 
 - **PEP 338**- Changed in version 3.1: Supply the package name to run a - `__main__`submodule.- Changed in version 3.4: namespace packages are also supported 

- -
- Read commands from standard input ( - `sys.stdin`- `-i`- If this option is given, the first element of - `sys.argv`- `"-"`and the current directory will be added to the start of- `sys.path`- Raises an - [auditing event](../library/sys.html#auditing)- `cpython.run_stdin`with no arguments.

- <script>
- Execute the Python code contained in - *script*, which must be a filesystem path (absolute or relative) referring to either a Python file, a directory containing a- `__main__.py`file, or a zipfile containing a- `__main__.py`file.- If this option is given, the first element of - `sys.argv`- If the script name refers directly to a Python file, the directory containing that file is added to the start of - `sys.path`- `__main__`- If the script name refers to a directory or zipfile, the script name is added to the start of - `sys.path`- `__main__.py`file in that location is executed as the- `__main__`- `-I`- `sys.path`- `PYTHON*`environment variables are ignored, too.- Raises an - [auditing event](../library/sys.html#auditing)- `cpython.run_file`with argument- `filename`.- See also - `runpy.run_path()`
- Equivalent functionality directly available to Python code 
 

If no interface option is given, [ -i](#cmdoption-i) is implied, 

`sys.argv[0]` is
an empty string (`""`) and the current directory will be added to the
start of [. Also, tab-completion and history editing is automatically enabled, if available on your platform (see](../library/sys.html#sys.path)

`sys.path`[Readline configuration](../library/site.html#rlcompleter-config)).

See also

Changed in version 3.4: Automatic enabling of tab-completion and history editing.

### 1.1.2. Generic options[¶](#generic-options)

- 
-?[¶](#cmdoption-0)
- 
-h[¶](#cmdoption-h)
- 
--help[¶](#cmdoption-help)
- Print a short description of all command line options and corresponding environment variables and exit. 

- 
--help-env[¶](#cmdoption-help-env)
- Print a short description of Python-specific environment variables and exit. - Added in version 3.11. 

- 
--help-xoptions[¶](#cmdoption-help-xoptions)
- Print a description of implementation-specific - `-X`- Added in version 3.11. 

- 
--help-all[¶](#cmdoption-help-all)
- Print complete usage information and exit. - Added in version 3.11. 

### 1.1.3. Miscellaneous options[¶](#miscellaneous-options)

- 
-b[¶](#cmdoption-b)
- Issue a warning when converting - `bytes`- `bytearray`- `str`- `bytes`or- `bytearray`with- `str`or- `bytes`with- `int`- `-bb`).

- 
-B[¶](#cmdoption-B)
- If given, Python won’t try to write - `.pyc`files on the import of source modules. See also- `PYTHONDONTWRITEBYTECODE`

- 
--check-hash-based-pycs default|always|never[¶](#cmdoption-check-hash-based-pycs)
- Control the validation behavior of hash-based - `.pyc`files. See- [Cached bytecode invalidation](../reference/import.html#pyc-invalidation). When set to- `default`, checked and unchecked hash-based bytecode cache files are validated according to their default semantics. When set to- `always`, all hash-based- `.pyc`files, whether checked or unchecked, are validated against their corresponding source file. When set to- `never`, hash-based- `.pyc`files are not validated against their corresponding source files.- The semantics of timestamp-based - `.pyc`files are unaffected by this option.

- 
-d[¶](#cmdoption-d)
- Turn on parser debugging output (for expert only). See also the - `PYTHONDEBUG`- This option requires a - [debug build of Python](configure.html#debug-build), otherwise it’s ignored.

- 
-E[¶](#cmdoption-E)
- Ignore all - `PYTHON*`environment variables, e.g.- `PYTHONPATH`- `PYTHONHOME`

- 
-i[¶](#cmdoption-i)
- Enter interactive mode after execution. - Using the - `-i`- Interactive mode will start even when - `sys.stdin`- `PYTHONSTARTUP`- This can be useful to inspect global variables or a stack trace when a script raises an exception. See also - `PYTHONINSPECT`

- 
-I[¶](#cmdoption-I)
- Run Python in isolated mode. This also implies - `-E`- `-P`- `-s`- In isolated mode - `sys.path`- `PYTHON*`environment variables are ignored, too. Further restrictions may be imposed to prevent the user from injecting malicious code.- Added in version 3.4. 

- 
-O[¶](#cmdoption-O)
- Remove assert statements and any code conditional on the value of - `__debug__`- [bytecode](../glossary.html#term-bytecode)) files by adding- `.opt-1`before the- `.pyc`extension (see- **PEP 488**- `PYTHONOPTIMIZE`- Changed in version 3.5: Modify - `.pyc`filenames according to- **PEP 488**

- 
-OO[¶](#cmdoption-OO)
- Do - `-O`- [bytecode](../glossary.html#term-bytecode)) files by adding- `.opt-2`before the- `.pyc`extension (see- **PEP 488**- Changed in version 3.5: Modify - `.pyc`filenames according to- **PEP 488**

- 
-P[¶](#cmdoption-P)
- Don’t prepend a potentially unsafe path to - `sys.path`- `python -m module`command line: Don’t prepend the current working directory.
- `python script.py`command line: Don’t prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
- `python -c code`and- `python`(REPL) command lines: Don’t prepend an empty string, which means the current working directory.
 - See also the - `PYTHONSAFEPATH`- `-E`- `-I`- Added in version 3.11. 

- 
-q[¶](#cmdoption-q)
- Don’t display the copyright and version messages even in interactive mode. - Added in version 3.2. 

- 
-R[¶](#cmdoption-R)
- Turn on hash randomization. This option only has an effect if the - `PYTHONHASHSEED`- `random`, since hash randomization is enabled by default.- On previous versions of Python, this option turns on hash randomization, so that the - `__hash__()`- Hash randomization is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict construction, - *O*(- *n*- 2) complexity. See- [https://ocert.org/advisories/ocert-2011-003.html](https://ocert.org/advisories/ocert-2011-003.html)for details.- `PYTHONHASHSEED`- Added in version 3.2.3. - Changed in version 3.7: The option is no longer ignored. 

- 
-s[¶](#cmdoption-s)
- Don’t add the - `user site-packages directory`- `sys.path`- See also - `PYTHONNOUSERSITE`- See also - **PEP 370**

- 
-S[¶](#cmdoption-S)
- Disable the import of the module - `site`- `sys.path`- `site`is explicitly imported later (call- `site.main()`

- 
-u[¶](#cmdoption-u)
- Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream. - See also - `PYTHONUNBUFFERED`- Changed in version 3.7: The text layer of the stdout and stderr streams now is unbuffered. 

- 
-v[¶](#cmdoption-v)
- Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice ( - `-vv`), print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.- Changed in version 3.10: The - `site`- `.pth`files being processed.- See also - `PYTHONVERBOSE`

- 
-W arg[¶](#cmdoption-W)
- Warning control. Python’s warning machinery by default prints warning messages to - `sys.stderr`- The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default): - -Wdefault # Warn once per call location -Werror # Convert to exceptions -Walways # Warn every time -Wall # Same as -Walways -Wmodule # Warn once per calling module -Wonce # Warn once per Python process -Wignore # Never warn - The action names can be abbreviated as desired and the interpreter will resolve them to the appropriate action name. For example, - `-Wi`is the same as- `-Wignore`.- The full form of argument is: - action:message:category:module:lineno - Empty fields match all values; trailing empty fields may be omitted. For example - `-W ignore::DeprecationWarning`ignores all DeprecationWarning warnings.- The - *action*field is as explained above but only applies to warnings that match the remaining fields.- The - *message*field must match the whole warning message; this match is case-insensitive.- The - *category*field matches the warning category (ex:- `DeprecationWarning`). This must be a class name; the match test whether the actual warning category of the message is a subclass of the specified warning category.- The - *module*field matches the (fully qualified) module name; this match is case-sensitive.- The - *lineno*field matches the line number, where zero matches all line numbers and is thus equivalent to an omitted line number.- Multiple - `-W`- `-W`options are ignored (though, a warning message is printed about invalid options when the first warning is issued).- Warnings can also be controlled using the - `PYTHONWARNINGS`- `warnings`- `warnings.filterwarnings()`- See - [The Warnings Filter](../library/warnings.html#warning-filter)and- [Describing Warning Filters](../library/warnings.html#describing-warning-filters)for more details.

- 
-x[¶](#cmdoption-x)
- Skip the first line of the source, allowing use of non-Unix forms of - `#!cmd`. This is intended for a DOS specific hack only.

- 
-X[¶](#cmdoption-X)
- Reserved for various implementation-specific options. CPython currently defines the following possible values: - `-X faulthandler`to enable- `faulthandler`- `PYTHONFAULTHANDLER`- Added in version 3.3. 
- `-X showrefcount`to output the total reference count and number of used memory blocks when the program finishes or after each statement in the interactive interpreter. This only works on- [debug builds](configure.html#debug-build).- Added in version 3.4. 
- `-X tracemalloc`to start tracing Python memory allocations using the- `tracemalloc`- `-X tracemalloc=NFRAME`to start tracing with a traceback limit of- *NFRAME*frames. See- `tracemalloc.start()`- `PYTHONTRACEMALLOC`- Added in version 3.4. 
- `-X int_max_str_digits`configures the- [integer string conversion length limitation](../library/stdtypes.html#int-max-str-digits). See also- `PYTHONINTMAXSTRDIGITS`- Added in version 3.11. 
- `-X importtime`to show how long each import takes. It shows module name, cumulative time (including nested imports) and self time (excluding nested imports). Note that its output may be broken in multi-threaded application. Typical usage is- `python3 -X importtime -c 'import asyncio'`. See also- `PYTHONPROFILEIMPORTTIME`- Added in version 3.7. 
- `-X dev`: enable- [Python Development Mode](../library/devmode.html#devmode), introducing additional runtime checks that are too expensive to be enabled by default. See also- `PYTHONDEVMODE`- Added in version 3.7. 
- `-X utf8`enables the- [Python UTF-8 Mode](../library/os.html#utf8-mode).- `-X utf8=0`explicitly disables- [Python UTF-8 Mode](../library/os.html#utf8-mode)(even when it would otherwise activate automatically). See also- `PYTHONUTF8`- Added in version 3.7. 
- `-X pycache_prefix=PATH`enables writing- `.pyc`files to a parallel tree rooted at the given directory instead of to the code tree. See also- `PYTHONPYCACHEPREFIX`- Added in version 3.8. 
- `-X warn_default_encoding`issues a- `EncodingWarning`- `PYTHONWARNDEFAULTENCODING`- Added in version 3.10. 
- `-X no_debug_ranges`disables the inclusion of the tables mapping extra location information (end line, start column offset and end column offset) to every instruction in code objects. This is useful when smaller code objects and pyc files are desired as well as suppressing the extra visual location indicators when the interpreter displays tracebacks. See also- `PYTHONNODEBUGRANGES`- Added in version 3.11. 
- `-X frozen_modules`determines whether or not frozen modules are ignored by the import machinery. A value of- `on`means they get imported and- `off`means they are ignored. The default is- `on`if this is an installed Python (the normal case). If it’s under development (running from the source tree) then the default is- `off`. Note that the- `importlib_bootstrap`and- `importlib_bootstrap_external`frozen modules are always used, even if this flag is set to- `off`. See also- `PYTHON_FROZEN_MODULES`- Added in version 3.11. 
- `-X perf`enables support for the Linux- `perf`profiler. When this option is provided, the- `perf`profiler will be able to report Python calls. This option is only available on some platforms and will do nothing if is not supported on the current system. The default value is “off”. See also- `PYTHONPERFSUPPORT`- [Python support for the Linux perf profiler](../howto/perf_profiling.html#perf-profiling).- Added in version 3.12. 
- `-X perf_jit`enables support for the Linux- `perf`profiler with DWARF support. When this option is provided, the- `perf`profiler will be able to report Python calls using DWARF information. This option is only available on some platforms and will do nothing if is not supported on the current system. The default value is “off”. See also- `PYTHON_PERF_JIT_SUPPORT`- [Python support for the Linux perf profiler](../howto/perf_profiling.html#perf-profiling).- Added in version 3.13. 
- `-X cpu_count=`overrides- *n*- `os.cpu_count()`- `os.process_cpu_count()`- `multiprocessing.cpu_count()`- *n*must be greater than or equal to 1. This option may be useful for users who need to limit CPU resources of a container system. See also- `PYTHON_CPU_COUNT`- *n*is- `default`, nothing is overridden.- Added in version 3.13. 
- `-X presite=`specifies a module that should be imported before the- *package.module*- `site`- `__main__`- `__main__`. This can be used to execute code early during Python initialization. Python needs to be- [built in debug mode](configure.html#debug-build)for this option to exist. See also- `PYTHON_PRESITE`- Added in version 3.13. 
- `-X gil=`forces the GIL to be disabled or enabled, respectively. Setting to- *0,1*- `0`is only available in builds configured with- `--disable-gil`- `PYTHON_GIL`- [Free-threaded CPython](../whatsnew/3.13.html#whatsnew313-free-threaded-cpython).- Added in version 3.13. 
 - It also allows passing arbitrary values and retrieving them through the - `sys._xoptions`- Added in version 3.2. - Changed in version 3.9: Removed the - `-X showalloccount`option.- Changed in version 3.10: Removed the - `-X oldparser`option.

### 1.1.4. Controlling color[¶](#controlling-color)

The Python interpreter is configured by default to use colors to highlight output in certain situations such as when displaying tracebacks. This behavior can be controlled by setting different environment variables.

Setting the environment variable `TERM` to `dumb` will disable color.

If the [ FORCE_COLOR](https://force-color.org/) environment variable is set, then color will be
enabled regardless of the value of TERM. This is useful on CI systems which
aren’t terminals but can still display ANSI escape sequences.

If the [ NO_COLOR](https://no-color.org/) environment variable is set, Python will disable all color
in the output. This takes precedence over 

`FORCE_COLOR`.All these environment variables are used also by other tools to control color
output. To control the color output only in the Python interpreter, the
[ PYTHON_COLORS](#envvar-PYTHON_COLORS) environment variable can be used. This variable takes
precedence over 

`NO_COLOR`, which in turn takes precedence over
`FORCE_COLOR`.### 1.1.5. Options you shouldn’t use[¶](#options-you-shouldn-t-use)

## 1.2. Environment variables[¶](#environment-variables)

These environment variables influence Python’s behavior, they are processed before the command-line switches other than -E or -I. It is customary that command-line switches override environmental variables where there is a conflict.

- 
PYTHONHOME[¶](#envvar-PYTHONHOME)
- Change the location of the standard Python libraries. By default, the libraries are searched in - *prefix*/lib/python- *version*- *exec_prefix*/lib/python- *version*- *prefix*- *exec_prefix*- `/usr/local`.- When - `PYTHONHOME`- *prefix*- *exec_prefix*- `PYTHONHOME`to- *prefix*:- *exec_prefix*

- 
PYTHONPATH[¶](#envvar-PYTHONPATH)
- Augment the default search path for module files. The format is the same as the shell’s - `PATH`: one or more directory pathnames separated by- `os.pathsep`- In addition to normal directories, individual - `PYTHONPATH`- The default search path is installation dependent, but generally begins with - *prefix*/lib/python- *version*- `PYTHONHOME`- *always*appended to- `PYTHONPATH`- An additional directory will be inserted in the search path in front of - `PYTHONPATH`- [Interface options](#using-on-interface-options). The search path can be manipulated from within a Python program as the variable- `sys.path`

- 
PYTHONSAFEPATH[¶](#envvar-PYTHONSAFEPATH)
- If this is set to a non-empty string, don’t prepend a potentially unsafe path to - `sys.path`- `-P`- Added in version 3.11. 

- 
PYTHONPLATLIBDIR[¶](#envvar-PYTHONPLATLIBDIR)
- If this is set to a non-empty string, it overrides the - `sys.platlibdir`- Added in version 3.9. 

- 
PYTHONSTARTUP[¶](#envvar-PYTHONSTARTUP)
- If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in interactive mode. The file is executed in the same namespace where interactive commands are executed so that objects defined or imported in it can be used without qualification in the interactive session. You can also change the prompts - `sys.ps1`- `sys.ps2`- `sys.__interactivehook__`- Raises an - [auditing event](../library/sys.html#auditing)- `cpython.run_startup`with the filename as the argument when called on startup.

- 
PYTHONOPTIMIZE[¶](#envvar-PYTHONOPTIMIZE)
- If this is set to a non-empty string it is equivalent to specifying the - `-O`- `-O`multiple times.

- 
PYTHONBREAKPOINT[¶](#envvar-PYTHONBREAKPOINT)
- If this is set, it names a callable using dotted-path notation. The module containing the callable will be imported and then the callable will be run by the default implementation of - `sys.breakpointhook()`- `breakpoint()`- `sys.breakpointhook()`to do nothing but return immediately.- Added in version 3.7. 

- 
PYTHONDEBUG[¶](#envvar-PYTHONDEBUG)
- If this is set to a non-empty string it is equivalent to specifying the - `-d`- `-d`multiple times.- This environment variable requires a - [debug build of Python](configure.html#debug-build), otherwise it’s ignored.

- 
PYTHONINSPECT[¶](#envvar-PYTHONINSPECT)
- If this is set to a non-empty string it is equivalent to specifying the - `-i`- This variable can also be modified by Python code using - `os.environ`- Raises an - [auditing event](../library/sys.html#auditing)- `cpython.run_stdin`with no arguments.- Changed in version 3.12.5: (also 3.11.10, 3.10.15, 3.9.20, and 3.8.20) Emits audit events. - Changed in version 3.13: Uses PyREPL if possible, in which case - `PYTHONSTARTUP`

- 
PYTHONUNBUFFERED[¶](#envvar-PYTHONUNBUFFERED)
- If this is set to a non-empty string it is equivalent to specifying the - `-u`

- 
PYTHONVERBOSE[¶](#envvar-PYTHONVERBOSE)
- If this is set to a non-empty string it is equivalent to specifying the - `-v`- `-v`multiple times.

- 
PYTHONCASEOK[¶](#envvar-PYTHONCASEOK)
- If this is set, Python ignores case in - `import`

- 
PYTHONDONTWRITEBYTECODE[¶](#envvar-PYTHONDONTWRITEBYTECODE)
- If this is set to a non-empty string, Python won’t try to write - `.pyc`files on the import of source modules. This is equivalent to specifying the- `-B`

- 
PYTHONPYCACHEPREFIX[¶](#envvar-PYTHONPYCACHEPREFIX)
- If this is set, Python will write - `.pyc`files in a mirror directory tree at this path, instead of in- `__pycache__`directories within the source tree. This is equivalent to specifying the- `-X`- `pycache_prefix=PATH`option.- Added in version 3.8. 

- 
PYTHONHASHSEED[¶](#envvar-PYTHONHASHSEED)
- If this variable is not set or set to - `random`, a random value is used to seed the hashes of str and bytes objects.- If - `PYTHONHASHSEED`- Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values. - The integer must be a decimal number in the range [0,4294967295]. Specifying the value 0 will disable hash randomization. - Added in version 3.2.3. 

- 
PYTHONINTMAXSTRDIGITS[¶](#envvar-PYTHONINTMAXSTRDIGITS)
- If this variable is set to an integer, it is used to configure the interpreter’s global - [integer string conversion length limitation](../library/stdtypes.html#int-max-str-digits).- Added in version 3.11. 

- 
PYTHONIOENCODING[¶](#envvar-PYTHONIOENCODING)
- If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax - `encodingname:errorhandler`. Both the- `encodingname`and the- `:errorhandler`parts are optional and have the same meaning as in- `str.encode()`- For stderr, the - `:errorhandler`part is ignored; the handler will always be- `'backslashreplace'`.- Changed in version 3.4: The - `encodingname`part is now optional.- Changed in version 3.6: On Windows, the encoding specified by this variable is ignored for interactive console buffers unless - `PYTHONLEGACYWINDOWSSTDIO`

- 
PYTHONNOUSERSITE[¶](#envvar-PYTHONNOUSERSITE)
- If this is set, Python won’t add the - `user site-packages directory`- `sys.path`- See also - **PEP 370**

- 
PYTHONUSERBASE[¶](#envvar-PYTHONUSERBASE)
- Defines the - `user base directory`- `user site-packages directory`- [installation paths](../library/sysconfig.html#sysconfig-user-scheme)for- `python -m pip install --user`.- See also - **PEP 370**

- 
PYTHONEXECUTABLE[¶](#envvar-PYTHONEXECUTABLE)
- If this environment variable is set, - `sys.argv[0]`will be set to its value instead of the value got through the C runtime. Only works on macOS.

- 
PYTHONWARNINGS[¶](#envvar-PYTHONWARNINGS)
- This is equivalent to the - `-W`- `-W`multiple times, with filters later in the list taking precedence over those earlier in the list.- The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default): - PYTHONWARNINGS=default # Warn once per call location PYTHONWARNINGS=error # Convert to exceptions PYTHONWARNINGS=always # Warn every time PYTHONWARNINGS=all # Same as PYTHONWARNINGS=always PYTHONWARNINGS=module # Warn once per calling module PYTHONWARNINGS=once # Warn once per Python process PYTHONWARNINGS=ignore # Never warn - See - [The Warnings Filter](../library/warnings.html#warning-filter)and- [Describing Warning Filters](../library/warnings.html#describing-warning-filters)for more details.

- 
PYTHONFAULTHANDLER[¶](#envvar-PYTHONFAULTHANDLER)
- If this environment variable is set to a non-empty string, - `faulthandler.enable()`- `SIGSEGV`- `SIGFPE`- `SIGABRT`- `SIGBUS`- `SIGILL`- `-X`- `faulthandler`option.- Added in version 3.3. 

- 
PYTHONTRACEMALLOC[¶](#envvar-PYTHONTRACEMALLOC)
- If this environment variable is set to a non-empty string, start tracing Python memory allocations using the - `tracemalloc`- `PYTHONTRACEMALLOC=1`stores only the most recent frame. See the- `tracemalloc.start()`- `-X`- `tracemalloc`option.- Added in version 3.4. 

- 
PYTHONPROFILEIMPORTTIME[¶](#envvar-PYTHONPROFILEIMPORTTIME)
- If this environment variable is set to a non-empty string, Python will show how long each import takes. This is equivalent to setting the - `-X`- `importtime`option.- Added in version 3.7. 

- 
PYTHONASYNCIODEBUG[¶](#envvar-PYTHONASYNCIODEBUG)
- If this environment variable is set to a non-empty string, enable the - [debug mode](../library/asyncio-dev.html#asyncio-debug-mode)of the- `asyncio`- Added in version 3.4. 

- 
PYTHONMALLOC[¶](#envvar-PYTHONMALLOC)
- Set the Python memory allocators and/or install debug hooks. - Set the family of memory allocators used by Python: - `default`: use the- [default memory allocators](../c-api/memory.html#default-memory-allocators).
- `malloc`: use the- `malloc()`function of the C library for all domains (- `PYMEM_DOMAIN_RAW`- `PYMEM_DOMAIN_MEM`- `PYMEM_DOMAIN_OBJ`
- `pymalloc`: use the- [pymalloc allocator](../c-api/memory.html#pymalloc)for- `PYMEM_DOMAIN_MEM`- `PYMEM_DOMAIN_OBJ`- `malloc()`function for the- `PYMEM_DOMAIN_RAW`
- `mimalloc`: use the- [mimalloc allocator](../c-api/memory.html#mimalloc)for- `PYMEM_DOMAIN_MEM`- `PYMEM_DOMAIN_OBJ`- `malloc()`function for the- `PYMEM_DOMAIN_RAW`
 - Install - [debug hooks](../c-api/memory.html#pymem-debug-hooks):- `debug`: install debug hooks on top of the- [default memory allocators](../c-api/memory.html#default-memory-allocators).
- `malloc_debug`: same as- `malloc`but also install debug hooks.
- `pymalloc_debug`: same as- `pymalloc`but also install debug hooks.
- `mimalloc_debug`: same as- `mimalloc`but also install debug hooks.
 - Added in version 3.6. - Changed in version 3.7: Added the - `"default"`allocator.

- 
PYTHONMALLOCSTATS[¶](#envvar-PYTHONMALLOCSTATS)
- If set to a non-empty string, Python will print statistics of the - [pymalloc memory allocator](../c-api/memory.html#pymalloc)every time a new pymalloc object arena is created, and on shutdown.- This variable is ignored if the - `PYTHONMALLOC`- `malloc()`allocator of the C library, or if Python is configured without- `pymalloc`support.- Changed in version 3.6: This variable can now also be used on Python compiled in release mode. It now has no effect if set to an empty string. 

- 
PYTHONLEGACYWINDOWSFSENCODING[¶](#envvar-PYTHONLEGACYWINDOWSFSENCODING)
- If set to a non-empty string, the default - [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler)mode will revert to their pre-3.6 values of ‘mbcs’ and ‘replace’, respectively. Otherwise, the new defaults ‘utf-8’ and ‘surrogatepass’ are used.- This may also be enabled at runtime with - `sys._enablelegacywindowsfsencoding()`- [Availability](../library/intro.html#availability): Windows.- Added in version 3.6: See - **PEP 529**

- 
PYTHONLEGACYWINDOWSSTDIO[¶](#envvar-PYTHONLEGACYWINDOWSSTDIO)
- If set to a non-empty string, does not use the new console reader and writer. This means that Unicode characters will be encoded according to the active console code page, rather than using utf-8. - This variable is ignored if the standard streams are redirected (to files or pipes) rather than referring to console buffers. - [Availability](../library/intro.html#availability): Windows.- Added in version 3.6. 

- 
PYTHONCOERCECLOCALE[¶](#envvar-PYTHONCOERCECLOCALE)
- If set to the value - `0`, causes the main Python command line application to skip coercing the legacy ASCII-based C and POSIX locales to a more capable UTF-8 based alternative.- If this variable is - *not*set (or is set to a value other than- `0`), the- `LC_ALL`locale override environment variable is also not set, and the current locale reported for the- `LC_CTYPE`category is either the default- `C`locale, or else the explicitly ASCII-based- `POSIX`locale, then the Python CLI will attempt to configure the following locales for the- `LC_CTYPE`category in the order listed before loading the interpreter runtime:- `C.UTF-8`
- `C.utf8`
- `UTF-8`
 - If setting one of these locale categories succeeds, then the - `LC_CTYPE`environment variable will also be set accordingly in the current process environment before the Python runtime is initialized. This ensures that in addition to being seen by both the interpreter itself and other locale-aware components running in the same process (such as the GNU- `readline`library), the updated setting is also seen in subprocesses (regardless of whether or not those processes are running a Python interpreter), as well as in operations that query the environment rather than the current C locale (such as Python’s own- `locale.getdefaultlocale()`- Configuring one of these locales (either explicitly or via the above implicit locale coercion) automatically enables the - `surrogateescape`- [error handler](../library/codecs.html#error-handlers)for- `sys.stdin`- `sys.stdout`- `sys.stderr`- `backslashreplace`as it does in any other locale). This stream handling behavior can be overridden using- `PYTHONIOENCODING`- For debugging purposes, setting - `PYTHONCOERCECLOCALE=warn`will cause Python to emit warning messages on- `stderr`if either the locale coercion activates, or else if a locale that- *would*have triggered coercion is still active when the Python runtime is initialized.- Also note that even when locale coercion is disabled, or when it fails to find a suitable target locale, - `PYTHONUTF8`- `ASCII`instead of- `UTF-8`for system interfaces.- [Availability](../library/intro.html#availability): Unix.- Added in version 3.7: See - **PEP 538**

- 
PYTHONDEVMODE[¶](#envvar-PYTHONDEVMODE)
- If this environment variable is set to a non-empty string, enable - [Python Development Mode](../library/devmode.html#devmode), introducing additional runtime checks that are too expensive to be enabled by default. This is equivalent to setting the- `-X`- `dev`option.- Added in version 3.7. 

- 
PYTHONUTF8[¶](#envvar-PYTHONUTF8)
- If set to - `1`, enable the- [Python UTF-8 Mode](../library/os.html#utf8-mode).- If set to - `0`, disable the- [Python UTF-8 Mode](../library/os.html#utf8-mode).- Setting any other non-empty string causes an error during interpreter initialisation. - Added in version 3.7. 

- 
PYTHONWARNDEFAULTENCODING[¶](#envvar-PYTHONWARNDEFAULTENCODING)
- If this environment variable is set to a non-empty string, issue a - `EncodingWarning`- See - [Opt-in EncodingWarning](../library/io.html#io-encoding-warning)for details.- Added in version 3.10. 

- 
PYTHONNODEBUGRANGES[¶](#envvar-PYTHONNODEBUGRANGES)
- If this variable is set, it disables the inclusion of the tables mapping extra location information (end line, start column offset and end column offset) to every instruction in code objects. This is useful when smaller code objects and pyc files are desired as well as suppressing the extra visual location indicators when the interpreter displays tracebacks. - Added in version 3.11. 

- 
PYTHONPERFSUPPORT[¶](#envvar-PYTHONPERFSUPPORT)
- If this variable is set to a nonzero value, it enables support for the Linux - `perf`profiler so Python calls can be detected by it.- If set to - `0`, disable Linux- `perf`profiler support.- See also the - `-X perf`- [Python support for the Linux perf profiler](../howto/perf_profiling.html#perf-profiling).- Added in version 3.12. 

- 
PYTHON_PERF_JIT_SUPPORT[¶](#envvar-PYTHON_PERF_JIT_SUPPORT)
- If this variable is set to a nonzero value, it enables support for the Linux - `perf`profiler so Python calls can be detected by it using DWARF information.- If set to - `0`, disable Linux- `perf`profiler support.- See also the - `-X perf_jit`- [Python support for the Linux perf profiler](../howto/perf_profiling.html#perf-profiling).- Added in version 3.13. 

- 
PYTHON_CPU_COUNT[¶](#envvar-PYTHON_CPU_COUNT)
- If this variable is set to a positive integer, it overrides the return values of - `os.cpu_count()`- `os.process_cpu_count()`- See also the - `-X cpu_count`- Added in version 3.13. 

- 
PYTHON_FROZEN_MODULES[¶](#envvar-PYTHON_FROZEN_MODULES)
- If this variable is set to - `on`or- `off`, it determines whether or not frozen modules are ignored by the import machinery. A value of- `on`means they get imported and- `off`means they are ignored. The default is- `on`for non-debug builds (the normal case) and- `off`for debug builds. Note that the- `importlib_bootstrap`and- `importlib_bootstrap_external`frozen modules are always used, even if this flag is set to- `off`.- See also the - `-X frozen_modules`- Added in version 3.13. 

- 
PYTHON_COLORS[¶](#envvar-PYTHON_COLORS)
- If this variable is set to - `1`, the interpreter will colorize various kinds of output. Setting it to- `0`deactivates this behavior. See also- [Controlling color](#using-on-controlling-color).- Added in version 3.13. 

- 
PYTHON_BASIC_REPL[¶](#envvar-PYTHON_BASIC_REPL)
- If this variable is set to any value, the interpreter will not attempt to load the Python-based - [REPL](../glossary.html#term-REPL)that requires- `curses`- `readline`- Added in version 3.13. 

- 
PYTHON_HISTORY[¶](#envvar-PYTHON_HISTORY)
- This environment variable can be used to set the location of a - `.python_history`file (by default, it is- `.python_history`in the user’s home directory).- Added in version 3.13. 

- 
PYTHON_GIL[¶](#envvar-PYTHON_GIL)
- If this variable is set to - `1`, the global interpreter lock (GIL) will be forced on. Setting it to- `0`forces the GIL off (needs Python configured with the- `--disable-gil`- See also the - `-X gil`- [Free-threaded CPython](../whatsnew/3.13.html#whatsnew313-free-threaded-cpython).- Added in version 3.13. 

- 
PYTHON_JIT[¶](#envvar-PYTHON_JIT)
- On builds where experimental just-in-time compilation is available, this variable can force the JIT to be disabled ( - `0`) or enabled (- `1`) at interpreter startup.- Added in version 3.13. 

### 1.2.1. Debug-mode variables[¶](#debug-mode-variables)

- 
PYTHONDUMPREFS[¶](#envvar-PYTHONDUMPREFS)
- If set, Python will dump objects and reference counts still alive after shutting down the interpreter. - Needs Python configured with the - `--with-trace-refs`

- 
PYTHONDUMPREFSFILE[¶](#envvar-PYTHONDUMPREFSFILE)
- If set, Python will dump objects and reference counts still alive after shutting down the interpreter into a file under the path given as the value to this environment variable. - Needs Python configured with the - `--with-trace-refs`- Added in version 3.11. 

- 
PYTHON_PRESITE[¶](#envvar-PYTHON_PRESITE)
- If this variable is set to a module, that module will be imported early in the interpreter lifecycle, before the - `site`- `__main__`- `__main__`.- This can be used to execute code early during Python initialization. - To import a submodule, use - `package.module`as the value, like in an import statement.- See also the - `-X presite`- Needs Python configured with the - `--with-pydebug`- Added in version 3.13.