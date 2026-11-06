# Pending removal in Python 3.17 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/deprecations/pending-removal-in-3.17.html](https://docs.python.org/deprecations/pending-removal-in-3.17.html)

---

# Pending removal in Python 3.17[¶](#pending-removal-in-python-3-17)

- 
- `collections.abc.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 
- 
- Before Python 3.14, old-style unions were implemented using the private class - `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like- `typing.get_origin()`- `typing.get_args()`
- `typing.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)