# Generic Operating System Services — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/allos.html](https://docs.python.org/library/allos.html)

---

# Generic Operating System Services[¶](#generic-operating-system-services)

The modules described in this chapter provide interfaces to operating system features that are available on (almost) all operating systems, such as files and a clock. The interfaces are generally modeled after the Unix or C interfaces, but they are available on most other systems as well. Here’s an overview:

- `os`— Miscellaneous operating system interfaces
- `io`— Core tools for working with streams
- `time`— Time access and conversions
- `logging`— Logging facility for Python
- `logging.config`— Logging configuration
- `logging.handlers`— Logging handlers
- `platform`— Access to underlying platform’s identifying data
- `errno`— Standard errno system symbols
- `ctypes`— A foreign function library for Python- [ctypes tutorial](ctypes.html#ctypes-tutorial)- [Loading dynamic link libraries](ctypes.html#loading-dynamic-link-libraries)
- [Accessing functions from loaded dlls](ctypes.html#accessing-functions-from-loaded-dlls)
- [Calling functions](ctypes.html#calling-functions)
- [Fundamental data types](ctypes.html#fundamental-data-types)
- [Calling functions, continued](ctypes.html#calling-functions-continued)
- [Calling variadic functions](ctypes.html#calling-variadic-functions)
- [Calling functions with your own custom data types](ctypes.html#calling-functions-with-your-own-custom-data-types)
- [Specifying the required argument types (function prototypes)](ctypes.html#specifying-the-required-argument-types-function-prototypes)
- [Return types](ctypes.html#return-types)
- [Passing pointers (or: passing parameters by reference)](ctypes.html#passing-pointers-or-passing-parameters-by-reference)
- [Structures and unions](ctypes.html#structures-and-unions)
- [Structure/union layout, alignment and byte order](ctypes.html#structure-union-layout-alignment-and-byte-order)
- [Bit fields in structures and unions](ctypes.html#bit-fields-in-structures-and-unions)
- [Arrays](ctypes.html#arrays)
- [Pointers](ctypes.html#pointers)
- [Thread safety without the GIL](ctypes.html#thread-safety-without-the-gil)
- [Type conversions](ctypes.html#type-conversions)
- [Incomplete Types](ctypes.html#incomplete-types)
- [Callback functions](ctypes.html#callback-functions)
- [Accessing values exported from dlls](ctypes.html#accessing-values-exported-from-dlls)
- [Surprises](ctypes.html#surprises)
- [Variable-sized data types](ctypes.html#variable-sized-data-types)
 
- [ctypes reference](ctypes.html#ctypes-reference)