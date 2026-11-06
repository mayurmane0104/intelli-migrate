# Python/C API reference manual — Python 3.14.6 documentation

**Source:** [http://docs.python.org/c-api/index.html](http://docs.python.org/c-api/index.html)

---

# Python/C API reference manual[¶](#python-c-api-reference-manual)

This manual documents the API used by C and C++ programmers who want to write
extension modules or embed Python.  It is a companion to [Extending and Embedding the Python Interpreter](../extending/index.html#extending-index),
which describes the general principles of extension writing but does not
document the API functions in detail.

- [Introduction](intro.html)
- [C API Stability](stable.html)
- [The Very High Level Layer](veryhigh.html)
- [Reference Counting](refcounting.html)
- [Exception Handling](exceptions.html)
- [Defining extension modules](extension-modules.html)
- [Utilities](utilities.html)- [Operating System Utilities](sys.html)
- [System Functions](sys.html#system-functions)
- [Process Control](sys.html#process-control)
- [Importing Modules](import.html)
- [Data marshalling support](marshal.html)
- [Parsing arguments and building values](arg.html)
- [String conversion and formatting](conversion.html)
- [Character classification and conversion](conversion.html#character-classification-and-conversion)
- [PyHash API](hash.html)
- [Reflection](reflection.html)
- [Codec registry and support functions](codec.html)
- [PyTime C API](time.html)
- [Support for Perf Maps](perfmaps.html)
 
- [Abstract Objects Layer](abstract.html)
- [Concrete Objects Layer](concrete.html)
- [Interpreter initialization and finalization](interp-lifecycle.html)
- [Thread states and the global interpreter lock](threads.html)
- [Asynchronous notifications](threads.html#asynchronous-notifications)
- [Operating system thread APIs](threads.html#operating-system-thread-apis)
- [Synchronization primitives](synchronization.html)
- [Thread-local storage support](tls.html)
- [Multiple interpreters in a Python process](subinterpreters.html)
- [Profiling and tracing](profiling.html)
- [Reference tracing](profiling.html#reference-tracing)
- [Python Initialization Configuration](init_config.html)
- [Memory Management](memory.html)
- [Object Implementation Support](objimpl.html)
- [API and ABI Versioning](apiabiversion.html)
- [Monitoring C API](monitoring.html)
- [Generating Execution Events](monitoring.html#generating-execution-events)