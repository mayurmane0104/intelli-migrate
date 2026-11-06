# rlcompleter — Completion function for GNU readline — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/rlcompleter.html](https://docs.python.org/3.13/library/rlcompleter.html)

---

`rlcompleter` — Completion function for GNU readline[¶](#module-rlcompleter)

**Source code:** [Lib/rlcompleter.py](https://github.com/python/cpython/tree/3.13/Lib/rlcompleter.py)

The `rlcompleter` module defines a completion function suitable to be
passed to [ set_completer()](readline.html#readline.set_completer) in the 

[module.](readline.html#module-readline)

`readline`When this module is imported on a Unix platform with the [ readline](readline.html#module-readline) module
available, an instance of the 

[class is automatically created and its](#rlcompleter.Completer)

`Completer`[method is set as the](#rlcompleter.Completer.complete)

`complete()`[readline completer](readline.html#readline-completion). The method provides completion of valid Python

[identifiers and keywords](../reference/lexical_analysis.html#identifiers).

Example:

```
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.
```
The `rlcompleter` module is designed for use with Python’s
[interactive mode](../tutorial/interpreter.html#tut-interactive).  Unless Python is run with the
[ -S](../using/cmdline.html#cmdoption-S) option, the module is automatically imported and configured
(see 

[Readline configuration](site.html#rlcompleter-config)).

On platforms without [ readline](readline.html#module-readline), the 

[class defined by this module can still be used for custom purposes.](#rlcompleter.Completer)

`Completer`- 
*class*rlcompleter.Completer[¶](#rlcompleter.Completer)
- Completer objects have the following method: - 
complete(*text*,*state*)[¶](#rlcompleter.Completer.complete)
- Return the next possible completion for - *text*.- When called by the - `readline`- `state == 0, 1, 2, ...`until the method returns- `None`.- If called for - *text*that doesn’t include a period character (- `'.'`), it will complete from names currently defined in- `__main__`- `builtins`- `keyword`- If called for a dotted name, it will try to evaluate anything without obvious side-effects (functions will not be evaluated, but it can generate calls to - `__getattr__()`- `dir()`- `None`
 
- 
complete(