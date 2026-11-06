# Built-in Constants — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/constants.html](https://docs.python.org/library/constants.html)

---

# Built-in Constants[¶](#built-in-constants)

A small number of constants live in the built-in namespace. They are:

- 
False[¶](#False)
- The false value of the - `bool`- `False`are illegal and raise a- `SyntaxError`

- 
True[¶](#True)
- The true value of the - `bool`- `True`are illegal and raise a- `SyntaxError`

- 
None[¶](#None)
- An object frequently used to represent the absence of a value, as when default arguments are not passed to a function. Assignments to - `None`are illegal and raise a- `SyntaxError`- `None`is the sole instance of the- `NoneType`

- 
NotImplemented[¶](#NotImplemented)
- A special value which should be returned by the binary special methods (e.g. - `__eq__()`- `__lt__()`- `__add__()`- `__rsub__()`- `__imul__()`- `__iand__()`- `NotImplemented`is the sole instance of the- `types.NotImplementedType`- Note - When a binary (or in-place) method returns - `NotImplemented`the interpreter will try the reflected operation on the other type (or some other fallback, depending on the operator). If all attempts return- `NotImplemented`, the interpreter will raise an appropriate exception. Incorrectly returning- `NotImplemented`will result in a misleading error message or the- `NotImplemented`value being returned to Python code.- See - [Implementing the arithmetic operations](numbers.html#implementing-the-arithmetic-operations)for examples.- Caution - `NotImplemented`and- `NotImplementedError`are not interchangeable. This constant should only be used as described above; see- `NotImplementedError`- Changed in version 3.9: Evaluating - `NotImplemented`in a boolean context was deprecated.- Changed in version 3.14: Evaluating - `NotImplemented`in a boolean context now raises a- `TypeError`- `True`- `DeprecationWarning`

- 
Ellipsis[¶](#Ellipsis)
- The same as the ellipsis literal “ - `...`”, an object frequently used to indicate that something is omitted. Assignment to- `Ellipsis`is possible, but assignment to- `...`raises a- `SyntaxError`- `Ellipsis`is the sole instance of the- `types.EllipsisType`

- 
__debug__[¶](#debug__)
- This constant is true if Python was not started with an - `-O`- `assert`

Note

The names [ None](#None), 

[,](#False)

`False`[and](#True)

`True`[cannot be reassigned (assignments to them, even as an attribute name, raise](#debug__)

`__debug__`[), so they can be considered “true” constants.](exceptions.html#SyntaxError)

`SyntaxError`## Constants added by the `site`[¶](#constants-added-by-the-site-module)

`site`The [ site](site.html#module-site) module (which is imported automatically during startup, except
if the 

[command-line option is given) adds several constants to the built-in namespace. They are useful for the interactive interpreter shell and should not be used in programs.](../using/cmdline.html#cmdoption-S)

`-S`- 
quit(*code=None*)[¶](#quit)
- 
exit(*code=None*)[¶](#exit)
- Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when accessed directly in the interactive interpreter or called as functions, raise - `SystemExit`

- help
- Object that when printed, prints the message “Type help() for interactive help, or help(object) for help about object.”, and when accessed directly in the interactive interpreter, invokes the built-in help system (see - `help()`

- 
copyright[¶](#copyright)
- 
credits[¶](#credits)
- Objects that when printed or called, print the text of copyright or credits, respectively. 

- 
license[¶](#license)
- Object that when printed, prints the message “Type license() to see the full license text”, and when called, displays the full license text in a pager-like fashion (one screen at a time).