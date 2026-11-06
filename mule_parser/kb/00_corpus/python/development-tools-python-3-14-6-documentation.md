# Development Tools — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/development.html](https://docs.python.org/library/development.html)

---

# Development Tools[¶](#development-tools)

The modules described in this chapter help you write software.  For example, the
[ pydoc](pydoc.html#module-pydoc) module takes a module and generates documentation based on the
module’s contents.  The 

[and](doctest.html#module-doctest)

`doctest`[modules contains frameworks for writing unit tests that automatically exercise code and verify that the expected output is produced.](unittest.html#module-unittest)

`unittest`The list of modules described in this chapter is:

- `typing`— Support for type hints- [Specification for the Python Type System](typing.html#specification-for-the-python-type-system)
- [Type aliases](typing.html#type-aliases)
- [NewType](typing.html#newtype)
- [Annotating callable objects](typing.html#annotating-callable-objects)
- [Generics](typing.html#generics)
- [Annotating tuples](typing.html#annotating-tuples)
- [The type of class objects](typing.html#the-type-of-class-objects)
- [Annotating generators and coroutines](typing.html#annotating-generators-and-coroutines)
- [User-defined generic types](typing.html#user-defined-generic-types)
- [The](typing.html#the-any-type)- `Any`type
- [Nominal vs structural subtyping](typing.html#nominal-vs-structural-subtyping)
- [Module contents](typing.html#module-contents)
- [Deprecation Timeline of Major Features](typing.html#deprecation-timeline-of-major-features)
 
- `pydoc`— Documentation generator and online help system
- [Python Development Mode](devmode.html)
- `doctest`— Test interactive Python examples
- `unittest`— Unit testing framework
- `unittest.mock`— mock object library
- `unittest.mock`— getting started- [Using Mock](unittest.mock-examples.html#using-mock)- [Mock patching methods](unittest.mock-examples.html#mock-patching-methods)
- [Mock for method calls on an object](unittest.mock-examples.html#mock-for-method-calls-on-an-object)
- [Mocking classes](unittest.mock-examples.html#mocking-classes)
- [Naming your mocks](unittest.mock-examples.html#naming-your-mocks)
- [Tracking all calls](unittest.mock-examples.html#tracking-all-calls)
- [Setting return values and attributes](unittest.mock-examples.html#setting-return-values-and-attributes)
- [Raising exceptions with mocks](unittest.mock-examples.html#raising-exceptions-with-mocks)
- [Side effect functions and iterables](unittest.mock-examples.html#side-effect-functions-and-iterables)
- [Mocking asynchronous iterators](unittest.mock-examples.html#mocking-asynchronous-iterators)
- [Mocking asynchronous context manager](unittest.mock-examples.html#mocking-asynchronous-context-manager)
- [Creating a mock from an existing object](unittest.mock-examples.html#creating-a-mock-from-an-existing-object)
- [Using side_effect to return per file content](unittest.mock-examples.html#using-side-effect-to-return-per-file-content)
 
- [Patch decorators](unittest.mock-examples.html#patch-decorators)
- [Further examples](unittest.mock-examples.html#further-examples)- [Mocking chained calls](unittest.mock-examples.html#mocking-chained-calls)
- [Partial mocking](unittest.mock-examples.html#partial-mocking)
- [Mocking a generator method](unittest.mock-examples.html#mocking-a-generator-method)
- [Applying the same patch to every test method](unittest.mock-examples.html#applying-the-same-patch-to-every-test-method)
- [Mocking unbound methods](unittest.mock-examples.html#mocking-unbound-methods)
- [Checking multiple calls with mock](unittest.mock-examples.html#checking-multiple-calls-with-mock)
- [Coping with mutable arguments](unittest.mock-examples.html#coping-with-mutable-arguments)
- [Nesting patches](unittest.mock-examples.html#nesting-patches)
- [Mocking a dictionary with MagicMock](unittest.mock-examples.html#mocking-a-dictionary-with-magicmock)
- [Mock subclasses and their attributes](unittest.mock-examples.html#mock-subclasses-and-their-attributes)
- [Mocking imports with patch.dict](unittest.mock-examples.html#mocking-imports-with-patch-dict)
- [Tracking order of calls and less verbose call assertions](unittest.mock-examples.html#tracking-order-of-calls-and-less-verbose-call-assertions)
- [More complex argument matching](unittest.mock-examples.html#more-complex-argument-matching)
 
 
- `test`— Regression tests package for Python
- `test.support`— Utilities for the Python test suite
- `test.support.socket_helper`— Utilities for socket tests
- `test.support.script_helper`— Utilities for the Python execution tests
- `test.support.bytecode_helper`— Support tools for testing correct bytecode generation
- `test.support.threading_helper`— Utilities for threading tests
- `test.support.os_helper`— Utilities for os tests
- `test.support.import_helper`— Utilities for import tests
- `test.support.warnings_helper`— Utilities for warnings tests