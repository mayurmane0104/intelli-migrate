# pdb — The Python Debugger — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/pdb.html](https://docs.python.org/3.13/library/pdb.html)

---

`pdb` — The Python Debugger[¶](#module-pdb)

**Source code:** [Lib/pdb.py](https://github.com/python/cpython/tree/3.13/Lib/pdb.py)

The module `pdb` defines an interactive source code debugger for Python
programs.  It supports setting (conditional) breakpoints and single stepping at
the source line level, inspection of stack frames, source code listing, and
evaluation of arbitrary Python code in the context of any stack frame.  It also
supports post-mortem debugging and can be called under program control.

The debugger is extensible – it is actually defined as the class [ Pdb](#pdb.Pdb).
This is currently undocumented but easily understood by reading the source.  The
extension interface uses the modules 

[and](bdb.html#module-bdb)

`bdb`[.](cmd.html#module-cmd)

`cmd`See also

- Module `faulthandler`
- Used to dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal. 
- Module `traceback`
- Standard interface to extract, format and print stack traces of Python programs. 

The typical usage to break into the debugger is to insert:

```
import pdb; pdb.set_trace()
```
Or:

```
breakpoint()
```
at the location you want to break into the debugger, and then run the program.
You can then step through the code following this statement, and continue
running without the debugger using the [ continue](#pdbcommand-continue) command.

Changed in version 3.7: The built-in [ breakpoint()](functions.html#breakpoint), when called with defaults, can be used
instead of 

`import pdb; pdb.set_trace()`.```
def double(x):
   breakpoint()
   return x * 2
val = 3
print(f"{val} * 2 is {double(val)}")
```
The debugger’s prompt is `(Pdb)`, which is the indicator that you are in debug mode:

```
> ...(2)double()
-> breakpoint()
(Pdb) p x
3
(Pdb) continue
3 * 2 is 6
```
Changed in version 3.3: Tab-completion via the [ readline](readline.html#module-readline) module is available for commands and
command arguments, e.g. the current global and local names are offered as
arguments of the 

`p` command.## Command-line interface[¶](#command-line-interface)

You can also invoke `pdb` from the command line to debug other scripts.  For
example:

```
python -m pdb [-c command] (-m module | pyfile) [args ...]
```
When invoked as a module, pdb will automatically enter post-mortem debugging if the program being debugged exits abnormally. After post-mortem debugging (or after normal exit of the program), pdb will restart the program. Automatic restarting preserves pdb’s state (such as breakpoints) and in most cases is more useful than quitting the debugger upon program’s exit.

- 
-c, --command <command>[¶](#cmdoption-pdb-c)
- To execute commands as if given in a - `.pdbrc`file; see- [Debugger commands](#debugger-commands).- Changed in version 3.2: Added the - `-c`option.

- 
-m <module>[¶](#cmdoption-pdb-m)
- To execute modules similar to the way - `python -m`does. As with a script, the debugger will pause execution just before the first line of the module.- Changed in version 3.7: Added the - `-m`option.

Typical usage to execute a statement under control of the debugger is:

```
>>> import pdb
>>> def f(x):
...     print(1 / x)
>>> pdb.run("f(2)")
> <string>(1)<module>()
(Pdb) continue
0.5
>>>
```
The typical usage to inspect a crashed program is:

```
>>> import pdb
>>> def f(x):
...     print(1 / x)
...
>>> f(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
ZeroDivisionError: division by zero
>>> pdb.pm()
> <stdin>(2)f()
(Pdb) p x
0
(Pdb)
```
Changed in version 3.13: The implementation of [ PEP 667](https://peps.python.org/pep-0667/) means that name assignments made via 

`pdb`
will immediately affect the active scope, even when running inside an
[optimized scope](../glossary.html#term-optimized-scope).

The module defines the following functions; each enters the debugger in a slightly different way:

- 
pdb.run(*statement*,*globals=None*,*locals=None*)[¶](#pdb.run)
- Execute the - *statement*(given as a string or a code object) under debugger control. The debugger prompt appears before any code is executed; you can set breakpoints and type- `continue`- `step`- `next`- *globals*and- *locals*arguments specify the environment in which the code is executed; by default the dictionary of the module- `__main__`- `exec()`- `eval()`

- 
pdb.runeval(*expression*,*globals=None*,*locals=None*)[¶](#pdb.runeval)
- Evaluate the - *expression*(given as a string or a code object) under debugger control. When- `runeval()`returns, it returns the value of the- *expression*. Otherwise this function is similar to- `run()`

- 
pdb.runcall(*function*,**args*,***kwds*)[¶](#pdb.runcall)
- Call the - *function*(a function or method object, not a string) with the given arguments. When- `runcall()`returns, it returns whatever the function call returned. The debugger prompt appears as soon as the function is entered.

- 
pdb.set_trace(***,*header=None*)[¶](#pdb.set_trace)
- Enter the debugger at the calling stack frame. This is useful to hard-code a breakpoint at a given point in a program, even if the code is not otherwise being debugged (e.g. when an assertion fails). If given, - *header*is printed to the console just before debugging begins.- Changed in version 3.7: The keyword-only argument - *header*.- Changed in version 3.13: - `set_trace()`will enter the debugger immediately, rather than on the next line of code to be executed.

- 
pdb.post_mortem(*t=None*)[¶](#pdb.post_mortem)
- Enter post-mortem debugging of the given exception or - [traceback object](../reference/datamodel.html#traceback-objects). If no value is given, it uses the exception that is currently being handled, or raises- `ValueError`if there isn’t one.- Changed in version 3.13: Support for exception objects was added. 

- 
pdb.pm()[¶](#pdb.pm)
- Enter post-mortem debugging of the exception found in - `sys.last_exc`

The `run*` functions and [ set_trace()](#pdb.set_trace) are aliases for instantiating the

[class and calling the method of the same name. If you want to access further features, you have to do this yourself:](#pdb.Pdb)

`Pdb`- 
*class*pdb.Pdb(*completekey='tab'*,*stdin=None*,*stdout=None*,*skip=None*,*nosigint=False*,*readrc=True*)[¶](#pdb.Pdb)
- `Pdb`is the debugger class.- The - *completekey*,- *stdin*and- *stdout*arguments are passed to the underlying- `cmd.Cmd`- The - *skip*argument, if given, must be an iterable of glob-style module name patterns. The debugger will not step into frames that originate in a module that matches one of these patterns.- [[1]](#id3)- By default, Pdb sets a handler for the SIGINT signal (which is sent when the user presses - `Ctrl`-- `C`on the console) when you give a- `continue`- `Ctrl`-- `C`. If you want Pdb not to touch the SIGINT handler, set- *nosigint*to true.- The - *readrc*argument defaults to true and controls whether Pdb will load .pdbrc files from the filesystem.- Example call to enable tracing with - *skip*:- import pdb; pdb.Pdb(skip=['django.*']).set_trace() - Raises an - [auditing event](sys.html#auditing)- `pdb.Pdb`with no arguments.- Changed in version 3.1: Added the - *skip*parameter.- Changed in version 3.2: Added the - *nosigint*parameter. Previously, a SIGINT handler was never set by Pdb.- Changed in version 3.6: The - *readrc*argument.

## Debugger commands[¶](#debugger-commands)

The commands recognized by the debugger are listed below.  Most commands can be
abbreviated to one or two letters as indicated; e.g. `h(elp)` means that
either `h` or `help` can be used to enter the help command (but not `he`
or `hel`, nor `H` or `Help` or `HELP`).  Arguments to commands must be
separated by whitespace (spaces or tabs).  Optional arguments are enclosed in
square brackets (`[]`) in the command syntax; the square brackets must not be
typed.  Alternatives in the command syntax are separated by a vertical bar
(`|`).

Entering a blank line repeats the last command entered.  Exception: if the last
command was a [ list](#pdbcommand-list) command, the next 11 lines are listed.

Commands that the debugger doesn’t recognize are assumed to be Python statements
and are executed in the context of the program being debugged.  Python
statements can also be prefixed with an exclamation point (`!`).  This is a
powerful way to inspect the program being debugged; it is even possible to
change a variable or call a function.  When an exception occurs in such a
statement, the exception name is printed but the debugger’s state is not
changed.

Changed in version 3.13: Expressions/Statements whose prefix is a pdb command are now correctly identified and executed.

The debugger supports [aliases](#debugger-aliases).  Aliases can have
parameters which allows one a certain level of adaptability to the context under
examination.

Multiple commands may be entered on a single line, separated by `;;`.  (A
single `;` is not used as it is the separator for multiple commands in a line
that is passed to the Python parser.)  No intelligence is applied to separating
the commands; the input is split at the first `;;` pair, even if it is in the
middle of a quoted string. A workaround for strings with double semicolons
is to use implicit string concatenation `';'';'` or `";"";"`.

To set a temporary global variable, use a *convenience variable*. A *convenience
variable* is a variable whose name starts with `$`.  For example, `$foo = 1`
sets a global variable `$foo` which you can use in the debugger session.  The
*convenience variables* are cleared when the program resumes execution so it’s
less likely to interfere with your program compared to using normal variables
like `foo = 1`.

There are three preset *convenience variables*:

- `$_frame`: the current frame you are debugging
- `$_retval`: the return value if the frame is returning
- `$_exception`: the exception if the frame is raising an exception

Added in version 3.12: Added the *convenience variable* feature.

If a file `.pdbrc` exists in the user’s home directory or in the current
directory, it is read with `'utf-8'` encoding and executed as if it had been
typed at the debugger prompt, with the exception that empty lines and lines
starting with `#` are ignored.  This is particularly useful for aliases.  If both
files exist, the one in the home directory is read first and aliases defined there
can be overridden by the local file.

Changed in version 3.2: `.pdbrc` can now contain commands that continue debugging, such as
[ continue](#pdbcommand-continue) or 

[. Previously, these commands had no effect.](#pdbcommand-next)

`next`Changed in version 3.11: `.pdbrc` is now read with `'utf-8'` encoding. Previously, it was read
with the system locale encoding.

- 
h(elp) [command][¶](#pdbcommand-help)
- Without argument, print the list of available commands. With a - *command*as argument, print help about that command.- `help pdb`displays the full documentation (the docstring of the- `pdb`module). Since the- *command*argument must be an identifier,- `help exec`must be entered to get help on the- `!`command.

- 
w(here)[¶](#pdbcommand-where)
- Print a stack trace, with the most recent frame at the bottom. An arrow ( - `>`) indicates the current frame, which determines the context of most commands.

- 
d(own) [count][¶](#pdbcommand-down)
- Move the current frame - *count*(default one) levels down in the stack trace (to a newer frame).

- 
u(p) [count][¶](#pdbcommand-up)
- Move the current frame - *count*(default one) levels up in the stack trace (to an older frame).

- 
b(reak) [([filename:]lineno | function) [, condition]][¶](#pdbcommand-break)
- With a - *lineno*argument, set a break at line- *lineno*in the current file. The line number may be prefixed with a- *filename*and a colon, to specify a breakpoint in another file (possibly one that hasn’t been loaded yet). The file is searched on- `sys.path`- *filename*are- `/abspath/to/file.py`,- `relpath/file.py`,- `module`and- `package.module`.- With a - *function*argument, set a break at the first executable statement within that function.- *function*can be any expression that evaluates to a function in the current namespace.- If a second argument is present, it is an expression which must evaluate to true before the breakpoint is honored. - Without argument, list all breaks, including for each breakpoint, the number of times that breakpoint has been hit, the current ignore count, and the associated condition if any. - Each breakpoint is assigned a number to which all the other breakpoint commands refer. 

- 
tbreak [([filename:]lineno | function) [, condition]][¶](#pdbcommand-tbreak)
- Temporary breakpoint, which is removed automatically when it is first hit. The arguments are the same as for - `break`

- 
cl(ear) [filename:lineno | bpnumber ...][¶](#pdbcommand-clear)
- With a - *filename:lineno*argument, clear all the breakpoints at this line. With a space separated list of breakpoint numbers, clear those breakpoints. Without argument, clear all breaks (but first ask confirmation).

- 
disable bpnumber [bpnumber ...][¶](#pdbcommand-disable)
- Disable the breakpoints given as a space separated list of breakpoint numbers. Disabling a breakpoint means it cannot cause the program to stop execution, but unlike clearing a breakpoint, it remains in the list of breakpoints and can be (re-)enabled. 

- 
enable bpnumber [bpnumber ...][¶](#pdbcommand-enable)
- Enable the breakpoints specified. 

- 
ignore bpnumber [count][¶](#pdbcommand-ignore)
- Set the ignore count for the given breakpoint number. If - *count*is omitted, the ignore count is set to 0. A breakpoint becomes active when the ignore count is zero. When non-zero, the- *count*is decremented each time the breakpoint is reached and the breakpoint is not disabled and any associated condition evaluates to true.

- 
condition bpnumber [condition][¶](#pdbcommand-condition)
- Set a new - *condition*for the breakpoint, an expression which must evaluate to true before the breakpoint is honored. If- *condition*is absent, any existing condition is removed; i.e., the breakpoint is made unconditional.

- 
commands [bpnumber][¶](#pdbcommand-commands)
- Specify a list of commands for breakpoint number - *bpnumber*. The commands themselves appear on the following lines. Type a line containing just- `end`to terminate the commands. An example:- (Pdb) commands 1 (com) p some_variable (com) end (Pdb) - To remove all commands from a breakpoint, type - `commands`and follow it immediately with- `end`; that is, give no commands.- With no - *bpnumber*argument,- `commands`refers to the last breakpoint set.- You can use breakpoint commands to start your program up again. Simply use the - `continue`- `step`- Specifying any command resuming execution (currently - `continue`- `step`- `next`- `return`- `jump`- `quit`- If you use the - `silent`command in the command list, the usual message about stopping at a breakpoint is not printed. This may be desirable for breakpoints that are to print a specific message and then continue. If none of the other commands print anything, you see no sign that the breakpoint was reached.

- 
s(tep)[¶](#pdbcommand-step)
- Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function). 

- 
n(ext)[¶](#pdbcommand-next)
- Continue execution until the next line in the current function is reached or it returns. (The difference between - `next`- `step`- `step`stops inside a called function, while- `next`executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

- 
unt(il) [lineno][¶](#pdbcommand-until)
- Without argument, continue execution until the line with a number greater than the current one is reached. - With - *lineno*, continue execution until a line with a number greater or equal to- *lineno*is reached. In both cases, also stop when the current frame returns.- Changed in version 3.2: Allow giving an explicit line number. 

- 
r(eturn)[¶](#pdbcommand-return)
- Continue execution until the current function returns. 

- 
c(ont(inue))[¶](#pdbcommand-continue)
- Continue execution, only stop when a breakpoint is encountered. 

- 
j(ump) lineno[¶](#pdbcommand-jump)
- Set the next line that will be executed. Only available in the bottom-most frame. This lets you jump back and execute code again, or jump forward to skip code that you don’t want to run. - It should be noted that not all jumps are allowed – for instance it is not possible to jump into the middle of a - `for`- `finally`

- 
l(ist) [first[, last]][¶](#pdbcommand-list)
- List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing. With - `.`as argument, list 11 lines around the current line. With one argument, list 11 lines around at that line. With two arguments, list the given range; if the second argument is less than the first, it is interpreted as a count.- The current line in the current frame is indicated by - `->`. If an exception is being debugged, the line where the exception was originally raised or propagated is indicated by- `>>`, if it differs from the current line.- Changed in version 3.2: Added the - `>>`marker.

- 
ll | longlist[¶](#pdbcommand-ll)
- List all source code for the current function or frame. Interesting lines are marked as for - `list`- Added in version 3.2. 

- 
a(rgs)[¶](#pdbcommand-args)
- Print the arguments of the current function and their current values. 

- 
p expression[¶](#pdbcommand-p)
- Evaluate - *expression*in the current context and print its value.- Note - `print()`can also be used, but is not a debugger command — this executes the Python- `print()`

- 
pp expression[¶](#pdbcommand-pp)
- Like the - `p`- *expression*is pretty-printed using the- `pprint`

- 
whatis expression[¶](#pdbcommand-whatis)
- Print the type of - *expression*.

- 
source expression[¶](#pdbcommand-source)
- Try to get source code of - *expression*and display it.- Added in version 3.2. 

- 
display [expression][¶](#pdbcommand-display)
- Display the value of - *expression*if it changed, each time execution stops in the current frame.- Without - *expression*, list all display expressions for the current frame.- Note - Display evaluates - *expression*and compares to the result of the previous evaluation of- *expression*, so when the result is mutable, display may not be able to pick up the changes.- Example: - lst = [] breakpoint() pass lst.append(1) print(lst) - Display won’t realize - `lst`has been changed because the result of evaluation is modified in place by- `lst.append(1)`before being compared:- > example.py(3)<module>() -> pass (Pdb) display lst display lst: [] (Pdb) n > example.py(4)<module>() -> lst.append(1) (Pdb) n > example.py(5)<module>() -> print(lst) (Pdb) - You can do some tricks with copy mechanism to make it work: - > example.py(3)<module>() -> pass (Pdb) display lst[:] display lst[:]: [] (Pdb) n > example.py(4)<module>() -> lst.append(1) (Pdb) n > example.py(5)<module>() -> print(lst) display lst[:]: [1] [old: []] (Pdb) - Added in version 3.2. 

- 
undisplay [expression][¶](#pdbcommand-undisplay)
- Do not display - *expression*anymore in the current frame. Without- *expression*, clear all display expressions for the current frame.- Added in version 3.2. 

- 
interact[¶](#pdbcommand-interact)
- Start an interactive interpreter (using the - `code`- `exit()`or- `quit()`to exit the interpreter and return to the debugger.- Note - As - `interact`creates a new dedicated namespace for code execution, assignments to variables will not affect the original namespaces. However, modifications to any referenced mutable objects will be reflected in the original namespaces as usual.- Added in version 3.2. - Changed in version 3.13: - `exit()`and- `quit()`can be used to exit the- `interact`- Changed in version 3.13: - `interact`- `sys.stderr`

- 
alias [name [command]][¶](#pdbcommand-alias)
- Create an alias called - *name*that executes- *command*. The- *command*must- *not*be enclosed in quotes. Replaceable parameters can be indicated by- `%1`,- `%2`, … and- `%9`, while- `%*`is replaced by all the parameters. If- *command*is omitted, the current alias for- *name*is shown. If no arguments are given, all aliases are listed.- Aliases may be nested and can contain anything that can be legally typed at the pdb prompt. Note that internal pdb commands - *can*be overridden by aliases. Such a command is then hidden until the alias is removed. Aliasing is recursively applied to the first word of the command line; all other words in the line are left alone.- As an example, here are two useful aliases (especially when placed in the - `.pdbrc`file):- # Print instance variables (usage "pi classInst") alias pi for k in %1.__dict__.keys(): print(f"%1.{k} = {%1.__dict__[k]}") # Print instance variables in self alias ps pi self 

- 
unalias name[¶](#pdbcommand-unalias)
- Delete the specified alias - *name*.

- 
! statement[¶](#pdbcommand-0)
- Execute the (one-line) - *statement*in the context of the current stack frame. The exclamation point can be omitted unless the first word of the statement resembles a debugger command, e.g.:- (Pdb) ! n=42 (Pdb) - To set a global variable, you can prefix the assignment command with a - `global`- (Pdb) global list_options; list_options = ['-l'] (Pdb) 

- 
run [args ...][¶](#pdbcommand-run)
- 
restart [args ...][¶](#pdbcommand-restart)
- Restart the debugged Python program. If - *args*is supplied, it is split with- `shlex`- `sys.argv`- `restart`- `run`

- 
q(uit)[¶](#pdbcommand-quit)
- Quit from the debugger. The program being executed is aborted. 

- 
debug code[¶](#pdbcommand-debug)
- Enter a recursive debugger that steps through - *code*(which is an arbitrary expression or statement to be executed in the current environment).

- 
retval[¶](#pdbcommand-retval)
- Print the return value for the last return of the current function. 

- 
exceptions [excnumber][¶](#pdbcommand-exceptions)
- List or jump between chained exceptions. - When using - `pdb.pm()`or- `Pdb.post_mortem(...)`with a chained exception instead of a traceback, it allows the user to move between the chained exceptions using- `exceptions`command to list exceptions, and- `exceptions <number>`to switch to that exception.- Example: - def out(): try: middle() except Exception as e: raise ValueError("reraise middle() error") from e def middle(): try: return inner(0) except Exception as e: raise ValueError("Middle fail") def inner(x): 1 / x out() - calling - `pdb.pm()`will allow to move between exceptions:- > example.py(5)out() -> raise ValueError("reraise middle() error") from e (Pdb) exceptions 0 ZeroDivisionError('division by zero') 1 ValueError('Middle fail') > 2 ValueError('reraise middle() error') (Pdb) exceptions 0 > example.py(16)inner() -> 1 / x (Pdb) up > example.py(10)middle() -> return inner(0) - Added in version 3.13. 

Footnotes