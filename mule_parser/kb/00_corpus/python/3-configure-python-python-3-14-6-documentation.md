# 3. Configure Python — Python 3.14.6 documentation

**Source:** [https://docs.python.org/using/configure.html](https://docs.python.org/using/configure.html)

---

# 3. Configure Python[¶](#configure-python)

## 3.1. Build Requirements[¶](#build-requirements)

To build CPython, you will need:

- A - [C11](https://en.cppreference.com/w/c/11)compiler.- [Optional C11 features](https://en.wikipedia.org/wiki/C11_(C_standard_revision)#Optional_features)are not required.
- On Windows, Microsoft Visual Studio 2017 or later is required. 
- Support for - [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)floating-point numbers and- [floating-point Not-a-Number (NaN)](https://en.wikipedia.org/wiki/NaN#Floating_point).
- Support for threads. 

Changed in version 3.5: On Windows, Visual Studio 2015 or later is now required.

Changed in version 3.6: Selected C99 features, like `<stdint.h>` and `static inline` functions,
are now required.

Changed in version 3.7: Thread support is now required.

Changed in version 3.11: C11 compiler, IEEE 754 and NaN support are now required. On Windows, Visual Studio 2017 or later is required.

See also [ PEP 7](https://peps.python.org/pep-0007/) “Style Guide for C Code” and 

[“CPython platform support”.](https://peps.python.org/pep-0011/)

**PEP 11**### 3.1.1. Requirements for optional modules[¶](#requirements-for-optional-modules)

Some [optional modules](../glossary.html#term-optional-module) of the standard library
require third-party libraries installed for development
(for example, header files must be available).

Missing requirements are reported in the `configure` output.
Modules that are missing due to missing dependencies are listed near the end
of the `make` output,
sometimes using an internal name, for example, `_ctypes` for [ ctypes](../library/ctypes.html#module-ctypes)
module.

If you distribute a CPython interpreter without optional modules, it’s best practice to advise users, who generally expect that standard library modules are available.

Dependencies to build optional modules are:

| Dependency | Minimum version | Python module | 
|---|---|---|
| 3.3.0 recommended | ||
| 2.5.0 | ||
| 
 | ||
| 3.0.18 recommended (1.1.1 minimum) | ||
| 3.15.2 | ||
| 8.5.12 | ||
| 1.2.2.1 | ||
| 1.4.5 | 

Note that the table does not include all optional modules; in particular,
platform-specific modules like [ winreg](../library/winreg.html#module-winreg) are not listed here.

See also

- The - [devguide](https://devguide.python.org/getting-started/setup-building/#install-dependencies)includes a full list of dependencies required to build all modules and instructions on how to install them on common platforms.
- `--with-system-expat`- [libexpat](https://libexpat.github.io/)library.

Changed in version 3.1: Tcl/Tk version 8.3.1 is now required for [ tkinter](../library/tkinter.html#module-tkinter).

Changed in version 3.5: Tcl/Tk version 8.4 is now required for [ tkinter](../library/tkinter.html#module-tkinter).

Changed in version 3.10: OpenSSL 1.1.1 is now required for [ hashlib](../library/hashlib.html#module-hashlib) and 

[. SQLite 3.7.15 is now required for](../library/ssl.html#module-ssl)

`ssl`[.](../library/sqlite3.html#module-sqlite3)

`sqlite3`Changed in version 3.11: Tcl/Tk version 8.5.12 is now required for [ tkinter](../library/tkinter.html#module-tkinter).

Changed in version 3.13: SQLite 3.15.2 is now required for [ sqlite3](../library/sqlite3.html#module-sqlite3).

## 3.2. Generated files[¶](#generated-files)

To reduce build dependencies, Python source code contains multiple generated files. Commands to regenerate all generated files:

```
make regen-all
make regen-stdlib-module-names
make regen-limited-abi
make regen-configure
```
The `Makefile.pre.in` file documents generated files, their inputs, and tools used
to regenerate them. Search for `regen-*` make targets.

### 3.2.1. configure script[¶](#configure-script)

The `make regen-configure` command regenerates the `aclocal.m4` file and
the `configure` script using the `Tools/build/regen-configure.sh` shell
script which uses an Ubuntu container to get the same tools versions and have a
reproducible output.

The container is optional, the following command can be run locally:

```
autoreconf -ivf -Werror
```
The generated files can change depending on the exact versions of the
tools used.
The container that CPython uses has
[Autoconf](https://gnu.org/software/autoconf) 2.72,
`aclocal` from [Automake](https://www.gnu.org/software/automake) 1.16.5,
and [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) 1.8.1.

Changed in version 3.13: Autoconf 2.71 and aclocal 1.16.5 and are now used to regenerate
`configure`.

Changed in version 3.14: Autoconf 2.72 is now used to regenerate `configure`.

## 3.3. Configure Options[¶](#configure-options)

List all `configure` script options using:

```
./configure --help
```
See also the `Misc/SpecialBuilds.txt` in the Python source distribution.

### 3.3.1. General Options[¶](#general-options)

- 
--enable-loadable-sqlite-extensions[¶](#cmdoption-enable-loadable-sqlite-extensions)
- Support loadable extensions in the - `_sqlite`extension module (default is no) of the- `sqlite3`- See the - `sqlite3.Connection.enable_load_extension()`- `sqlite3`- Added in version 3.6. 

- 
--enable-big-digits=[15|30][¶](#cmdoption-enable-big-digits)
- Define the size in bits of Python - `int`- By default, the digit size is 30. - Define the - `PYLONG_BITS_IN_DIGIT`to- `15`or- `30`.

- 
--with-suffix=SUFFIX[¶](#cmdoption-with-suffix)
- Set the Python executable suffix to - *SUFFIX*.- The default suffix is - `.exe`on Windows and macOS (- `python.exe`executable),- `.js`on Emscripten node,- `.html`on Emscripten browser,- `.wasm`on WASI, and an empty string on other platforms (- `python`executable).- Changed in version 3.11: The default suffix on WASM platform is one of - `.js`,- `.html`or- `.wasm`.

- 
--with-tzpath=<list of absolute paths separated by pathsep>[¶](#cmdoption-with-tzpath)
- Select the default time zone search path for - `zoneinfo.TZPATH`- [Compile-time configuration](../library/zoneinfo.html#zoneinfo-data-compile-time-config)of the- `zoneinfo`- Default: - `/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo`.- See - `os.pathsep`- Added in version 3.9. 

- 
--without-decimal-contextvar[¶](#cmdoption-without-decimal-contextvar)
- Build the - `_decimal`extension module using a thread-local context rather than a coroutine-local context (default), see the- `decimal`- See - `decimal.HAVE_CONTEXTVAR`- `contextvars`- Added in version 3.9. 

- 
--with-dbmliborder=<list of backend names>[¶](#cmdoption-with-dbmliborder)
- Override order to check db backends for the - `dbm`- A valid value is a colon ( - `:`) separated string with the backend names:- `ndbm`;
- `gdbm`;
- `bdb`.
 

- 
--without-c-locale-coercion[¶](#cmdoption-without-c-locale-coercion)
- Disable C locale coercion to a UTF-8 based locale (enabled by default). - Don’t define the - `PY_COERCE_C_LOCALE`macro.- See - `PYTHONCOERCECLOCALE`- **PEP 538**

- 
--with-platlibdir=DIRNAME[¶](#cmdoption-with-platlibdir)
- Python library directory name (default is - `lib`).- Fedora and SuSE use - `lib64`on 64-bit platforms.- See - `sys.platlibdir`- Added in version 3.9. 

- 
--with-wheel-pkg-dir=PATH[¶](#cmdoption-with-wheel-pkg-dir)
- Directory of wheel packages used by the - `ensurepip`- Some Linux distribution packaging policies recommend against bundling dependencies. For example, Fedora installs wheel packages in the - `/usr/share/python-wheels/`directory and don’t install the- `ensurepip._bundled`package.- Added in version 3.10. 

- 
--with-pkg-config=[check|yes|no][¶](#cmdoption-with-pkg-config)
- Whether configure should use - **pkg-config**to detect build dependencies.- `check`(default):- **pkg-config**is optional
- `yes`:- **pkg-config**is mandatory
- `no`: configure does not use- **pkg-config**even when present
 - Added in version 3.11. 

- 
--enable-pystats[¶](#cmdoption-enable-pystats)
- Turn on internal Python performance statistics gathering. - By default, statistics gathering is off. Use - `python3 -X pystats`command or set- `PYTHONSTATS=1`environment variable to turn on statistics gathering at Python startup.- At Python exit, dump statistics if statistics gathering was on and not cleared. - Effects: - Add - `-X pystats`
- Add - `PYTHONSTATS`environment variable.
- Define the - `Py_STATS`macro.
- Add functions to the - `sys`- `sys._stats_on()`: Turns on statistics gathering.
- `sys._stats_off()`: Turns off statistics gathering.
- `sys._stats_clear()`: Clears the statistics.
- `sys._stats_dump()`: Dump statistics to file, and clears the statistics.
 
 - The statistics will be dumped to a arbitrary (probably unique) file in - `/tmp/py_stats/`(Unix) or- `C:\temp\py_stats\`(Windows). If that directory does not exist, results will be printed on stderr.- Use - `Tools/scripts/summarize_stats.py`to read the stats.- Statistics: - Opcode: - Specialization: success, failure, hit, deferred, miss, deopt, failures; 
- Execution count; 
- Pair count. 
 
- Call: - Inlined Python calls; 
- PyEval calls; 
- Frames pushed; 
- Frame object created; 
- Eval calls: vector, generator, legacy, function VECTORCALL, build class, slot, function “ex”, API, method. 
 
- Object: - incref and decref; 
- interpreter incref and decref; 
- allocations: all, 512 bytes, 4 kiB, big; 
- free; 
- to/from free lists; 
- dictionary materialized/dematerialized; 
- type cache; 
- optimization attempts; 
- optimization traces created/executed; 
- uops executed. 
 
- Garbage collector: - Garbage collections; 
- Objects visited; 
- Objects collected. 
 
 - Added in version 3.11. 

- 
--disable-gil[¶](#cmdoption-disable-gil)
- Enables support for running Python without the - [global interpreter lock](../glossary.html#term-global-interpreter-lock)(GIL):- [free-threaded build](../glossary.html#term-free-threaded-build).- Defines the - `Py_GIL_DISABLED`macro and adds- `"t"`to- `sys.abiflags`- See - [Free-threaded CPython](../whatsnew/3.13.html#whatsnew313-free-threaded-cpython)for more detail.- Added in version 3.13. 

- 
--enable-experimental-jit=[no|yes|yes-off|interpreter][¶](#cmdoption-enable-experimental-jit)
- Indicate how to integrate the - [experimental just-in-time compiler](../whatsnew/3.14.html#whatsnew314-jit-compiler).- `no`: Don’t build the JIT.
- `yes`: Enable the JIT. To disable it at runtime, set the environment variable- `PYTHON_JIT=0`
- `yes-off`: Build the JIT, but disable it by default. To enable it at runtime, set the environment variable- `PYTHON_JIT=1`
- `interpreter`: Enable the “JIT interpreter” (only useful for those debugging the JIT itself). To disable it at runtime, set the environment variable- `PYTHON_JIT=0`
 - `--enable-experimental-jit=no`is the default behavior if the option is not provided, and- `--enable-experimental-jit`is shorthand for- `--enable-experimental-jit=yes`. See- `Tools/jit/README.md`for more information, including how to install the necessary build-time dependencies.- Note - When building CPython with JIT enabled, ensure that your system has Python 3.11 or later installed. - Added in version 3.13. 

- 
PKG_CONFIG[¶](#cmdoption-arg-PKG_CONFIG)
- Path to - `pkg-config`utility.

- 
PKG_CONFIG_LIBDIR[¶](#cmdoption-arg-PKG_CONFIG_LIBDIR)

- 
PKG_CONFIG_PATH[¶](#cmdoption-arg-PKG_CONFIG_PATH)
- `pkg-config`options.

### 3.3.2. C compiler options[¶](#c-compiler-options)

- 
CC[¶](#cmdoption-arg-CC)
- C compiler command. 

- 
CFLAGS[¶](#cmdoption-arg-CFLAGS)
- C compiler flags. 

- 
CPP[¶](#cmdoption-arg-CPP)
- C preprocessor command. 

- 
CPPFLAGS[¶](#cmdoption-arg-CPPFLAGS)
- C preprocessor flags, e.g. - `-I`.- *include_dir*

### 3.3.3. Linker options[¶](#linker-options)

- 
LDFLAGS[¶](#cmdoption-arg-LDFLAGS)
- Linker flags, e.g. - `-L`.- *library_directory*

- 
LIBS[¶](#cmdoption-arg-LIBS)
- Libraries to pass to the linker, e.g. - `-l`.- *library*

- 
MACHDEP[¶](#cmdoption-arg-MACHDEP)
- Name for machine-dependent library files. 

### 3.3.4. Options for third-party dependencies[¶](#options-for-third-party-dependencies)

Added in version 3.11.

- 
BZIP2_CFLAGS[¶](#cmdoption-arg-BZIP2_CFLAGS)

- 
BZIP2_LIBS[¶](#cmdoption-arg-BZIP2_LIBS)
- C compiler and linker flags to link Python to - `libbz2`, used by- `bz2`- `pkg-config`.

- 
CURSES_CFLAGS[¶](#cmdoption-arg-CURSES_CFLAGS)

- 
CURSES_LIBS[¶](#cmdoption-arg-CURSES_LIBS)
- C compiler and linker flags for - `libncurses`or- `libncursesw`, used by- `curses`- `pkg-config`.

- 
GDBM_CFLAGS[¶](#cmdoption-arg-GDBM_CFLAGS)

- 
GDBM_LIBS[¶](#cmdoption-arg-GDBM_LIBS)
- C compiler and linker flags for - `gdbm`.

- 
LIBEDIT_CFLAGS[¶](#cmdoption-arg-LIBEDIT_CFLAGS)

- 
LIBEDIT_LIBS[¶](#cmdoption-arg-LIBEDIT_LIBS)
- C compiler and linker flags for - `libedit`, used by- `readline`- `pkg-config`.

- 
LIBFFI_CFLAGS[¶](#cmdoption-arg-LIBFFI_CFLAGS)

- 
LIBMPDEC_CFLAGS[¶](#cmdoption-arg-LIBMPDEC_CFLAGS)

- 
LIBMPDEC_LIBS[¶](#cmdoption-arg-LIBMPDEC_LIBS)
- C compiler and linker flags for - `libmpdec`, used by- `decimal`- `pkg-config`.- Note - These environment variables have no effect unless - `--with-system-libmpdec`

- 
LIBLZMA_CFLAGS[¶](#cmdoption-arg-LIBLZMA_CFLAGS)

- 
LIBREADLINE_CFLAGS[¶](#cmdoption-arg-LIBREADLINE_CFLAGS)

- 
LIBREADLINE_LIBS[¶](#cmdoption-arg-LIBREADLINE_LIBS)
- C compiler and linker flags for - `libreadline`, used by- `readline`- `pkg-config`.

- 
LIBSQLITE3_CFLAGS[¶](#cmdoption-arg-LIBSQLITE3_CFLAGS)

- 
LIBSQLITE3_LIBS[¶](#cmdoption-arg-LIBSQLITE3_LIBS)
- C compiler and linker flags for - `libsqlite3`, used by- `sqlite3`- `pkg-config`.

- 
LIBUUID_CFLAGS[¶](#cmdoption-arg-LIBUUID_CFLAGS)

- 
LIBZSTD_CFLAGS[¶](#cmdoption-arg-LIBZSTD_CFLAGS)

- 
LIBZSTD_LIBS[¶](#cmdoption-arg-LIBZSTD_LIBS)
- C compiler and linker flags for - `libzstd`, used by- `compression.zstd`- `pkg-config`.- Added in version 3.14. 

- 
PANEL_CFLAGS[¶](#cmdoption-arg-PANEL_CFLAGS)

- 
PANEL_LIBS[¶](#cmdoption-arg-PANEL_LIBS)
- C compiler and linker flags for PANEL, overriding - `pkg-config`.- C compiler and linker flags for - `libpanel`or- `libpanelw`, used by- `curses.panel`- `pkg-config`.

- 
TCLTK_CFLAGS[¶](#cmdoption-arg-TCLTK_CFLAGS)

- 
TCLTK_LIBS[¶](#cmdoption-arg-TCLTK_LIBS)
- C compiler and linker flags for TCLTK, overriding - `pkg-config`.

- 
ZLIB_CFLAGS[¶](#cmdoption-arg-ZLIB_CFLAGS)

### 3.3.5. WebAssembly Options[¶](#webassembly-options)

- 
--enable-wasm-dynamic-linking[¶](#cmdoption-enable-wasm-dynamic-linking)
- Turn on dynamic linking support for WASM. - Dynamic linking enables - `dlopen`. File size of the executable increases due to limited dead code elimination and additional features.- Added in version 3.11. 

- 
--enable-wasm-pthreads[¶](#cmdoption-enable-wasm-pthreads)
- Turn on pthreads support for WASM. - Added in version 3.11. 

### 3.3.6. Install Options[¶](#install-options)

- 
--prefix=PREFIX[¶](#cmdoption-prefix)
- Install architecture-independent files in PREFIX. On Unix, it defaults to - `/usr/local`.- This value can be retrieved at runtime using - `sys.prefix`- As an example, one can use - `--prefix="$HOME/.local/"`to install a Python in its home directory.

- 
--exec-prefix=EPREFIX[¶](#cmdoption-exec-prefix)
- Install architecture-dependent files in EPREFIX, defaults to - `--prefix`- This value can be retrieved at runtime using - `sys.exec_prefix`

### 3.3.7. Performance options[¶](#performance-options)

Configuring Python using `--enable-optimizations --with-lto` (PGO + LTO) is
recommended for best performance. The experimental `--enable-bolt` flag can
also be used to improve performance.

- 
--enable-optimizations[¶](#cmdoption-enable-optimizations)
- Enable Profile Guided Optimization (PGO) using - `PROFILE_TASK`- The C compiler Clang requires - `llvm-profdata`program for PGO. On macOS, GCC also requires it: GCC is just an alias to Clang on macOS.- Disable also semantic interposition in libpython if - `--enable-shared`and GCC is used: add- `-fno-semantic-interposition`to the compiler and linker flags.- Note - During the build, you may encounter compiler warnings about profile data not being available for some source files. These warnings are harmless, as only a subset of the code is exercised during profile data acquisition. To disable these warnings on Clang, manually suppress them by adding - `-Wno-profile-instr-unprofiled`to- `CFLAGS`- Added in version 3.6. - Changed in version 3.10: Use - `-fno-semantic-interposition`on GCC.

- 
PROFILE_TASK[¶](#envvar-PROFILE_TASK)
- Environment variable used in the Makefile: Python command line arguments for the PGO generation task. - Default: - `-m test --pgo --timeout=$(TESTTIMEOUT)`.- Added in version 3.8. - Changed in version 3.13: Task failure is no longer ignored silently. 

- 
--with-lto=[full|thin|no|yes][¶](#cmdoption-with-lto)
- Enable Link Time Optimization (LTO) in any build (disabled by default). - The C compiler Clang requires - `llvm-ar`for LTO (- `ar`on macOS), as well as an LTO-aware linker (- `ld.gold`or- `lld`).- Added in version 3.6. - Added in version 3.11: To use ThinLTO feature, use - `--with-lto=thin`on Clang.- Changed in version 3.12: Use ThinLTO as the default optimization policy on Clang if the compiler accepts the flag. 

- 
--enable-bolt[¶](#cmdoption-enable-bolt)
- Enable usage of the - [BOLT post-link binary optimizer](https://github.com/llvm/llvm-project/tree/main/bolt)(disabled by default).- BOLT is part of the LLVM project but is not always included in their binary distributions. This flag requires that - `llvm-bolt`and- `merge-fdata`are available.- BOLT is still a fairly new project so this flag should be considered experimental for now. Because this tool operates on machine code its success is dependent on a combination of the build environment + the other optimization configure args + the CPU architecture, and not all combinations are supported. BOLT versions before LLVM 16 are known to crash BOLT under some scenarios. Use of LLVM 16 or newer for BOLT optimization is strongly encouraged. - The - `BOLT_INSTRUMENT_FLAGS`and- `BOLT_APPLY_FLAGS`- **configure**variables can be defined to override the default set of arguments for- **llvm-bolt**to instrument and apply BOLT data to binaries, respectively.- Added in version 3.12. 

- 
BOLT_APPLY_FLAGS[¶](#cmdoption-arg-BOLT_APPLY_FLAGS)
- Arguments to - `llvm-bolt`when creating a- [BOLT optimized binary](https://github.com/facebookarchive/BOLT).- Added in version 3.12. 

- 
BOLT_INSTRUMENT_FLAGS[¶](#cmdoption-arg-BOLT_INSTRUMENT_FLAGS)
- Arguments to - `llvm-bolt`when instrumenting binaries.- Added in version 3.12. 

- 
--with-computed-gotos[¶](#cmdoption-with-computed-gotos)
- Enable computed gotos in evaluation loop (enabled by default on supported compilers). 

- 
--with-tail-call-interp[¶](#cmdoption-with-tail-call-interp)
- Enable interpreters using tail calls in CPython. If enabled, enabling PGO ( - `--enable-optimizations`- [preserve_none](https://clang.llvm.org/docs/AttributeReference.html#preserve-none)calling convention. For example, Clang 19 and newer supports this feature.- Added in version 3.14. 

- 
--without-mimalloc[¶](#cmdoption-without-mimalloc)
- Disable the fast - [mimalloc](../c-api/memory.html#mimalloc)allocator (enabled by default).- This option cannot be used together with - `--disable-gil`- [free-threaded](../glossary.html#term-free-threading)build requires mimalloc.- See also - `PYTHONMALLOC`

- 
--without-pymalloc[¶](#cmdoption-without-pymalloc)
- Disable the specialized Python memory allocator - [pymalloc](../c-api/memory.html#pymalloc)(enabled by default).- See also - `PYTHONMALLOC`

- 
--without-doc-strings[¶](#cmdoption-without-doc-strings)
- Disable static documentation strings to reduce the memory footprint (enabled by default). Documentation strings defined in Python are not affected. - Don’t define the - `WITH_DOC_STRINGS`macro.- See the - `PyDoc_STRVAR()`macro.

- 
--enable-profiling[¶](#cmdoption-enable-profiling)
- Enable C-level code profiling with - `gprof`(disabled by default).

- 
--with-strict-overflow[¶](#cmdoption-with-strict-overflow)
- Add - `-fstrict-overflow`to the C compiler flags (by default we add- `-fno-strict-overflow`instead).

- 
--without-remote-debug[¶](#cmdoption-without-remote-debug)
- Deactivate remote debugging support described in - **PEP 768**- **PEP 768**- 
Py_REMOTE_DEBUG[¶](#c.Py_REMOTE_DEBUG)
- This macro is defined by default, unless Python is configured with - `--without-remote-debug`- Note that even if the macro is defined, remote debugging may not be available (for example, on an incompatible platform). 
 - Added in version 3.14. 
- 
Py_REMOTE_DEBUG

### 3.3.8. Python Debug Build[¶](#python-debug-build)

A debug build is Python built with the [ --with-pydebug](#cmdoption-with-pydebug) configure
option.

Effects of a debug build:

- Display all warnings by default: the list of default warning filters is empty in the - `warnings`
- Add - `d`to- `sys.abiflags`
- Add - `sys.gettotalrefcount()`function.
- Add - `-X showrefcount`
- Add - `-d`- `PYTHONDEBUG`
- Add support for the - `__lltrace__`variable: enable low-level tracing in the bytecode evaluation loop if the variable is defined.
- Install - [debug hooks on memory allocators](../c-api/memory.html#default-memory-allocators)to detect buffer overflow and other memory errors.
- Define - `Py_DEBUG`and- `Py_REF_DEBUG`macros.
- Add runtime checks: code surrounded by - `#ifdef Py_DEBUG`and- `#endif`. Enable- `assert(...)`and- `_PyObject_ASSERT(...)`assertions: don’t set the- `NDEBUG`macro (see also the- `--with-assertions`- Add sanity checks on the function arguments. 
- Unicode and int objects are created with their memory filled with a pattern to detect usage of uninitialized objects. 
- Ensure that functions which can clear or replace the current exception are not called with an exception raised. 
- Check that deallocator functions don’t change the current exception. 
- The garbage collector ( - `gc.collect()`
- The - `Py_SAFE_DOWNCAST()`macro checks for integer underflow and overflow when downcasting from wide types to narrow types.
 

See also the [Python Development Mode](../library/devmode.html#devmode) and the
[ --with-trace-refs](#cmdoption-with-trace-refs) configure option.

Changed in version 3.8: Release builds are now ABI compatible with debug builds: defining the
`Py_DEBUG` macro no longer implies the `Py_TRACE_REFS` macro (see the
[ --with-trace-refs](#cmdoption-with-trace-refs) option). However, debug builds still expose
more symbols than release builds and code built against a debug build is not
necessarily compatible with a release build.

### 3.3.9. Debug options[¶](#debug-options)

- 
--with-pydebug[¶](#cmdoption-with-pydebug)
- [Build Python in debug mode](#debug-build): define the- `Py_DEBUG`macro (disabled by default).

- 
--with-trace-refs[¶](#cmdoption-with-trace-refs)
- Enable tracing references for debugging purpose (disabled by default). - Effects: - Define the - `Py_TRACE_REFS`macro.
- Add - `sys.getobjects()`
- Add - `PYTHONDUMPREFS`
 - The - `PYTHONDUMPREFS`- [Statically allocated objects](../c-api/typeobj.html#static-types)are not traced.- Added in version 3.8. - Changed in version 3.13: This build is now ABI compatible with release build and - [debug build](#debug-build).

- 
--with-assertions[¶](#cmdoption-with-assertions)
- Build with C assertions enabled (default is no): - `assert(...);`and- `_PyObject_ASSERT(...);`.- If set, the - `NDEBUG`macro is not defined in the- `OPT`- See also the - `--with-pydebug`- [debug build](#debug-build)) which also enables assertions.- Added in version 3.6. 

- 
--with-valgrind[¶](#cmdoption-with-valgrind)
- Enable Valgrind support (default is no). 

- 
--with-dtrace[¶](#cmdoption-with-dtrace)
- Enable DTrace support (default is no). - See - [Instrumenting CPython with DTrace and SystemTap](../howto/instrumentation.html#instrumentation).- Added in version 3.6. 

- 
--with-address-sanitizer[¶](#cmdoption-with-address-sanitizer)
- Enable AddressSanitizer memory error detector, - `asan`(default is no). To improve ASan detection capabilities you may also want to combine this with- `--without-pymalloc`- Added in version 3.6. 

- 
--with-memory-sanitizer[¶](#cmdoption-with-memory-sanitizer)
- Enable MemorySanitizer allocation error detector, - `msan`(default is no).- Added in version 3.6. 

- 
--with-undefined-behavior-sanitizer[¶](#cmdoption-with-undefined-behavior-sanitizer)
- Enable UndefinedBehaviorSanitizer undefined behaviour detector, - `ubsan`(default is no).- Added in version 3.6. 

- 
--with-thread-sanitizer[¶](#cmdoption-with-thread-sanitizer)
- Enable ThreadSanitizer data race detector, - `tsan`(default is no).- Added in version 3.13. 

### 3.3.10. Linker options[¶](#id13)

- Enable building a shared Python library: - `libpython`(default is no).

- 
--without-static-libpython[¶](#cmdoption-without-static-libpython)
- Do not build - `libpythonMAJOR.MINOR.a`and do not install- `python.o`(built and enabled by default).- Added in version 3.10. 

### 3.3.11. Libraries options[¶](#libraries-options)

- 
--with-libs='lib1 ...'[¶](#cmdoption-with-libs)
- Link against additional libraries (default is no). 

- 
--with-system-expat[¶](#cmdoption-with-system-expat)
- Build the - `pyexpat`module using an installed- `expat`library (default is no).

- 
--with-system-libmpdec[¶](#cmdoption-with-system-libmpdec)
- Build the - `_decimal`extension module using an installed- `mpdecimal`library, see the- `decimal`- Added in version 3.3. - Changed in version 3.13: Default to using the installed - `mpdecimal`library.- Changed in version 3.15: A bundled copy of the library will no longer be selected implicitly if an installed - `mpdecimal`library is not found. In Python 3.15 only, it can still be selected explicitly using- `--with-system-libmpdec=no`or- `--without-system-libmpdec`.- Deprecated since version 3.13, will be removed in version 3.16: A copy of the - `mpdecimal`library sources will no longer be distributed with Python 3.16.- See also 

- 
--with-readline=readline|editline[¶](#cmdoption-with-readline)
- Designate a backend library for the - `readline`- readline: Use readline as the backend. 
- editline: Use editline as the backend. 
 - Added in version 3.10. 

- 
--without-readline[¶](#cmdoption-without-readline)
- Don’t build the - `readline`- Don’t define the - `HAVE_LIBREADLINE`macro.- Added in version 3.10. 

- 
--with-libm=STRING[¶](#cmdoption-with-libm)
- Override - `libm`math library to- *STRING*(default is system-dependent).

- 
--with-libc=STRING[¶](#cmdoption-with-libc)
- Override - `libc`C library to- *STRING*(default is system-dependent).

- 
--with-openssl=DIR[¶](#cmdoption-with-openssl)
- Root of the OpenSSL directory. - Added in version 3.7. 

- 
--with-openssl-rpath=[no|auto|DIR][¶](#cmdoption-with-openssl-rpath)
- Set runtime library directory (rpath) for OpenSSL libraries: - `no`(default): don’t set rpath;
- `auto`: auto-detect rpath from- `--with-openssl`- `pkg-config`;
- *DIR*: set an explicit rpath.
 - Added in version 3.10. 

### 3.3.12. Security Options[¶](#security-options)

- 
--with-hash-algorithm=[fnv|siphash13|siphash24][¶](#cmdoption-with-hash-algorithm)
- Select hash algorithm for use in - `Python/pyhash.c`:- `siphash13`(default);
- `siphash24`;
- `fnv`.
 - Added in version 3.4. - Added in version 3.11: - `siphash13`is added and it is the new default.

- 
--with-builtin-hashlib-hashes=md5,sha1,sha256,sha512,sha3,blake2[¶](#cmdoption-with-builtin-hashlib-hashes)
- Built-in hash modules: - `md5`;
- `sha1`;
- `sha256`;
- `sha512`;
- `sha3`(with shake);
- `blake2`.
 - Added in version 3.9. 

- 
--with-ssl-default-suites=[python|openssl|STRING][¶](#cmdoption-with-ssl-default-suites)
- Override the OpenSSL default cipher suites string: - `python`(default): use Python’s preferred selection;
- `openssl`: leave OpenSSL’s defaults untouched;
- *STRING*: use a custom string
 - See the - `ssl`- Added in version 3.7. - Changed in version 3.10: The settings - `python`and- *STRING*also set TLS 1.2 as minimum protocol version.

- 
--disable-safety[¶](#cmdoption-disable-safety)
- Disable compiler options that are - [recommended by OpenSSF](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md)for security reasons with no performance overhead. If this option is not enabled, CPython will be built based on safety compiler options with no slow down. When this option is enabled, CPython will not be built with the compiler options listed below.- The following compiler options are disabled with - `--disable-safety`:- [-fstack-protector-strong](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#enable-run-time-checks-for-stack-based-buffer-overflows): Enable run-time checks for stack-based buffer overflows.
- [-Wtrampolines](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#enable-warning-about-trampolines-that-require-executable-stacks): Enable warnings about trampolines that require executable stacks.
 - Added in version 3.14. 

- 
--enable-slower-safety[¶](#cmdoption-enable-slower-safety)
- Enable compiler options that are - [recommended by OpenSSF](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md)for security reasons which require overhead. If this option is not enabled, CPython will not be built based on safety compiler options which performance impact. When this option is enabled, CPython will be built with the compiler options listed below.- The following compiler options are enabled with - `--enable-slower-safety`:- [-D_FORTIFY_SOURCE=3](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#fortify-sources-for-unsafe-libc-usage-and-buffer-overflows): Fortify sources with compile- and run-time checks for unsafe libc usage and buffer overflows.
 - Added in version 3.14. 

### 3.3.13. macOS Options[¶](#macos-options)

See [Mac/README.rst](https://github.com/python/cpython/tree/3.14/Mac/README.rst).

- 
--enable-universalsdk[¶](#cmdoption-enable-universalsdk)

- 
--enable-universalsdk=SDKDIR[¶](#cmdoption-0)
- Create a universal binary build. - *SDKDIR*specifies which macOS SDK should be used to perform the build (default is no).

- 
--enable-framework[¶](#cmdoption-enable-framework)

- 
--enable-framework=INSTALLDIR[¶](#cmdoption-1)
- Create a Python.framework rather than a traditional Unix install. Optional - *INSTALLDIR*specifies the installation path (default is no).

- 
--with-universal-archs=ARCH[¶](#cmdoption-with-universal-archs)
- Specify the kind of universal binary that should be created. This option is only valid when - `--enable-universalsdk`- Options: - `universal2`(x86-64 and arm64);
- `32-bit`(PPC and i386);
- `64-bit`(PPC64 and x86-64);
- `3-way`(i386, PPC and x86-64);
- `intel`(i386 and x86-64);
- `intel-32`(i386);
- `intel-64`(x86-64);
- `all`(PPC, i386, PPC64 and x86-64).
 - Note that values for this configuration item are - *not*the same as the identifiers used for universal binary wheels on macOS. See the Python Packaging User Guide for details on the- [packaging platform compatibility tags used on macOS](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/#macos)

- 
--with-framework-name=FRAMEWORK[¶](#cmdoption-with-framework-name)
- Specify the name for the python framework on macOS only valid when - `--enable-framework`- `Python`).

- 
--with-app-store-compliance[¶](#cmdoption-with-app-store-compliance)

- 
--with-app-store-compliance=PATCH-FILE[¶](#cmdoption-2)
- The Python standard library contains strings that are known to trigger automated inspection tool errors when submitted for distribution by the macOS and iOS App Stores. If enabled, this option will apply the list of patches that are known to correct app store compliance. A custom patch file can also be specified. This option is disabled by default. - Added in version 3.13. 

### 3.3.14. iOS Options[¶](#ios-options)

See [iOS/README.rst](https://github.com/python/cpython/tree/3.14/iOS/README.rst).

- 
--enable-framework=INSTALLDIR[¶](#cmdoption-3)
- Create a Python.framework. Unlike macOS, the - *INSTALLDIR*argument specifying the installation path is mandatory.

- 
--with-framework-name=FRAMEWORK[¶](#cmdoption-4)
- Specify the name for the framework (default: - `Python`).

### 3.3.15. Cross Compiling Options[¶](#cross-compiling-options)

Cross compiling, also known as cross building, can be used to build Python for another CPU architecture or platform. Cross compiling requires a Python interpreter for the build platform. The version of the build Python must match the version of the cross compiled host Python.

- 
--build=BUILD[¶](#cmdoption-build)
- configure for building on BUILD, usually guessed by - **config.guess**.

- 
--host=HOST[¶](#cmdoption-host)
- cross-compile to build programs to run on HOST (target platform) 

- 
--with-build-python=path/to/python[¶](#cmdoption-with-build-python)
- path to build - `python`binary for cross compiling- Added in version 3.11. 

- 
CONFIG_SITE=file[¶](#cmdoption-arg-CONFIG_SITE)
- An environment variable that points to a file with configure overrides. - Example - *config.site*file:- # config.site-aarch64 ac_cv_buggy_getaddrinfo=no ac_cv_file__dev_ptmx=yes ac_cv_file__dev_ptc=no 

- 
HOSTRUNNER[¶](#cmdoption-arg-HOSTRUNNER)
- Program to run CPython for the host platform for cross-compilation. - Added in version 3.11. 

Cross compiling example:

```
CONFIG_SITE=config.site-aarch64 ../configure \
    --build=x86_64-pc-linux-gnu \
    --host=aarch64-unknown-linux-gnu \
    --with-build-python=../x86_64/python
```
## 3.4. Python Build System[¶](#python-build-system)

### 3.4.1. Main files of the build system[¶](#main-files-of-the-build-system)

- `configure.ac`=>- `configure`;
- `Makefile.pre.in`=>- `Makefile`(created by- `configure`);
- `pyconfig.h`(created by- `configure`);
- `Modules/Setup`: C extensions built by the Makefile using- `Module/makesetup`shell script;

### 3.4.2. Main build steps[¶](#main-build-steps)

- C files ( - `.c`) are built as object files (- `.o`).
- A static - `libpython`library (- `.a`) is created from objects files.
- `python.o`and the static- `libpython`library are linked into the final- `python`program.
- C extensions are built by the Makefile (see - `Modules/Setup`).

### 3.4.3. Main Makefile targets[¶](#main-makefile-targets)

#### 3.4.3.1. make[¶](#make)

For the most part, when rebuilding after editing some code or
refreshing your checkout from upstream, all you need to do is execute
`make`, which (per Make’s semantics) builds the default target, the
first one defined in the Makefile.  By tradition (including in the
CPython project) this is usually the `all` target. The
`configure` script expands an `autoconf` variable,
`@DEF_MAKE_ALL_RULE@` to describe precisely which targets ```
make
all
```
 will build. The three choices are:

- `profile-opt`(configured with- `--enable-optimizations`)
- `build_wasm`(chosen if the host platform matches- `wasm32-wasi*`or- `wasm32-emscripten`)
- `build_all`(configured without explicitly using either of the others)

Depending on the most recent source file changes, Make will rebuild
any targets (object files and executables) deemed out-of-date,
including running `configure` again if necessary. Source/target
dependencies are many and maintained manually however, so Make
sometimes doesn’t have all the information necessary to correctly
detect all targets which need to be rebuilt.  Depending on which
targets aren’t rebuilt, you might experience a number of problems. If
you have build or test problems which you can’t otherwise explain,
`make clean && make` should work around most dependency problems, at
the expense of longer build times.

#### 3.4.3.2. make platform[¶](#make-platform)

Build the `python` program, but don’t build the standard library
extension modules. This generates a file named `platform` which
contains a single line describing the details of the build platform,
e.g., `macosx-14.3-arm64-3.12` or `linux-x86_64-3.13`.

#### 3.4.3.3. make profile-opt[¶](#make-profile-opt)

Build Python using profile-guided optimization (PGO).  You can use the
configure [ --enable-optimizations](#cmdoption-enable-optimizations) option to make this the
default target of the 

`make` command (`make all` or just
`make`).#### 3.4.3.4. make clean[¶](#make-clean)

Remove built files.

#### 3.4.3.5. make distclean[¶](#make-distclean)

In addition to the work done by `make clean`, remove files
created by the configure script.  `configure` will have to be run
before building again. [[6]](#id16)

#### 3.4.3.6. make install[¶](#make-install)

Build the `all` target and install Python.

#### 3.4.3.7. make test[¶](#make-test)

Build the `all` target and run the Python test suite with the
`--fast-ci` option without GUI tests. Variables:

- `TESTOPTS`: additional regrtest command-line options.
- `TESTPYTHONOPTS`: additional Python command-line options.
- `TESTTIMEOUT`: timeout in seconds (default: 10 minutes).

#### 3.4.3.8. make ci[¶](#make-ci)

This is similar to `make test`, but uses the `-ugui` to also run GUI tests.

Added in version 3.14.

#### 3.4.3.9. make buildbottest[¶](#make-buildbottest)

This is similar to `make test`, but uses the `--slow-ci`
option and default timeout of 20 minutes, instead of `--fast-ci` option.

#### 3.4.3.10. make regen-all[¶](#make-regen-all)

Regenerate (almost) all generated files. These include (but are not
limited to) bytecode cases, and parser generator file.
`make regen-stdlib-module-names` and `autoconf` must be run
separately for the remaining [generated files](#generated-files).

### 3.4.4. C extensions[¶](#c-extensions)

Some C extensions are built as built-in modules, like the `sys` module.
They are built with the `Py_BUILD_CORE_BUILTIN` macro defined.
Built-in modules have no `__file__` attribute:

```
>>> import sys
>>> sys
<module 'sys' (built-in)>
>>> sys.__file__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute '__file__'
```
Other C extensions are built as dynamic libraries, like the `_asyncio` module.
They are built with the `Py_BUILD_CORE_MODULE` macro defined.
Example on Linux x86-64:

```
>>> import _asyncio
>>> _asyncio
<module '_asyncio' from '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'>
>>> _asyncio.__file__
'/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'
```
`Modules/Setup` is used to generate Makefile targets to build C extensions.
At the beginning of the files, C extensions are built as built-in modules.
Extensions defined after the `*shared*` marker are built as dynamic libraries.

The `PyAPI_FUNC()`, `PyAPI_DATA()` and
[ PyMODINIT_FUNC](../c-api/extension-modules.html#c.PyMODINIT_FUNC) macros of 

`Include/exports.h` are defined
differently depending if the `Py_BUILD_CORE_MODULE` macro is defined:- Use - `Py_EXPORTED_SYMBOL`if the- `Py_BUILD_CORE_MODULE`is defined
- Use - `Py_IMPORTED_SYMBOL`otherwise.

If the `Py_BUILD_CORE_BUILTIN` macro is used by mistake on a C extension
built as a shared library, its `PyInit_` function is not exported,
causing an *xxx*()[ ImportError](../library/exceptions.html#ImportError) on import.

## 3.5. Compiler and linker flags[¶](#compiler-and-linker-flags)

Options set by the `./configure` script and environment variables and used by
`Makefile`.

### 3.5.1. Preprocessor flags[¶](#preprocessor-flags)

- 
CONFIGURE_CPPFLAGS[¶](#envvar-CONFIGURE_CPPFLAGS)
- Value of - `CPPFLAGS`- `./configure`script.- Added in version 3.6. 

- 
CPPFLAGS[¶](#envvar-CPPFLAGS)
- (Objective) C/C++ preprocessor flags, e.g. - `-I`if you have headers in a nonstandard directory- *include_dir*- *include_dir*.- Both - `CPPFLAGS`- `LDFLAGS`

- 
BASECPPFLAGS[¶](#envvar-BASECPPFLAGS)
- Added in version 3.4. 

- 
PY_CPPFLAGS[¶](#envvar-PY_CPPFLAGS)
- Extra preprocessor flags added for building the interpreter object files. - Default: - `$(BASECPPFLAGS) -I. -I$(srcdir)/Include $(CONFIGURE_CPPFLAGS) $(CPPFLAGS)`.- Added in version 3.2. 

### 3.5.2. Compiler flags[¶](#compiler-flags)

- 
CC[¶](#envvar-CC)
- C compiler command. - Example: - `gcc -pthread`.

- 
CXX[¶](#envvar-CXX)
- C++ compiler command. - Example: - `g++ -pthread`.

- 
CFLAGS[¶](#envvar-CFLAGS)
- C compiler flags. 

- 
CFLAGS_NODIST[¶](#envvar-CFLAGS_NODIST)
- `CFLAGS_NODIST`- *not*be part of- `CFLAGS`- [gh-65320](https://github.com/python/cpython/issues/65320)).- In particular, - `CFLAGS`- the compiler flag - `-I`(for setting the search path for include files). The- `-I`flags are processed from left to right, and any flags in- `CFLAGS`- `-I`flags.
- hardening flags such as - `-Werror`because distributions cannot control whether packages installed by users conform to such heightened standards.
 - Added in version 3.5. 

- 
COMPILEALL_OPTS[¶](#envvar-COMPILEALL_OPTS)
- Options passed to the - `compileall`- `make install`. Default:- `-j0`.- Added in version 3.12. 

- 
EXTRA_CFLAGS[¶](#envvar-EXTRA_CFLAGS)
- Extra C compiler flags. 

- 
CONFIGURE_CFLAGS_NODIST[¶](#envvar-CONFIGURE_CFLAGS_NODIST)
- Value of - `CFLAGS_NODIST`- `./configure`script.- Added in version 3.5. 

- 
BASECFLAGS[¶](#envvar-BASECFLAGS)
- Base compiler flags. 

- 
OPT[¶](#envvar-OPT)
- Optimization flags. 

- 
CFLAGS_ALIASING[¶](#envvar-CFLAGS_ALIASING)
- Strict or non-strict aliasing flags used to compile - `Python/dtoa.c`.- Added in version 3.7. 

- 
CFLAGS_CEVAL[¶](#envvar-CFLAGS_CEVAL)
- Flags used to compile - `Python/ceval.c`.- Added in version 3.14.5. 

- 
CCSHARED[¶](#envvar-CCSHARED)
- Compiler flags used to build a shared library. - For example, - `-fPIC`is used on Linux and on BSD.

- 
CFLAGSFORSHARED[¶](#envvar-CFLAGSFORSHARED)
- Extra C flags added for building the interpreter object files. - Default: - `$(CCSHARED)`when- `--enable-shared`

- 
PY_CFLAGS[¶](#envvar-PY_CFLAGS)
- Default: - `$(BASECFLAGS) $(OPT) $(CONFIGURE_CFLAGS) $(CFLAGS) $(EXTRA_CFLAGS)`.

- 
PY_CFLAGS_NODIST[¶](#envvar-PY_CFLAGS_NODIST)
- Default: - `$(CONFIGURE_CFLAGS_NODIST) $(CFLAGS_NODIST) -I$(srcdir)/Include/internal`.- Added in version 3.5. 

- 
PY_STDMODULE_CFLAGS[¶](#envvar-PY_STDMODULE_CFLAGS)
- C flags used for building the interpreter object files. - Default: - `$(PY_CFLAGS) $(PY_CFLAGS_NODIST) $(PY_CPPFLAGS) $(CFLAGSFORSHARED)`.- Added in version 3.7. 

- 
PY_CORE_CFLAGS[¶](#envvar-PY_CORE_CFLAGS)
- Default: - `$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE`.- Added in version 3.2. 

- 
PY_BUILTIN_MODULE_CFLAGS[¶](#envvar-PY_BUILTIN_MODULE_CFLAGS)
- Compiler flags to build a standard library extension module as a built-in module, like the - `posix`- Default: - `$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE_BUILTIN`.- Added in version 3.8. 

- 
PURIFY[¶](#envvar-PURIFY)
- Purify command. Purify is a memory debugger program. - Default: empty string (not used). 

### 3.5.3. Linker flags[¶](#linker-flags)

- 
LINKCC[¶](#envvar-LINKCC)
- Linker command used to build programs like - `python`and- `_testembed`.- Default: - `$(PURIFY) $(CC)`.

- 
CONFIGURE_LDFLAGS[¶](#envvar-CONFIGURE_LDFLAGS)
- Value of - `LDFLAGS`- `./configure`script.- Avoid assigning - `CFLAGS`- `LDFLAGS`- Added in version 3.2. 

- 
LDFLAGS_NODIST[¶](#envvar-LDFLAGS_NODIST)
- `LDFLAGS_NODIST`- `CFLAGS_NODIST`- *not*be part of- `LDFLAGS`- [gh-65320](https://github.com/python/cpython/issues/65320)).- In particular, - `LDFLAGS`- the compiler flag - `-L`(for setting the search path for libraries). The- `-L`flags are processed from left to right, and any flags in- `LDFLAGS`- `-L`flags.
 

- 
CONFIGURE_LDFLAGS_NODIST[¶](#envvar-CONFIGURE_LDFLAGS_NODIST)
- Value of - `LDFLAGS_NODIST`- `./configure`script.- Added in version 3.8. 

- 
LDFLAGS[¶](#envvar-LDFLAGS)
- Linker flags, e.g. - `-L`if you have libraries in a nonstandard directory- *lib_dir*- *lib_dir*.- Both - `CPPFLAGS`- `LDFLAGS`

- 
LIBS[¶](#envvar-LIBS)
- Linker flags to pass libraries to the linker when linking the Python executable. - Example: - `-lrt`.

- 
LDSHARED[¶](#envvar-LDSHARED)
- Command to build a shared library. - Default: - `@LDSHARED@ $(PY_LDFLAGS)`.

- 
BLDSHARED[¶](#envvar-BLDSHARED)
- Command to build - `libpython`shared library.- Default: - `@BLDSHARED@ $(PY_CORE_LDFLAGS)`.

- 
PY_LDFLAGS[¶](#envvar-PY_LDFLAGS)
- Default: - `$(CONFIGURE_LDFLAGS) $(LDFLAGS)`.

- 
PY_LDFLAGS_NODIST[¶](#envvar-PY_LDFLAGS_NODIST)
- Default: - `$(CONFIGURE_LDFLAGS_NODIST) $(LDFLAGS_NODIST)`.- Added in version 3.8. 

- 
PY_CORE_LDFLAGS[¶](#envvar-PY_CORE_LDFLAGS)
- Linker flags used for building the interpreter object files. - Added in version 3.8. 

Footnotes

[6](#id14)]

`git clean -fdx` is an even more extreme way to “clean” your
checkout. It removes all files not known to Git.
When bug hunting using `git bisect`, this is
[recommended between probes](https://github.com/python/cpython/issues/114505#issuecomment-1907021718)
to guarantee a completely clean build. **Use with care**, as it
will delete all files not checked into Git, including your
new, uncommitted work.