# abc — Abstract Base Classes — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/abc.html](https://docs.python.org/library/abc.html)

---

`abc` — Abstract Base Classes[¶](#module-abc)

**Source code:** [Lib/abc.py](https://github.com/python/cpython/tree/3.14/Lib/abc.py)

This module provides the infrastructure for defining [abstract base
classes](../glossary.html#term-abstract-base-class) (ABCs) in Python, as outlined in [ PEP 3119](https://peps.python.org/pep-3119/);
see the PEP for why this was added to Python. (See also 

[and the](https://peps.python.org/pep-3141/)

**PEP 3141**[module regarding a type hierarchy for numbers based on ABCs.)](numbers.html#module-numbers)

`numbers`The [ collections](collections.html#module-collections) module has some concrete classes that derive from
ABCs; these can, of course, be further derived. In addition, the

[submodule has some ABCs that can be used to test whether a class or instance provides a particular interface, for example, if it is](collections.abc.html#module-collections.abc)

`collections.abc`[hashable](../glossary.html#term-hashable)or if it is a

[mapping](../glossary.html#term-mapping).

This module provides the metaclass [ ABCMeta](#abc.ABCMeta) for defining ABCs and
a helper class 

[to alternatively define ABCs through inheritance:](#abc.ABC)

`ABC`- 
*class*abc.ABC[¶](#abc.ABC)
- A helper class that has - `ABCMeta`- `ABC`avoiding sometimes confusing metaclass usage, for example:- from abc import ABC class MyABC(ABC): pass - Note that the type of - `ABC`is still- `ABCMeta`- `ABC`requires the usual precautions regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the metaclass keyword and using- `ABCMeta`directly, for example:- from abc import ABCMeta class MyABC(metaclass=ABCMeta): pass - Added in version 3.4. 

- 
*class*abc.ABCMeta[¶](#abc.ABCMeta)
- Metaclass for defining Abstract Base Classes (ABCs). - Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as “virtual subclasses” – these and their descendants will be considered subclasses of the registering ABC by the built-in - `issubclass()`- `super()`- [[1]](#id2)- Classes created with a metaclass of - `ABCMeta`have the following method:- 
register(*subclass*)[¶](#abc.ABCMeta.register)
- Register - *subclass*as a “virtual subclass” of this ABC. For example:- from abc import ABC class MyABC(ABC): pass MyABC.register(tuple) assert issubclass(tuple, MyABC) assert isinstance((), MyABC) - Changed in version 3.3: Returns the registered subclass, to allow usage as a class decorator. - Changed in version 3.4: To detect calls to - `register()`, you can use the- `get_cache_token()`
 - You can also override this method in an abstract base class: - 
__subclasshook__(*subclass*)[¶](#abc.ABCMeta.__subclasshook__)
- (Must be defined as a class method.) - Check whether - *subclass*is considered a subclass of this ABC. This means that you can customize the behavior of- `issubclass()`- `register()`- `__subclasscheck__()`- This method should return - `True`,- `False`or- `NotImplemented`- `True`, the- *subclass*is considered a subclass of this ABC. If it returns- `False`, the- *subclass*is not considered a subclass of this ABC, even if it would normally be one. If it returns- `NotImplemented`, the subclass check is continued with the usual mechanism.
 - For a demonstration of these concepts, look at this example ABC definition: - class Foo: def __getitem__(self, index): ... def __len__(self): ... def get_iterator(self): return iter(self) class MyIterable(ABC): @abstractmethod def __iter__(self): while False: yield None def get_iterator(self): return self.__iter__() @classmethod def __subclasshook__(cls, C): if cls is MyIterable: if any("__iter__" in B.__dict__ for B in C.__mro__): return True return NotImplemented MyIterable.register(Foo) - The ABC - `MyIterable`defines the standard iterable method,- `__iter__()`- `get_iterator()`method is also part of the- `MyIterable`abstract base class, but it does not have to be overridden in non-abstract derived classes.- The - `__subclasshook__()`- `__iter__()`- `__dict__`- `__mro__`- `MyIterable`too.- Finally, the last line makes - `Foo`a virtual subclass of- `MyIterable`, even though it does not define an- `__iter__()`- `__len__()`- `__getitem__()`- `get_iterator`available as a method of- `Foo`, so it is provided separately.
- 
register(

The `abc` module also provides the following decorator:

- 
@abc.abstractmethod[¶](#abc.abstractmethod)
- A decorator indicating abstract methods. - Using this decorator requires that the class’s metaclass is - `ABCMeta`- `ABCMeta`cannot be instantiated unless all of its abstract methods and properties are overridden. The abstract methods can be called using any of the normal ‘super’ call mechanisms.- `abstractmethod()`may be used to declare abstract methods for properties and descriptors.- Dynamically adding abstract methods to a class, or attempting to modify the abstraction status of a method or class once it is created, are only supported using the - `update_abstractmethods()`- `abstractmethod()`only affects subclasses derived using regular inheritance; “virtual subclasses” registered with the ABC’s- `register()`- When - `abstractmethod()`is applied in combination with other method descriptors, it should be applied as the innermost decorator, as shown in the following usage examples:- class C(ABC): @abstractmethod def my_abstract_method(self, arg1): ... @classmethod @abstractmethod def my_abstract_classmethod(cls, arg2): ... @staticmethod @abstractmethod def my_abstract_staticmethod(arg3): ... @property @abstractmethod def my_abstract_property(self): ... @my_abstract_property.setter @abstractmethod def my_abstract_property(self, val): ... @abstractmethod def _get_x(self): ... @abstractmethod def _set_x(self, val): ... x = property(_get_x, _set_x) - In order to correctly interoperate with the abstract base class machinery, the descriptor must identify itself as abstract using - `__isabstractmethod__`. In general, this attribute should be- `True`if any of the methods used to compose the descriptor are abstract. For example, Python’s built-in- `property`- class Descriptor: ... @property def __isabstractmethod__(self): return any(getattr(f, '__isabstractmethod__', False) for f in (self._fget, self._fset, self._fdel)) - Note - Unlike Java abstract methods, these abstract methods may have an implementation. This implementation can be called via the - `super()`

The `abc` module also supports the following legacy decorators:

- 
@abc.abstractclassmethod[¶](#abc.abstractclassmethod)
- Added in version 3.2. - Deprecated since version 3.3: It is now possible to use - `classmethod`- `abstractmethod()`- A subclass of the built-in - `classmethod()`- `abstractmethod()`- This special case is deprecated, as the - `classmethod()`- class C(ABC): @classmethod @abstractmethod def my_abstract_classmethod(cls, arg): ... 

- 
@abc.abstractstaticmethod[¶](#abc.abstractstaticmethod)
- Added in version 3.2. - Deprecated since version 3.3: It is now possible to use - `staticmethod`- `abstractmethod()`- A subclass of the built-in - `staticmethod()`- `abstractmethod()`- This special case is deprecated, as the - `staticmethod()`- class C(ABC): @staticmethod @abstractmethod def my_abstract_staticmethod(arg): ... 

- 
@abc.abstractproperty[¶](#abc.abstractproperty)
- Deprecated since version 3.3: It is now possible to use - `property`- `property.getter()`- `property.setter()`- `property.deleter()`- `abstractmethod()`- A subclass of the built-in - `property()`- This special case is deprecated, as the - `property()`- class C(ABC): @property @abstractmethod def my_abstract_property(self): ... - The above example defines a read-only property; you can also define a read-write abstract property by appropriately marking one or more of the underlying methods as abstract: - class C(ABC): @property def x(self): ... @x.setter @abstractmethod def x(self, val): ... - If only some components are abstract, only those components need to be updated to create a concrete property in a subclass: - class D(C): @C.x.setter def x(self, val): ... 

The `abc` module also provides the following functions:

- 
abc.get_cache_token()[¶](#abc.get_cache_token)
- Returns the current abstract base class cache token. - The token is an opaque object (that supports equality testing) identifying the current version of the abstract base class cache for virtual subclasses. The token changes with every call to - `ABCMeta.register()`- Added in version 3.4. 

- 
abc.update_abstractmethods(*cls*)[¶](#abc.update_abstractmethods)
- A function to recalculate an abstract class’s abstraction status. This function should be called if a class’s abstract methods have been implemented or changed after it was created. Usually, this function should be called from within a class decorator. - Returns - *cls*, to allow usage as a class decorator.- If - *cls*is not an instance of- `ABCMeta`- Note - This function assumes that - *cls*’s superclasses are already updated. It does not update any subclasses.- Added in version 3.10. 

Footnotes