# Data Persistence — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/persistence.html](https://docs.python.org/3.13/library/persistence.html)

---

# Data Persistence[¶](#data-persistence)

The modules described in this chapter support storing Python data in a
persistent form on disk.  The [ pickle](pickle.html#module-pickle) and 

[modules can turn many Python data types into a stream of bytes and then recreate the objects from the bytes. The various DBM-related modules support a family of hash-based file formats that store a mapping of strings to other strings.](marshal.html#module-marshal)

`marshal`The list of modules described in this chapter is:

- `pickle`— Python object serialization
- `copyreg`— Register- `pickle`support functions
- `shelve`— Python object persistence
- `marshal`— Internal Python object serialization
- `dbm`— Interfaces to Unix “databases”
- `sqlite3`— DB-API 2.0 interface for SQLite databases- [Tutorial](sqlite3.html#tutorial)
- [Reference](sqlite3.html#reference)
- [How-to guides](sqlite3.html#how-to-guides)- [How to use placeholders to bind values in SQL queries](sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
- [How to adapt custom Python types to SQLite values](sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values)
- [How to convert SQLite values to custom Python types](sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types)
- [Adapter and converter recipes](sqlite3.html#adapter-and-converter-recipes)
- [How to use connection shortcut methods](sqlite3.html#how-to-use-connection-shortcut-methods)
- [How to use the connection context manager](sqlite3.html#how-to-use-the-connection-context-manager)
- [How to work with SQLite URIs](sqlite3.html#how-to-work-with-sqlite-uris)
- [How to create and use row factories](sqlite3.html#how-to-create-and-use-row-factories)
- [How to handle non-UTF-8 text encodings](sqlite3.html#how-to-handle-non-utf-8-text-encodings)
 
- [Explanation](sqlite3.html#explanation)