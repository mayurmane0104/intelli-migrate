# site — Site-specific configuration hook — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/site.html](https://docs.python.org/library/site.html)

---

`site` — Site-specific configuration hook[¶](#module-site)

**Source code:** [Lib/site.py](https://github.com/python/cpython/tree/3.14/Lib/site.py)

**This module is automatically imported during initialization.** The automatic
import can be suppressed using the interpreter’s [ -S](../using/cmdline.html#cmdoption-S) option.

Importing this module normally appends site-specific paths to the module search path
and adds [callables](constants.html#site-consts), including [ help()](functions.html#help) to the built-in
namespace. However, Python startup option 

[blocks this and this module can be safely imported with no automatic modifications to the module search path or additions to the builtins. To explicitly trigger the usual site-specific additions, call the](../using/cmdline.html#cmdoption-S)

`-S`[function.](#site.main)

`main()`Changed in version 3.3: Importing the module used to trigger paths manipulation even when using
[ -S](../using/cmdline.html#cmdoption-S).

It starts by constructing up to four directories from a head and a tail part.
For the head part, it uses `sys.prefix` and `sys.exec_prefix`; empty heads
are skipped.  For the tail part, it uses the empty string and then
`lib/site-packages` (on Windows) or
`lib/python` (on Unix and macOS). (The
optional suffix “t” indicates the *X.Y[t]*/site-packages[free-threaded build](../glossary.html#term-free-threaded-build), and is
appended if `"t"` is present in the [ sys.abiflags](sys.html#sys.abiflags) constant.)
For each
of the distinct head-tail combinations, it sees if it refers to an existing
directory, and if so, adds it to 

`sys.path` and also inspects the newly
added path for configuration files.Changed in version 3.5: Support for the “site-python” directory has been removed.

Changed in version 3.13: On Unix, [Free threading](../glossary.html#term-free-threading) Python installations are
identified by the “t” suffix in the version-specific directory name, such as
`lib/python3.13t/`.

Changed in version 3.14: `site` is no longer responsible for updating [ sys.prefix](sys.html#sys.prefix) and

[on](sys.html#sys.exec_prefix)

`sys.exec_prefix`[Virtual Environments](sys_path_init.html#sys-path-init-virtual-environments). This is now done during the

[path initialization](sys_path_init.html#sys-path-init). As a result, under

[Virtual Environments](sys_path_init.html#sys-path-init-virtual-environments),

`sys.prefix` and
`sys.exec_prefix` no longer depend on the `site` initialization,
and are therefore unaffected by [.](../using/cmdline.html#cmdoption-S)

`-S`When running under a [virtual environment](sys_path_init.html#sys-path-init-virtual-environments),
the `pyvenv.cfg` file in [ sys.prefix](sys.html#sys.prefix) is checked for site-specific
configurations. If the 

`include-system-site-packages` key exists and is set to
`true` (case-insensitive), the system-level prefixes will be searched for
site-packages, otherwise they won’t.A path configuration file is a file whose name has the form *name*.pth`sys.path`.  Non-existing items
are never added to `sys.path`, and no check is made that the item refers to a
directory rather than a file.  No item is added to `sys.path` more than
once.  Blank lines and lines beginning with `#` are skipped.  Lines starting
with `import` (followed by space or tab) are executed.

Note

An executable line in a `.pth` file is run at every Python startup,
regardless of whether a particular module is actually going to be used.
Its impact should thus be kept to a minimum.
The primary intended purpose of executable lines is to make the
corresponding module(s) importable
(load 3rd-party import hooks, adjust `PATH` etc).
Any other initialization is supposed to be done upon a module’s
actual import, if and when it happens.
Limiting a code chunk to a single line is a deliberate measure
to discourage putting anything more complex here.

Changed in version 3.13: The `.pth` files are now decoded by UTF-8 at first and then by the
[locale encoding](../glossary.html#term-locale-encoding) if it fails.

For example, suppose `sys.prefix` and `sys.exec_prefix` are set to
`/usr/local`.  The Python X.Y library is then installed in
`/usr/local/lib/python`.  Suppose this has
a subdirectory *X.Y*`/usr/local/lib/python` with three
subsubdirectories, *X.Y*/site-packages`foo`, `bar` and `spam`, and two path
configuration files, `foo.pth` and `bar.pth`.  Assume
`foo.pth` contains the following:

```
# foo package configuration
foo
bar
bletch
```
and `bar.pth` contains:

```
# bar package configuration
bar
```
Then the following version-specific directories are added to
`sys.path`, in this order:

```
/usr/local/lib/pythonX.Y/site-packages/bar
/usr/local/lib/pythonX.Y/site-packages/foo
```
Note that `bletch` is omitted because it doesn’t exist; the `bar`
directory precedes the `foo` directory because `bar.pth` comes
alphabetically before `foo.pth`; and `spam` is omitted because it is
not mentioned in either path configuration file.

`sitecustomize`[¶](#module-sitecustomize)

After these path manipulations, an attempt is made to import a module named
`sitecustomize`, which can perform arbitrary site-specific customizations.
It is typically created by a system administrator in the site-packages
directory.  If this import fails with an [ ImportError](exceptions.html#ImportError) or its subclass
exception, and the exception’s 

[attribute equals](exceptions.html#ImportError.name)

`name``'sitecustomize'`,
it is silently ignored.  If Python is started without output streams available, as
with `pythonw.exe` on Windows (which is used by default to start IDLE),
attempted output from `sitecustomize` is ignored.  Any other exception
causes a silent and perhaps mysterious failure of the process.`usercustomize`[¶](#module-usercustomize)

After this, an attempt is made to import a module named `usercustomize`,
which can perform arbitrary user-specific customizations, if
[ ENABLE_USER_SITE](#site.ENABLE_USER_SITE) is true.  This file is intended to be created in the
user site-packages directory (see below), which is part of 

`sys.path` unless
disabled by [. If this import fails with an](../using/cmdline.html#cmdoption-s)

`-s`[or its subclass exception, and the exception’s](exceptions.html#ImportError)

`ImportError`[attribute equals](exceptions.html#ImportError.name)

`name``'usercustomize'`, it is silently ignored.Note that for some non-Unix systems, `sys.prefix` and `sys.exec_prefix` are
empty, and the path manipulations are skipped; however the import of
[ sitecustomize](#module-sitecustomize) and 

`usercustomize` is still attempted.## Readline configuration[¶](#readline-configuration)

On systems that support [ readline](readline.html#module-readline), this module will also import and
configure the 

[module, if Python is started in](rlcompleter.html#module-rlcompleter)

`rlcompleter`[interactive mode](../tutorial/interpreter.html#tut-interactive)and without the

[option. The default behavior is to enable tab completion and to use](../using/cmdline.html#cmdoption-S)

`-S``~/.python_history` as the history save file.  To disable it, delete (or
override) the [attribute in your](sys.html#sys.__interactivehook__)

`sys.__interactivehook__`[or](#module-sitecustomize)

`sitecustomize`[module or your](#module-usercustomize)

`usercustomize`[file.](../using/cmdline.html#envvar-PYTHONSTARTUP)

`PYTHONSTARTUP`Changed in version 3.4: Activation of rlcompleter and history was made automatic.

## Module contents[¶](#module-contents)

- 
site.PREFIXES[¶](#site.PREFIXES)
- A list of prefixes for site-packages directories. 

- 
site.ENABLE_USER_SITE[¶](#site.ENABLE_USER_SITE)
- Flag showing the status of the user site-packages directory. - `True`means that it is enabled and was added to- `sys.path`.- `False`means that it was disabled by user request (with- `-s`- `PYTHONNOUSERSITE`- `None`means it was disabled for security reasons (mismatch between user or group id and effective id) or by an administrator.

- 
site.USER_SITE[¶](#site.USER_SITE)
- Path to the user site-packages for the running Python. Can be - `None`if- `getusersitepackages()`- `~/.local/lib/python`for UNIX and non-framework macOS builds,- *X.Y*[t]/site-packages- `~/Library/Python/`for macOS framework builds, and- *X.Y*/lib/python/site-packages- *%APPDATA%*\Python\Python- *XY*\site-packages- `.pth`files in it will be processed.

- 
site.USER_BASE[¶](#site.USER_BASE)
- Path to the base directory for the user site-packages. Can be - `None`if- `getuserbase()`- `~/.local`for UNIX and macOS non-framework builds,- `~/Library/Python/`for macOS framework builds, and- *X.Y*- *%APPDATA%*\Python- [user installation scheme](sysconfig.html#sysconfig-user-scheme). See also- `PYTHONUSERBASE`

- 
site.main()[¶](#site.main)
- Adds all the standard site-specific directories to the module search path. This function is called automatically when this module is imported, unless the Python interpreter was started with the - `-S`- Changed in version 3.3: This function used to be called unconditionally. 

- 
site.addsitedir(*sitedir*,*known_paths=None*)[¶](#site.addsitedir)
- Add a directory to sys.path and process its - `.pth`files. Typically used in- `sitecustomize`- `usercustomize`

- 
site.getsitepackages()[¶](#site.getsitepackages)
- Return a list containing all global site-packages directories. - Added in version 3.2. 

- 
site.getuserbase()[¶](#site.getuserbase)
- Return the path of the user base directory, - `USER_BASE`- `PYTHONUSERBASE`- Added in version 3.2. 

- 
site.getusersitepackages()[¶](#site.getusersitepackages)
- Return the path of the user-specific site-packages directory, - `USER_SITE`- `USER_BASE`- `sys.path`- `ENABLE_USER_SITE`- Added in version 3.2. 

## Command-line interface[¶](#command-line-interface)

The `site` module also provides a way to get the user directories from the
command line:

```
$ python -m site --user-site
/home/user/.local/lib/python3.11/site-packages
```
If it is called without arguments, it will print the contents of
[ sys.path](sys.html#sys.path) on the standard output, followed by the value of

[and whether the directory exists, then the same thing for](#site.USER_BASE)

`USER_BASE`[, and finally the value of](#site.USER_SITE)

`USER_SITE`[.](#site.ENABLE_USER_SITE)

`ENABLE_USER_SITE`- 
--user-base[¶](#cmdoption-site-user-base)
- Print the path to the user base directory. 

- 
--user-site[¶](#cmdoption-site-user-site)
- Print the path to the user site-packages directory. 

If both options are given, user base and user site will be printed (always in
this order), separated by [ os.pathsep](os.html#os.pathsep).

If any option is given, the script will exit with one of these values: `0` if
the user site-packages directory is enabled, `1` if it was disabled by the
user, `2` if it is disabled for security reasons or by an administrator, and a
value greater than 2 if there is an error.

See also

- **PEP 370**
- [The initialization of the sys.path module search path](sys_path_init.html#sys-path-init)– The initialization of- `sys.path`