# 4. Building C and C++ Extensions — Python 3.14.6 documentation

**Source:** [https://docs.python.org/extending/building.html](https://docs.python.org/extending/building.html)

---

# 4. Building C and C++ Extensions[¶](#building-c-and-c-extensions)

A C extension for CPython is a shared library (for example, a `.so` file on
Linux, `.pyd` on Windows), which exports an *initialization function*.

See [Defining extension modules](../c-api/extension-modules.html#extension-modules) for details.

## 4.1. Building C and C++ Extensions with setuptools[¶](#building-c-and-c-extensions-with-setuptools)

Building, packaging and distributing extension modules is best done with
third-party tools, and is out of scope of this document.
One suitable tool is Setuptools, whose documentation can be found at
[https://setuptools.pypa.io/en/latest/setuptools.html](https://setuptools.pypa.io/en/latest/setuptools.html).

The [ distutils](../library/distutils.html#module-distutils) module, which was included in the standard library
until Python 3.12, is now maintained as part of Setuptools.