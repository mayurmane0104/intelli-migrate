# importlib — The implementation of import — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/importlib.html](https://docs.python.org/3.13/library/importlib.html)

---

`importlib` — The implementation of `import`[¶](#module-importlib)

Added in version 3.1.

**Source code:** [Lib/importlib/__init__.py](https://github.com/python/cpython/tree/3.13/Lib/importlib/__init__.py)

## Introduction[¶](#introduction)

The purpose of the `importlib` package is three-fold.

One is to provide the
implementation of the [ import](../reference/simple_stmts.html#import) statement (and thus, by extension, the

[function) in Python source code. This provides an implementation of](functions.html#import__)

`__import__()``import` which is portable to any Python
interpreter. This also provides an implementation which is easier to
comprehend than one implemented in a programming language other than Python.Two, the components to implement [ import](../reference/simple_stmts.html#import) are exposed in this
package, making it easier for users to create their own custom objects (known
generically as an 

[importer](../glossary.html#term-importer)) to participate in the import process.

Three, the package contains modules exposing additional functionality for managing aspects of Python packages:

- `importlib.metadata`
- `importlib.resources`

See also

- [The import statement](../reference/simple_stmts.html#import)
- The language reference for the - `import`
- [Packages specification](https://www.python.org/doc/essays/packages/)
- Original specification of packages. Some semantics have changed since the writing of this document (e.g. redirecting based on - `None`in- `sys.modules`
- The `__import__()`
- The - `import`
- [The initialization of the sys.path module search path](sys_path_init.html#sys-path-init)
- The initialization of - `sys.path`
- **PEP 235**
- Import on Case-Insensitive Platforms 
- **PEP 263**
- Defining Python Source Code Encodings 
- **PEP 302**
- New Import Hooks 
- **PEP 328**
- Imports: Multi-Line and Absolute/Relative 
- **PEP 366**
- Main module explicit relative imports 
- **PEP 420**
- Implicit namespace packages 
- **PEP 451**
- A ModuleSpec Type for the Import System 
- **PEP 488**
- Elimination of PYO files 
- **PEP 489**
- Multi-phase extension module initialization 
- **PEP 552**
- Deterministic pycs 
- **PEP 3120**
- Using UTF-8 as the Default Source Encoding 
- **PEP 3147**
- PYC Repository Directories 

## Functions[¶](#functions)

- 
importlib.__import__(*name*,*globals=None*,*locals=None*,*fromlist=()*,*level=0*)[¶](#importlib.__import__)
- An implementation of the built-in - `__import__()`function.- Note - Programmatic importing of modules should use - `import_module()`

- 
importlib.import_module(*name*,*package=None*)[¶](#importlib.import_module)
- Import a module. The - *name*argument specifies what module to import in absolute or relative terms (e.g. either- `pkg.mod`or- `..mod`). If the name is specified in relative terms, then the- *package*argument must be set to the name of the package which is to act as the anchor for resolving the package name (e.g.- `import_module('..mod', 'pkg.subpkg')`will import- `pkg.mod`).- The - `import_module()`function acts as a simplifying wrapper around- `importlib.__import__()`- `importlib.__import__()`. The most important difference between these two functions is that- `import_module()`returns the specified package or module (e.g.- `pkg.mod`), while- `__import__()`- `pkg`).- If you are dynamically importing a module that was created since the interpreter began execution (e.g., created a Python source file), you may need to call - `invalidate_caches()`- Changed in version 3.3: Parent packages are automatically imported. 

- 
importlib.invalidate_caches()[¶](#importlib.invalidate_caches)
- Invalidate the internal caches of finders stored at - `sys.meta_path`- `invalidate_caches()`then it will be called to perform the invalidation. This function should be called if any modules are created/installed while your program is running to guarantee all finders will notice the new module’s existence.- Added in version 3.3. - Changed in version 3.10: Namespace packages created/installed in a different - `sys.path`

- 
importlib.reload(*module*)[¶](#importlib.reload)
- Reload a previously imported - *module*. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (which can be different if re-importing causes a different object to be placed in- `sys.modules`- When - `reload()`is executed:- Python module’s code is recompiled and the module-level code re-executed, defining a new set of objects which are bound to names in the module’s dictionary by reusing the - [loader](../glossary.html#term-loader)which originally loaded the module. The- `init`function of extension modules is not called a second time.
- As with all other objects in Python the old objects are only reclaimed after their reference counts drop to zero. 
- The names in the module namespace are updated to point to any new or changed objects. 
- Other references to the old objects (such as names external to the module) are not rebound to refer to the new objects and must be updated in each namespace where they occur if that is desired. 
 - There are a number of other caveats: - When a module is reloaded, its dictionary (containing the module’s global variables) is retained. Redefinitions of names will override the old definitions, so this is generally not a problem. If the new version of a module does not define a name that was defined by the old version, the old definition remains. This feature can be used to the module’s advantage if it maintains a global table or cache of objects — with a - `try`- try: cache except NameError: cache = {} - It is generally not very useful to reload built-in or dynamically loaded modules. Reloading - `sys`- `__main__`- `builtins`- If a module imports objects from another module using - `from`- `import`- `reload()`for the other module does not redefine the objects imported from it — one way around this is to re-execute the- `from`statement, another is to use- `import`and qualified names (- *module.name*) instead.- If a module instantiates instances of a class, reloading the module that defines the class does not affect the method definitions of the instances — they continue to use the old class definition. The same is true for derived classes. - Added in version 3.4. - Changed in version 3.7: - `ModuleNotFoundError`- `ModuleSpec`- Warning - This function is not thread-safe. Calling it from multiple threads can result in unexpected behavior. It’s recommended to use the - `threading.Lock`

`importlib.abc` – Abstract base classes related to import[¶](#module-importlib.abc)

**Source code:** [Lib/importlib/abc.py](https://github.com/python/cpython/tree/3.13/Lib/importlib/abc.py)

The `importlib.abc` module contains all of the core abstract base classes
used by [ import](../reference/simple_stmts.html#import). Some subclasses of the core abstract base classes
are also provided to help in implementing the core ABCs.

ABC hierarchy:

```
object
 +-- MetaPathFinder
 +-- PathEntryFinder
 +-- Loader
      +-- ResourceLoader --------+
      +-- InspectLoader          |
           +-- ExecutionLoader --+
                                 +-- FileLoader
                                 +-- SourceLoader
```
- 
*class*importlib.abc.MetaPathFinder[¶](#importlib.abc.MetaPathFinder)
- An abstract base class representing a - [meta path finder](../glossary.html#term-meta-path-finder).- Added in version 3.3. - Changed in version 3.10: No longer a subclass of - `Finder`.- 
find_spec(*fullname*,*path*,*target=None*)[¶](#importlib.abc.MetaPathFinder.find_spec)
- An abstract method for finding a - [spec](../glossary.html#term-module-spec)for the specified module. If this is a top-level import,- *path*will be- `None`. Otherwise, this is a search for a subpackage or module and- *path*will be the value of- `__path__`- `None`is returned. When passed in,- `target`is a module object that the finder may use to make a more educated guess about what spec to return.- `importlib.util.spec_from_loader()`- `MetaPathFinders`.- Added in version 3.4. 
 - 
invalidate_caches()[¶](#importlib.abc.MetaPathFinder.invalidate_caches)
- An optional method which, when called, should invalidate any internal cache used by the finder. Used by - `importlib.invalidate_caches()`- `sys.meta_path`- Changed in version 3.4: Returns - `None`when called instead of- `NotImplemented`
 
- 
find_spec(

- 
*class*importlib.abc.PathEntryFinder[¶](#importlib.abc.PathEntryFinder)
- An abstract base class representing a - [path entry finder](../glossary.html#term-path-entry-finder). Though it bears some similarities to- `MetaPathFinder`- `PathEntryFinder`is meant for use only within the path-based import subsystem provided by- `importlib.machinery.PathFinder`- Added in version 3.3. - Changed in version 3.10: No longer a subclass of - `Finder`.- 
find_spec(*fullname*,*target=None*)[¶](#importlib.abc.PathEntryFinder.find_spec)
- An abstract method for finding a - [spec](../glossary.html#term-module-spec)for the specified module. The finder will search for the module only within the- [path entry](../glossary.html#term-path-entry)to which it is assigned. If a spec cannot be found,- `None`is returned. When passed in,- `target`is a module object that the finder may use to make a more educated guess about what spec to return.- `importlib.util.spec_from_loader()`- `PathEntryFinders`.- Added in version 3.4. 
 - 
invalidate_caches()[¶](#importlib.abc.PathEntryFinder.invalidate_caches)
- An optional method which, when called, should invalidate any internal cache used by the finder. Used by - `importlib.machinery.PathFinder.invalidate_caches()`
 
- 
find_spec(

- 
*class*importlib.abc.Loader[¶](#importlib.abc.Loader)
- An abstract base class for a - [loader](../glossary.html#term-loader). See- **PEP 302**- Loaders that wish to support resource reading should implement a - `get_resource_reader()`method as specified by- `importlib.resources.abc.ResourceReader`- Changed in version 3.7: Introduced the optional - `get_resource_reader()`method.- 
create_module(*spec*)[¶](#importlib.abc.Loader.create_module)
- A method that returns the module object to use when importing a module. This method may return - `None`, indicating that default module creation semantics should take place.- Added in version 3.4. - Changed in version 3.6: This method is no longer optional when - `exec_module()`
 - 
exec_module(*module*)[¶](#importlib.abc.Loader.exec_module)
- An abstract method that executes the module in its own namespace when a module is imported or reloaded. The module should already be initialized when - `exec_module()`is called. When this method exists,- `create_module()`- Added in version 3.4. - Changed in version 3.6: - `create_module()`
 - 
load_module(*fullname*)[¶](#importlib.abc.Loader.load_module)
- A legacy method for loading a module. If the module cannot be loaded, - `ImportError`- If the requested module already exists in - `sys.modules`- `sys.modules`before any loading begins, to prevent recursion from the import. If the loader inserted a module and the load fails, it must be removed by the loader from- `sys.modules`; modules already in- `sys.modules`before the loader began execution should be left alone.- The loader should set several attributes on the module (note that some of these attributes can change when a module is reloaded): 
- `module.__cached__`- *(deprecated)*
- `module.__package__`- *(deprecated)*
- `module.__loader__`- *(deprecated)*
 - When - `exec_module()`- Changed in version 3.4: Raise - `ImportError`- `NotImplementedError`- `exec_module()`- Deprecated since version 3.4, will be removed in version 3.15: The recommended API for loading a module is - `exec_module()`- `create_module()`- `load_module()`. The import machinery takes care of all the other responsibilities of- `load_module()`when- `exec_module()`is implemented.
 
- 
create_module(

- 
*class*importlib.abc.ResourceLoader[¶](#importlib.abc.ResourceLoader)
- *Superseded by TraversableResources*- An abstract base class for a - [loader](../glossary.html#term-loader)which implements the optional- **PEP 302**- Deprecated since version 3.7: This ABC is deprecated in favour of supporting resource loading through - `importlib.resources.abc.TraversableResources`- 
*abstractmethod*get_data(*path*)[¶](#importlib.abc.ResourceLoader.get_data)
- An abstract method to return the bytes for the data located at - *path*. Loaders that have a file-like storage back-end that allows storing arbitrary data can implement this abstract method to give direct access to the data stored.- `OSError`- *path*cannot be found. The- *path*is expected to be constructed using a module’s- `__file__`- `__path__`- Changed in version 3.4: Raises - `OSError`- `NotImplementedError`
 
- 

- 
*class*importlib.abc.InspectLoader[¶](#importlib.abc.InspectLoader)
- An abstract base class for a - [loader](../glossary.html#term-loader)which implements the optional- **PEP 302**- 
get_code(*fullname*)[¶](#importlib.abc.InspectLoader.get_code)
- Return the code object for a module, or - `None`if the module does not have a code object (as would be the case, for example, for a built-in module). Raise an- `ImportError`- Note - While the method has a default implementation, it is suggested that it be overridden if possible for performance. - Changed in version 3.4: No longer abstract and a concrete implementation is provided. 
 - 
*abstractmethod*get_source(*fullname*)[¶](#importlib.abc.InspectLoader.get_source)
- An abstract method to return the source of a module. It is returned as a text string using - [universal newlines](../glossary.html#term-universal-newlines), translating all recognized line separators into- `'\n'`characters. Returns- `None`if no source is available (e.g. a built-in module). Raises- `ImportError`- Changed in version 3.4: Raises - `ImportError`- `NotImplementedError`
 - 
is_package(*fullname*)[¶](#importlib.abc.InspectLoader.is_package)
- An optional method to return a true value if the module is a package, a false value otherwise. - `ImportError`- [loader](../glossary.html#term-loader)cannot find the module.- Changed in version 3.4: Raises - `ImportError`- `NotImplementedError`
 - 
*static*source_to_code(*data*,*path='<string>'*)[¶](#importlib.abc.InspectLoader.source_to_code)
- Create a code object from Python source. - The - *data*argument can be whatever the- `compile()`- *path*argument should be the “path” to where the source code originated from, which can be an abstract concept (e.g. location in a zip file).- With the subsequent code object one can execute it in a module by running - `exec(code, module.__dict__)`.- Added in version 3.4. - Changed in version 3.5: Made the method static. 
 - 
exec_module(*module*)[¶](#importlib.abc.InspectLoader.exec_module)
- Implementation of - `Loader.exec_module()`- Added in version 3.4. 
 - 
load_module(*fullname*)[¶](#importlib.abc.InspectLoader.load_module)
- Implementation of - `Loader.load_module()`- Deprecated since version 3.4, will be removed in version 3.15: use - `exec_module()`
 
- 
get_code(

- 
*class*importlib.abc.ExecutionLoader[¶](#importlib.abc.ExecutionLoader)
- An abstract base class which inherits from - `InspectLoader`- **PEP 302**- 
*abstractmethod*get_filename(*fullname*)[¶](#importlib.abc.ExecutionLoader.get_filename)
- An abstract method that is to return the value of - `__file__`- `ImportError`- If source code is available, then the method should return the path to the source file, regardless of whether a bytecode was used to load the module. - Changed in version 3.4: Raises - `ImportError`- `NotImplementedError`
 
- 

- 
*class*importlib.abc.FileLoader(*fullname*,*path*)[¶](#importlib.abc.FileLoader)
- An abstract base class which inherits from - `ResourceLoader`- `ExecutionLoader`- `ResourceLoader.get_data()`- `ExecutionLoader.get_filename()`- The - *fullname*argument is a fully resolved name of the module the loader is to handle. The- *path*argument is the path to the file for the module.- Added in version 3.3. - 
name[¶](#importlib.abc.FileLoader.name)
- The name of the module the loader can handle. 
 - 
path[¶](#importlib.abc.FileLoader.path)
- Path to the file of the module. 
 - 
load_module(*fullname*)[¶](#importlib.abc.FileLoader.load_module)
- Calls super’s - `load_module()`.- Deprecated since version 3.4, will be removed in version 3.15: Use - `Loader.exec_module()`
 - 
*abstractmethod*get_data(*path*)[¶](#importlib.abc.FileLoader.get_data)
- Reads - *path*as a binary file and returns the bytes from it.
 
- 
name

- 
*class*importlib.abc.SourceLoader[¶](#importlib.abc.SourceLoader)
- An abstract base class for implementing source (and optionally bytecode) file loading. The class inherits from both - `ResourceLoader`- `ExecutionLoader`
- `ExecutionLoader.get_filename()`
- Should only return the path to the source file; sourceless loading is not supported. 
 
 - The abstract methods defined by this class are to add optional bytecode file support. Not implementing these optional methods (or causing them to raise - `NotImplementedError`- *and*bytecode files; it does not allow for- *sourceless*loading where only bytecode is provided. Bytecode files are an optimization to speed up loading by removing the parsing step of Python’s compiler, and so no bytecode-specific API is exposed.- 
path_stats(*path*)[¶](#importlib.abc.SourceLoader.path_stats)
- Optional abstract method which returns a - `dict`- `'mtime'`(mandatory): an integer or floating-point number representing the modification time of the source code;
- `'size'`(optional): the size in bytes of the source code.
 - Any other keys in the dictionary are ignored, to allow for future extensions. If the path cannot be handled, - `OSError`- Added in version 3.3. - Changed in version 3.4: Raise - `OSError`- `NotImplementedError`
 - 
path_mtime(*path*)[¶](#importlib.abc.SourceLoader.path_mtime)
- Optional abstract method which returns the modification time for the specified path. - Deprecated since version 3.3: This method is deprecated in favour of - `path_stats()`- `OSError`- Changed in version 3.4: Raise - `OSError`- `NotImplementedError`
 - 
set_data(*path*,*data*)[¶](#importlib.abc.SourceLoader.set_data)
- Optional abstract method which writes the specified bytes to a file path. Any intermediate directories which do not exist are to be created automatically. - When writing to the path fails because the path is read-only ( - `errno.EACCES`- `PermissionError`- Changed in version 3.4: No longer raises - `NotImplementedError`
 - 
get_code(*fullname*)[¶](#importlib.abc.SourceLoader.get_code)
- Concrete implementation of - `InspectLoader.get_code()`
 - 
exec_module(*module*)[¶](#importlib.abc.SourceLoader.exec_module)
- Concrete implementation of - `Loader.exec_module()`- Added in version 3.4. 
 - 
load_module(*fullname*)[¶](#importlib.abc.SourceLoader.load_module)
- Concrete implementation of - `Loader.load_module()`- Deprecated since version 3.4, will be removed in version 3.15: Use - `exec_module()`
 - 
get_source(*fullname*)[¶](#importlib.abc.SourceLoader.get_source)
- Concrete implementation of - `InspectLoader.get_source()`
 - 
is_package(*fullname*)[¶](#importlib.abc.SourceLoader.is_package)
- Concrete implementation of - `InspectLoader.is_package()`- `ExecutionLoader.get_filename()`- `__init__`when the file extension is removed- **and**the module name itself does not end in- `__init__`.
 

- 
*class*importlib.abc.ResourceReader[¶](#importlib.abc.ResourceReader)
- *Superseded by TraversableResources*- An - [abstract base class](../glossary.html#term-abstract-base-class)to provide the ability to read- *resources*.- From the perspective of this ABC, a - *resource*is a binary artifact that is shipped within a package. Typically this is something like a data file that lives next to the- `__init__.py`file of the package. The purpose of this class is to help abstract out the accessing of such data files so that it does not matter if the package and its data file(s) are stored e.g. in a zip file versus on the file system.- For any of methods of this class, a - *resource*argument is expected to be a- [path-like object](../glossary.html#term-path-like-object)which represents conceptually just a file name. This means that no subdirectory paths should be included in the- *resource*argument. This is because the location of the package the reader is for, acts as the “directory”. Hence the metaphor for directories and file names is packages and resources, respectively. This is also why instances of this class are expected to directly correlate to a specific package (instead of potentially representing multiple packages or a module).- Loaders that wish to support resource reading are expected to provide a method called - `get_resource_reader(fullname)`which returns an object implementing this ABC’s interface. If the module specified by fullname is not a package, this method should return- `None`- Added in version 3.7. - Deprecated since version 3.12, will be removed in version 3.14: Use - `importlib.resources.abc.TraversableResources`- 
*abstractmethod*open_resource(*resource*)[¶](#importlib.abc.ResourceReader.open_resource)
- Returns an opened, - [file-like object](../glossary.html#term-file-like-object)for binary reading of the- *resource*.- If the resource cannot be found, - `FileNotFoundError`
 - 
*abstractmethod*resource_path(*resource*)[¶](#importlib.abc.ResourceReader.resource_path)
- Returns the file system path to the - *resource*.- If the resource does not concretely exist on the file system, raise - `FileNotFoundError`
 - 
*abstractmethod*is_resource(*name*)[¶](#importlib.abc.ResourceReader.is_resource)
- Returns - `True`if the named- *name*is considered a resource.- `FileNotFoundError`- *name*does not exist.
 - 
*abstractmethod*contents()[¶](#importlib.abc.ResourceReader.contents)
- Returns an - [iterable](../glossary.html#term-iterable)of strings over the contents of the package. Do note that it is not required that all names returned by the iterator be actual resources, e.g. it is acceptable to return names for which- `is_resource()`- Allowing non-resource names to be returned is to allow for situations where how a package and its resources are stored are known a priori and the non-resource names would be useful. For instance, returning subdirectory names is allowed so that when it is known that the package and resources are stored on the file system then those subdirectory names can be used directly. - The abstract method returns an iterable of no items. 
 
- 

- 
*class*importlib.abc.Traversable[¶](#importlib.abc.Traversable)
- An object with a subset of - `pathlib.Path`- For a representation of the object on the file-system, use - `importlib.resources.as_file()`- Added in version 3.9. - Deprecated since version 3.12, will be removed in version 3.14: Use - `importlib.resources.abc.Traversable`- 
name[¶](#importlib.abc.Traversable.name)
- Abstract. The base name of this object without any parent references. 
 - 
*abstractmethod*iterdir()[¶](#importlib.abc.Traversable.iterdir)
- Yield - `Traversable`objects in- `self`.
 - 
*abstractmethod*is_dir()[¶](#importlib.abc.Traversable.is_dir)
- Return - `True`if- `self`is a directory.
 - 
*abstractmethod*is_file()[¶](#importlib.abc.Traversable.is_file)
- Return - `True`if- `self`is a file.
 - 
*abstractmethod*joinpath(*child*)[¶](#importlib.abc.Traversable.joinpath)
- Return Traversable child in - `self`.
 - 
*abstractmethod*__truediv__(*child*)[¶](#importlib.abc.Traversable.__truediv__)
- Return - `Traversable`child in- `self`.
 - 
*abstractmethod*open(*mode='r'*,**args*,***kwargs*)[¶](#importlib.abc.Traversable.open)
- *mode*may be ‘r’ or ‘rb’ to open as text or binary. Return a handle suitable for reading (same as- `pathlib.Path.open`- When opening as text, accepts encoding parameters such as those accepted by - `io.TextIOWrapper`
 - 
read_bytes()[¶](#importlib.abc.Traversable.read_bytes)
- Read contents of - `self`as bytes.
 - 
read_text(*encoding=None*)[¶](#importlib.abc.Traversable.read_text)
- Read contents of - `self`as text.
 
- 
name

- 
*class*importlib.abc.TraversableResources[¶](#importlib.abc.TraversableResources)
- An abstract base class for resource readers capable of serving the - `importlib.resources.files()`- `importlib.resources.abc.ResourceReader`- `importlib.resources.abc.ResourceReader`’s abstract methods. Therefore, any loader supplying- `importlib.abc.TraversableResources`also supplies ResourceReader.- Loaders that wish to support resource reading are expected to implement this interface. - Added in version 3.9. - Deprecated since version 3.12, will be removed in version 3.14: Use - `importlib.resources.abc.TraversableResources`- 
*abstractmethod*files()[¶](#importlib.abc.TraversableResources.files)
- Returns a - `importlib.resources.abc.Traversable`
 
- 

`importlib.machinery` – Importers and path hooks[¶](#module-importlib.machinery)

**Source code:** [Lib/importlib/machinery.py](https://github.com/python/cpython/tree/3.13/Lib/importlib/machinery.py)

This module contains the various objects that help [ import](../reference/simple_stmts.html#import)
find and load modules.

- 
importlib.machinery.SOURCE_SUFFIXES[¶](#importlib.machinery.SOURCE_SUFFIXES)
- A list of strings representing the recognized file suffixes for source modules. - Added in version 3.3. 

- 
importlib.machinery.DEBUG_BYTECODE_SUFFIXES[¶](#importlib.machinery.DEBUG_BYTECODE_SUFFIXES)
- A list of strings representing the file suffixes for non-optimized bytecode modules. - Added in version 3.3. - Deprecated since version 3.5: Use - `BYTECODE_SUFFIXES`

- 
importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES[¶](#importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES)
- A list of strings representing the file suffixes for optimized bytecode modules. - Added in version 3.3. - Deprecated since version 3.5: Use - `BYTECODE_SUFFIXES`

- 
importlib.machinery.BYTECODE_SUFFIXES[¶](#importlib.machinery.BYTECODE_SUFFIXES)
- A list of strings representing the recognized file suffixes for bytecode modules (including the leading dot). - Added in version 3.3. - Changed in version 3.5: The value is no longer dependent on - `__debug__`.

- 
importlib.machinery.EXTENSION_SUFFIXES[¶](#importlib.machinery.EXTENSION_SUFFIXES)
- A list of strings representing the recognized file suffixes for extension modules. - Added in version 3.3. 

- 
importlib.machinery.all_suffixes()[¶](#importlib.machinery.all_suffixes)
- Returns a combined list of strings representing all file suffixes for modules recognized by the standard import machinery. This is a helper for code which simply needs to know if a filesystem path potentially refers to a module without needing any details on the kind of module (for example, - `inspect.getmodulename()`- Added in version 3.3. 

- 
*class*importlib.machinery.BuiltinImporter[¶](#importlib.machinery.BuiltinImporter)
- An - [importer](../glossary.html#term-importer)for built-in modules. All known built-in modules are listed in- `sys.builtin_module_names`- `importlib.abc.MetaPathFinder`- `importlib.abc.InspectLoader`- Only class methods are defined by this class to alleviate the need for instantiation. - Changed in version 3.5: As part of - **PEP 489**- `Loader.create_module()`and- `Loader.exec_module()`

- 
*class*importlib.machinery.FrozenImporter[¶](#importlib.machinery.FrozenImporter)
- An - [importer](../glossary.html#term-importer)for frozen modules. This class implements the- `importlib.abc.MetaPathFinder`- `importlib.abc.InspectLoader`- Only class methods are defined by this class to alleviate the need for instantiation. - Changed in version 3.4: Gained - `create_module()`and- `exec_module()`methods.

- 
*class*importlib.machinery.WindowsRegistryFinder[¶](#importlib.machinery.WindowsRegistryFinder)
- [Finder](../glossary.html#term-finder)for modules declared in the Windows registry. This class implements the- `importlib.abc.MetaPathFinder`- Only class methods are defined by this class to alleviate the need for instantiation. - Added in version 3.3. - Deprecated since version 3.6: Use - `site`

- 
*class*importlib.machinery.PathFinder[¶](#importlib.machinery.PathFinder)
- A - [Finder](../glossary.html#term-finder)for- `sys.path`- `__path__`attributes. This class implements the- `importlib.abc.MetaPathFinder`- Only class methods are defined by this class to alleviate the need for instantiation. - 
*classmethod*find_spec(*fullname*,*path=None*,*target=None*)[¶](#importlib.machinery.PathFinder.find_spec)
- Class method that attempts to find a - [spec](../glossary.html#term-module-spec)for the module specified by- *fullname*on- `sys.path`- *path*. For each path entry that is searched,- `sys.path_importer_cache`- [path entry finder](../glossary.html#term-path-entry-finder)to look for the module being searched for. If no entry is found in- `sys.path_importer_cache`, then- `sys.path_hooks`- `sys.path_importer_cache`along with being queried about the module. If no finder is ever found then- `None`is both stored in the cache and returned.- Added in version 3.4. - Changed in version 3.5: If the current working directory – represented by an empty string – is no longer valid then - `None`is returned but no value is cached in- `sys.path_importer_cache`
 - 
*classmethod*invalidate_caches()[¶](#importlib.machinery.PathFinder.invalidate_caches)
- Calls - `importlib.abc.PathEntryFinder.invalidate_caches()`- `sys.path_importer_cache`- `sys.path_importer_cache`set to- `None`are deleted.- Changed in version 3.7: Entries of - `None`in- `sys.path_importer_cache`
 - Changed in version 3.4: Calls objects in - `sys.path_hooks`- `''`(i.e. the empty string).
- 

- 
*class*importlib.machinery.FileFinder(*path*,**loader_details*)[¶](#importlib.machinery.FileFinder)
- A concrete implementation of - `importlib.abc.PathEntryFinder`- The - *path*argument is the directory for which the finder is in charge of searching.- The - *loader_details*argument is a variable number of 2-item tuples each containing a loader and a sequence of file suffixes the loader recognizes. The loaders are expected to be callables which accept two arguments of the module’s name and the path to the file found.- The finder will cache the directory contents as necessary, making stat calls for each module search to verify the cache is not outdated. Because cache staleness relies upon the granularity of the operating system’s state information of the file system, there is a potential race condition of searching for a module, creating a new file, and then searching for the module the new file represents. If the operations happen fast enough to fit within the granularity of stat calls, then the module search will fail. To prevent this from happening, when you create a module dynamically, make sure to call - `importlib.invalidate_caches()`- Added in version 3.3. - 
path[¶](#importlib.machinery.FileFinder.path)
- The path the finder will search in. 
 - 
find_spec(*fullname*,*target=None*)[¶](#importlib.machinery.FileFinder.find_spec)
- Attempt to find the spec to handle - *fullname*within- `path`- Added in version 3.4. 
 - 
invalidate_caches()[¶](#importlib.machinery.FileFinder.invalidate_caches)
- Clear out the internal cache. 
 - 
*classmethod*path_hook(**loader_details*)[¶](#importlib.machinery.FileFinder.path_hook)
- A class method which returns a closure for use on - `sys.path_hooks`- `FileFinder`is returned by the closure using the path argument given to the closure directly and- *loader_details*indirectly.- If the argument to the closure is not an existing directory, - `ImportError`
 
- 
path

- 
*class*importlib.machinery.SourceFileLoader(*fullname*,*path*)[¶](#importlib.machinery.SourceFileLoader)
- A concrete implementation of - `importlib.abc.SourceLoader`- `importlib.abc.FileLoader`- Added in version 3.3. - 
name[¶](#importlib.machinery.SourceFileLoader.name)
- The name of the module that this loader will handle. 
 - 
path[¶](#importlib.machinery.SourceFileLoader.path)
- The path to the source file. 
 - 
path_stats(*path*)[¶](#importlib.machinery.SourceFileLoader.path_stats)
- Concrete implementation of - `importlib.abc.SourceLoader.path_stats()`
 - 
set_data(*path*,*data*)[¶](#importlib.machinery.SourceFileLoader.set_data)
- Concrete implementation of - `importlib.abc.SourceLoader.set_data()`
 - 
load_module(*name=None*)[¶](#importlib.machinery.SourceFileLoader.load_module)
- Concrete implementation of - `importlib.abc.Loader.load_module()`- Deprecated since version 3.6, will be removed in version 3.15: Use - `importlib.abc.Loader.exec_module()`
 
- 
name

- 
*class*importlib.machinery.SourcelessFileLoader(*fullname*,*path*)[¶](#importlib.machinery.SourcelessFileLoader)
- A concrete implementation of - `importlib.abc.FileLoader`- Please note that direct use of bytecode files (and thus not source code files) inhibits your modules from being usable by all Python implementations or new versions of Python which change the bytecode format. - Added in version 3.3. - 
name[¶](#importlib.machinery.SourcelessFileLoader.name)
- The name of the module the loader will handle. 
 - 
path[¶](#importlib.machinery.SourcelessFileLoader.path)
- The path to the bytecode file. 
 - 
get_source(*fullname*)[¶](#importlib.machinery.SourcelessFileLoader.get_source)
- Returns - `None`as bytecode files have no source when this loader is used.
 - 
load_module(*name=None*)[¶](#importlib.machinery.SourcelessFileLoader.load_module)
 - Concrete implementation of - `importlib.abc.Loader.load_module()`- Deprecated since version 3.6, will be removed in version 3.15: Use - `importlib.abc.Loader.exec_module()`
- 
name

- 
*class*importlib.machinery.ExtensionFileLoader(*fullname*,*path*)[¶](#importlib.machinery.ExtensionFileLoader)
- A concrete implementation of - `importlib.abc.ExecutionLoader`- The - *fullname*argument specifies the name of the module the loader is to support. The- *path*argument is the path to the extension module’s file.- Note that, by default, importing an extension module will fail in subinterpreters if it doesn’t implement multi-phase init (see - **PEP 489**- Added in version 3.3. - Changed in version 3.12: Multi-phase init is now required for use in subinterpreters. - 
name[¶](#importlib.machinery.ExtensionFileLoader.name)
- Name of the module the loader supports. 
 - 
path[¶](#importlib.machinery.ExtensionFileLoader.path)
- Path to the extension module. 
 - 
create_module(*spec*)[¶](#importlib.machinery.ExtensionFileLoader.create_module)
- Creates the module object from the given specification in accordance with - **PEP 489**- Added in version 3.5. 
 - 
exec_module(*module*)[¶](#importlib.machinery.ExtensionFileLoader.exec_module)
- Initializes the given module object in accordance with - **PEP 489**- Added in version 3.5. 
 - 
is_package(*fullname*)[¶](#importlib.machinery.ExtensionFileLoader.is_package)
- Returns - `True`if the file path points to a package’s- `__init__`module based on- `EXTENSION_SUFFIXES`
 - 
get_code(*fullname*)[¶](#importlib.machinery.ExtensionFileLoader.get_code)
- Returns - `None`as extension modules lack a code object.
 - 
get_source(*fullname*)[¶](#importlib.machinery.ExtensionFileLoader.get_source)
- Returns - `None`as extension modules do not have source code.
 
- 
name

- 
*class*importlib.machinery.NamespaceLoader(*name*,*path*,*path_finder*)[¶](#importlib.machinery.NamespaceLoader)
- A concrete implementation of - `importlib.abc.InspectLoader`- `__loader__`attribute on namespace packages:- >>> from importlib.machinery import NamespaceLoader >>> import my_namespace >>> isinstance(my_namespace.__loader__, NamespaceLoader) True >>> import importlib.abc >>> isinstance(my_namespace.__loader__, importlib.abc.Loader) True - Added in version 3.11. 

- 
*class*importlib.machinery.ModuleSpec(*name*,*loader*,***,*origin=None*,*loader_state=None*,*is_package=None*)[¶](#importlib.machinery.ModuleSpec)
- A specification for a module’s import-system-related state. This is typically exposed as the module’s - `__spec__`- `module.__spec__.origin == module.__file__`. Note, however, that while the- *values*are usually equivalent, they can differ since there is no synchronization between the two objects. For example, it is possible to update the module’s- `__file__`- `__spec__.origin`- Added in version 3.4. - 
name[¶](#importlib.machinery.ModuleSpec.name)
- The module’s fully qualified name (see - `module.__name__`- [finder](../glossary.html#term-finder)should always set this attribute to a non-empty string.
 - 
loader[¶](#importlib.machinery.ModuleSpec.loader)
- The - [loader](../glossary.html#term-loader)used to load the module (see- `module.__loader__`- [finder](../glossary.html#term-finder)should always set this attribute.
 - 
origin[¶](#importlib.machinery.ModuleSpec.origin)
- The location the - [loader](../glossary.html#term-loader)should use to load the module (see- `module.__file__`- `.py`file this is the filename. The- [finder](../glossary.html#term-finder)should always set this attribute to a meaningful value for the loader to use. In the uncommon case that there is not one (like for namespace packages), it should be set to- `None`.
 - 
submodule_search_locations[¶](#importlib.machinery.ModuleSpec.submodule_search_locations)
- A (possibly empty) - [sequence](../glossary.html#term-sequence)of strings enumerating the locations in which a package’s submodules will be found (see- `module.__path__`- The - [finder](../glossary.html#term-finder)should set this attribute to a sequence, even an empty one, to indicate to the import system that the module is a package. It should be set to- `None`for non-package modules. It is set automatically later to a special object for namespace packages.
 - 
loader_state[¶](#importlib.machinery.ModuleSpec.loader_state)
- The - [finder](../glossary.html#term-finder)may set this attribute to an object containing additional, module-specific data to use when loading the module. Otherwise it should be set to- `None`.
 - 
cached[¶](#importlib.machinery.ModuleSpec.cached)
- The filename of a compiled version of the module’s code (see - `module.__cached__`- [finder](../glossary.html#term-finder)should always set this attribute but it may be- `None`for modules that do not need compiled code stored.
 - 
parent[¶](#importlib.machinery.ModuleSpec.parent)
- (Read-only) The fully qualified name of the package the module is in (or the empty string for a top-level module). See - `module.__package__`- `name`
 
- 
name

- 
*class*importlib.machinery.AppleFrameworkLoader(*name*,*path*)[¶](#importlib.machinery.AppleFrameworkLoader)
- A specialization of - `importlib.machinery.ExtensionFileLoader`- For compatibility with the iOS App Store, - *all*binary modules in an iOS app must be dynamic libraries, contained in a framework with appropriate metadata, stored in the- `Frameworks`folder of the packaged app. There can be only a single binary per framework, and there can be no executable binary material outside the Frameworks folder.- To accommodate this requirement, when running on iOS, extension module binaries are - *not*packaged as- `.so`files on- `sys.path`, but as individual standalone frameworks. To discover those frameworks, this loader is registered against the- `.fwork`file extension, with a- `.fwork`file acting as a placeholder in the original location of the binary on- `sys.path`. The- `.fwork`file contains the path of the actual binary in the- `Frameworks`folder, relative to the app bundle. To allow for resolving a framework-packaged binary back to the original location, the framework is expected to contain a- `.origin`file that contains the location of the- `.fwork`file, relative to the app bundle.- For example, consider the case of an import - `from foo.bar import _whiz`, where- `_whiz`is implemented with the binary module- `sources/foo/bar/_whiz.abi3.so`, with- `sources`being the location registered on- `sys.path`, relative to the application bundle. This module- *must*be distributed as- `Frameworks/foo.bar._whiz.framework/foo.bar._whiz`(creating the framework name from the full import path of the module), with an- `Info.plist`file in the- `.framework`directory identifying the binary as a framework. The- `foo.bar._whiz`module would be represented in the original location with a- `sources/foo/bar/_whiz.abi3.fwork`marker file, containing the path- `Frameworks/foo.bar._whiz/foo.bar._whiz`. The framework would also contain- `Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin`, containing the path to the- `.fwork`file.- When a module is loaded with this loader, the - `__file__`for the module will report as the location of the- `.fwork`file. This allows code to use the- `__file__`of a module as an anchor for file system traveral. However, the spec origin will reference the location of the- *actual*binary in the- `.framework`folder.- The Xcode project building the app is responsible for converting any - `.so`files from wherever they exist in the- `PYTHONPATH`into frameworks in the- `Frameworks`folder (including stripping extensions from the module file, the addition of framework metadata, and signing the resulting framework), and creating the- `.fwork`and- `.origin`files. This will usually be done with a build step in the Xcode project; see the iOS documentation for details on how to construct this build step.- Added in version 3.13. - [Availability](intro.html#availability): iOS.- 
name[¶](#importlib.machinery.AppleFrameworkLoader.name)
- Name of the module the loader supports. 
 - 
path[¶](#importlib.machinery.AppleFrameworkLoader.path)
- Path to the - `.fwork`file for the extension module.
 
- 
name

`importlib.util` – Utility code for importers[¶](#module-importlib.util)

**Source code:** [Lib/importlib/util.py](https://github.com/python/cpython/tree/3.13/Lib/importlib/util.py)

This module contains the various objects that help in the construction of
an [importer](../glossary.html#term-importer).

- 
importlib.util.MAGIC_NUMBER[¶](#importlib.util.MAGIC_NUMBER)
- The bytes which represent the bytecode version number. If you need help with loading/writing bytecode then consider - `importlib.abc.SourceLoader`- Added in version 3.4. 

- 
importlib.util.cache_from_source(*path*,*debug_override=None*,***,*optimization=None*)[¶](#importlib.util.cache_from_source)
- Return the - **PEP 3147**- **PEP 488**- *path*. For example, if- *path*is- `/foo/bar/baz.py`the return value would be- `/foo/bar/__pycache__/baz.cpython-32.pyc`for Python 3.2. The- `cpython-32`string comes from the current magic tag (see- `get_tag()`; if- `sys.implementation.cache_tag`is not defined then- `NotImplementedError`- The - *optimization*parameter is used to specify the optimization level of the bytecode file. An empty string represents no optimization, so- `/foo/bar/baz.py`with an- *optimization*of- `''`will result in a bytecode path of- `/foo/bar/__pycache__/baz.cpython-32.pyc`.- `None`causes the interpreter’s optimization level to be used. Any other value’s string representation is used, so- `/foo/bar/baz.py`with an- *optimization*of- `2`will lead to the bytecode path of- `/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc`. The string representation of- *optimization*can only be alphanumeric, else- `ValueError`- The - *debug_override*parameter is deprecated and can be used to override the system’s value for- `__debug__`. A- `True`value is the equivalent of setting- *optimization*to the empty string. A- `False`value is the same as setting- *optimization*to- `1`. If both- *debug_override*an- *optimization*are not- `None`then- `TypeError`- Added in version 3.4. - Changed in version 3.5: The - *optimization*parameter was added and the- *debug_override*parameter was deprecated.- Changed in version 3.6: Accepts a - [path-like object](../glossary.html#term-path-like-object).

- 
importlib.util.source_from_cache(*path*)[¶](#importlib.util.source_from_cache)
- Given the - *path*to a- **PEP 3147**- *path*is- `/foo/bar/__pycache__/baz.cpython-32.pyc`the returned path would be- `/foo/bar/baz.py`.- *path*need not exist, however if it does not conform to- **PEP 3147**- **PEP 488**- `ValueError`- `sys.implementation.cache_tag`is not defined,- `NotImplementedError`- Added in version 3.4. - Changed in version 3.6: Accepts a - [path-like object](../glossary.html#term-path-like-object).

- 
importlib.util.decode_source(*source_bytes*)[¶](#importlib.util.decode_source)
- Decode the given bytes representing source code and return it as a string with universal newlines (as required by - `importlib.abc.InspectLoader.get_source()`- Added in version 3.4. 

- 
importlib.util.resolve_name(*name*,*package*)[¶](#importlib.util.resolve_name)
- Resolve a relative module name to an absolute one. - If - **name**has no leading dots, then- **name**is simply returned. This allows for usage such as- `importlib.util.resolve_name('sys', __spec__.parent)`without doing a check to see if the- **package**argument is needed.- `ImportError`- **name**is a relative module name but- **package**is a false value (e.g.- `None`or the empty string).- `ImportError`is also raised if a relative name would escape its containing package (e.g. requesting- `..bacon`from within the- `spam`package).- Added in version 3.3. - Changed in version 3.9: To improve consistency with import statements, raise - `ImportError`- `ValueError`

- 
importlib.util.find_spec(*name*,*package=None*)[¶](#importlib.util.find_spec)
- Find the - [spec](../glossary.html#term-module-spec)for a module, optionally relative to the specified- **package**name. If the module is in- `sys.modules`- `sys.modules[name].__spec__`is returned (unless the spec would be- `None`or is not set, in which case- `ValueError`- `sys.meta_path`- `None`is returned if no spec is found.- If - **name**is for a submodule (contains a dot), the parent module is automatically imported.- **name**and- **package**work the same as for- `import_module()`.- Added in version 3.4. - Changed in version 3.7: Raises - `ModuleNotFoundError`- `AttributeError`- **package**is in fact not a package (i.e. lacks a- `__path__`

- 
importlib.util.module_from_spec(*spec*)[¶](#importlib.util.module_from_spec)
- Create a new module based on - **spec**and- `spec.loader.create_module`- If - `spec.loader.create_module`- `None`, then any pre-existing attributes will not be reset. Also, no- `AttributeError`- **spec**or setting an attribute on the module.- This function is preferred over using - `types.ModuleType`- **spec**is used to set as many import-controlled attributes on the module as possible.- Added in version 3.5. 

- 
importlib.util.spec_from_loader(*name*,*loader*,***,*origin=None*,*is_package=None*)[¶](#importlib.util.spec_from_loader)
- A factory function for creating a - `ModuleSpec`- [loader](../glossary.html#term-loader)APIs, such as- `InspectLoader.is_package()`, to fill in any missing information on the spec.- Added in version 3.4. 

- 
importlib.util.spec_from_file_location(*name*,*location*,***,*loader=None*,*submodule_search_locations=None*)[¶](#importlib.util.spec_from_file_location)
- A factory function for creating a - `ModuleSpec`- Added in version 3.4. - Changed in version 3.6: Accepts a - [path-like object](../glossary.html#term-path-like-object).

- 
importlib.util.source_hash(*source_bytes*)[¶](#importlib.util.source_hash)
- Return the hash of - *source_bytes*as bytes. A hash-based- `.pyc`file embeds the- `source_hash()`of the corresponding source file’s contents in its header.- Added in version 3.7. 

- 
importlib.util._incompatible_extension_module_restrictions(***,*disable_check*)[¶](#importlib.util._incompatible_extension_module_restrictions)
- A context manager that can temporarily skip the compatibility check for extension modules. By default the check is enabled and will fail when a single-phase init module is imported in a subinterpreter. It will also fail for a multi-phase init module that doesn’t explicitly support a per-interpreter GIL, when imported in an interpreter with its own GIL. - Note that this function is meant to accommodate an unusual case; one which is likely to eventually go away. There’s is a pretty good chance this is not what you were looking for. - You can get the same effect as this function by implementing the basic interface of multi-phase init ( - **PEP 489**- Warning - Using this function to disable the check can lead to unexpected behavior and even crashes. It should only be used during extension module development. - Added in version 3.12. 

- 
*class*importlib.util.LazyLoader(*loader*)[¶](#importlib.util.LazyLoader)
- A class which postpones the execution of the loader of a module until the module has an attribute accessed. - This class - **only**works with loaders that define- `exec_module()`- `create_module()`- `None`or a type for which its- `__class__`attribute can be mutated along with not using- [slots](../glossary.html#term-__slots__). Finally, modules which substitute the object placed into- `sys.modules`- `ValueError`- Note - For projects where startup time is critical, this class allows for potentially minimizing the cost of loading a module if it is never used. For projects where startup time is not essential then use of this class is - **heavily**discouraged due to error messages created during loading being postponed and thus occurring out of context.- Added in version 3.5. - Changed in version 3.6: Began calling - `create_module()`- `importlib.machinery.BuiltinImporter`- `importlib.machinery.ExtensionFileLoader`- 
*classmethod*factory(*loader*)[¶](#importlib.util.LazyLoader.factory)
- A class method which returns a callable that creates a lazy loader. This is meant to be used in situations where the loader is passed by class instead of by instance. - suffixes = importlib.machinery.SOURCE_SUFFIXES loader = importlib.machinery.SourceFileLoader lazy_loader = importlib.util.LazyLoader.factory(loader) finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes)) 
 
- 

## Examples[¶](#examples)

### Importing programmatically[¶](#importing-programmatically)

To programmatically import a module, use [ importlib.import_module()](#importlib.import_module).

```
import importlib
itertools = importlib.import_module('itertools')
```
### Checking if a module can be imported[¶](#checking-if-a-module-can-be-imported)

If you need to find out if a module can be imported without actually doing the
import, then you should use [ importlib.util.find_spec()](#importlib.util.find_spec).

Note that if `name` is a submodule (contains a dot),
[ importlib.util.find_spec()](#importlib.util.find_spec) will import the parent module.

```
import importlib.util
import sys
# For illustrative purposes.
name = 'itertools'
if name in sys.modules:
    print(f"{name!r} already in sys.modules")
elif (spec := importlib.util.find_spec(name)) is not None:
    # If you chose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    print(f"{name!r} has been imported")
else:
    print(f"can't find the {name!r} module")
```
### Importing a source file directly[¶](#importing-a-source-file-directly)

This recipe should be used with caution: it is an approximation of an import
statement where the file path is specified directly, rather than
[ sys.path](sys.html#sys.path) being searched. Alternatives should first be considered first,
such as modifying 

`sys.path` when a proper module is required, or using
[when the global namespace resulting from running a Python file is appropriate.](runpy.html#runpy.run_path)

`runpy.run_path()`To import a Python source file directly from a path, use the following recipe:

```
import importlib.util
import sys
def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
# For illustrative purposes only (use of `json` is arbitrary).
import json
file_path = json.__file__
module_name = json.__name__
# Similar outcome as `import json`.
json = import_from_path(module_name, file_path)
```
### Implementing lazy imports[¶](#implementing-lazy-imports)

The example below shows how to implement lazy imports:

```
>>> import importlib.util
>>> import sys
>>> def lazy_import(name):
...     spec = importlib.util.find_spec(name)
...     loader = importlib.util.LazyLoader(spec.loader)
...     spec.loader = loader
...     module = importlib.util.module_from_spec(spec)
...     sys.modules[name] = module
...     loader.exec_module(module)
...     return module
...
>>> lazy_typing = lazy_import("typing")
>>> #lazy_typing is a real module object,
>>> #but it is not loaded in memory yet.
>>> lazy_typing.TYPE_CHECKING
False
```
### Setting up an importer[¶](#setting-up-an-importer)

For deep customizations of import, you typically want to implement an
[importer](../glossary.html#term-importer). This means managing both the [finder](../glossary.html#term-finder) and [loader](../glossary.html#term-loader)
side of things. For finders there are two flavours to choose from depending on
your needs: a [meta path finder](../glossary.html#term-meta-path-finder) or a [path entry finder](../glossary.html#term-path-entry-finder). The
former is what you would put on [ sys.meta_path](sys.html#sys.meta_path) while the latter is what
you create using a 

[path entry hook](../glossary.html#term-path-entry-hook)on

[which works with](sys.html#sys.path_hooks)

`sys.path_hooks`[entries to potentially create a finder. This example will show you how to register your own importers so that import will use them (for creating an importer for yourself, read the documentation for the appropriate classes defined within this package):](sys.html#sys.path)

`sys.path````
import importlib.machinery
import sys
# For illustrative purposes only.
SpamMetaPathFinder = importlib.machinery.PathFinder
SpamPathEntryFinder = importlib.machinery.FileFinder
loader_details = (importlib.machinery.SourceFileLoader,
                  importlib.machinery.SOURCE_SUFFIXES)
# Setting up a meta path finder.
# Make sure to put the finder in the proper location in the list in terms of
# priority.
sys.meta_path.append(SpamMetaPathFinder)
# Setting up a path entry finder.
# Make sure to put the path hook in the proper location in the list in terms
# of priority.
sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))
```
### Approximating `importlib.import_module()`[¶](#approximating-importlib-import-module)

`importlib.import_module()`Import itself is implemented in Python code, making it possible to
expose most of the import machinery through importlib. The following
helps illustrate the various APIs that importlib exposes by providing an
approximate implementation of
[ importlib.import_module()](#importlib.import_module):

```
import importlib.util
import sys
def import_module(name, package=None):
    """An approximate implementation of import."""
    absolute_name = importlib.util.resolve_name(name, package)
    try:
        return sys.modules[absolute_name]
    except KeyError:
        pass
    path = None
    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.__spec__.submodule_search_locations
    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        msg = f'No module named {absolute_name!r}'
        raise ModuleNotFoundError(msg, name=absolute_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[absolute_name] = module
    spec.loader.exec_module(module)
    if path is not None:
        setattr(parent_module, child_name, module)
    return module
```