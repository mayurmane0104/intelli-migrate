# Deprecations — Python 3.14.6 documentation

**Source:** [https://docs.python.org/3/deprecations/index.html](https://docs.python.org/3/deprecations/index.html)

---

# Deprecations[¶](#deprecations)

## Pending removal in Python 3.15[¶](#pending-removal-in-python-3-15)

- The import system: - Setting - `__cached__`- `__spec__.cached`- `__cached__`will cease to be set or take into consideration by the import system or standard library. (- [gh-97879](https://github.com/python/cpython/issues/97879))
- Setting - `__package__`- `__spec__.parent`- `__package__`will cease to be set or take into consideration by the import system or standard library. (- [gh-97879](https://github.com/python/cpython/issues/97879))
 
- 
- The undocumented - `ctypes.SetPointerType()`function has been deprecated since Python 3.13.
 
- 
- The obsolete and rarely used - `CGIHTTPRequestHandler`- *Anything*is better than CGI to interface a web server with a request handler.
- The - `--cgi`flag to the- **python -m http.server**command-line interface has been deprecated since Python 3.13.
 
- 
- `load_module()`method: use- `exec_module()`instead.
 
- 
- `PurePath.is_reserved()`- `os.path.isreserved()`
 
- 
- `java_ver()`
 
- 
- The - *check_home*argument of- `sysconfig.is_python_build()`
 
- 
- `RLock()`
 
- 
- `types.CodeType`- `co_lnotab`- **PEP 626**- `DeprecationWarning`- [gh-101866](https://github.com/python/cpython/issues/101866).)
 
- 
- The undocumented keyword argument syntax for creating - `NamedTuple`- `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
- When using the functional syntax of - `TypedDict`- *fields*parameter (- `TD = TypedDict("TD")`) or passing- `None`(- `TD = TypedDict("TD", None)`) has been deprecated since Python 3.13. Use- `class TD(TypedDict): pass`or- `TD = TypedDict("TD", {})`to create a TypedDict with zero field.
- The - `typing.no_type_check_decorator()`- `typing`
 
- `wave`- The - `getmark()`- `setmark()`, and- `getmarkers()`- `Wave_read`- `Wave_write`
 
- 
- `load_module()`- `exec_module()`- [gh-125746](https://github.com/python/cpython/issues/125746).)
 

## Pending removal in Python 3.16[¶](#pending-removal-in-python-3-16)

- The import system: - Setting - `__loader__`- `__spec__.loader`- `__loader__`will cease to be set or taken into consideration by the import system or the standard library.
 
- 
- The - `'u'`format code (- `wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the- `'w'`format code (- `Py_UCS4`
 
- 
- `asyncio.iscoroutinefunction()`is deprecated and will be removed in Python 3.16; use- `inspect.iscoroutinefunction()`- [gh-122875](https://github.com/python/cpython/issues/122875).)
- `asyncio`- Users should use - `asyncio.run()`- `asyncio.Runner`- *loop_factory*to use the desired event loop implementation.- For example, to use - `asyncio.SelectorEventLoop`- import asyncio async def main(): ... asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop) - (Contributed by Kumar Aditya in - [gh-127949](https://github.com/python/cpython/issues/127949).)
 
- 
- Bitwise inversion on boolean types, - `~True`or- `~False`has been deprecated since Python 3.12, as it produces surprising and unintuitive results (- `-2`and- `-1`). Use- `not x`instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to- `int`explicitly (- `~int(x)`).
 
- 
- Calling the Python implementation of - `functools.reduce()`- *function*or- *sequence*as keyword arguments has been deprecated since Python 3.14.
 
- 
Support for custom logging handlers with the *strm*argument is deprecated and scheduled for removal in Python 3.16. Define handlers with the*stream*argument instead. (Contributed by Mariusz Felisiak in[gh-115032](https://github.com/python/cpython/issues/115032).)
- 
- Valid extensions start with a ‘.’ or are empty for - `mimetypes.MimeTypes.add_type()`- `ValueError`- [gh-75223](https://github.com/python/cpython/issues/75223).)
 
- 
- The - `ExecError`exception has been deprecated since Python 3.14. It has not been used by any function in- `shutil`since Python 3.4, and is now an alias of- `RuntimeError`
 
- 
- The - `Class.get_methods`
 
- `sys`- The - `_enablelegacywindowsfsencoding()`- `PYTHONLEGACYWINDOWSFSENCODING`
 
- 
- The - `sysconfig.expand_makefile_vars()`function has been deprecated since Python 3.14. Use the- `vars`argument of- `sysconfig.get_paths()`
 
- 
- The undocumented and unused - `TarFile.tarfile`attribute has been deprecated since Python 3.13.
 

## Pending removal in Python 3.17[¶](#pending-removal-in-python-3-17)

- 
- `collections.abc.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 
- 
- Before Python 3.14, old-style unions were implemented using the private class - `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like- `typing.get_origin()`- `typing.get_args()`
- `typing.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 

## Pending removal in Python 3.18[¶](#pending-removal-in-python-3-18)

## Pending removal in Python 3.19[¶](#pending-removal-in-python-3-19)

## Pending removal in future versions[¶](#pending-removal-in-future-versions)

The following APIs will be removed in the future, although there is currently no date scheduled for their removal.

- 
- Nesting argument groups and nesting mutually exclusive groups are deprecated. 
- Passing the undocumented keyword argument - *prefix_chars*to- `add_argument_group()`
- The - `argparse.FileType`
 
- 
- Generators: - `throw(type, exc, tb)`and- `athrow(type, exc, tb)`signature is deprecated: use- `throw(exc)`and- `athrow(exc)`instead, the single argument signature.
- Currently Python accepts numeric literals immediately followed by keywords, for example - `0in x`,- `1or x`,- `0if 1else 2`. It allows confusing and ambiguous expressions like- `[0x1for x in y]`(which can be interpreted as- `[0x1 for x in y]`or- `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords- `and`- `else`- `for`- `if`- `in`- `is`- `or`- [gh-87999](https://github.com/python/cpython/issues/87999))
- Support for - `__index__()`and- `__int__()`method returning non-int type: these methods will be required to return an instance of a strict subclass of- `int`
- Support for - `__float__()`method returning a strict subclass of- `float`- `float`.
- Support for - `__complex__()`method returning a strict subclass of- `complex`- `complex`.
- Passing a complex number as the - *real*or- *imag*argument in the- `complex()`- [gh-109218](https://github.com/python/cpython/issues/109218).)
 
- `calendar`- `calendar.January`and- `calendar.February`constants are deprecated and replaced by- `calendar.JANUARY`- `calendar.FEBRUARY`- [gh-103636](https://github.com/python/cpython/issues/103636).)
- `codecs`- `open()`- `codecs.open()`- [gh-133038](https://github.com/python/cpython/issues/133038))
- `codeobject.co_lnotab`- `codeobject.co_lines()`
- 
- `utcnow()`- `datetime.datetime.now(tz=datetime.UTC)`.
- `utcfromtimestamp()`- `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.
 
- `gettext`
- 
- `cache_from_source()`- *debug_override*parameter is deprecated: use the- *optimization*parameter instead.
 
- 
- `EntryPoints`tuple interface.
- Implicit - `None`on return values.
 
- `logging`- `warn()`method has been deprecated since Python 3.3, use- `warning()`
- `mailbox`
- `os`- `os.register_at_fork()`
- `pydoc.ErrorDuringImport`: A tuple value for- *exc_info*parameter is deprecated, use an exception instance.
- `re`- [gh-91760](https://github.com/python/cpython/issues/91760).)
- `sre_compile`,- `sre_constants`and- `sre_parse`modules.
- `shutil`- `rmtree()`- *onerror*parameter is deprecated in Python 3.12; use the- *onexc*parameter instead.
- `ssl`- `ssl.SSLContext`
- `ssl.SSLContext`- `set_npn_protocols()`- `selected_npn_protocol()`are deprecated: use ALPN instead.
- `ssl.OP_NO_SSL*`options
- `ssl.OP_NO_TLS*`options
- `ssl.PROTOCOL_SSLv3`
- `ssl.PROTOCOL_TLS`
- `ssl.PROTOCOL_TLSv1`
- `ssl.PROTOCOL_TLSv1_1`
- `ssl.PROTOCOL_TLSv1_2`
- `ssl.TLSVersion.SSLv3`
- `ssl.TLSVersion.TLSv1`
- `ssl.TLSVersion.TLSv1_1`
 
- `threading`- `threading.Condition.notifyAll()`: use- `notify_all()`
- `threading.Event.isSet()`: use- `is_set()`
- `threading.Thread.isDaemon()`,- `threading.Thread.setDaemon()`- `threading.Thread.daemon`
- `threading.Thread.getName()`,- `threading.Thread.setName()`- `threading.Thread.name`
- `threading.currentThread()`: use- `threading.current_thread()`
- `threading.activeCount()`: use- `threading.active_count()`
 
- The internal class - `typing._UnionGenericAlias`is no longer used to implement- `typing.Union`- [gh-105499](https://github.com/python/cpython/issues/105499).)
- `unittest.IsolatedAsyncioTestCase`- `None`from a test case.
- `urllib.parse`- `urlparse()`- `splitattr()`
- `splithost()`
- `splitnport()`
- `splitpasswd()`
- `splitport()`
- `splitquery()`
- `splittag()`
- `splittype()`
- `splituser()`
- `splitvalue()`
- `to_bytes()`
 
- `wsgiref`- `SimpleHandler.stdout.write()`should not do partial writes.
- `xml.etree.ElementTree`- `Element`- `True`. Prefer explicit- `len(elem)`or- `elem is not None`tests instead.
- `sys._clear_type_cache()`- `sys._clear_internal_caches()`

## C API deprecations[¶](#c-api-deprecations)

### Pending removal in Python 3.15[¶](#id1)

- The - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`
- `PyWeakref_GetObject()`- `PyWeakref_GET_OBJECT()`- `PyWeakref_GetRef()`- [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyWeakref_GetRef()`on Python 3.12 and older.
- `Py_UNICODE`- `Py_UNICODE_WIDE`macro: Use- `wchar_t`instead.
- `PyUnicode_AsDecodedObject()`: Use- `PyCodec_Decode()`
- `PyUnicode_AsDecodedUnicode()`: Use- `PyCodec_Decode()`- `str`- `bytes`
- `PyUnicode_AsEncodedObject()`: Use- `PyCodec_Encode()`
- `PyUnicode_AsEncodedUnicode()`: Use- `PyCodec_Encode()`- `bytes`- `str`
- Python initialization functions, deprecated in Python 3.13: - `Py_GetPath()`- `PyConfig_Get("module_search_paths")`- `sys.path`
- `Py_GetPrefix()`- `PyConfig_Get("base_prefix")`- `sys.base_prefix`- `PyConfig_Get("prefix")`(- `sys.prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.
- `Py_GetExecPrefix()`- `PyConfig_Get("base_exec_prefix")`- `sys.base_exec_prefix`- `PyConfig_Get("exec_prefix")`(- `sys.exec_prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.
- `Py_GetProgramFullPath()`- `PyConfig_Get("executable")`- `sys.executable`
- `Py_GetProgramName()`- `PyConfig_Get("executable")`- `sys.executable`
- `Py_GetPythonHome()`- `PyConfig_Get("home")`- `PYTHONHOME`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyConfig_Get()`
- Functions to configure Python’s initialization, deprecated in Python 3.11: - `PySys_SetArgvEx()`: Set- `PyConfig.argv`
- `PySys_SetArgv()`: Set- `PyConfig.argv`
- `Py_SetProgramName()`: Set- `PyConfig.program_name`
- `Py_SetPythonHome()`: Set- `PyConfig.home`
- `PySys_ResetWarnOptions()`- `sys.warnoptions`- `warnings.filters`instead.
 - The - `Py_InitializeFromConfig()`- `PyConfig`
- Global configuration variables: - `Py_DebugFlag`- `PyConfig.parser_debug`- `PyConfig_Get("parser_debug")`
- `Py_VerboseFlag`- `PyConfig.verbose`- `PyConfig_Get("verbose")`
- `Py_QuietFlag`- `PyConfig.quiet`- `PyConfig_Get("quiet")`
- `Py_InteractiveFlag`- `PyConfig.interactive`- `PyConfig_Get("interactive")`
- `Py_InspectFlag`- `PyConfig.inspect`- `PyConfig_Get("inspect")`
- `Py_OptimizeFlag`- `PyConfig.optimization_level`- `PyConfig_Get("optimization_level")`
- `Py_NoSiteFlag`- `PyConfig.site_import`- `PyConfig_Get("site_import")`
- `Py_BytesWarningFlag`- `PyConfig.bytes_warning`- `PyConfig_Get("bytes_warning")`
- `Py_FrozenFlag`- `PyConfig.pathconfig_warnings`- `PyConfig_Get("pathconfig_warnings")`
- `Py_IgnoreEnvironmentFlag`- `PyConfig.use_environment`- `PyConfig_Get("use_environment")`
- `Py_DontWriteBytecodeFlag`- `PyConfig.write_bytecode`- `PyConfig_Get("write_bytecode")`
- `Py_NoUserSiteDirectory`- `PyConfig.user_site_directory`- `PyConfig_Get("user_site_directory")`
- `Py_UnbufferedStdioFlag`- `PyConfig.buffered_stdio`- `PyConfig_Get("buffered_stdio")`
- `Py_HashRandomizationFlag`- `PyConfig.use_hash_seed`- `PyConfig.hash_seed`- `PyConfig_Get("hash_seed")`
- `Py_IsolatedFlag`- `PyConfig.isolated`- `PyConfig_Get("isolated")`
- `Py_LegacyWindowsFSEncodingFlag`- `PyPreConfig.legacy_windows_fs_encoding`- `PyConfig_Get("legacy_windows_fs_encoding")`
- `Py_LegacyWindowsStdioFlag`- `PyConfig.legacy_windows_stdio`- `PyConfig_Get("legacy_windows_stdio")`
- `Py_FileSystemDefaultEncoding`,- `Py_HasFileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`- `PyConfig_Get("filesystem_encoding")`
- `Py_FileSystemDefaultEncodeErrors`: Use- `PyConfig.filesystem_errors`- `PyConfig_Get("filesystem_errors")`
- `Py_UTF8Mode`: Use- `PyPreConfig.utf8_mode`- `PyConfig_Get("utf8_mode")`- `Py_PreInitialize()`
 - The - `Py_InitializeFromConfig()`- `PyConfig`- `PyConfig_Get()`

### Pending removal in Python 3.18[¶](#id2)

- The following private functions are deprecated and planned for removal in Python 3.18: - `_PyBytes_Join()`: use- `PyBytes_Join()`
- `_PyDict_GetItemStringWithError()`: use- `PyDict_GetItemStringRef()`
- `_PyDict_Pop()`: use- `PyDict_Pop()`
- `_PyLong_Sign()`: use- `PyLong_GetSign()`
- `_PyLong_FromDigits()`and- `_PyLong_New()`: use- `PyLongWriter_Create()`
- `_PyThreadState_UncheckedGet()`: use- `PyThreadState_GetUnchecked()`
- `_PyUnicode_AsString()`: use- `PyUnicode_AsUTF8()`
- `_PyUnicodeWriter_Init()`: replace- `_PyUnicodeWriter_Init(&writer)`with- `writer = PyUnicodeWriter_Create(0)`
- `_PyUnicodeWriter_Finish()`: replace- `_PyUnicodeWriter_Finish(&writer)`with- `PyUnicodeWriter_Finish(writer)`
- `_PyUnicodeWriter_Dealloc()`: replace- `_PyUnicodeWriter_Dealloc(&writer)`with- `PyUnicodeWriter_Discard(writer)`
- `_PyUnicodeWriter_WriteChar()`: replace- `_PyUnicodeWriter_WriteChar(&writer, ch)`with- `PyUnicodeWriter_WriteChar(writer, ch)`
- `_PyUnicodeWriter_WriteStr()`: replace- `_PyUnicodeWriter_WriteStr(&writer, str)`with- `PyUnicodeWriter_WriteStr(writer, str)`
- `_PyUnicodeWriter_WriteSubstring()`: replace- `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)`with- `PyUnicodeWriter_WriteSubstring(writer, str, start, end)`
- `_PyUnicodeWriter_WriteASCIIString()`: replace- `_PyUnicodeWriter_WriteASCIIString(&writer, str)`with- `PyUnicodeWriter_WriteASCII(writer, str)`
- `_PyUnicodeWriter_WriteLatin1String()`: replace- `_PyUnicodeWriter_WriteLatin1String(&writer, str)`with- `PyUnicodeWriter_WriteUTF8(writer, str)`
- `_PyUnicodeWriter_Prepare()`: (no replacement).
- `_PyUnicodeWriter_PrepareKind()`: (no replacement).
- `_Py_HashPointer()`: use- `Py_HashPointer()`
- `_Py_fopen_obj()`: use- `Py_fopen()`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get these new public functions on Python 3.13 and older. (Contributed by Victor Stinner in- [gh-128863](https://github.com/python/cpython/issues/128863).)

### Pending removal in future versions[¶](#id3)

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

- `Py_TPFLAGS_HAVE_FINALIZE`
- `PyErr_Fetch()`- `PyErr_GetRaisedException()`
- `PyErr_NormalizeException()`- `PyErr_GetRaisedException()`
- `PyErr_Restore()`- `PyErr_SetRaisedException()`
- `PyModule_GetFilename()`- `PyModule_GetFilenameObject()`
- `PyOS_AfterFork()`- `PyOS_AfterFork_Child()`
- `PySlice_GetIndicesEx()`- `PySlice_Unpack()`- `PySlice_AdjustIndices()`
- `PyUnicode_READY()`
- `PyErr_Display()`: Use- `PyErr_DisplayException()`
- `_PyErr_ChainExceptions()`: Use- `_PyErr_ChainExceptions1()`instead.
- `PyBytesObject.ob_shash`member: call- `PyObject_Hash()`
- Thread Local Storage (TLS) API: - `PyThread_create_key()`- `PyThread_tss_alloc()`
- `PyThread_delete_key()`- `PyThread_tss_free()`
- `PyThread_set_key_value()`- `PyThread_tss_set()`
- `PyThread_get_key_value()`- `PyThread_tss_get()`
- `PyThread_delete_key_value()`- `PyThread_tss_delete()`
- `PyThread_ReInitTLS()`