# 4. Building C and C++ Extensions — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/extending/building.html](https://docs.python.org/3.13/extending/building.html)

---

# 4. Building C and C++ Extensions[¶](#building-c-and-c-extensions)

A C extension for CPython is a shared library (e.g. a `.so` file on Linux,
`.pyd` on Windows), which exports an *initialization function*.

To be importable, the shared library must be available on [ PYTHONPATH](../using/cmdline.html#envvar-PYTHONPATH),
and must be named after the module name, with an appropriate extension.
When using setuptools, the correct filename is generated automatically.

The initialization function has the signature:

It returns either a fully initialized module, or a [ PyModuleDef](../c-api/module.html#c.PyModuleDef)
instance. See 

[Initializing C modules](../c-api/module.html#initializing-modules)for details.

For modules with ASCII-only names, the function must be named
`PyInit_`, with *<name>*`<name>` replaced by the name of the module.
When using [Multi-phase initialization](../c-api/module.html#multi-phase-initialization), non-ASCII module names
are allowed. In this case, the initialization function name is
`PyInitU_`, with *<name>*`<name>` encoded using Python’s
*punycode* encoding with hyphens replaced by underscores. In Python:

```
def initfunc_name(name):
    try:
        suffix = b'_' + name.encode('ascii')
    except UnicodeEncodeError:
        suffix = b'U_' + name.encode('punycode').replace(b'-', b'_')
    return b'PyInit' + suffix
```
It is possible to export multiple modules from a single shared library by
defining multiple initialization functions. However, importing them requires
using symbolic links or a custom importer, because by default only the
function corresponding to the filename is found.
See the *“Multiple modules in one library”* section in [ PEP 489](https://peps.python.org/pep-0489/) for details.

## 4.1. Building C and C++ Extensions with setuptools[¶](#building-c-and-c-extensions-with-setuptools)

Python 3.12 and newer no longer come with distutils. Please refer to the
`setuptools` documentation at
[https://setuptools.readthedocs.io/en/latest/setuptools.html](https://setuptools.readthedocs.io/en/latest/setuptools.html)
to learn more about how build and distribute C/C++ extensions with setuptools.