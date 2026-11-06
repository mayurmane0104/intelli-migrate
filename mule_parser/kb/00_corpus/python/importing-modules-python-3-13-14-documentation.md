# Importing Modules — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/import.html](https://docs.python.org/3.13/c-api/import.html)

---

# Importing Modules[¶](#importing-modules)

- 
[PyObject](structures.html#c.PyObject)*PyImport_ImportModule(const char *name)[¶](#c.PyImport_ImportModule)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is a wrapper around - `PyImport_Import()`- [PyObject](structures.html#c.PyObject)*.

- 
[PyObject](structures.html#c.PyObject)*PyImport_ImportModuleNoBlock(const char *name)[¶](#c.PyImport_ImportModuleNoBlock)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This function is a deprecated alias of - `PyImport_ImportModule()`- Changed in version 3.3: This function used to fail immediately when the import lock was held by another thread. In Python 3.3 though, the locking scheme switched to per-module locks for most purposes, so this function’s special behaviour isn’t needed anymore. - Deprecated since version 3.13, will be removed in version 3.15: Use - `PyImport_ImportModule()`

- 
[PyObject](structures.html#c.PyObject)*PyImport_ImportModuleEx(const char *name,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals,[PyObject](structures.html#c.PyObject)*fromlist)[¶](#c.PyImport_ImportModuleEx)
- *Return value: New reference.*- Import a module. This is best described by referring to the built-in Python function - `__import__()`- The return value is a new reference to the imported module or top-level package, or - `NULL`with an exception set on failure. Like for- `__import__()`- *fromlist*was given.- Failing imports remove incomplete module objects, like with - `PyImport_ImportModule()`

- 
[PyObject](structures.html#c.PyObject)*PyImport_ImportModuleLevelObject([PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals,[PyObject](structures.html#c.PyObject)*fromlist, int level)[¶](#c.PyImport_ImportModuleLevelObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Import a module. This is best described by referring to the built-in Python function - `__import__()`- `__import__()`function calls this function directly.- The return value is a new reference to the imported module or top-level package, or - `NULL`with an exception set on failure. Like for- `__import__()`- *fromlist*was given.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyImport_ImportModuleLevel(const char *name,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals,[PyObject](structures.html#c.PyObject)*fromlist, int level)[¶](#c.PyImport_ImportModuleLevel)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyImport_ImportModuleLevelObject()`- Changed in version 3.3: Negative values for - *level*are no longer accepted.

- 
[PyObject](structures.html#c.PyObject)*PyImport_Import([PyObject](structures.html#c.PyObject)*name)[¶](#c.PyImport_Import)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is a higher-level interface that calls the current “import hook function” (with an explicit - *level*of 0, meaning absolute import). It invokes the- `__import__()`- `__builtins__`of the current globals. This means that the import is done using whatever import hooks are installed in the current environment.- This function always uses absolute imports. 

- 
[PyObject](structures.html#c.PyObject)*PyImport_ReloadModule([PyObject](structures.html#c.PyObject)*m)[¶](#c.PyImport_ReloadModule)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Reload a module. Return a new reference to the reloaded module, or - `NULL`with an exception set on failure (the module still exists in this case).

- 
[PyObject](structures.html#c.PyObject)*PyImport_AddModuleRef(const char *name)[¶](#c.PyImport_AddModuleRef)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return the module object corresponding to a module name. - The - *name*argument may be of the form- `package.module`. First check the modules dictionary if there’s one there, and if not, create a new one and insert it in the modules dictionary.- Return a - [strong reference](../glossary.html#term-strong-reference)to the module on success. Return- `NULL`with an exception set on failure.- The module name - *name*is decoded from UTF-8.- This function does not load or import the module; if the module wasn’t already loaded, you will get an empty module object. Use - `PyImport_ImportModule()`- *name*are not created if not already present.- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyImport_AddModuleObject([PyObject](structures.html#c.PyObject)*name)[¶](#c.PyImport_AddModuleObject)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Similar to - `PyImport_AddModuleRef()`- [borrowed reference](../glossary.html#term-borrowed-reference)and- *name*is a Python- `str`- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyImport_AddModule(const char *name)[¶](#c.PyImport_AddModule)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyImport_AddModuleRef()`- [borrowed reference](../glossary.html#term-borrowed-reference).

- 
[PyObject](structures.html#c.PyObject)*PyImport_ExecCodeModule(const char *name,[PyObject](structures.html#c.PyObject)*co)[¶](#c.PyImport_ExecCodeModule)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Given a module name (possibly of the form - `package.module`) and a code object read from a Python bytecode file or obtained from the built-in function- `compile()`- `NULL`with an exception set if an error occurred.- *name*is removed from- `sys.modules`- *name*was already in- `sys.modules`on entry to- `PyImport_ExecCodeModule()`- `sys.modules`is dangerous, as imports of such modules have no way to know that the module object is an unknown (and probably damaged with respect to the module author’s intents) state.- The module’s - `__spec__`- `__loader__`- `__loader__`(if set) and to an instance of- `SourceFileLoader`- The module’s - `__file__`- `co_filename`- `__cached__`- This function will reload the module if it was already imported. See - `PyImport_ReloadModule()`- If - *name*points to a dotted name of the form- `package.module`, any package structures not already created will still not be created.- See also - `PyImport_ExecCodeModuleEx()`- `PyImport_ExecCodeModuleWithPathnames()`- Changed in version 3.12: The setting of - `__cached__`- `__loader__`- `ModuleSpec`

- 
[PyObject](structures.html#c.PyObject)*PyImport_ExecCodeModuleEx(const char *name,[PyObject](structures.html#c.PyObject)*co, const char *pathname)[¶](#c.PyImport_ExecCodeModuleEx)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Like - `PyImport_ExecCodeModule()`- `__file__`- *pathname*if it is non-- `NULL`.- See also - `PyImport_ExecCodeModuleWithPathnames()`

- 
[PyObject](structures.html#c.PyObject)*PyImport_ExecCodeModuleObject([PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*co,[PyObject](structures.html#c.PyObject)*pathname,[PyObject](structures.html#c.PyObject)*cpathname)[¶](#c.PyImport_ExecCodeModuleObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Like - `PyImport_ExecCodeModuleEx()`- `__cached__`- *cpathname*if it is non-- `NULL`. Of the three functions, this is the preferred one to use.- Added in version 3.3. - Changed in version 3.12: Setting - `__cached__`- `ModuleSpec`

- 
[PyObject](structures.html#c.PyObject)*PyImport_ExecCodeModuleWithPathnames(const char *name,[PyObject](structures.html#c.PyObject)*co, const char *pathname, const char *cpathname)[¶](#c.PyImport_ExecCodeModuleWithPathnames)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Like - `PyImport_ExecCodeModuleObject()`- *name*,- *pathname*and- *cpathname*are UTF-8 encoded strings. Attempts are also made to figure out what the value for- *pathname*should be from- *cpathname*if the former is set to- `NULL`.- Added in version 3.2. - Changed in version 3.3: Uses - `imp.source_from_cache()`in calculating the source path if only the bytecode path is provided.- Changed in version 3.12: No longer uses the removed - `imp`module.

- 
long PyImport_GetMagicNumber()[¶](#c.PyImport_GetMagicNumber)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the magic number for Python bytecode files (a.k.a. - `.pyc`file). The magic number should be present in the first four bytes of the bytecode file, in little-endian byte order. Returns- `-1`on error.- Changed in version 3.3: Return value of - `-1`upon failure.

- 
const char *PyImport_GetMagicTag()[¶](#c.PyImport_GetMagicTag)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the magic tag string for - **PEP 3147**- `sys.implementation.cache_tag`is authoritative and should be used instead of this function.- Added in version 3.2. 

- 
[PyObject](structures.html#c.PyObject)*PyImport_GetModuleDict()[¶](#c.PyImport_GetModuleDict)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the dictionary used for the module administration (a.k.a. - `sys.modules`). Note that this is a per-interpreter variable.

- 
[PyObject](structures.html#c.PyObject)*PyImport_GetModule([PyObject](structures.html#c.PyObject)*name)[¶](#c.PyImport_GetModule)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.- Return the already imported module with the given name. If the module has not been imported yet then returns - `NULL`but does not set an error. Returns- `NULL`and sets an error if the lookup failed.- Added in version 3.7. 

- 
[PyObject](structures.html#c.PyObject)*PyImport_GetImporter([PyObject](structures.html#c.PyObject)*path)[¶](#c.PyImport_GetImporter)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a finder object for a - `sys.path`- `pkg.__path__`item- *path*, possibly by fetching it from the- `sys.path_importer_cache`- `sys.path_hooks`- `None`if no hook could; this tells our caller that the- [path based finder](../glossary.html#term-path-based-finder)could not find a finder for this path item. Cache the result in- `sys.path_importer_cache`. Return a new reference to the finder object.

- 
int PyImport_ImportFrozenModuleObject([PyObject](structures.html#c.PyObject)*name)[¶](#c.PyImport_ImportFrozenModuleObject)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Load a frozen module named - *name*. Return- `1`for success,- `0`if the module is not found, and- `-1`with an exception set if the initialization failed. To access the imported module on a successful load, use- `PyImport_ImportModule()`- Added in version 3.3. - Changed in version 3.4: The - `__file__`attribute is no longer set on the module.

- 
int PyImport_ImportFrozenModule(const char *name)[¶](#c.PyImport_ImportFrozenModule)
- *Part of the*- [Stable ABI](stable.html#stable).- Similar to - `PyImport_ImportFrozenModuleObject()`

- 
struct _frozen[¶](#c._frozen)
- This is the structure type definition for frozen module descriptors, as generated by the - **freeze**utility (see- `Tools/freeze/`in the Python source distribution). Its definition, found in- `Include/import.h`, is:- struct _frozen { const char *name; const unsigned char *code; int size; bool is_package; }; - Changed in version 3.11: The new - `is_package`field indicates whether the module is a package or not. This replaces setting the- `size`field to a negative value.

- 
const struct [_frozen](#c._frozen)*PyImport_FrozenModules[¶](#c.PyImport_FrozenModules)
- This pointer is initialized to point to an array of - `_frozen`- `NULL`or zero. When a frozen module is imported, it is searched in this table. Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.

- 
int PyImport_AppendInittab(const char *name, [PyObject](structures.html#c.PyObject)*(*initfunc)(void))[¶](#c.PyImport_AppendInittab)
- *Part of the*- [Stable ABI](stable.html#stable).- Add a single module to the existing table of built-in modules. This is a convenience wrapper around - `PyImport_ExtendInittab()`- `-1`if the table could not be extended. The new module can be imported by the name- *name*, and uses the function- *initfunc*as the initialization function called on the first attempted import. This should be called before- `Py_Initialize()`

- 
struct _inittab[¶](#c._inittab)
- Structure describing a single entry in the list of built-in modules. Programs which embed Python may use an array of these structures in conjunction with - `PyImport_ExtendInittab()`- 
const char *name[¶](#c._inittab.name)
- The module name, as an ASCII encoded string. 
 
- 
const char *name

- 
int PyImport_ExtendInittab(struct [_inittab](#c._inittab)*newtab)[¶](#c.PyImport_ExtendInittab)
- Add a collection of modules to the table of built-in modules. The - *newtab*array must end with a sentinel entry which contains- `NULL`for the- `name`- `0`on success or- `-1`if insufficient memory could be allocated to extend the internal table. In the event of failure, no modules are added to the internal table. This must be called before- `Py_Initialize()`- If Python is initialized multiple times, - `PyImport_AppendInittab()`- `PyImport_ExtendInittab()`

- 
struct [_inittab](#c._inittab)*PyImport_Inittab[¶](#c.PyImport_Inittab)
- The table of built-in modules used by Python initialization. Do not use this directly; use - `PyImport_AppendInittab()`- `PyImport_ExtendInittab()`