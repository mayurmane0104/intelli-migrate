# Extending and Embedding the Python Interpreter — Python 3.14.6 documentation

**Source:** [http://docs.python.org/extending/index.html](http://docs.python.org/extending/index.html)

---

# Extending and Embedding the Python Interpreter[¶](#extending-and-embedding-the-python-interpreter)

This document describes how to write modules in C or C++ to extend the Python interpreter with new modules. Those modules can not only define new functions but also new object types and their methods. The document also describes how to embed the Python interpreter in another application, for use as an extension language. Finally, it shows how to compile and link extension modules so that they can be loaded dynamically (at run time) into the interpreter, if the underlying operating system supports this feature.

This document assumes basic knowledge about Python.  For an informal
introduction to the language, see [The Python Tutorial](../tutorial/index.html#tutorial-index).  [The Python Language Reference](../reference/index.html#reference-index)
gives a more formal definition of the language.  [The Python Standard Library](../library/index.html#library-index) documents
the existing object types, functions and modules (both built-in and written in
Python) that give the language its wide application range.

For a detailed description of the whole Python/C API, see the separate
[Python/C API reference manual](../c-api/index.html#c-api-index).

## Recommended third party tools[¶](#recommended-third-party-tools)

This guide only covers the basic tools for creating extensions provided
as part of this version of CPython. Some [third party tools](../c-api/intro.html#c-api-tools) offer both simpler and more sophisticated approaches to creating
C and C++ extensions for Python.

## Creating extensions without third party tools[¶](#creating-extensions-without-third-party-tools)

This section of the guide covers creating C and C++ extensions without assistance from third party tools. It is intended primarily for creators of those tools, rather than being a recommended way to create your own C extensions.

See also

[ PEP 489](https://peps.python.org/pep-0489/) – Multi-phase extension module initialization

- [1. Extending Python with C or C++](extending.html)- [1.1. A Simple Example](extending.html#a-simple-example)
- [1.2. Intermezzo: Errors and Exceptions](extending.html#intermezzo-errors-and-exceptions)
- [1.3. Back to the Example](extending.html#back-to-the-example)
- [1.4. The Module’s Method Table and Initialization Function](extending.html#the-module-s-method-table-and-initialization-function)
- [1.5. Compilation and Linkage](extending.html#compilation-and-linkage)
- [1.6. Calling Python Functions from C](extending.html#calling-python-functions-from-c)
- [1.7. Extracting Parameters in Extension Functions](extending.html#extracting-parameters-in-extension-functions)
- [1.8. Keyword Parameters for Extension Functions](extending.html#keyword-parameters-for-extension-functions)
- [1.9. Building Arbitrary Values](extending.html#building-arbitrary-values)
- [1.10. Reference Counts](extending.html#reference-counts)
- [1.11. Writing Extensions in C++](extending.html#writing-extensions-in-c)
- [1.12. Providing a C API for an Extension Module](extending.html#providing-a-c-api-for-an-extension-module)
 
- [2. Defining Extension Types: Tutorial](newtypes_tutorial.html)
- [3. Defining Extension Types: Assorted Topics](newtypes.html)
- [4. Building C and C++ Extensions](building.html)
- [5. Building C and C++ Extensions on Windows](windows.html)

## Embedding the CPython runtime in a larger application[¶](#embedding-the-cpython-runtime-in-a-larger-application)

Sometimes, rather than creating an extension that runs inside the Python interpreter as the main application, it is desirable to instead embed the CPython runtime inside a larger application. This section covers some of the details involved in doing that successfully.