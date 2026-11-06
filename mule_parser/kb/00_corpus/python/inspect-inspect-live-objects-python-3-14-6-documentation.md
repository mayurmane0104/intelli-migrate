# inspect — Inspect live objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/inspect.html](https://docs.python.org/library/inspect.html)

---

`inspect` — Inspect live objects[¶](#inspect-inspect-live-objects)

**Source code:** [Lib/inspect.py](https://github.com/python/cpython/tree/3.14/Lib/inspect.py)

The `inspect` module provides several useful functions to help get
information about live objects such as modules, classes, methods, functions,
tracebacks, frame objects, and code objects.  For example, it can help you
examine the contents of a class, retrieve the source code of a method, extract
and format the argument list for a function, or get all the information you need
to display a detailed traceback.

There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the interpreter stack.

## Types and members[¶](#types-and-members)

The [ getmembers()](#inspect.getmembers) function retrieves the members of an object such as a
class or module. The functions whose names begin with “is” are mainly
provided as convenient choices for the second argument to 

`getmembers()`.
They also help you determine when you can expect to find the following special
attributes (see [Import-related attributes on module objects](../reference/datamodel.html#import-mod-attrs)for module attributes):

| Type | Attribute | Description | 
|---|---|---|
| class | __doc__ | documentation string | 
| __name__ | name with which this class was defined | |
| __qualname__ | qualified name | |
| __module__ | name of module in which this class was defined | |
| __type_params__ | A tuple containing the
 | |
| method | __doc__ | documentation string | 
| __name__ | name with which this method was defined | |
| __qualname__ | qualified name | |
| __func__ | function object containing implementation of method | |
| __self__ | instance to which this
method is bound, or
 | |
| __module__ | name of module in which this method was defined | |
| function | __doc__ | documentation string | 
| __name__ | name with which this function was defined | |
| __qualname__ | qualified name | |
| __code__ | code object containing
compiled function
 | |
| __defaults__ | tuple of any default values for positional or keyword parameters | |
| __kwdefaults__ | mapping of any default values for keyword-only parameters | |
| __globals__ | global namespace in which this function was defined | |
| __builtins__ | builtins namespace | |
| __annotations__ | mapping of parameters
names to annotations;
 | |
| __type_params__ | A tuple containing the
 | |
| __module__ | name of module in which this function was defined | |
| traceback | tb_frame | frame object at this level | 
| tb_lasti | index of last attempted instruction in bytecode | |
| tb_lineno | current line number in Python source code | |
| tb_next | next inner traceback object (called by this level) | |
| frame | f_back | next outer frame object (this frame’s caller) | 
| f_builtins | builtins namespace seen by this frame | |
| f_code | code object being executed in this frame | |
| f_globals | global namespace seen by this frame | |
| f_lasti | index of last attempted instruction in bytecode | |
| f_lineno | current line number in Python source code | |
| f_locals | local namespace seen by this frame | |
| f_generator | returns the generator or
coroutine object that
owns this frame, or
 | |
| f_trace | tracing function for this
frame, or  | |
| f_trace_lines | indicate whether a tracing event is triggered for each source source line | |
| f_trace_opcodes | indicate whether per-opcode events are requested | |
| clear() | used to clear all references to local variables | |
| code | co_argcount | number of arguments (not including keyword only arguments, * or ** args) | 
| co_code | string of raw compiled bytecode | |
| co_cellvars | tuple of names of cell variables (referenced by containing scopes) | |
| co_consts | tuple of constants used in the bytecode | |
| co_filename | name of file in which this code object was created | |
| co_firstlineno | number of first line in Python source code | |
| co_flags | bitmap of  | |
| co_lnotab | encoded mapping of line numbers to bytecode indices | |
| co_freevars | tuple of names of free variables (referenced via a function’s closure) | |
| co_posonlyargcount | number of positional only arguments | |
| co_kwonlyargcount | number of keyword only arguments (not including ** arg) | |
| co_name | name with which this code object was defined | |
| co_qualname | fully qualified name with which this code object was defined | |
| co_names | tuple of names other than arguments and function locals | |
| co_nlocals | number of local variables | |
| co_stacksize | virtual machine stack space required | |
| co_varnames | tuple of names of arguments and local variables | |
| co_lines() | returns an iterator that yields successive bytecode ranges | |
| co_positions() | returns an iterator of source code positions for each bytecode instruction | |
| replace() | returns a copy of the code object with new values | |
| generator | __name__ | name | 
| __qualname__ | qualified name | |
| gi_frame | frame | |
| gi_running | is the generator running? | |
| gi_suspended | is the generator suspended? | |
| gi_code | code | |
| gi_yieldfrom | object being iterated by
 | |
| async generator | __name__ | name | 
| __qualname__ | qualified name | |
| ag_await | object being awaited on,
or  | |
| ag_frame | frame | |
| ag_running | is the generator running? | |
| ag_suspended | is the generator suspended? | |
| ag_code | code | |
| coroutine | __name__ | name | 
| __qualname__ | qualified name | |
| cr_await | object being awaited on,
or  | |
| cr_frame | frame | |
| cr_running | is the coroutine running? | |
| cr_suspended | is the coroutine suspended? | |
| cr_code | code | |
| cr_origin | where coroutine was
created, or  | |
| builtin | __doc__ | documentation string | 
| __name__ | original name of this function or method | |
| __qualname__ | qualified name | |
| __self__ | instance to which a
method is bound, or
 | 

Changed in version 3.5: Add `__qualname__` and `gi_yieldfrom` attributes to generators.

The `__name__` attribute of generators is now set from the function
name, instead of the code name, and it can now be modified.

Changed in version 3.7: Add `cr_origin` attribute to coroutines.

Changed in version 3.10: Add `__builtins__` attribute to functions.

Changed in version 3.11: Add `gi_suspended` attribute to generators.

Changed in version 3.11: Add `cr_suspended` attribute to coroutines.

Changed in version 3.12: Add `ag_suspended` attribute to async generators.

Changed in version 3.14: Add `f_generator` attribute to frames.

- 
inspect.getmembers(*object*[,*predicate*])[¶](#inspect.getmembers)
- Return all the members of an object in a list of - `(name, value)`pairs sorted by name. If the optional- *predicate*argument—which will be called with the- `value`object of each member—is supplied, only members for which the predicate returns a true value are included.- Note - `getmembers()`will only return class attributes defined in the metaclass when the argument is a class and those attributes have been listed in the metaclass’ custom- `__dir__()`

- 
inspect.getmembers_static(*object*[,*predicate*])[¶](#inspect.getmembers_static)
- Return all the members of an object in a list of - `(name, value)`pairs sorted by name without triggering dynamic lookup via the descriptor protocol, __getattr__ or __getattribute__. Optionally, only return members that satisfy a given predicate.- Note - `getmembers_static()`may not be able to retrieve all members that getmembers can fetch (like dynamically created attributes) and may find members that getmembers can’t (like descriptors that raise AttributeError). It can also return descriptor objects instead of instance members in some cases.- Added in version 3.11. 

- 
inspect.getmodulename(*path*)[¶](#inspect.getmodulename)
- Return the name of the module named by the file - *path*, without including the names of enclosing packages. The file extension is checked against all of the entries in- `importlib.machinery.all_suffixes()`- `None`is returned.- Note that this function - *only*returns a meaningful name for actual Python modules - paths that potentially refer to Python packages will still return- `None`.- Changed in version 3.3: The function is based directly on - `importlib`

- 
inspect.ismodule(*object*)[¶](#inspect.ismodule)
- Return - `True`if the object is a module.

- 
inspect.isclass(*object*)[¶](#inspect.isclass)
- Return - `True`if the object is a class, whether built-in or created in Python code.- This function returns - `False`for- [generic aliases](stdtypes.html#types-genericalias)of classes, such as- `list[int]`.

- 
inspect.ismethod(*object*)[¶](#inspect.ismethod)
- Return - `True`if the object is a bound method written in Python.- Note - For example, given this class: - >>> class Greeter: ... def say_hello(self): ... print('hello!') - A bound method (also known as an - *instance method*) is created when accessing- `say_hello`(a- [function](../glossary.html#term-function)defined in the- `Greeter`namespace) through an instance of the- `Greeter`class:- >>> instance = Greeter() >>> instance.say_hello <bound method Greeter.say_hello of <__main__.Greeter object ...>> >>> ismethod(instance.say_hello) True >>> isfunction(instance.say_hello) False - Accessing - `say_hello`through the- `Greeter`class will return the function itself. For this function,- `ismethod()`will return- `False`, but- `isfunction()`- `True`:- >>> Greeter.say_hello <function Greeter.say_hello at 0x7f7503854a90> >>> ismethod(Greeter.say_hello) False >>> isfunction(Greeter.say_hello) True - See - [Methods](stdtypes.html#typesmethods)for details.

- 
inspect.isfunction(*object*)[¶](#inspect.isfunction)
- Return - `True`if the object is a Python function, which includes functions created by a- [lambda](../glossary.html#term-lambda)expression.- See the note for - `ismethod()`

- 
inspect.isgeneratorfunction(*object*)[¶](#inspect.isgeneratorfunction)
- Return - `True`if the object is a Python generator function.- It also returns - `True`for bound methods created from Python generator functions (see- [Methods](stdtypes.html#typesmethods)for more information).- Changed in version 3.8: Functions wrapped in - `functools.partial()`- `True`if the wrapped function is a Python generator function.- Changed in version 3.13: Functions wrapped in - `functools.partialmethod()`- `True`if the wrapped function is a Python generator function.

- 
inspect.isgenerator(*object*)[¶](#inspect.isgenerator)
- Return - `True`if the object is a generator.

- 
inspect.iscoroutinefunction(*object*)[¶](#inspect.iscoroutinefunction)
- Return - `True`if the object is a- [coroutine function](../glossary.html#term-coroutine-function)(a function defined with an- `async def`- `functools.partial()`- `markcoroutinefunction()`- Added in version 3.5. - Changed in version 3.8: Functions wrapped in - `functools.partial()`- `True`if the wrapped function is a- [coroutine function](../glossary.html#term-coroutine-function).- Changed in version 3.12: Sync functions marked with - `markcoroutinefunction()`- `True`.- Changed in version 3.13: Functions wrapped in - `functools.partialmethod()`- `True`if the wrapped function is a- [coroutine function](../glossary.html#term-coroutine-function).

- 
inspect.markcoroutinefunction(*func*)[¶](#inspect.markcoroutinefunction)
- Decorator to mark a callable as a - [coroutine function](../glossary.html#term-coroutine-function)if it would not otherwise be detected by- `iscoroutinefunction()`- This may be of use for sync functions that return a - [coroutine](../glossary.html#term-coroutine), if the function is passed to an API that requires- `iscoroutinefunction()`- When possible, using an - `async def`- `iscoroutine()`- Added in version 3.12. 

- 
inspect.iscoroutine(*object*)[¶](#inspect.iscoroutine)
- Return - `True`if the object is a- [coroutine](../glossary.html#term-coroutine)created by an- `async def`- Added in version 3.5. 

- 
inspect.isawaitable(*object*)[¶](#inspect.isawaitable)
- Return - `True`if the object can be used in- `await`- Can also be used to distinguish generator-based coroutines from regular generators: - import types def gen(): yield @types.coroutine def gen_coro(): yield assert not isawaitable(gen()) assert isawaitable(gen_coro()) - Added in version 3.5. 

- 
inspect.isasyncgenfunction(*object*)[¶](#inspect.isasyncgenfunction)
- Return - `True`if the object is an- [asynchronous generator](../glossary.html#term-asynchronous-generator)function, for example:- >>> async def agen(): ... yield 1 ... >>> inspect.isasyncgenfunction(agen) True - Added in version 3.6. - Changed in version 3.8: Functions wrapped in - `functools.partial()`- `True`if the wrapped function is an- [asynchronous generator](../glossary.html#term-asynchronous-generator)function.- Changed in version 3.13: Functions wrapped in - `functools.partialmethod()`- `True`if the wrapped function is a- [asynchronous generator](../glossary.html#term-asynchronous-generator)function.

- 
inspect.isasyncgen(*object*)[¶](#inspect.isasyncgen)
- Return - `True`if the object is an- [asynchronous generator iterator](../glossary.html#term-asynchronous-generator-iterator)created by an- [asynchronous generator](../glossary.html#term-asynchronous-generator)function.- Added in version 3.6. 

- 
inspect.istraceback(*object*)[¶](#inspect.istraceback)
- Return - `True`if the object is a traceback.

- 
inspect.isframe(*object*)[¶](#inspect.isframe)
- Return - `True`if the object is a frame.

- 
inspect.iscode(*object*)[¶](#inspect.iscode)
- Return - `True`if the object is a code.

- 
inspect.isbuiltin(*object*)[¶](#inspect.isbuiltin)
- Return - `True`if the object is a built-in function or a bound built-in method.

- 
inspect.ismethodwrapper(*object*)[¶](#inspect.ismethodwrapper)
- Return - `True`if the type of object is a- `MethodWrapperType`- These are instances of - `MethodWrapperType`- `__str__()`- `__eq__()`- `__repr__()`- Added in version 3.11. 

- 
inspect.isroutine(*object*)[¶](#inspect.isroutine)
- Return - `True`if the object is a user-defined or built-in function or method.

- 
inspect.isabstract(*object*)[¶](#inspect.isabstract)
- Return - `True`if the object is an abstract base class.

- 
inspect.ismethoddescriptor(*object*)[¶](#inspect.ismethoddescriptor)
- Return - `True`if the object is a method descriptor, but not if- `ismethod()`- `isclass()`- `isfunction()`- `isbuiltin()`- This, for example, is true of - `int.__add__`. An object passing this test has a- `__get__()`- `__set__()`- `__delete__()`- `__name__`- `__doc__`- Methods implemented via descriptors that also pass one of the other tests return - `False`from the- `ismethoddescriptor()`test, simply because the other tests promise more – you can, e.g., count on having the- `__func__`- `ismethod()`- Changed in version 3.13: This function no longer incorrectly reports objects with - `__get__()`- `__delete__()`- `__set__()`

- 
inspect.isdatadescriptor(*object*)[¶](#inspect.isdatadescriptor)
- Return - `True`if the object is a data descriptor.- Data descriptors have a - `__set__`- `__delete__`- `__name__`- `__doc__`attributes (properties, getsets, and members have both of these attributes), but this is not guaranteed.

- 
inspect.isgetsetdescriptor(*object*)[¶](#inspect.isgetsetdescriptor)
- Return - `True`if the object is a getset descriptor.- **CPython implementation detail:**getsets are attributes defined in extension modules via- `PyGetSetDef`- `False`.

- 
inspect.ismemberdescriptor(*object*)[¶](#inspect.ismemberdescriptor)
- Return - `True`if the object is a member descriptor.- **CPython implementation detail:**Member descriptors are attributes defined in extension modules via- `PyMemberDef`- `False`.

## Retrieving source code[¶](#retrieving-source-code)

- 
inspect.getdoc(*object*)[¶](#inspect.getdoc)
- Get the documentation string for an object, cleaned up with - `cleandoc()`- `None`if the documentation string is invalid or missing.- Changed in version 3.5: Documentation strings are now inherited if not overridden. 

- 
inspect.getcomments(*object*)[¶](#inspect.getcomments)
- Return in a single string any lines of comments immediately preceding the object’s source code (for a class, function, or method), or at the top of the Python source file (if the object is a module). If the object’s source code is unavailable, return - `None`. This could happen if the object has been defined in C or the interactive shell.

- 
inspect.getfile(*object*)[¶](#inspect.getfile)
- Return the name of the (text or binary) file in which an object was defined. This will fail with a - `TypeError`

- 
inspect.getmodule(*object*)[¶](#inspect.getmodule)
- Try to guess which module an object was defined in. Return - `None`if the module cannot be determined.

- 
inspect.getsourcefile(*object*)[¶](#inspect.getsourcefile)
- Return the name of the Python source file in which an object was defined or - `None`if no way can be identified to get the source. This will fail with a- `TypeError`

- 
inspect.getsourcelines(*object*)[¶](#inspect.getsourcelines)
- Return a list of source lines and starting line number for an object. The argument may be a module, class, method, function, traceback, frame, or code object. The source code is returned as a list of the lines corresponding to the object and the line number indicates where in the original source file the first line of code was found. An - `OSError`- `TypeError`

- 
inspect.getsource(*object*)[¶](#inspect.getsource)
- Return the text of the source code for an object. The argument may be a module, class, method, function, traceback, frame, or code object. The source code is returned as a single string. An - `OSError`- `TypeError`

- 
inspect.cleandoc(*doc*)[¶](#inspect.cleandoc)
- Clean up indentation from docstrings that are indented to line up with blocks of code. - All leading whitespace is removed from the first line. Any leading whitespace that can be uniformly removed from the second line onwards is removed. Empty lines at the beginning and end are subsequently removed. Also, all tabs are expanded to spaces. 

## Introspecting callables with the Signature object[¶](#introspecting-callables-with-the-signature-object)

Added in version 3.3.

The [ Signature](#inspect.Signature) object represents the call signature of a callable object
and its return annotation. To retrieve a 

`Signature` object,
use the `signature()`
function.- 
inspect.signature(*callable*,***,*follow_wrapped=True*,*globals=None*,*locals=None*,*eval_str=False*,*annotation_format=Format.VALUE*)[¶](#inspect.signature)
- Return a - `Signature`- *callable*:- >>> from inspect import signature >>> def foo(a, *, b:int, **kwargs): ... pass >>> sig = signature(foo) >>> str(sig) '(a, *, b: int, **kwargs)' >>> str(sig.parameters['b']) 'b: int' >>> sig.parameters['b'].annotation <class 'int'> - Accepts a wide range of Python callables, from plain functions and classes to - `functools.partial()`- If some of the annotations are strings (e.g., because - `from __future__ import annotations`was used),- `signature()`will attempt to automatically un-stringize the annotations using- `annotationlib.get_annotations()`- *globals*,- *locals*, and- *eval_str*parameters are passed into- `annotationlib.get_annotations()`when resolving the annotations; see the documentation for- `annotationlib.get_annotations()`for instructions on how to use these parameters. A member of the- `annotationlib.Format`- *annotation_format*parameter to control the format of the returned annotations. For example, use- `annotation_format=annotationlib.Format.STRING`to return annotations in string format.- Raises - `ValueError`- `TypeError`- *eval_str*is not false, the- `eval()`call(s) to un-stringize the annotations in- `annotationlib.get_annotations()`- A slash (/) in the signature of a function denotes that the parameters prior to it are positional-only. For more info, see - [the FAQ entry on positional-only parameters](../faq/programming.html#faq-positional-only-arguments).- Changed in version 3.5: The - *follow_wrapped*parameter was added. Pass- `False`to get a signature of- *callable*specifically (- `callable.__wrapped__`will not be used to unwrap decorated callables.)- Changed in version 3.10: The - *globals*,- *locals*, and- *eval_str*parameters were added.- Changed in version 3.14: The - *annotation_format*parameter was added.- Note - Some callables may not be introspectable in certain implementations of Python. For example, in CPython, some built-in functions defined in C provide no metadata about their arguments. - **CPython implementation detail:**If the passed object has a- `__signature__`attribute, we may use it to create the signature. The exact semantics are an implementation detail and are subject to unannounced changes. Consult the source code for current semantics.

- 
*class*inspect.Signature(*parameters=None*,***,*return_annotation=Signature.empty*)[¶](#inspect.Signature)
- A - `Signature`object represents the call signature of a function and its return annotation. For each parameter accepted by the function it stores a- `Parameter`- `parameters`- The optional - *parameters*argument is a sequence of- `Parameter`- The optional - *return_annotation*argument can be an arbitrary Python object. It represents the “return” annotation of the callable.- `Signature`objects are- *immutable*. Use- `Signature.replace()`- `copy.replace()`- Changed in version 3.5: - `Signature`objects are now picklable and- [hashable](../glossary.html#term-hashable).- 
empty[¶](#inspect.Signature.empty)
- A special class-level marker to specify absence of a return annotation. 
 - 
parameters[¶](#inspect.Signature.parameters)
- An ordered mapping of parameters’ names to the corresponding - `Parameter`- Changed in version 3.7: Python only explicitly guaranteed that it preserved the declaration order of keyword-only parameters as of version 3.7, although in practice this order had always been preserved in Python 3. 
 - 
return_annotation[¶](#inspect.Signature.return_annotation)
- The “return” annotation for the callable. If the callable has no “return” annotation, this attribute is set to - `Signature.empty`
 - 
bind(**args*,***kwargs*)[¶](#inspect.Signature.bind)
- Create a mapping from positional and keyword arguments to parameters. Returns - `BoundArguments`- `*args`and- `**kwargs`match the signature, or raises a- `TypeError`
 - 
bind_partial(**args*,***kwargs*)[¶](#inspect.Signature.bind_partial)
- Works the same way as - `Signature.bind()`- `functools.partial()`- `BoundArguments`- `TypeError`
 - 
replace(**[, parameters][, return_annotation]*)[¶](#inspect.Signature.replace)
- Create a new - `Signature`instance based on the instance- `replace()`was invoked on. It is possible to pass different- *parameters*and/or- *return_annotation*to override the corresponding properties of the base signature. To remove- `return_annotation`from the copied- `Signature`, pass in- `Signature.empty`- >>> def test(a, b): ... pass ... >>> sig = signature(test) >>> new_sig = sig.replace(return_annotation="new return anno") >>> str(new_sig) "(a, b) -> 'new return anno'" - `Signature`objects are also supported by the generic function- `copy.replace()`
 - 
format(***,*max_width=None*,*quote_annotation_strings=True*)[¶](#inspect.Signature.format)
- Create a string representation of the - `Signature`object.- If - *max_width*is passed, the method will attempt to fit the signature into lines of at most- *max_width*characters. If the signature is longer than- *max_width*, all parameters will be on separate lines.- If - *quote_annotation_strings*is False,- [annotations](../glossary.html#term-annotation)in the signature are displayed without opening and closing quotation marks if they are strings. This is useful if the signature was created with the- `STRING`- `from __future__ import annotations`was used.- Added in version 3.13. - Changed in version 3.14: The - *unquote_annotations*parameter was added.
 - 
*classmethod*from_callable(*obj*,***,*follow_wrapped=True*,*globals=None*,*locals=None*,*eval_str=False*)[¶](#inspect.Signature.from_callable)
- Return a - `Signature`(or its subclass) object for a given callable- *obj*.- This method simplifies subclassing of - `Signature`:- class MySignature(Signature): pass sig = MySignature.from_callable(sum) assert isinstance(sig, MySignature) - Its behavior is otherwise identical to that of - `signature()`- Added in version 3.5. - Changed in version 3.10: The - *globals*,- *locals*, and- *eval_str*parameters were added.
 
- 
empty

- 
*class*inspect.Parameter(*name*,*kind*,***,*default=Parameter.empty*,*annotation=Parameter.empty*)[¶](#inspect.Parameter)
- `Parameter`objects are- *immutable*. Instead of modifying a- `Parameter`object, you can use- `Parameter.replace()`- `copy.replace()`- Changed in version 3.5: Parameter objects are now picklable and - [hashable](../glossary.html#term-hashable).- 
empty[¶](#inspect.Parameter.empty)
- A special class-level marker to specify absence of default values and annotations. 
 - 
name[¶](#inspect.Parameter.name)
- The name of the parameter as a string. The name must be a valid Python identifier. - **CPython implementation detail:**CPython generates implicit parameter names of the form- `.0`on the code objects used to implement comprehensions and generator expressions.- Changed in version 3.6: These parameter names are now exposed by this module as names like - `implicit0`.
 - 
default[¶](#inspect.Parameter.default)
- The default value for the parameter. If the parameter has no default value, this attribute is set to - `Parameter.empty`
 - 
annotation[¶](#inspect.Parameter.annotation)
- The annotation for the parameter. If the parameter has no annotation, this attribute is set to - `Parameter.empty`
 - 
kind[¶](#inspect.Parameter.kind)
- Describes how argument values are bound to the parameter. The possible values are accessible via - `Parameter`(like- `Parameter.KEYWORD_ONLY`), and support comparison and ordering, in the following order:- Name - Meaning - *POSITIONAL_ONLY*- Value must be supplied as a positional argument. Positional only parameters are those which appear before a - `/`entry (if present) in a Python function definition.- *POSITIONAL_OR_KEYWORD*- Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python.) - *VAR_POSITIONAL*- A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a - `*args`parameter in a Python function definition.- *KEYWORD_ONLY*- Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a - `*`or- `*args`entry in a Python function definition.- *VAR_KEYWORD*- A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a - `**kwargs`parameter in a Python function definition.- Example: print all keyword-only arguments without default values: - >>> def foo(a, b, *, c, d=10): ... pass >>> sig = signature(foo) >>> for param in sig.parameters.values(): ... if (param.kind == param.KEYWORD_ONLY and ... param.default is param.empty): ... print('Parameter:', param) Parameter: c 
 - 
kind.description[¶](#inspect.Parameter.kind.description)
- Describes an enum value of - `Parameter.kind`- Added in version 3.8. - Example: print all descriptions of arguments: - >>> def foo(a, b, *, c, d=10): ... pass >>> sig = signature(foo) >>> for param in sig.parameters.values(): ... print(param.kind.description) positional or keyword positional or keyword keyword-only keyword-only 
 - 
replace(**[, name][, kind][, default][, annotation]*)[¶](#inspect.Parameter.replace)
- Create a new - `Parameter`instance based on the instance replaced was invoked on. To override a- `Parameter`attribute, pass the corresponding argument. To remove a default value or/and an annotation from a- `Parameter`, pass- `Parameter.empty`- >>> from inspect import Parameter >>> param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42) >>> str(param) 'foo=42' >>> str(param.replace()) # Will create a shallow copy of 'param' 'foo=42' >>> str(param.replace(default=Parameter.empty, annotation='spam')) "foo: 'spam'" - `Parameter`objects are also supported by the generic function- `copy.replace()`
 - Changed in version 3.4: In Python 3.3 - `Parameter`objects were allowed to have- `name`set to- `None`if their- `kind`was set to- `POSITIONAL_ONLY`. This is no longer permitted.
- 
empty

- 
*class*inspect.BoundArguments[¶](#inspect.BoundArguments)
- Result of a - `Signature.bind()`- `Signature.bind_partial()`- 
arguments[¶](#inspect.BoundArguments.arguments)
- A mutable mapping of parameters’ names to arguments’ values. Contains only explicitly bound arguments. Changes in - `arguments`- `args`- `kwargs`- Should be used in conjunction with - `Signature.parameters`- Note - Arguments for which - `Signature.bind()`- `Signature.bind_partial()`- `BoundArguments.apply_defaults()`- Changed in version 3.9: - `arguments`- `dict`- `collections.OrderedDict`
 - 
kwargs[¶](#inspect.BoundArguments.kwargs)
- A dict of keyword arguments values. Dynamically computed from the - `arguments`- `args`
 - 
apply_defaults()[¶](#inspect.BoundArguments.apply_defaults)
- Set default values for missing arguments. - For variable-positional arguments ( - `*args`) the default is an empty tuple.- For variable-keyword arguments ( - `**kwargs`) the default is an empty dict.- >>> def foo(a, b='ham', *args): pass >>> ba = inspect.signature(foo).bind('spam') >>> ba.apply_defaults() >>> ba.arguments {'a': 'spam', 'b': 'ham', 'args': ()} - Added in version 3.5. 
 - The - `args`- `kwargs`- def test(a, *, b): ... sig = signature(test) ba = sig.bind(10, b=20) test(*ba.args, **ba.kwargs) 
- 
arguments

See also

- **PEP 362**
- The detailed specification, implementation details and examples. 

## Classes and functions[¶](#classes-and-functions)

- 
inspect.getclasstree(*classes*,*unique=False*)[¶](#inspect.getclasstree)
- Arrange the given list of classes into a hierarchy of nested lists. Where a nested list appears, it contains classes derived from the class whose entry immediately precedes the list. Each entry is a 2-tuple containing a class and a tuple of its base classes. If the - *unique*argument is true, exactly one entry appears in the returned structure for each class in the given list. Otherwise, classes using multiple inheritance and their descendants will appear multiple times.

- 
inspect.getfullargspec(*func*)[¶](#inspect.getfullargspec)
- Get the names and default values of a Python function’s parameters. A - [named tuple](../glossary.html#term-named-tuple)is returned:- `FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)`- *args*is a list of the positional parameter names.- *varargs*is the name of the- `*`parameter or- `None`if arbitrary positional arguments are not accepted.- *varkw*is the name of the- `**`parameter or- `None`if arbitrary keyword arguments are not accepted.- *defaults*is an- *n*-tuple of default argument values corresponding to the last- *n*positional parameters, or- `None`if there are no such defaults defined.- *kwonlyargs*is a list of keyword-only parameter names in declaration order.- *kwonlydefaults*is a dictionary mapping parameter names from- *kwonlyargs*to the default values used if no argument is supplied.- *annotations*is a dictionary mapping parameter names to annotations. The special key- `"return"`is used to report the function return value annotation (if any).- Note that - `signature()`- [Signature Object](#inspect-signature-object)provide the recommended API for callable introspection, and support additional behaviours (like positional-only arguments) that are sometimes encountered in extension module APIs. This function is retained primarily for use in code that needs to maintain compatibility with the Python 2- `inspect`module API.- Changed in version 3.4: This function is now based on - `signature()`- `__wrapped__`attributes and includes the already bound first parameter in the signature output for bound methods.- Changed in version 3.6: This method was previously documented as deprecated in favour of - `signature()`- `getargspec()`API.- Changed in version 3.7: Python only explicitly guaranteed that it preserved the declaration order of keyword-only parameters as of version 3.7, although in practice this order had always been preserved in Python 3. 

- 
inspect.getargvalues(*frame*)[¶](#inspect.getargvalues)
- Get information about arguments passed into a particular frame. A - [named tuple](../glossary.html#term-named-tuple)- `ArgInfo(args, varargs, keywords, locals)`is returned.- *args*is a list of the argument names.- *varargs*and- *keywords*are the names of the- `*`and- `**`arguments or- `None`.- *locals*is the locals dictionary of the given frame.- Note - This function was inadvertently marked as deprecated in Python 3.5. 

- 
inspect.formatargvalues(*args*[,*varargs*,*varkw*,*locals*,*formatarg*,*formatvarargs*,*formatvarkw*,*formatvalue*])[¶](#inspect.formatargvalues)
- Format a pretty argument spec from the four values returned by - `getargvalues()`- Note - This function was inadvertently marked as deprecated in Python 3.5. 

- 
inspect.getmro(*cls*)[¶](#inspect.getmro)
- Return a tuple of class cls’s base classes, including cls, in method resolution order. No class appears more than once in this tuple. Note that the method resolution order depends on cls’s type. Unless a very peculiar user-defined metatype is in use, cls will be the first element of the tuple. 

- 
inspect.getcallargs(*func*,*/*,**args*,***kwds*)[¶](#inspect.getcallargs)
- Bind the - *args*and- *kwds*to the argument names of the Python function or method- *func*, as if it was called with them. For bound methods, bind also the first argument (typically named- `self`) to the associated instance. A dict is returned, mapping the argument names (including the names of the- `*`and- `**`arguments, if any) to their values from- *args*and- *kwds*. In case of invoking- *func*incorrectly, i.e. whenever- `func(*args, **kwds)`would raise an exception because of incompatible signature, an exception of the same type and the same or similar message is raised. For example:- >>> from inspect import getcallargs >>> def f(a, b=1, *pos, **named): ... pass ... >>> getcallargs(f, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)} True >>> getcallargs(f, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()} True >>> getcallargs(f) Traceback (most recent call last): ... TypeError: f() missing 1 required positional argument: 'a' - Added in version 3.2. - Deprecated since version 3.5: Use - `Signature.bind()`- `Signature.bind_partial()`

- 
inspect.getclosurevars(*func*)[¶](#inspect.getclosurevars)
- Get the mapping of external name references in a Python function or method - *func*to their current values. A- [named tuple](../glossary.html#term-named-tuple)- `ClosureVars(nonlocals, globals, builtins, unbound)`is returned.- *nonlocals*maps referenced names to lexical closure variables,- *globals*to the function’s module globals and- *builtins*to the builtins visible from the function body.- *unbound*is the set of names referenced in the function that could not be resolved at all given the current module globals and builtins.- `TypeError`- *func*is not a Python function or method.- Added in version 3.3. 

- 
inspect.unwrap(*func*,***,*stop=None*)[¶](#inspect.unwrap)
- Get the object wrapped by - *func*. It follows the chain of- `__wrapped__`attributes returning the last object in the chain.- *stop*is an optional callback accepting an object in the wrapper chain as its sole argument that allows the unwrapping to be terminated early if the callback returns a true value. If the callback never returns a true value, the last object in the chain is returned as usual. For example,- `signature()`- `__signature__`attribute defined.- `ValueError`- Added in version 3.4. 

- 
inspect.get_annotations(*obj*,***,*globals=None*,*locals=None*,*eval_str=False*,*format=annotationlib.Format.VALUE*)[¶](#inspect.get_annotations)
- Compute the annotations dict for an object. - This is an alias for - `annotationlib.get_annotations()`- Caution - This function may execute arbitrary code contained in annotations. See - [Security implications of introspecting annotations](annotationlib.html#annotationlib-security)for more information.- Added in version 3.10. - Changed in version 3.14: This function is now an alias for - `annotationlib.get_annotations()`- `inspect.get_annotations`will continue to work.

## The interpreter stack[¶](#the-interpreter-stack)

Some of the following functions return
[ FrameInfo](#inspect.FrameInfo) objects. For backwards compatibility these objects allow
tuple-like operations on all attributes except 

`positions`. This behavior
is considered deprecated and may be removed in the future.- 
*class*inspect.FrameInfo[¶](#inspect.FrameInfo)
- 
frame[¶](#inspect.FrameInfo.frame)
- The - [frame object](../reference/datamodel.html#frame-objects)that the record corresponds to.
 - 
filename[¶](#inspect.FrameInfo.filename)
- The file name associated with the code being executed by the frame this record corresponds to. 
 - 
lineno[¶](#inspect.FrameInfo.lineno)
- The line number of the current line associated with the code being executed by the frame this record corresponds to. 
 - 
function[¶](#inspect.FrameInfo.function)
- The function name that is being executed by the frame this record corresponds to. 
 - 
code_context[¶](#inspect.FrameInfo.code_context)
- A list of lines of context from the source code that’s being executed by the frame this record corresponds to. 
 - 
index[¶](#inspect.FrameInfo.index)
- The index of the current line being executed in the - `code_context`
 - 
positions[¶](#inspect.FrameInfo.positions)
- A - `dis.Positions`
 - Changed in version 3.5: Return a - [named tuple](../glossary.html#term-named-tuple)instead of a- `tuple`- Changed in version 3.11: - `FrameInfo`is now a class instance (that is backwards compatible with the previous- [named tuple](../glossary.html#term-named-tuple)).
- 
frame

- 
*class*inspect.Traceback[¶](#inspect.Traceback)
- 
filename[¶](#inspect.Traceback.filename)
- The file name associated with the code being executed by the frame this traceback corresponds to. 
 - 
lineno[¶](#inspect.Traceback.lineno)
- The line number of the current line associated with the code being executed by the frame this traceback corresponds to. 
 - 
function[¶](#inspect.Traceback.function)
- The function name that is being executed by the frame this traceback corresponds to. 
 - 
code_context[¶](#inspect.Traceback.code_context)
- A list of lines of context from the source code that’s being executed by the frame this traceback corresponds to. 
 - 
index[¶](#inspect.Traceback.index)
- The index of the current line being executed in the - `code_context`
 - 
positions[¶](#inspect.Traceback.positions)
- A - `dis.Positions`
 - Changed in version 3.11: - `Traceback`is now a class instance (that is backwards compatible with the previous- [named tuple](../glossary.html#term-named-tuple)).
- 
filename

Note

Keeping references to frame objects, as found in the first element of the frame records these functions return, can cause your program to create reference cycles. Once a reference cycle has been created, the lifespan of all objects which can be accessed from the objects which form the cycle can become much longer even if Python’s optional cycle detector is enabled. If such cycles must be created, it is important to ensure they are explicitly broken to avoid the delayed destruction of objects and increased memory consumption which occurs.

Though the cycle detector will catch these, destruction of the frames (and local
variables) can be made deterministic by removing the cycle in a
[ finally](../reference/compound_stmts.html#finally) clause.  This is also important if the cycle detector was
disabled when Python was compiled or using 

[. For example:](gc.html#gc.disable)

`gc.disable()````
def handle_stackframe_without_leak():
    frame = inspect.currentframe()
    try:
        # do something with the frame
    finally:
        del frame
```
If you want to keep the frame around (for example to print a traceback
later), you can also break reference cycles by using the
[ frame.clear()](../reference/datamodel.html#frame.clear) method.

The optional *context* argument supported by most of these functions specifies
the number of lines of context to return, which are centered around the current
line.

- 
inspect.getframeinfo(*frame*,*context=1*)[¶](#inspect.getframeinfo)
- Get information about a frame or traceback object. A - `Traceback`- Changed in version 3.11: A - `Traceback`

- 
inspect.getouterframes(*frame*,*context=1*)[¶](#inspect.getouterframes)
- Get a list of - `FrameInfo`- *frame*. The first entry in the returned list represents- *frame*; the last entry represents the outermost call on- *frame*’s stack.- Changed in version 3.5: A list of - [named tuples](../glossary.html#term-named-tuple)- `FrameInfo(frame, filename, lineno, function, code_context, index)`is returned.- Changed in version 3.11: A list of - `FrameInfo`

- 
inspect.getinnerframes(*traceback*,*context=1*)[¶](#inspect.getinnerframes)
- Get a list of - `FrameInfo`- *frame*. The first entry in the list represents- *traceback*; the last entry represents where the exception was raised.- Changed in version 3.5: A list of - [named tuples](../glossary.html#term-named-tuple)- `FrameInfo(frame, filename, lineno, function, code_context, index)`is returned.- Changed in version 3.11: A list of - `FrameInfo`

- 
inspect.currentframe()[¶](#inspect.currentframe)
- Return the frame object for the caller’s stack frame. - **CPython implementation detail:**This function relies on Python stack frame support in the interpreter, which isn’t guaranteed to exist in all implementations of Python. If running in an implementation without Python stack frame support this function returns- `None`.

- 
inspect.stack(*context=1*)[¶](#inspect.stack)
- Return a list of - `FrameInfo`- Changed in version 3.5: A list of - [named tuples](../glossary.html#term-named-tuple)- `FrameInfo(frame, filename, lineno, function, code_context, index)`is returned.- Changed in version 3.11: A list of - `FrameInfo`

- 
inspect.trace(*context=1*)[¶](#inspect.trace)
- Return a list of - `FrameInfo`- Changed in version 3.5: A list of - [named tuples](../glossary.html#term-named-tuple)- `FrameInfo(frame, filename, lineno, function, code_context, index)`is returned.- Changed in version 3.11: A list of - `FrameInfo`

## Fetching attributes statically[¶](#fetching-attributes-statically)

Both [ getattr()](functions.html#getattr) and 

[can trigger code execution when fetching or checking for the existence of attributes. Descriptors, like properties, will be invoked and](functions.html#hasattr)

`hasattr()`[and](../reference/datamodel.html#object.__getattr__)

`__getattr__()`[may be called.](../reference/datamodel.html#object.__getattribute__)

`__getattribute__()`For cases where you want passive introspection, like documentation tools, this
can be inconvenient. [ getattr_static()](#inspect.getattr_static) has a similar signature as 

[but avoids executing code when it fetches attributes.](functions.html#getattr)

`getattr()`- 
inspect.getattr_static(*obj*,*attr*)[¶](#inspect.getattr_static)
- 
inspect.getattr_static(*obj*,*attr*,*default*)
- Retrieve attributes without triggering dynamic lookup via the descriptor protocol, - `__getattr__()`- `__getattribute__()`- Note: this function may not be able to retrieve all attributes that getattr can fetch (like dynamically created attributes) and may find attributes that getattr can’t (like descriptors that raise AttributeError). It can also return descriptors objects instead of instance members. - If the instance - `__dict__`- Added in version 3.2. 

[ getattr_static()](#inspect.getattr_static) does not resolve descriptors, for example slot descriptors or
getset descriptors on objects implemented in C. The descriptor object
is returned instead of the underlying attribute.

You can handle these with code like the following. Note that for arbitrary getset descriptors invoking these may trigger code execution:

```
# example code for resolving the builtin descriptor types
class _foo:
    __slots__ = ['foo']
slot_descriptor = type(_foo.foo)
getset_descriptor = type(type(open(__file__)).name)
wrapper_descriptor = type(str.__dict__['__add__'])
descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)
result = getattr_static(some_object, 'foo')
if type(result) in descriptor_types:
    try:
        result = result.__get__()
    except AttributeError:
        # descriptors can raise AttributeError to
        # indicate there is no underlying value
        # in which case the descriptor itself will
        # have to do
        pass
```
## Current State of Generators, Coroutines, and Asynchronous Generators[¶](#current-state-of-generators-coroutines-and-asynchronous-generators)

When implementing coroutine schedulers and for other advanced uses of
generators, it is useful to determine whether a generator is currently
executing, is waiting to start or resume or execution, or has already
terminated. [ getgeneratorstate()](#inspect.getgeneratorstate) allows the current state of a
generator to be determined easily.

- 
inspect.getgeneratorstate(*generator*)[¶](#inspect.getgeneratorstate)
- Get current state of a generator-iterator. - Possible states are: - GEN_CREATED: Waiting to start execution. 
- GEN_RUNNING: Currently being executed by the interpreter. 
- GEN_SUSPENDED: Currently suspended at a yield expression. 
- GEN_CLOSED: Execution has completed. 
 - Added in version 3.2. 

- 
inspect.getcoroutinestate(*coroutine*)[¶](#inspect.getcoroutinestate)
- Get current state of a coroutine object. The function is intended to be used with coroutine objects created by - `async def`- `cr_running`and- `cr_frame`attributes.- Possible states are: - CORO_CREATED: Waiting to start execution. 
- CORO_RUNNING: Currently being executed by the interpreter. 
- CORO_SUSPENDED: Currently suspended at an await expression. 
- CORO_CLOSED: Execution has completed. 
 - Added in version 3.5. 

- 
inspect.getasyncgenstate(*agen*)[¶](#inspect.getasyncgenstate)
- Get current state of an asynchronous generator object. The function is intended to be used with asynchronous iterator objects created by - `async def`- `yield`- `ag_running`and- `ag_frame`attributes.- Possible states are: - AGEN_CREATED: Waiting to start execution. 
- AGEN_RUNNING: Currently being executed by the interpreter. 
- AGEN_SUSPENDED: Currently suspended at a yield expression. 
- AGEN_CLOSED: Execution has completed. 
 - Added in version 3.12. 

The current internal state of the generator can also be queried. This is mostly useful for testing purposes, to ensure that internal state is being updated as expected:

- 
inspect.getgeneratorlocals(*generator*)[¶](#inspect.getgeneratorlocals)
- Get the mapping of live local variables in - *generator*to their current values. A dictionary is returned that maps from variable names to values. This is the equivalent of calling- `locals()`- If - *generator*is a- [generator](../glossary.html#term-generator)with no currently associated frame, then an empty dictionary is returned.- `TypeError`- *generator*is not a Python generator object.- **CPython implementation detail:**This function relies on the generator exposing a Python stack frame for introspection, which isn’t guaranteed to be the case in all implementations of Python. In such cases, this function will always return an empty dictionary.- Added in version 3.3. 

- 
inspect.getcoroutinelocals(*coroutine*)[¶](#inspect.getcoroutinelocals)
- This function is analogous to - `getgeneratorlocals()`- `async def`- Added in version 3.5. 

- 
inspect.getasyncgenlocals(*agen*)[¶](#inspect.getasyncgenlocals)
- This function is analogous to - `getgeneratorlocals()`- `async def`- `yield`- Added in version 3.12. 

## Code Objects Bit Flags[¶](#code-objects-bit-flags)

Python code objects have a [ co_flags](../reference/datamodel.html#codeobject.co_flags) attribute,
which is a bitmap of the following flags:

- 
inspect.CO_OPTIMIZED[¶](#inspect.CO_OPTIMIZED)
- The code object is optimized, using fast locals. 

- 
inspect.CO_NEWLOCALS[¶](#inspect.CO_NEWLOCALS)
- If set, a new dict will be created for the frame’s - `f_locals`

- 
inspect.CO_VARARGS[¶](#inspect.CO_VARARGS)
- The code object has a variable positional parameter ( - `*args`-like).

- 
inspect.CO_VARKEYWORDS[¶](#inspect.CO_VARKEYWORDS)
- The code object has a variable keyword parameter ( - `**kwargs`-like).

- 
inspect.CO_NESTED[¶](#inspect.CO_NESTED)
- The flag is set when the code object is a nested function. 

- 
inspect.CO_GENERATOR[¶](#inspect.CO_GENERATOR)
- The flag is set when the code object is a generator function, i.e. a generator object is returned when the code object is executed. 

- 
inspect.CO_COROUTINE[¶](#inspect.CO_COROUTINE)
- The flag is set when the code object is a coroutine function. When the code object is executed it returns a coroutine object. See - **PEP 492**- Added in version 3.5. 

- 
inspect.CO_ITERABLE_COROUTINE[¶](#inspect.CO_ITERABLE_COROUTINE)
- The flag is used to transform generators into generator-based coroutines. Generator objects with this flag can be used in - `await`expression, and can- `yield from`coroutine objects. See- **PEP 492**- Added in version 3.5. 

- 
inspect.CO_ASYNC_GENERATOR[¶](#inspect.CO_ASYNC_GENERATOR)
- The flag is set when the code object is an asynchronous generator function. When the code object is executed it returns an asynchronous generator object. See - **PEP 525**- Added in version 3.6. 

- 
inspect.CO_HAS_DOCSTRING[¶](#inspect.CO_HAS_DOCSTRING)
- The flag is set when there is a docstring for the code object in the source code. If set, it will be the first item in - `co_consts`- Added in version 3.14. 

- 
inspect.CO_METHOD[¶](#inspect.CO_METHOD)
- The flag is set when the code object is a function defined in class scope. - Added in version 3.14. 

Note

The flags are specific to CPython, and may not be defined in other
Python implementations.  Furthermore, the flags are an implementation
detail, and can be removed or deprecated in future Python releases.
It’s recommended to use public APIs from the `inspect` module
for any introspection needs.

## Buffer flags[¶](#buffer-flags)

- 
*class*inspect.BufferFlags[¶](#inspect.BufferFlags)
- This is an - `enum.IntFlag`- `__buffer__()`- [buffer protocol](../c-api/buffer.html#bufferobjects).- The meaning of the flags is explained at - [Buffer request types](../c-api/buffer.html#buffer-request-types).- 
SIMPLE[¶](#inspect.BufferFlags.SIMPLE)
 - 
WRITABLE[¶](#inspect.BufferFlags.WRITABLE)
 - 
FORMAT[¶](#inspect.BufferFlags.FORMAT)
 - 
ND[¶](#inspect.BufferFlags.ND)
 - 
STRIDES[¶](#inspect.BufferFlags.STRIDES)
 - 
C_CONTIGUOUS[¶](#inspect.BufferFlags.C_CONTIGUOUS)
 - 
F_CONTIGUOUS[¶](#inspect.BufferFlags.F_CONTIGUOUS)
 - 
ANY_CONTIGUOUS[¶](#inspect.BufferFlags.ANY_CONTIGUOUS)
 - 
INDIRECT[¶](#inspect.BufferFlags.INDIRECT)
 - 
CONTIG[¶](#inspect.BufferFlags.CONTIG)
 - 
CONTIG_RO[¶](#inspect.BufferFlags.CONTIG_RO)
 - 
STRIDED[¶](#inspect.BufferFlags.STRIDED)
 - 
STRIDED_RO[¶](#inspect.BufferFlags.STRIDED_RO)
 - 
RECORDS[¶](#inspect.BufferFlags.RECORDS)
 - 
RECORDS_RO[¶](#inspect.BufferFlags.RECORDS_RO)
 - 
FULL[¶](#inspect.BufferFlags.FULL)
 - 
FULL_RO[¶](#inspect.BufferFlags.FULL_RO)
 - 
READ[¶](#inspect.BufferFlags.READ)
 - 
WRITE[¶](#inspect.BufferFlags.WRITE)
 - Added in version 3.12. 
- 
SIMPLE

## Command-line interface[¶](#command-line-interface)

The `inspect` module also provides a basic introspection capability
from the command line.

By default, accepts the name of a module and prints the source of that module. A class or function within the module can be printed instead by appended a colon and the qualified name of the target object.

- 
--details[¶](#cmdoption-inspect-details)
- Print information about the specified object rather than the source code