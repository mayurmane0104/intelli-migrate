# imp — Access the import internals — Python 3.11.15 documentation

**Source:** [https://docs.python.org/3.11/library/imp.html](https://docs.python.org/3.11/library/imp.html)

---

`imp`[import](../reference/import.html#importsystem) internals[¶](#module-imp)

`imp`**Source code:** [Lib/imp.py](https://github.com/python/cpython/tree/3.11/Lib/imp.py)

Deprecated since version 3.4, will be removed in version 3.12: The [ imp](#module-imp) module is deprecated in favor of 

[.](importlib.html#module-importlib)

`importlib`This module provides an interface to the mechanisms used to implement the
[ import](../reference/simple_stmts.html#import) statement.  It defines the following constants and functions:

- 
imp.get_magic()[¶](#imp.get_magic)
- Return the magic string value used to recognize byte-compiled code files ( - `.pyc`files). (This value may be different for each Python version.)- Deprecated since version 3.4: Use - `importlib.util.MAGIC_NUMBER`

- 
imp.get_suffixes()[¶](#imp.get_suffixes)
- Return a list of 3-element tuples, each describing a particular type of module. Each triple has the form - `(suffix, mode, type)`, where- *suffix*is a string to be appended to the module name to form the filename to search for,- *mode*is the mode string to pass to the built-in- `open()`- `'r'`for text files or- `'rb'`for binary files), and- *type*is the file type, which has one of the values- `PY_SOURCE`- `PY_COMPILED`- `C_EXTENSION`- Deprecated since version 3.3: Use the constants defined on - `importlib.machinery`

- 
imp.find_module(*name*[,*path*])[¶](#imp.find_module)
- Try to find the module - *name*. If- *path*is omitted or- `None`, the list of directory names given by- `sys.path`is searched, but first a few special places are searched: the function tries to find a built-in module with the given name (- `C_BUILTIN`- `PY_FROZEN`- Otherwise, - *path*must be a list of directory names; each directory is searched for files with any of the suffixes returned by- `get_suffixes()`- If search is successful, the return value is a 3-element tuple - `(file, pathname, description)`:- *file*is an open- [file object](../glossary.html#term-file-object)positioned at the beginning,- *pathname*is the pathname of the file found, and- *description*is a 3-element tuple as contained in the list returned by- `get_suffixes()`- If the module is built-in or frozen then - *file*and- *pathname*are both- `None`and the- *description*tuple contains empty strings for its suffix and mode; the module type is indicated as given in parentheses above. If the search is unsuccessful,- `ImportError`- If the module is a package, - *file*is- `None`,- *pathname*is the package path and the last item in the- *description*tuple is- `PKG_DIRECTORY`- This function does not handle hierarchical module names (names containing dots). In order to find - *P.M*, that is, submodule- *M*of package- *P*, use- `find_module()`- `load_module()`- *P*, and then use- `find_module()`- *path*argument set to- `P.__path__`. When- *P*itself has a dotted name, apply this recipe recursively.- Deprecated since version 3.3: Use - `importlib.util.find_spec()`- `importlib.find_loader()`- [Examples](importlib.html#importlib-examples)section of the- `importlib`

- 
imp.load_module(*name*,*file*,*pathname*,*description*)[¶](#imp.load_module)
- Load a module that was previously found by - `find_module()`- *name*argument indicates the full module name (including the package name, if this is a submodule of a package). The- *file*argument is an open file, and- *pathname*is the corresponding file name; these can be- `None`and- `''`, respectively, when the module is a package or not being loaded from a file. The- *description*argument is a tuple, as would be returned by- `get_suffixes()`- If the load is successful, the return value is the module object; otherwise, an exception (usually - `ImportError`- **Important:**the caller is responsible for closing the- *file*argument, if it was not- `None`, even when an exception is raised. This is best done using a- `try`- `finally`- Deprecated since version 3.3: If previously used in conjunction with - `imp.find_module()`- `importlib.import_module()`- `imp.find_module()`- `imp.load_module()`- `importlib.util.spec_from_file_location()`- `importlib.util.module_from_spec()`- [Examples](importlib.html#importlib-examples)section of the- `importlib`

- 
imp.new_module(*name*)[¶](#imp.new_module)
- Return a new empty module object called - *name*. This object is- *not*inserted in- `sys.modules`.- Deprecated since version 3.4: Use - `importlib.util.module_from_spec()`

- 
imp.reload(*module*)[¶](#imp.reload)
- Reload a previously imported - *module*. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (the same as the- *module*argument).- When - `reload(module)`is executed:- Python modules’ code is recompiled and the module-level code reexecuted, defining a new set of objects which are bound to names in the module’s dictionary. The - `init`function of extension modules is not called a second time.
- As with all other objects in Python the old objects are only reclaimed after their reference counts drop to zero. 
- The names in the module namespace are updated to point to any new or changed objects. 
- Other references to the old objects (such as names external to the module) are not rebound to refer to the new objects and must be updated in each namespace where they occur if that is desired. 
 - There are a number of other caveats: - When a module is reloaded, its dictionary (containing the module’s global variables) is retained. Redefinitions of names will override the old definitions, so this is generally not a problem. If the new version of a module does not define a name that was defined by the old version, the old definition remains. This feature can be used to the module’s advantage if it maintains a global table or cache of objects — with a - `try`- try: cache except NameError: cache = {} - It is legal though generally not very useful to reload built-in or dynamically loaded modules, except for - `sys`- `__main__`- `builtins`- If a module imports objects from another module using - `from`- `import`- `reload()`- `from`statement, another is to use- `import`and qualified names (- *module*.*name*) instead.- If a module instantiates instances of a class, reloading the module that defines the class does not affect the method definitions of the instances — they continue to use the old class definition. The same is true for derived classes. - Changed in version 3.3: Relies on both - `__name__`and- `__loader__`being defined on the module being reloaded instead of just- `__name__`.- Deprecated since version 3.4: Use - `importlib.reload()`

The following functions are conveniences for handling [ PEP 3147](https://peps.python.org/pep-3147/) byte-compiled
file paths.

New in version 3.2.

- 
imp.cache_from_source(*path*,*debug_override=None*)[¶](#imp.cache_from_source)
- Return the - **PEP 3147**- *path*. For example, if- *path*is- `/foo/bar/baz.py`the return value would be- `/foo/bar/__pycache__/baz.cpython-32.pyc`for Python 3.2. The- `cpython-32`string comes from the current magic tag (see- `get_tag()`- `sys.implementation.cache_tag`is not defined then- `NotImplementedError`- `True`or- `False`for- *debug_override*you can override the system’s value for- `__debug__`, leading to optimized bytecode.- *path*need not exist.- Changed in version 3.3: If - `sys.implementation.cache_tag`is- `None`, then- `NotImplementedError`- Deprecated since version 3.4: Use - `importlib.util.cache_from_source()`- Changed in version 3.5: The - *debug_override*parameter no longer creates a- `.pyo`file.

- 
imp.source_from_cache(*path*)[¶](#imp.source_from_cache)
- Given the - *path*to a- **PEP 3147**- *path*is- `/foo/bar/__pycache__/baz.cpython-32.pyc`the returned path would be- `/foo/bar/baz.py`.- *path*need not exist, however if it does not conform to- **PEP 3147**- `ValueError`- `sys.implementation.cache_tag`is not defined,- `NotImplementedError`- Changed in version 3.3: Raise - `NotImplementedError`- `sys.implementation.cache_tag`is not defined.- Deprecated since version 3.4: Use - `importlib.util.source_from_cache()`

- 
imp.get_tag()[¶](#imp.get_tag)
- Return the - **PEP 3147**- `get_magic()`- Deprecated since version 3.4: Use - `sys.implementation.cache_tag`directly starting in Python 3.3.

The following functions help interact with the import system’s internal locking mechanism. Locking semantics of imports are an implementation detail which may vary from release to release. However, Python ensures that circular imports work without any deadlocks.

- 
imp.lock_held()[¶](#imp.lock_held)
- Return - `True`if the global import lock is currently held, else- `False`. On platforms without threads, always return- `False`.- On platforms with threads, a thread executing an import first holds a global import lock, then sets up a per-module lock for the rest of the import. This blocks other threads from importing the same module until the original import completes, preventing other threads from seeing incomplete module objects constructed by the original thread. An exception is made for circular imports, which by construction have to expose an incomplete module object at some point. - Changed in version 3.3: The locking scheme has changed to per-module locks for the most part. A global import lock is kept for some critical tasks, such as initializing the per-module locks. - Deprecated since version 3.4. 

- 
imp.acquire_lock()[¶](#imp.acquire_lock)
- Acquire the interpreter’s global import lock for the current thread. This lock should be used by import hooks to ensure thread-safety when importing modules. - Once a thread has acquired the import lock, the same thread may acquire it again without blocking; the thread must release it once for each time it has acquired it. - On platforms without threads, this function does nothing. - Changed in version 3.3: The locking scheme has changed to per-module locks for the most part. A global import lock is kept for some critical tasks, such as initializing the per-module locks. - Deprecated since version 3.4. 

- 
imp.release_lock()[¶](#imp.release_lock)
- Release the interpreter’s global import lock. On platforms without threads, this function does nothing. - Changed in version 3.3: The locking scheme has changed to per-module locks for the most part. A global import lock is kept for some critical tasks, such as initializing the per-module locks. - Deprecated since version 3.4. 

The following constants with integer values, defined in this module, are used
to indicate the search result of [ find_module()](#imp.find_module).

- 
imp.PY_SOURCE[¶](#imp.PY_SOURCE)
- The module was found as a source file. - Deprecated since version 3.3. 

- 
imp.PY_COMPILED[¶](#imp.PY_COMPILED)
- The module was found as a compiled code object file. - Deprecated since version 3.3. 

- 
imp.C_EXTENSION[¶](#imp.C_EXTENSION)
- The module was found as dynamically loadable shared library. - Deprecated since version 3.3. 

- 
imp.PKG_DIRECTORY[¶](#imp.PKG_DIRECTORY)
- The module was found as a package directory. - Deprecated since version 3.3. 

- 
imp.C_BUILTIN[¶](#imp.C_BUILTIN)
- The module was found as a built-in module. - Deprecated since version 3.3. 

- 
imp.PY_FROZEN[¶](#imp.PY_FROZEN)
- The module was found as a frozen module. - Deprecated since version 3.3. 

- 
*class*imp.NullImporter(*path_string*)[¶](#imp.NullImporter)
- The - `NullImporter`- **PEP 302**- `ImportError`- `NullImporter`- Instances have only one method: - 
find_module(*fullname*[,*path*])[¶](#imp.NullImporter.find_module)
- This method always returns - `None`, indicating that the requested module could not be found.
 - Changed in version 3.3: - `None`is inserted into- `sys.path_importer_cache`instead of an instance of- `NullImporter`- Deprecated since version 3.4: Insert - `None`into- `sys.path_importer_cache`instead.
- 
find_module(

## Examples[¶](#examples)

The following function emulates what was the standard import statement up to
Python 1.4 (no hierarchical module names).  (This *implementation* wouldn’t work
in that version, since [ find_module()](#imp.find_module) has been extended and

[has been added in 1.4.)](#imp.load_module)

`load_module()````
import imp
import sys
def __import__(name, globals=None, locals=None, fromlist=None):
    # Fast path: see if the module has already been imported.
    try:
        return sys.modules[name]
    except KeyError:
        pass
    # If any of the following calls raises an exception,
    # there's a problem we can't handle -- let the caller handle it.
    fp, pathname, description = imp.find_module(name)
    try:
        return imp.load_module(name, fp, pathname, description)
    finally:
        # Since we may exit via an exception, close fp explicitly.
        if fp:
            fp.close()
```