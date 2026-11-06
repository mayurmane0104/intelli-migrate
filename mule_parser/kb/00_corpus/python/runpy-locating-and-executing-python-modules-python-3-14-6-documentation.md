# runpy — Locating and executing Python modules — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/runpy.html](https://docs.python.org/library/runpy.html)

---

`runpy` — Locating and executing Python modules[¶](#module-runpy)

**Source code:** [Lib/runpy.py](https://github.com/python/cpython/tree/3.14/Lib/runpy.py)

The `runpy` module is used to locate and run Python modules without
importing them first. Its main use is to implement the [ -m](../using/cmdline.html#cmdoption-m) command
line switch that allows scripts to be located using the Python module
namespace rather than the filesystem.

Note that this is *not* a sandbox module - all code is executed in the
current process, and any side effects (such as cached imports of other
modules) will remain in place after the functions have returned.

Furthermore, any functions and classes defined by the executed code are not
guaranteed to work correctly after a `runpy` function has returned.
If that limitation is not acceptable for a given use case, [ importlib](importlib.html#module-importlib)
is likely to be a more suitable choice than this module.

The `runpy` module provides two functions:

- 
runpy.run_module(*mod_name*,*init_globals=None*,*run_name=None*,*alter_sys=False*)[¶](#runpy.run_module)
- Execute the code of the specified module and return the resulting module’s globals dictionary. The module’s code is first located using the standard import mechanism (refer to - **PEP 302**- The - *mod_name*argument should be an absolute module name. If the module name refers to a package rather than a normal module, then that package is imported and the- `__main__`- The optional dictionary argument - *init_globals*may be used to pre-populate the module’s globals dictionary before the code is executed.- *init_globals*will not be modified. If any of the special global variables below are defined in- *init_globals*, those definitions are overridden by- `run_module()`.- The special global variables - `__name__`,- `__spec__`,- `__file__`,- `__cached__`,- `__loader__`and- `__package__`are set in the globals dictionary before the module code is executed. (Note that this is a minimal set of variables - other variables may be set implicitly as an interpreter implementation detail.)- `__name__`is set to- *run_name*if this optional argument is not- `None`- `mod_name + '.__main__'`if the named module is a package and to the- *mod_name*argument otherwise.- `__spec__`will be set appropriately for the- *actually*imported module (that is,- `__spec__.name`will always be- *mod_name*or- `mod_name + '.__main__'`, never- *run_name*).- `__file__`,- `__cached__`,- `__loader__`and- `__package__`are- [set as normal](../reference/datamodel.html#import-mod-attrs)based on the module spec.- If the argument - *alter_sys*is supplied and evaluates to- `True`- `sys.argv[0]`is updated with the value of- `__file__`and- `sys.modules[__name__]`is updated with a temporary module object for the module being executed. Both- `sys.argv[0]`and- `sys.modules[__name__]`are restored to their original values before the function returns.- Note that this manipulation of - `sys`- `sys`module be left alone when invoking this function from threaded code.- See also - The - `-m`- Changed in version 3.1: Added ability to execute packages by looking for a - `__main__`- Changed in version 3.2: Added - `__cached__`global variable (see- **PEP 3147**- Changed in version 3.4: Updated to take advantage of the module spec feature added by - **PEP 451**- `__cached__`to be set correctly for modules run this way, as well as ensuring the real module name is always accessible as- `__spec__.name`.- Changed in version 3.12: The setting of - `__cached__`,- `__loader__`, and- `__package__`are deprecated. See- `ModuleSpec`

- 
runpy.run_path(*path_name*,*init_globals=None*,*run_name=None*)[¶](#runpy.run_path)
- Execute the code at the named filesystem location and return the resulting module’s globals dictionary. As with a script name supplied to the CPython command line, - *file_path*may refer to a Python source file, a compiled bytecode file or a valid- `sys.path`- `__main__`- `__main__.py`file).- For a simple script, the specified code is simply executed in a fresh module namespace. For a valid - `sys.path`- `sys.path`. The function then looks for and executes a- `__main__`- `__main__`entry located elsewhere on- `sys.path`if there is no such module at the specified location.- The optional dictionary argument - *init_globals*may be used to pre-populate the module’s globals dictionary before the code is executed.- *init_globals*will not be modified. If any of the special global variables below are defined in- *init_globals*, those definitions are overridden by- `run_path()`.- The special global variables - `__name__`,- `__spec__`,- `__file__`,- `__cached__`,- `__loader__`and- `__package__`are set in the globals dictionary before the module code is executed. (Note that this is a minimal set of variables - other variables may be set implicitly as an interpreter implementation detail.)- `__name__`is set to- *run_name*if this optional argument is not- `None`- `'<run_path>'`otherwise.- If - *file_path*directly references a script file (whether as source or as precompiled byte code), then- `__file__`will be set to- *file_path*, and- `__spec__`,- `__cached__`,- `__loader__`and- `__package__`will all be set to- `None`- If - *file_path*is a reference to a valid- `sys.path`- `__spec__`will be set appropriately for the imported- `__main__`- `__spec__.name`will always be- `__main__`).- `__file__`,- `__cached__`,- `__loader__`and- `__package__`will be- [set as normal](../reference/datamodel.html#import-mod-attrs)based on the module spec.- A number of alterations are also made to the - `sys`- `sys.path`- `sys.argv[0]`is updated with the value of- *file_path*and- `sys.modules[__name__]`is updated with a temporary module object for the module being executed. All modifications to items in- `sys`are reverted before the function returns.- Note that, unlike - `run_module()`- `sys`- `sys.path`- See also - [Interface options](../using/cmdline.html#using-on-interface-options)for equivalent functionality on the command line (- `python path/to/script`).- Added in version 3.2. - Changed in version 3.4: Updated to take advantage of the module spec feature added by - **PEP 451**- `__cached__`to be set correctly in the case where- `__main__`is imported from a valid- `sys.path`- Changed in version 3.12: The setting of - `__cached__`,- `__loader__`, and- `__package__`are deprecated.

See also

- **PEP 338**
- PEP written and implemented by Nick Coghlan. 
- **PEP 366**
- PEP written and implemented by Nick Coghlan. 
- **PEP 451**
- PEP written and implemented by Eric Snow 

[Command line and environment](../using/cmdline.html#using-on-general) - CPython command line details

The [ importlib.import_module()](importlib.html#importlib.import_module) function