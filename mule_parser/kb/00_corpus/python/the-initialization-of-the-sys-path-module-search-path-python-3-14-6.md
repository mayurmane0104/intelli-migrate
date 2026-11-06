# The initialization of the sys.path module search path — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/sys_path_init.html](https://docs.python.org/library/sys_path_init.html)

---

# The initialization of the `sys.path`[¶](#the-initialization-of-the-sys-path-module-search-path)

`sys.path`A module search path is initialized when Python starts. This module search path
may be accessed at [ sys.path](sys.html#sys.path).

The first entry in the module search path is the directory that contains the
input script, if there is one. Otherwise, the first entry is the current
directory, which is the case when executing the interactive shell, a [ -c](../using/cmdline.html#cmdoption-c)
command, or 

[module.](../using/cmdline.html#cmdoption-m)

`-m`The [ PYTHONPATH](../using/cmdline.html#envvar-PYTHONPATH) environment variable is often used to add directories
to the search path. If this environment variable is found then the contents are
added to the module search path.

Note

[ PYTHONPATH](../using/cmdline.html#envvar-PYTHONPATH) will affect all installed Python versions/environments.
Be wary of setting this in your shell profile or global environment variables.
The 

[module offers more nuanced techniques as mentioned below.](site.html#module-site)

`site`The next items added are the directories containing standard Python modules as
well as any [extension module](../glossary.html#term-extension-module)s that these modules depend on. Extension
modules are `.pyd` files on Windows and `.so` files on other platforms. The
directory with the platform-independent Python modules is called `prefix`.
The directory with the extension modules is called `exec_prefix`.

The [ PYTHONHOME](../using/cmdline.html#envvar-PYTHONHOME) environment variable may be used to set the 

`prefix`
and `exec_prefix` locations. Otherwise these directories are found by using
the Python executable as a starting point and then looking for various ‘landmark’
files and directories. Note that any symbolic links are followed so the real
Python executable location is used as the search starting point. The Python
executable location is called `home`.Once `home` is determined, the `prefix` directory is found by first looking
for `python` (*majorversion**minorversion*.zip`python311.zip`). On Windows
the zip archive is searched for in `home` and on Unix the archive is expected
to be in `lib`. Note that the expected zip archive location is added to the
module search path even if the archive does not exist. If no archive was found,
Python on Windows will continue the search for `prefix` by looking for `Lib\os.py`.
Python on Unix will look for `lib/python`
(*majorversion*.*minorversion*/os.py`lib/python3.11/os.py`). On Windows `prefix` and `exec_prefix` are the same,
however on other platforms `lib/python`
(*majorversion*.*minorversion*/lib-dynload`lib/python3.11/lib-dynload`) is searched for and used as an anchor for
`exec_prefix`. On some platforms `lib` may be `lib64` or another value,
see [ sys.platlibdir](sys.html#sys.platlibdir) and 

[.](../using/cmdline.html#envvar-PYTHONPLATLIBDIR)

`PYTHONPLATLIBDIR`Once found, `prefix` and `exec_prefix` are available at
[ sys.base_prefix](sys.html#sys.base_prefix) and 

[respectively.](sys.html#sys.base_exec_prefix)

`sys.base_exec_prefix`If [ PYTHONHOME](../using/cmdline.html#envvar-PYTHONHOME) is not set, and a 

`pyvenv.cfg` file is found alongside
the main executable, or in its parent directory, [and](sys.html#sys.prefix)

`sys.prefix`[get set to the directory containing](sys.html#sys.exec_prefix)

`sys.exec_prefix``pyvenv.cfg`,
otherwise they are set to the same value as [and](sys.html#sys.base_prefix)

`sys.base_prefix`[, respectively. This is used by](sys.html#sys.base_exec_prefix)

`sys.base_exec_prefix`[Virtual Environments](#sys-path-init-virtual-environments).

Finally, the [ site](site.html#module-site) module is processed and 

`site-packages` directories
are added to the module search path. A common way to customize the search path is
to create [or](site.html#module-sitecustomize)

`sitecustomize`[modules as described in the](site.html#module-usercustomize)

`usercustomize``site` module documentation.Note

Certain command line options may further affect path calculations.
See [ -E](../using/cmdline.html#cmdoption-E), 

[,](../using/cmdline.html#cmdoption-I)

`-I`[and](../using/cmdline.html#cmdoption-s)

`-s`[for further details.](../using/cmdline.html#cmdoption-S)

`-S`Changed in version 3.14: [ sys.prefix](sys.html#sys.prefix) and 

[are now set to the](sys.html#sys.exec_prefix)

`sys.exec_prefix``pyvenv.cfg` directory during the path initialization. This was previously
done by [, therefore affected by](site.html#module-site)

`site`[.](../using/cmdline.html#cmdoption-S)

`-S`## Virtual Environments[¶](#virtual-environments)

Virtual environments place a `pyvenv.cfg` file in their prefix, which causes
[ sys.prefix](sys.html#sys.prefix) and 

[to point to them, instead of the base installation.](sys.html#sys.exec_prefix)

`sys.exec_prefix`The `prefix` and `exec_prefix` values of the base installation are available
at [ sys.base_prefix](sys.html#sys.base_prefix) and 

[.](sys.html#sys.base_exec_prefix)

`sys.base_exec_prefix`As well as being used as a marker to identify virtual environments,
`pyvenv.cfg` may also be used to configure the [ site](site.html#module-site) initialization.
Please refer to 

`site`’s
[virtual environments documentation](site.html#site-virtual-environments-configuration).

Note

[ PYTHONHOME](../using/cmdline.html#envvar-PYTHONHOME) overrides the 

`pyvenv.cfg` detection.Note

There are other ways how “virtual environments” could be implemented, this
documentation refers implementations based on the `pyvenv.cfg` mechanism,
such as [ venv](venv.html#module-venv). Most virtual environment implementations follow the
model set by 

`venv`, but there may be exotic implementations that
diverge from it.## _pth files[¶](#pth-files)

To completely override [ sys.path](sys.html#sys.path) create a 

`._pth` file with the same
name as the shared library or executable (`python._pth` or `python311._pth`).
The shared library path is always known on Windows, however it may not be
available on other platforms. In the `._pth` file specify one line for each path
to add to `sys.path`. The file based on the shared library name overrides
the one based on the executable, which allows paths to be restricted for any
program loading the runtime if desired.When the file exists, all registry and environment variables are ignored,
isolated mode is enabled, and [ site](site.html#module-site) is not imported unless one line in the
file specifies 

`import site`. Blank paths and lines starting with `#` are
ignored. Each path may be absolute or relative to the location of the file.
Import statements other than to `site` are not permitted, and arbitrary code
cannot be specified.Note that `.pth` files (without leading underscore) will be processed normally
by the [ site](site.html#module-site) module when 

`import site` has been specified.## Embedded Python[¶](#embedded-python)

If Python is embedded within another application [ Py_InitializeFromConfig()](../c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) and
the 

[structure can be used to initialize Python. The path specific details are described at](../c-api/init_config.html#c.PyConfig)

`PyConfig`[Python Path Configuration](../c-api/init_config.html#init-path-config).

See also

- [Finding modules](../using/windows.html#windows-finding-modules)for detailed Windows notes.
- [Using Python on Unix platforms](../using/unix.html#using-on-unix)for Unix details.