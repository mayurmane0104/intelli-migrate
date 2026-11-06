# types — Dynamic type creation and names for built-in types — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/types.html](https://docs.python.org/3.13/library/types.html)

---

`types` — Dynamic type creation and names for built-in types[¶](#module-types)

**Source code:** [Lib/types.py](https://github.com/python/cpython/tree/3.13/Lib/types.py)

This module defines utility functions to assist in dynamic creation of new types.

It also defines names for some object types that are used by the standard
Python interpreter, but not exposed as builtins like [ int](functions.html#int) or

[are.](stdtypes.html#str)

`str`Finally, it provides some additional type-related utility classes and functions that are not fundamental enough to be builtins.

## Dynamic Type Creation[¶](#dynamic-type-creation)

- 
types.new_class(*name*,*bases=()*,*kwds=None*,*exec_body=None*)[¶](#types.new_class)
- Creates a class object dynamically using the appropriate metaclass. - The first three arguments are the components that make up a class definition header: the class name, the base classes (in order), the keyword arguments (such as - `metaclass`).- The - *exec_body*argument is a callback that is used to populate the freshly created class namespace. It should accept the class namespace as its sole argument and update the namespace directly with the class contents. If no callback is provided, it has the same effect as passing in- `lambda ns: None`.- Added in version 3.3. 

- 
types.prepare_class(*name*,*bases=()*,*kwds=None*)[¶](#types.prepare_class)
- Calculates the appropriate metaclass and creates the class namespace. - The arguments are the components that make up a class definition header: the class name, the base classes (in order) and the keyword arguments (such as - `metaclass`).- The return value is a 3-tuple: - `metaclass, namespace, kwds`- *metaclass*is the appropriate metaclass,- *namespace*is the prepared class namespace and- *kwds*is an updated copy of the passed in- *kwds*argument with any- `'metaclass'`entry removed. If no- *kwds*argument is passed in, this will be an empty dict.- Added in version 3.3. - Changed in version 3.6: The default value for the - `namespace`element of the returned tuple has changed. Now an insertion-order-preserving mapping is used when the metaclass does not have a- `__prepare__`method.

See also

- [Metaclasses](../reference/datamodel.html#metaclasses)
- Full details of the class creation process supported by these functions 
- **PEP 3115**
- Introduced the - `__prepare__`namespace hook

- 
types.resolve_bases(*bases*)[¶](#types.resolve_bases)
- Resolve MRO entries dynamically as specified by - **PEP 560**- This function looks for items in - *bases*that are not instances of- `type`- `__mro_entries__()`- *bases*item is an instance of- `type`, or it doesn’t have an- `__mro_entries__()`method, then it is included in the return tuple unchanged.- Added in version 3.7. 

- 
types.get_original_bases(*cls*,*/*)[¶](#types.get_original_bases)
- Return the tuple of objects originally given as the bases of - *cls*before the- `__mro_entries__()`- **PEP 560**- [Generics](typing.html#user-defined-generics).- For classes that have an - `__orig_bases__`attribute, this function returns the value of- `cls.__orig_bases__`. For classes without the- `__orig_bases__`attribute,- `cls.__bases__`- Examples: - from typing import TypeVar, Generic, NamedTuple, TypedDict T = TypeVar("T") class Foo(Generic[T]): ... class Bar(Foo[int], float): ... class Baz(list[str]): ... Eggs = NamedTuple("Eggs", [("a", int), ("b", str)]) Spam = TypedDict("Spam", {"a": int, "b": str}) assert Bar.__bases__ == (Foo, float) assert get_original_bases(Bar) == (Foo[int], float) assert Baz.__bases__ == (list,) assert get_original_bases(Baz) == (list[str],) assert Eggs.__bases__ == (tuple,) assert get_original_bases(Eggs) == (NamedTuple,) assert Spam.__bases__ == (dict,) assert get_original_bases(Spam) == (TypedDict,) assert int.__bases__ == (object,) assert get_original_bases(int) == (object,) - Added in version 3.12. 

See also

[ PEP 560](https://peps.python.org/pep-0560/) - Core support for typing module and generic types

## Standard Interpreter Types[¶](#standard-interpreter-types)

This module provides names for many of the types that are required to
implement a Python interpreter. It deliberately avoids including some of
the types that arise only incidentally during processing such as the
`listiterator` type.

Typical use of these names is for [ isinstance()](functions.html#isinstance) or

[checks.](functions.html#issubclass)

`issubclass()`If you instantiate any of these types, note that signatures may vary between Python versions.

Standard names are defined for the following types:

- 
types.FunctionType[¶](#types.FunctionType)
- 
types.LambdaType[¶](#types.LambdaType)
- The type of user-defined functions and functions created by - `lambda`- Raises an - [auditing event](sys.html#auditing)- `function.__new__`with argument- `code`.- The audit event only occurs for direct instantiation of function objects, and is not raised for normal compilation. 

- 
types.CoroutineType[¶](#types.CoroutineType)
- The type of - [coroutine](../glossary.html#term-coroutine)objects, created by- `async def`- Added in version 3.5. 

- 
types.AsyncGeneratorType[¶](#types.AsyncGeneratorType)
- The type of - [asynchronous generator](../glossary.html#term-asynchronous-generator)-iterator objects, created by asynchronous generator functions.- Added in version 3.6. 

- 
*class*types.CodeType(***kwargs*)[¶](#types.CodeType)
- The type of - [code objects](../reference/datamodel.html#code-objects)such as returned by- `compile()`- Raises an - [auditing event](sys.html#auditing)- `code.__new__`with arguments- `code`,- `filename`,- `name`,- `argcount`,- `posonlyargcount`,- `kwonlyargcount`,- `nlocals`,- `stacksize`,- `flags`.- Note that the audited arguments may not match the names or positions required by the initializer. The audit event only occurs for direct instantiation of code objects, and is not raised for normal compilation. 

- 
types.CellType[¶](#types.CellType)
- The type for cell objects: such objects are used as containers for a function’s - [closure variables](../glossary.html#term-closure-variable).- Added in version 3.8. 

- 
types.MethodType[¶](#types.MethodType)
- The type of methods of user-defined class instances. 

- 
types.BuiltinFunctionType[¶](#types.BuiltinFunctionType)
- 
types.BuiltinMethodType[¶](#types.BuiltinMethodType)
- The type of built-in functions like - `len()`- `sys.exit()`

- 
types.WrapperDescriptorType[¶](#types.WrapperDescriptorType)
- The type of methods of some built-in data types and base classes such as - `object.__init__()`- `object.__lt__()`- Added in version 3.7. 

- 
types.MethodWrapperType[¶](#types.MethodWrapperType)
- The type of - *bound*methods of some built-in data types and base classes. For example it is the type of- `object().__str__`.- Added in version 3.7. 

- 
*class*types.NotImplementedType[¶](#types.NotImplementedType)
- The type of - `NotImplemented`- Added in version 3.10. 

- 
types.MethodDescriptorType[¶](#types.MethodDescriptorType)
- The type of methods of some built-in data types such as - `str.join()`- Added in version 3.7. 

- 
types.ClassMethodDescriptorType[¶](#types.ClassMethodDescriptorType)
- The type of - *unbound*class methods of some built-in data types such as- `dict.__dict__['fromkeys']`.- Added in version 3.7. 

- 
*class*types.ModuleType(*name*,*doc=None*)[¶](#types.ModuleType)
- The type of - [modules](../glossary.html#term-module). The constructor takes the name of the module to be created and optionally its- [docstring](../glossary.html#term-docstring).- See also - [Documentation on module objects](../reference/datamodel.html#module-objects)
- Provides details on the special attributes that can be found on instances of - `ModuleType`.
- `importlib.util.module_from_spec()`
- Modules created using the - `ModuleType`constructor are created with many of their special attributes unset or set to default values.- `module_from_spec()`provides a more robust way of creating- `ModuleType`instances which ensures the various attributes are set appropriately.
 

- 
*class*types.GenericAlias(*t_origin*,*t_args*)[¶](#types.GenericAlias)
- The type of - [parameterized generics](stdtypes.html#types-genericalias)such as- `list[int]`.- `t_origin`should be a non-parameterized generic class, such as- `list`,- `tuple`or- `dict`.- `t_args`should be a- `tuple`- `t_origin`:- >>> from types import GenericAlias >>> list[int] == GenericAlias(list, (int,)) True >>> dict[str, int] == GenericAlias(dict, (str, int)) True - Added in version 3.9. - Changed in version 3.9.2: This type can now be subclassed. - See also - [Generic Alias Types](stdtypes.html#types-genericalias)
- In-depth documentation on instances of - `types.GenericAlias`
- **PEP 585**
- Introducing the - `types.GenericAlias`class
 

- 
*class*types.UnionType[¶](#types.UnionType)
- The type of - [union type expressions](stdtypes.html#types-union).- Added in version 3.10. 

- 
*class*types.TracebackType(*tb_next*,*tb_frame*,*tb_lasti*,*tb_lineno*)[¶](#types.TracebackType)
- The type of traceback objects such as found in - `sys.exception().__traceback__`.- See - [the language reference](../reference/datamodel.html#traceback-objects)for details of the available attributes and operations, and guidance on creating tracebacks dynamically.

- 
types.FrameType[¶](#types.FrameType)
- The type of - [frame objects](../reference/datamodel.html#frame-objects)such as found in- `tb.tb_frame`- `tb`is a traceback object.

- 
types.GetSetDescriptorType[¶](#types.GetSetDescriptorType)
- The type of objects defined in extension modules with - `PyGetSetDef`, such as- `FrameType.f_locals`- `array.array.typecode`. This type is used as descriptor for object attributes; it has the same purpose as the- `property`

- 
types.MemberDescriptorType[¶](#types.MemberDescriptorType)
- The type of objects defined in extension modules with - `PyMemberDef`, such as- `datetime.timedelta.days`. This type is used as descriptor for simple C data members which use standard conversion functions; it has the same purpose as the- `property`- In addition, when a class is defined with a - `__slots__`- `MemberDescriptorType`will be added as an attribute on the class. This allows the slot to appear in the class’s- `__dict__`- **CPython implementation detail:**In other implementations of Python, this type may be identical to- `GetSetDescriptorType`.

- 
*class*types.MappingProxyType(*mapping*)[¶](#types.MappingProxyType)
- Read-only proxy of a mapping. It provides a dynamic view on the mapping’s entries, which means that when the mapping changes, the view reflects these changes. - `MappingProxyType`s are- [generic](typing.html#generics)over two types, signifying (respectively) the types of the underlying mapping’s keys and values.- Added in version 3.3. - Changed in version 3.9: Updated to support the new union ( - `|`) operator from- **PEP 584**- key in proxy
- Return - `True`if the underlying mapping has a key- *key*, else- `False`.
 - proxy[key]
- Return the item of the underlying mapping with key - *key*. Raises a- `KeyError`- *key*is not in the underlying mapping.
 - iter(proxy)
- Return an iterator over the keys of the underlying mapping. This is a shortcut for - `iter(proxy.keys())`.
 - len(proxy)
- Return the number of items in the underlying mapping. 
 - 
copy()[¶](#types.MappingProxyType.copy)
- Return a shallow copy of the underlying mapping. 
 - 
get(*key*[,*default*])[¶](#types.MappingProxyType.get)
- Return the value for - *key*if- *key*is in the underlying mapping, else- *default*. If- *default*is not given, it defaults to- `None`, so that this method never raises a- `KeyError`
 - 
items()[¶](#types.MappingProxyType.items)
- Return a new view of the underlying mapping’s items ( - `(key, value)`pairs).
 - 
keys()[¶](#types.MappingProxyType.keys)
- Return a new view of the underlying mapping’s keys. 
 - 
values()[¶](#types.MappingProxyType.values)
- Return a new view of the underlying mapping’s values. 
 - reversed(proxy)
- Return a reverse iterator over the keys of the underlying mapping. - Added in version 3.9. 
 - hash(proxy)
- Return a hash of the underlying mapping. - Added in version 3.12. 
 

- 
*class*types.CapsuleType[¶](#types.CapsuleType)
- The type of - [capsule objects](../c-api/capsule.html#capsules).- Added in version 3.13. 

## Additional Utility Classes and Functions[¶](#additional-utility-classes-and-functions)

- 
*class*types.SimpleNamespace[¶](#types.SimpleNamespace)
- A simple - `object`- Unlike - `object`- `SimpleNamespace`you can add and remove attributes.- `SimpleNamespace`objects may be initialized in the same way as- `dict`- [iterable](../glossary.html#term-iterable)object producing key-value pairs). All such keys must be strings.- The type is roughly equivalent to the following code: - class SimpleNamespace: def __init__(self, mapping_or_iterable=(), /, **kwargs): self.__dict__.update(mapping_or_iterable) self.__dict__.update(kwargs) def __repr__(self): items = (f"{k}={v!r}" for k, v in self.__dict__.items()) return "{}({})".format(type(self).__name__, ", ".join(items)) def __eq__(self, other): if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace): return self.__dict__ == other.__dict__ return NotImplemented - `SimpleNamespace`may be useful as a replacement for- `class NS: pass`. However, for a structured record type use- `namedtuple()`- `SimpleNamespace`objects are supported by- `copy.replace()`- Added in version 3.3. - Changed in version 3.9: Attribute order in the repr changed from alphabetical to insertion (like - `dict`).- Changed in version 3.13: Added support for an optional positional argument. 

- 
types.DynamicClassAttribute(*fget=None*,*fset=None*,*fdel=None*,*doc=None*)[¶](#types.DynamicClassAttribute)
- Route attribute access on a class to __getattr__. - This is a descriptor, used to define attributes that act differently when accessed through an instance and through a class. Instance access remains normal, but access to an attribute through a class will be routed to the class’s __getattr__ method; this is done by raising AttributeError. - This allows one to have properties active on an instance, and have virtual attributes on the class with the same name (see - `enum.Enum`- Added in version 3.4. 

## Coroutine Utility Functions[¶](#coroutine-utility-functions)

- 
types.coroutine(*gen_func*)[¶](#types.coroutine)
- This function transforms a - [generator](../glossary.html#term-generator)function into a- [coroutine function](../glossary.html#term-coroutine-function)which returns a generator-based coroutine. The generator-based coroutine is still a- [generator iterator](../glossary.html#term-generator-iterator), but is also considered to be a- [coroutine](../glossary.html#term-coroutine)object and is- [awaitable](../glossary.html#term-awaitable). However, it may not necessarily implement the- `__await__()`- If - *gen_func*is a generator function, it will be modified in-place.- If - *gen_func*is not a generator function, it will be wrapped. If it returns an instance of- `collections.abc.Generator`- *awaitable*proxy object. All other types of objects will be returned as is.- Added in version 3.5.