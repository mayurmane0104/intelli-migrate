# zipimport — Import modules from Zip archives — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/zipimport.html](https://docs.python.org/library/zipimport.html)

---

`zipimport` — Import modules from Zip archives[¶](#module-zipimport)

**Source code:** [Lib/zipimport.py](https://github.com/python/cpython/tree/3.14/Lib/zipimport.py)

This module adds the ability to import Python modules (`*.py`,
`*.pyc`) and packages from ZIP-format archives. It is usually not
needed to use the `zipimport` module explicitly; it is automatically used
by the built-in [ import](../reference/simple_stmts.html#import) mechanism for 

[items that are paths to ZIP archives.](sys.html#sys.path)

`sys.path`Typically, [ sys.path](sys.html#sys.path) is a list of directory names as strings.  This module
also allows an item of 

`sys.path` to be a string naming a ZIP file archive.
The ZIP archive can contain a subdirectory structure to support package imports,
and a path within the archive can be specified to only import from a
subdirectory.  For example, the path `example.zip/lib/` would only
import from the `lib/` subdirectory within the archive.Any files may be present in the ZIP archive, but importers are only invoked for
`.py` and `.pyc` files.  ZIP import of dynamic modules
(`.pyd`, `.so`) is disallowed. Note that if an archive only contains
`.py` files, Python will not attempt to modify the archive by adding the
corresponding `.pyc` file, meaning that if a ZIP archive
doesn’t contain `.pyc` files, importing may be rather slow.

Changed in version 3.13: ZIP64 is supported

Changed in version 3.8: Previously, ZIP archives with an archive comment were not supported.

See also

- [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
- Documentation on the ZIP file format by Phil Katz, the creator of the format and algorithms used. 
- **PEP 273**
- Written by James C. Ahlstrom, who also provided an implementation. Python 2.3 follows the specification in - **PEP 273**- **PEP 302**
- `importlib`
- Package providing the relevant protocols for all importers to implement. 

This module defines an exception:

- 
*exception*zipimport.ZipImportError[¶](#zipimport.ZipImportError)
- Exception raised by zipimporter objects. It’s a subclass of - `ImportError`- `ImportError`, too.

## zipimporter Objects[¶](#zipimporter-objects)

[ zipimporter](#zipimport.zipimporter) is the class for importing ZIP files.

- 
*class*zipimport.zipimporter(*archivepath*)[¶](#zipimport.zipimporter)
- Create a new zipimporter instance. - *archivepath*must be a path to a ZIP file, or to a specific path within a ZIP file. For example, an- *archivepath*of- `foo/bar.zip/lib`will look for modules in the- `lib`directory inside the ZIP file- `foo/bar.zip`(provided that it exists).- `ZipImportError`- *archivepath*doesn’t point to a valid ZIP archive.- Changed in version 3.12: Methods - `find_loader()`and- `find_module()`, deprecated in 3.10 are now removed. Use- `find_spec()`- 
create_module(*spec*)[¶](#zipimport.zipimporter.create_module)
- Implementation of - `importlib.abc.Loader.create_module()`- `None`- Added in version 3.10. 
 - 
exec_module(*module*)[¶](#zipimport.zipimporter.exec_module)
- Implementation of - `importlib.abc.Loader.exec_module()`- Added in version 3.10. 
 - 
find_spec(*fullname*,*target=None*)[¶](#zipimport.zipimporter.find_spec)
- An implementation of - `importlib.abc.PathEntryFinder.find_spec()`- Added in version 3.10. 
 - 
get_code(*fullname*)[¶](#zipimport.zipimporter.get_code)
- Return the code object for the specified module. Raise - `ZipImportError`
 - 
get_data(*pathname*)[¶](#zipimport.zipimporter.get_data)
- Return the data associated with - *pathname*. Raise- `OSError`
 - 
get_filename(*fullname*)[¶](#zipimport.zipimporter.get_filename)
- Return the value - `__file__`would be set to if the specified module was imported. Raise- `ZipImportError`- Added in version 3.1. 
 - 
get_source(*fullname*)[¶](#zipimport.zipimporter.get_source)
- Return the source code for the specified module. Raise - `ZipImportError`- `None`
 - 
is_package(*fullname*)[¶](#zipimport.zipimporter.is_package)
- Return - `True`if the module specified by- *fullname*is a package. Raise- `ZipImportError`
 - 
load_module(*fullname*)[¶](#zipimport.zipimporter.load_module)
- Load the module specified by - *fullname*.- *fullname*must be the fully qualified (dotted) module name. Returns the imported module on success, raises- `ZipImportError`- Deprecated since version 3.10, will be removed in version 3.15: Use - `exec_module()`
 - 
invalidate_caches()[¶](#zipimport.zipimporter.invalidate_caches)
- Clear out the internal cache of information about files found within the ZIP archive. - Added in version 3.10. 
 - 
archive[¶](#zipimport.zipimporter.archive)
- The file name of the importer’s associated ZIP file, without a possible subpath. 
 - 
prefix[¶](#zipimport.zipimporter.prefix)
- The subpath within the ZIP file where modules are searched. This is the empty string for zipimporter objects which point to the root of the ZIP file. 
 - The - `archive`- `prefix`- *archivepath*argument given to the- `zipimporter`constructor.
- 
create_module(

## Examples[¶](#examples)

Here is an example that imports a module from a ZIP archive - note that the
`zipimport` module is not explicitly used.

```
$ unzip -l example_archive.zip
Archive:  example_archive.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     8467  01-01-00 12:30   example.py
 --------                   -------
     8467                   1 file
```
```
>>> import sys
>>> # Add the archive to the front of the module search path
>>> sys.path.insert(0, 'example_archive.zip')
>>> import example
>>> example.__file__
'example_archive.zip/example.py'
```