# collections.abc — Abstract Base Classes for Containers — Python 3.14.6 documentation

**Source:** [https://docs.python.org/3.14/library/collections.abc.html](https://docs.python.org/3.14/library/collections.abc.html)

---

`collections.abc` — Abstract Base Classes for Containers[¶](#module-collections.abc)

Added in version 3.3: Formerly, this module was part of the [ collections](collections.html#module-collections) module.

**Source code:** [Lib/_collections_abc.py](https://github.com/python/cpython/tree/3.14/Lib/_collections_abc.py)

This module provides [abstract base classes](../glossary.html#term-abstract-base-class) that
can be used to test whether a class provides a particular interface; for
example, whether it is [hashable](../glossary.html#term-hashable) or whether it is a [mapping](../glossary.html#term-mapping).

An [ issubclass()](functions.html#issubclass) or 

[test for an interface works in one of three ways.](functions.html#isinstance)

`isinstance()`- A newly written class can inherit directly from one of the abstract base classes. The class must supply the required abstract methods. The remaining mixin methods come from inheritance and can be overridden if desired. Other methods may be added as needed: - class C(Sequence): # Direct inheritance def __init__(self): ... # Extra method not required by the ABC def __getitem__(self, index): ... # Required abstract method def __len__(self): ... # Required abstract method def count(self, value): ... # Optionally override a mixin method - >>> issubclass(C, Sequence) True >>> isinstance(C(), Sequence) True 
- Existing classes and built-in classes can be registered as “virtual subclasses” of the ABCs. Those classes should define the full API including all of the abstract methods and all of the mixin methods. This lets users rely on - `issubclass()`- `isinstance()`- class D: # No inheritance def __init__(self): ... # Extra method not required by the ABC def __getitem__(self, index): ... # Abstract method def __len__(self): ... # Abstract method def count(self, value): ... # Mixin method def index(self, value): ... # Mixin method Sequence.register(D) # Register instead of inherit - >>> issubclass(D, Sequence) True >>> isinstance(D(), Sequence) True - In this example, class - `D`does not need to define- `__contains__`,- `__iter__`, and- `__reversed__`because the- [in-operator](../reference/expressions.html#comparisons), the- [iteration](../glossary.html#term-iterable)logic, and the- `reversed()`- `__getitem__`and- `__len__`.
- Some simple interfaces are directly recognizable by the presence of the required methods (unless those methods have been set to - `None`- class E: def __iter__(self): ... def __next__(self): ... - >>> issubclass(E, Iterable) True >>> isinstance(E(), Iterable) True - Complex interfaces do not support this last technique because an interface is more than just the presence of method names. Interfaces specify semantics and relationships between methods that cannot be inferred solely from the presence of specific method names. For example, knowing that a class supplies - `__getitem__`,- `__len__`, and- `__iter__`is insufficient for distinguishing a- `Sequence`- `Mapping`

Added in version 3.9: These abstract classes now support `[]`. See [Generic Alias Type](stdtypes.html#types-genericalias)
and [ PEP 585](https://peps.python.org/pep-0585/).

## Collections Abstract Base Classes[¶](#collections-abstract-base-classes)

The collections module offers the following [ABCs](../glossary.html#term-abstract-base-class):

| ABC | Inherits from | Abstract Methods | Mixin Methods | 
|---|---|---|---|
| 
 | |||
| 
 | |||
| 
 | |||
| 
 | 
 | ||
| 
 | |||
| 
 | 
 | ||
| 
 | |||
| 
 | |||
| 
 | |||
| 
 | 
 | ||
| 
 | Inherited  `append`,`clear`,`reverse`,`extend`,`pop`,`remove`, and`__iadd__` | ||
| 
 | Inherited  | ||
| 
 | 
 | ||
| 
 | Inherited  `clear`,`pop`,`remove`,`__ior__`,`__iand__`,`__ixor__`, and`__isub__` | ||
| 
 | 
 | ||
| 
 | Inherited  `pop`,`popitem`,`clear`,`update`,
and`setdefault` | ||
| 
 | |||
| 
 | |||
| 
 | |||
| 
 | |||
| 
 | |||
| 
 | 
 | ||
| 
 | |||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 

Footnotes

## Collections Abstract Base Classes – Detailed Descriptions[¶](#collections-abstract-base-classes-detailed-descriptions)

- 
*class*collections.abc.Container[¶](#collections.abc.Container)
- ABC for classes that provide the - `__contains__()`

- 
*class*collections.abc.Hashable[¶](#collections.abc.Hashable)
- ABC for classes that provide the - `__hash__()`

- 
*class*collections.abc.Callable[¶](#collections.abc.Callable)
- ABC for classes that provide the - `__call__()`- See - [Annotating callable objects](typing.html#annotating-callables)for details on how to use- `Callable`in type annotations.

- 
*class*collections.abc.Iterable[¶](#collections.abc.Iterable)
- ABC for classes that provide the - `__iter__()`- Checking - `isinstance(obj, Iterable)`detects classes that are registered as- `Iterable`or that have an- `__iter__()`- `__getitem__()`- [iterable](../glossary.html#term-iterable)is to call- `iter(obj)`.

- 
*class*collections.abc.Collection[¶](#collections.abc.Collection)
- ABC for sized iterable container classes. - Added in version 3.6. 

- 
*class*collections.abc.Iterator[¶](#collections.abc.Iterator)
- ABC for classes that provide the - `__iter__()`- `__next__()`- [iterator](../glossary.html#term-iterator).

- 
*class*collections.abc.Reversible[¶](#collections.abc.Reversible)
- ABC for iterable classes that also provide the - `__reversed__()`- Added in version 3.6. 

- 
*class*collections.abc.Generator[¶](#collections.abc.Generator)
- ABC for - [generator](../glossary.html#term-generator)classes that implement the protocol defined in- **PEP 342**- [iterators](../glossary.html#term-iterator)with the- `send()`- `throw()`- `close()`- See - [Annotating generators and coroutines](typing.html#annotating-generators-and-coroutines)for details on using- `Generator`in type annotations.- Added in version 3.5. 

- 
*class*collections.abc.Sequence[¶](#collections.abc.Sequence)
- 
*class*collections.abc.MutableSequence[¶](#collections.abc.MutableSequence)
- 
*class*collections.abc.ByteString[¶](#collections.abc.ByteString)
- ABCs for read-only and mutable - [sequences](../glossary.html#term-sequence).- Implementation note: Some of the mixin methods, such as - `__iter__()`- `__reversed__()`- `index()`- `__getitem__()`- `__getitem__()`is implemented with constant access speed, the mixin methods will have linear performance; however, if the underlying method is linear (as it would be with a linked list), the mixins will have quadratic performance and will likely need to be overridden.- 
index(*value*,*start=0*,*stop=None*)[¶](#collections.abc.ByteString.index)
- Return first index of - *value*.- Raises - `ValueError`- Supporting the - *start*and- *stop*arguments is optional, but recommended.- Changed in version 3.5: The - `index()`- *stop*and- *start*arguments.
 - Deprecated since version 3.12, will be removed in version 3.17: The - `ByteString`ABC has been deprecated.- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**
- 
index(

- 
*class*collections.abc.Mapping[¶](#collections.abc.Mapping)
- 
*class*collections.abc.MutableMapping[¶](#collections.abc.MutableMapping)
- ABCs for read-only and mutable - [mappings](../glossary.html#term-mapping).

- 
*class*collections.abc.MappingView[¶](#collections.abc.MappingView)
- 
*class*collections.abc.ItemsView[¶](#collections.abc.ItemsView)
- 
*class*collections.abc.KeysView[¶](#collections.abc.KeysView)
- 
*class*collections.abc.ValuesView[¶](#collections.abc.ValuesView)
- ABCs for mapping, items, keys, and values - [views](../glossary.html#term-dictionary-view).

- 
*class*collections.abc.Awaitable[¶](#collections.abc.Awaitable)
- ABC for - [awaitable](../glossary.html#term-awaitable)objects, which can be used in- `await`- `__await__()`- [Coroutine](../glossary.html#term-coroutine)objects and instances of the- `Coroutine`- Note - In CPython, generator-based coroutines ( - [generators](../glossary.html#term-generator)decorated with- `@types.coroutine`- *awaitables*, even though they do not have an- `__await__()`- `isinstance(gencoro, Awaitable)`for them will return- `False`. Use- `inspect.isawaitable()`- Added in version 3.5. 

- 
*class*collections.abc.Coroutine[¶](#collections.abc.Coroutine)
- ABC for - [coroutine](../glossary.html#term-coroutine)compatible classes. These implement the following methods, defined in- [Coroutine Objects](../reference/datamodel.html#coroutine-objects):- `send()`- `throw()`- `close()`- `__await__()`- `Coroutine`instances are also instances of- `Awaitable`- Note - In CPython, generator-based coroutines ( - [generators](../glossary.html#term-generator)decorated with- `@types.coroutine`- *awaitables*, even though they do not have an- `__await__()`- `isinstance(gencoro, Coroutine)`for them will return- `False`. Use- `inspect.isawaitable()`- See - [Annotating generators and coroutines](typing.html#annotating-generators-and-coroutines)for details on using- `Coroutine`in type annotations. The variance and order of type parameters correspond to those of- `Generator`- Added in version 3.5. 

- 
*class*collections.abc.AsyncIterable[¶](#collections.abc.AsyncIterable)
- ABC for classes that provide an - `__aiter__`method. See also the definition of- [asynchronous iterable](../glossary.html#term-asynchronous-iterable).- Added in version 3.5. 

- 
*class*collections.abc.AsyncIterator[¶](#collections.abc.AsyncIterator)
- ABC for classes that provide - `__aiter__`and- `__anext__`methods. See also the definition of- [asynchronous iterator](../glossary.html#term-asynchronous-iterator).- Added in version 3.5. 

- 
*class*collections.abc.AsyncGenerator[¶](#collections.abc.AsyncGenerator)
- ABC for - [asynchronous generator](../glossary.html#term-asynchronous-generator)classes that implement the protocol defined in- **PEP 525**- **PEP 492**- See - [Annotating generators and coroutines](typing.html#annotating-generators-and-coroutines)for details on using- `AsyncGenerator`in type annotations.- Added in version 3.6. 

- 
*class*collections.abc.Buffer[¶](#collections.abc.Buffer)
- ABC for classes that provide the - `__buffer__()`- [buffer protocol](../c-api/buffer.html#bufferobjects). See- **PEP 688**- Added in version 3.12. 

## Examples and Recipes[¶](#examples-and-recipes)

ABCs allow us to ask classes or instances if they provide particular functionality, for example:

```
size = None
if isinstance(myvar, collections.abc.Sized):
    size = len(myvar)
```
Several of the ABCs are also useful as mixins that make it easier to develop
classes supporting container APIs.  For example, to write a class supporting
the full [ Set](#collections.abc.Set) API, it is only necessary to supply the three underlying
abstract methods: 

[,](../reference/datamodel.html#object.__contains__)

`__contains__()`[, and](stdtypes.html#container.__iter__)

`__iter__()`[. The ABC supplies the remaining methods such as](../reference/datamodel.html#object.__len__)

`__len__()``__and__()` and [:](stdtypes.html#frozenset.isdisjoint)

`isdisjoint()````
class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)
    def __iter__(self):
        return iter(self.elements)
    def __contains__(self, value):
        return value in self.elements
    def __len__(self):
        return len(self.elements)
s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically
```
Notes on using [ Set](#collections.abc.Set) and 

[as a mixin:](#collections.abc.MutableSet)

`MutableSet`- Since some set operations create new sets, the default mixin methods need a way to create new instances from an - [iterable](../glossary.html#term-iterable). The class constructor is assumed to have a signature in the form- `ClassName(iterable)`. That assumption is factored-out to an internal- `classmethod`- `_from_iterable()`which calls- `cls(iterable)`to produce a new set. If the- `Set`- `_from_iterable()`with a classmethod or regular method that can construct new instances from an iterable argument.
- To override the comparisons (presumably for speed, as the semantics are fixed), redefine - `__le__()`- `__ge__()`
- The - `Set`- `_hash()`method to compute a hash value for the set; however,- `__hash__()`- [hashable](../glossary.html#term-hashable)or immutable. To add set hashability using mixins, inherit from both- `Set`and- `Hashable`- `__hash__ = Set._hash`.

See also

- [OrderedSet recipe](https://code.activestate.com/recipes/576694/)for an example built on- `MutableSet`