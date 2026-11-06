# Python/C API Reference Manual — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/index.html](https://docs.python.org/3.13/c-api/index.html)

---

# Python/C API Reference Manual[¶](#python-c-api-reference-manual)

This manual documents the API used by C and C++ programmers who want to write
extension modules or embed Python.  It is a companion to [Extending and Embedding the Python Interpreter](../extending/index.html#extending-index),
which describes the general principles of extension writing but does not
document the API functions in detail.

- [Introduction](intro.html)
- [C API Stability](stable.html)
- [The Very High Level Layer](veryhigh.html)
- [Reference Counting](refcounting.html)
- [Exception Handling](exceptions.html)
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
- [Initialization, Finalization, and Threads](init.html)- [Before Python Initialization](init.html#before-python-initialization)
- [Global configuration variables](init.html#global-configuration-variables)
- [Initializing and finalizing the interpreter](init.html#initializing-and-finalizing-the-interpreter)
- [Process-wide parameters](init.html#process-wide-parameters)
- [Thread State and the Global Interpreter Lock](init.html#thread-state-and-the-global-interpreter-lock)
- [Sub-interpreter support](init.html#sub-interpreter-support)
- [Asynchronous Notifications](init.html#asynchronous-notifications)
- [Profiling and Tracing](init.html#profiling-and-tracing)
- [Reference tracing](init.html#reference-tracing)
- [Advanced Debugger Support](init.html#advanced-debugger-support)
- [Thread Local Storage Support](init.html#thread-local-storage-support)
- [Synchronization Primitives](init.html#synchronization-primitives)
- [Operating System Thread APIs](init.html#operating-system-thread-apis)
 
- [Python Initialization Configuration](init_config.html)
- [Memory Management](memory.html)
- [Object Implementation Support](objimpl.html)
- [API and ABI Versioning](apiabiversion.html)
- [Monitoring C API](monitoring.html)
- [Generating Execution Events](monitoring.html#generating-execution-events)