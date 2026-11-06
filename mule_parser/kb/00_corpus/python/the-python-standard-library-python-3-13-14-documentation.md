# The Python Standard Library — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/index.html](https://docs.python.org/3.13/library/index.html)

---

# The Python Standard Library[¶](#the-python-standard-library)

While [The Python Language Reference](../reference/index.html#reference-index) describes the exact syntax and
semantics of the Python language, this library reference manual
describes the standard library that is distributed with Python. It also
describes some of the optional components that are commonly included
in Python distributions.

Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.

In addition to the standard library, there is an active collection of
hundreds of thousands of components (from individual programs and modules to
packages and entire application development frameworks), available from
the [Python Package Index](https://pypi.org).

- [Introduction](intro.html)
- [Built-in Functions](functions.html)
- [Built-in Constants](constants.html)
- [Built-in Types](stdtypes.html)- [Truth Value Testing](stdtypes.html#truth-value-testing)
- [Boolean Operations —](stdtypes.html#boolean-operations-and-or-not)- `and`,- `or`,- `not`
- [Comparisons](stdtypes.html#comparisons)
- [Numeric Types —](stdtypes.html#numeric-types-int-float-complex)- `int`,- `float`,- `complex`
- [Boolean Type -](stdtypes.html#boolean-type-bool)- `bool`
- [Iterator Types](stdtypes.html#iterator-types)
- [Sequence Types —](stdtypes.html#sequence-types-list-tuple-range)- `list`,- `tuple`,- `range`
- [Text Sequence Type —](stdtypes.html#text-sequence-type-str)- `str`
- [Binary Sequence Types —](stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)- `bytes`,- `bytearray`,- `memoryview`
- [Set Types —](stdtypes.html#set-types-set-frozenset)- `set`,- `frozenset`
- [Mapping Types —](stdtypes.html#mapping-types-dict)- `dict`
- [Context Manager Types](stdtypes.html#context-manager-types)
- [Type Annotation Types — Generic Alias, Union](stdtypes.html#type-annotation-types-generic-alias-union)
- [Other Built-in Types](stdtypes.html#other-built-in-types)
- [Special Attributes](stdtypes.html#special-attributes)
- [Integer string conversion length limitation](stdtypes.html#integer-string-conversion-length-limitation)
 
- [Built-in Exceptions](exceptions.html)
- [Text Processing Services](text.html)- `string`— Common string operations
- `re`— Regular expression operations
- `difflib`— Helpers for computing deltas
- `textwrap`— Text wrapping and filling
- `unicodedata`— Unicode Database
- `stringprep`— Internet String Preparation
- `readline`— GNU readline interface
- `rlcompleter`— Completion function for GNU readline
 
- [Binary Data Services](binary.html)
- [Data Types](datatypes.html)- `datetime`— Basic date and time types
- `zoneinfo`— IANA time zone support
- `calendar`— General calendar-related functions
- `collections`— Container datatypes
- `collections.abc`— Abstract Base Classes for Containers
- `heapq`— Heap queue algorithm
- `bisect`— Array bisection algorithm
- `array`— Efficient arrays of numeric values
- `weakref`— Weak references
- `types`— Dynamic type creation and names for built-in types
- `copy`— Shallow and deep copy operations
- `pprint`— Data pretty printer
- `reprlib`— Alternate- `repr()`implementation
- `enum`— Support for enumerations
- `graphlib`— Functionality to operate with graph-like structures
 
- [Numeric and Mathematical Modules](numeric.html)
- [Functional Programming Modules](functional.html)
- [File and Directory Access](filesys.html)- `pathlib`— Object-oriented filesystem paths
- `os.path`— Common pathname manipulations
- `stat`— Interpreting- `stat()`results
- `filecmp`— File and Directory Comparisons
- `tempfile`— Generate temporary files and directories
- `glob`— Unix style pathname pattern expansion
- `fnmatch`— Unix filename pattern matching
- `linecache`— Random access to text lines
- `shutil`— High-level file operations
 
- [Data Persistence](persistence.html)
- [Data Compression and Archiving](archiving.html)
- [File Formats](fileformats.html)
- [Cryptographic Services](crypto.html)
- [Generic Operating System Services](allos.html)- `os`— Miscellaneous operating system interfaces
- `io`— Core tools for working with streams
- `time`— Time access and conversions
- `logging`— Logging facility for Python
- `logging.config`— Logging configuration
- `logging.handlers`— Logging handlers
- `platform`— Access to underlying platform’s identifying data
- `errno`— Standard errno system symbols
- `ctypes`— A foreign function library for Python
 
- [Command-line interface libraries](cmdlinelibs.html)- `argparse`— Parser for command-line options, arguments and subcommands
- `optparse`— Parser for command line options
- `getpass`— Portable password input
- `fileinput`— Iterate over lines from multiple input streams
- `curses`— Terminal handling for character-cell displays
- `curses.textpad`— Text input widget for curses programs
- `curses.ascii`— Utilities for ASCII characters
- `curses.panel`— A panel stack extension for curses
- `cmd`— Support for line-oriented command interpreters
 
- [Concurrent Execution](concurrency.html)- `threading`— Thread-based parallelism
- `multiprocessing`— Process-based parallelism
- `multiprocessing.shared_memory`— Shared memory for direct access across processes
- [The](concurrent.html)- `concurrent`package
- `concurrent.futures`— Launching parallel tasks
- `subprocess`— Subprocess management
- `sched`— Event scheduler
- `queue`— A synchronized queue class
- `contextvars`— Context Variables
- `_thread`— Low-level threading API
 
- [Networking and Interprocess Communication](ipc.html)
- [Internet Data Handling](netdata.html)- `email`— An email and MIME handling package
- `json`— JSON encoder and decoder
- `mailbox`— Manipulate mailboxes in various formats
- `mimetypes`— Map filenames to MIME types
- `base64`— Base16, Base32, Base64, Base85 Data Encodings
- `binascii`— Convert between binary and ASCII
- `quopri`— Encode and decode MIME quoted-printable data
 
- [Structured Markup Processing Tools](markup.html)- `html`— HyperText Markup Language support
- `html.parser`— Simple HTML and XHTML parser
- `html.entities`— Definitions of HTML general entities
- [XML Processing Modules](xml.html)
- `xml.etree.ElementTree`— The ElementTree XML API
- `xml.dom`— The Document Object Model API
- `xml.dom.minidom`— Minimal DOM implementation
- `xml.dom.pulldom`— Support for building partial DOM trees
- `xml.sax`— Support for SAX2 parsers
- `xml.sax.handler`— Base classes for SAX handlers
- `xml.sax.saxutils`— SAX Utilities
- `xml.sax.xmlreader`— Interface for XML parsers
- `xml.parsers.expat`— Fast XML parsing using Expat
 
- [Internet Protocols and Support](internet.html)- `webbrowser`— Convenient web-browser controller
- `wsgiref`— WSGI Utilities and Reference Implementation
- `urllib`— URL handling modules
- `urllib.request`— Extensible library for opening URLs
- `urllib.response`— Response classes used by urllib
- `urllib.parse`— Parse URLs into components
- `urllib.error`— Exception classes raised by urllib.request
- `urllib.robotparser`— Parser for robots.txt
- `http`— HTTP modules
- `http.client`— HTTP protocol client
- `ftplib`— FTP protocol client
- `poplib`— POP3 protocol client
- `imaplib`— IMAP4 protocol client
- `smtplib`— SMTP protocol client
- `uuid`— UUID objects according to- **RFC 4122**
- `socketserver`— A framework for network servers
- `http.server`— HTTP servers
- `http.cookies`— HTTP state management
- `http.cookiejar`— Cookie handling for HTTP clients
- `xmlrpc`— XMLRPC server and client modules
- `xmlrpc.client`— XML-RPC client access
- `xmlrpc.server`— Basic XML-RPC servers
- `ipaddress`— IPv4/IPv6 manipulation library
 
- [Multimedia Services](mm.html)
- [Internationalization](i18n.html)
- [Graphical user interfaces with Tk](tk.html)- `tkinter`— Python interface to Tcl/Tk
- `tkinter.colorchooser`— Color choosing dialog
- `tkinter.font`— Tkinter font wrapper
- [Tkinter Dialogs](dialog.html)
- `tkinter.messagebox`— Tkinter message prompts
- `tkinter.scrolledtext`— Scrolled Text Widget
- `tkinter.dnd`— Drag and drop support
- `tkinter.ttk`— Tk themed widgets
- [IDLE — Python editor and shell](idle.html)
- `turtle`— Turtle graphics
 
- [Development Tools](development.html)- `typing`— Support for type hints
- `pydoc`— Documentation generator and online help system
- [Python Development Mode](devmode.html)
- `doctest`— Test interactive Python examples
- `unittest`— Unit testing framework
- `unittest.mock`— mock object library
- `unittest.mock`— getting started
- `test`— Regression tests package for Python
- `test.support`— Utilities for the Python test suite
- `test.support.socket_helper`— Utilities for socket tests
- `test.support.script_helper`— Utilities for the Python execution tests
- `test.support.bytecode_helper`— Support tools for testing correct bytecode generation
- `test.support.threading_helper`— Utilities for threading tests
- `test.support.os_helper`— Utilities for os tests
- `test.support.import_helper`— Utilities for import tests
- `test.support.warnings_helper`— Utilities for warnings tests
 
- [Debugging and Profiling](debug.html)
- [Software Packaging and Distribution](distribution.html)
- [Python Runtime Services](python.html)- `sys`— System-specific parameters and functions
- `sys.monitoring`— Execution event monitoring
- `sysconfig`— Provide access to Python’s configuration information
- `builtins`— Built-in objects
- `__main__`— Top-level code environment
- `warnings`— Warning control
- `dataclasses`— Data Classes
- `contextlib`— Utilities for- `with`-statement contexts
- `abc`— Abstract Base Classes
- `atexit`— Exit handlers
- `traceback`— Print or retrieve a stack traceback
- `__future__`— Future statement definitions
- `gc`— Garbage Collector interface
- `inspect`— Inspect live objects
- `site`— Site-specific configuration hook
 
- [Custom Python Interpreters](custominterp.html)
- [Importing Modules](modules.html)- `zipimport`— Import modules from Zip archives
- `pkgutil`— Package extension utility
- `modulefinder`— Find modules used by a script
- `runpy`— Locating and executing Python modules
- `importlib`— The implementation of- `import`
- `importlib.resources`– Package resource reading, opening and access
- `importlib.resources.abc`– Abstract base classes for resources
- `importlib.metadata`– Accessing package metadata
- [The initialization of the](sys_path_init.html)- `sys.path`module search path
 
- [Python Language Services](language.html)- `ast`— Abstract Syntax Trees
- `symtable`— Access to the compiler’s symbol tables
- `token`— Constants used with Python parse trees
- `keyword`— Testing for Python keywords
- `tokenize`— Tokenizer for Python source
- `tabnanny`— Detection of ambiguous indentation
- `pyclbr`— Python module browser support
- `py_compile`— Compile Python source files
- `compileall`— Byte-compile Python libraries
- `dis`— Disassembler for Python bytecode
- `pickletools`— Tools for pickle developers
 
- [MS Windows Specific Services](windows.html)
- [Unix-specific services](unix.html)- `shlex`— Simple lexical analysis
- `posix`— The most common POSIX system calls
- `pwd`— The password database
- `grp`— The group database
- `termios`— POSIX style tty control
- `tty`— Terminal control functions
- `pty`— Pseudo-terminal utilities
- `fcntl`— The- `fcntl`and- `ioctl`system calls
- `resource`— Resource usage information
- `syslog`— Unix syslog library routines
 
- [Modules command-line interface (CLI)](cmdline.html)
- [Superseded Modules](superseded.html)
- [Removed Modules](removed.html)
- [Security Considerations](security_warnings.html)