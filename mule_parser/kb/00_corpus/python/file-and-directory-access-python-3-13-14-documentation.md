# File and Directory Access — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/filesys.html](https://docs.python.org/3.13/library/filesys.html)

---

# File and Directory Access[¶](#file-and-directory-access)

The modules described in this chapter deal with disk files and directories. For example, there are modules for reading the properties of files, manipulating paths in a portable way, and creating temporary files. The full list of modules in this chapter is:

- `pathlib`— Object-oriented filesystem paths
- `os.path`— Common pathname manipulations
- `stat`— Interpreting- `stat()`results
- `filecmp`— File and Directory Comparisons
- `tempfile`— Generate temporary files and directories
- `glob`— Unix style pathname pattern expansion
- `fnmatch`— Unix filename pattern matching
- `linecache`— Random access to text lines
- `shutil`— High-level file operations

See also

- Module `os`
- Operating system interfaces, including functions to work with files at a lower level than Python - [file objects](../glossary.html#term-file-object).
- Module `io`
- Python’s built-in I/O library, including both abstract classes and some concrete classes such as file I/O. 
- Built-in function `open()`
- The standard way to open files for reading and writing with Python.