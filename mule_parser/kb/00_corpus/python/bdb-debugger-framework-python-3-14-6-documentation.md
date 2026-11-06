# bdb — Debugger framework — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/bdb.html](https://docs.python.org/library/bdb.html)

---

`bdb` — Debugger framework[¶](#module-bdb)

**Source code:** [Lib/bdb.py](https://github.com/python/cpython/tree/3.14/Lib/bdb.py)

The `bdb` module handles basic debugger functions, like setting breakpoints
or managing execution via the debugger.

The following exception is defined:

The `bdb` module also defines two classes:

- 
*class*bdb.Breakpoint(*self*,*file*,*line*,*temporary=False*,*cond=None*,*funcname=None*)[¶](#bdb.Breakpoint)
- This class implements temporary breakpoints, ignore counts, disabling and (re-)enabling, and conditionals. - Breakpoints are indexed by number through a list called - `bpbynumber`- `(file, line)`pairs through- `bplist`- `Breakpoint`. The latter points to a list of such instances since there may be more than one breakpoint per line.- When creating a breakpoint, its associated - `file name`- `funcname`- `hit`- `conditional`- `hit`.- `Breakpoint`instances have the following methods:- 
deleteMe()[¶](#bdb.Breakpoint.deleteMe)
- Delete the breakpoint from the list associated to a file/line. If it is the last breakpoint in that position, it also deletes the entry for the file/line. 
 - 
enable()[¶](#bdb.Breakpoint.enable)
- Mark the breakpoint as enabled. 
 - 
disable()[¶](#bdb.Breakpoint.disable)
- Mark the breakpoint as disabled. 
 - 
bpformat()[¶](#bdb.Breakpoint.bpformat)
- Return a string with all the information about the breakpoint, nicely formatted: - Breakpoint number. 
- Temporary status (del or keep). 
- File/line position. 
- Break condition. 
- Number of times to ignore. 
- Number of times hit. 
 - Added in version 3.2. 
 - 
bpprint(*out=None*)[¶](#bdb.Breakpoint.bpprint)
- Print the output of - `bpformat()`- *out*, or if it is- `None`, to standard output.
 - `Breakpoint`instances have the following attributes:- 
file[¶](#bdb.Breakpoint.file)
- File name of the - `Breakpoint`.
 - 
temporary[¶](#bdb.Breakpoint.temporary)
- `True`if a- `Breakpoint`at (file, line) is temporary.
 - 
cond[¶](#bdb.Breakpoint.cond)
- Condition for evaluating a - `Breakpoint`at (file, line).
 - 
funcname[¶](#bdb.Breakpoint.funcname)
- Function name that defines whether a - `Breakpoint`is hit upon entering the function.
 - 
enabled[¶](#bdb.Breakpoint.enabled)
- `True`if- `Breakpoint`is enabled.
 - 
bpbynumber[¶](#bdb.Breakpoint.bpbynumber)
- Numeric index for a single instance of a - `Breakpoint`.
 - 
ignore[¶](#bdb.Breakpoint.ignore)
- Number of times to ignore a - `Breakpoint`.
 - 
hits[¶](#bdb.Breakpoint.hits)
- Count of the number of times a - `Breakpoint`has been hit.
 
- 
deleteMe()

- 
*class*bdb.Bdb(*skip=None*,*backend='settrace'*)[¶](#bdb.Bdb)
- The - `Bdb`class acts as a generic Python debugger base class.- This class takes care of the details of the trace facility; a derived class should implement user interaction. The standard debugger class ( - `pdb.Pdb`- The - *skip*argument, if given, must be an iterable of glob-style module name patterns. The debugger will not step into frames that originate in a module that matches one of these patterns. Whether a frame is considered to originate in a certain module is determined by the- `__name__`in the frame globals.- The - *backend*argument specifies the backend to use for- `Bdb`. It can be either- `'settrace'`or- `'monitoring'`.- `'settrace'`uses- `sys.settrace()`- `'monitoring'`backend uses the new- `sys.monitoring`- `'monitoring'`backend to achieve better performance.- Changed in version 3.1: Added the - *skip*parameter.- Changed in version 3.14: Added the - *backend*parameter.- The following methods of - `Bdb`normally don’t need to be overridden.- 
canonic(*filename*)[¶](#bdb.Bdb.canonic)
- Return canonical form of - *filename*.- For real file names, the canonical form is an operating-system-dependent, - `case-normalized`- `absolute path`- *filename*with angle brackets, such as- `"<stdin>"`generated in interactive mode, is returned unchanged.
 - 
start_trace(*self*)[¶](#bdb.Bdb.start_trace)
- Start tracing. For - `'settrace'`backend, this method is equivalent to- `sys.settrace(self.trace_dispatch)`- Added in version 3.14. 
 - 
stop_trace(*self*)[¶](#bdb.Bdb.stop_trace)
- Stop tracing. For - `'settrace'`backend, this method is equivalent to- `sys.settrace(None)`- Added in version 3.14. 
 - 
reset()[¶](#bdb.Bdb.reset)
- Set the - `botframe`,- `stopframe`,- `returnframe`and- `quitting`
 - 
trace_dispatch(*frame*,*event*,*arg*)[¶](#bdb.Bdb.trace_dispatch)
- This function is installed as the trace function of debugged frames. Its return value is the new trace function (in most cases, that is, itself). - The default implementation decides how to dispatch a frame, depending on the type of event (passed as a string) that is about to be executed. - *event*can be one of the following:- `"line"`: A new line of code is going to be executed.
- `"call"`: A function is about to be called, or another code block entered.
- `"return"`: A function or other code block is about to return.
- `"exception"`: An exception has occurred.
- `"c_call"`: A C function is about to be called.
- `"c_return"`: A C function has returned.
- `"c_exception"`: A C function has raised an exception.
 - For the Python events, specialized functions (see below) are called. For the C events, no action is taken. - The - *arg*parameter depends on the previous event.- See the documentation for - `sys.settrace()`- [The standard type hierarchy](../reference/datamodel.html#types).
 - 
dispatch_line(*frame*)[¶](#bdb.Bdb.dispatch_line)
- If the debugger should stop on the current line, invoke the - `user_line()`- `BdbQuit`- `quitting`- `user_line()`). Return a reference to the- `trace_dispatch()`
 - 
dispatch_call(*frame*,*arg*)[¶](#bdb.Bdb.dispatch_call)
- If the debugger should stop on this function call, invoke the - `user_call()`- `BdbQuit`- `quitting`- `user_call()`). Return a reference to the- `trace_dispatch()`
 - 
dispatch_return(*frame*,*arg*)[¶](#bdb.Bdb.dispatch_return)
- If the debugger should stop on this function return, invoke the - `user_return()`- `BdbQuit`- `quitting`- `user_return()`). Return a reference to the- `trace_dispatch()`
 - 
dispatch_exception(*frame*,*arg*)[¶](#bdb.Bdb.dispatch_exception)
- If the debugger should stop at this exception, invokes the - `user_exception()`- `BdbQuit`- `quitting`- `user_exception()`). Return a reference to the- `trace_dispatch()`
 - Normally derived classes don’t override the following methods, but they may if they want to redefine the definition of stopping and breakpoints. - 
is_skipped_module(*module_name*)[¶](#bdb.Bdb.is_skipped_module)
- Return - `True`if- *module_name*matches any skip pattern.
 - 
stop_here(*frame*)[¶](#bdb.Bdb.stop_here)
- Return - `True`if- *frame*is below the starting frame in the stack.
 - 
break_here(*frame*)[¶](#bdb.Bdb.break_here)
- Return - `True`if there is an effective breakpoint for this line.- Check whether a line or function breakpoint exists and is in effect. Delete temporary breakpoints based on information from - `effective()`
 - 
break_anywhere(*frame*)[¶](#bdb.Bdb.break_anywhere)
- Return - `True`if any breakpoint exists for- *frame*’s filename.
 - Derived classes should override these methods to gain control over debugger operation. - 
user_call(*frame*,*argument_list*)[¶](#bdb.Bdb.user_call)
- Called from - `dispatch_call()`- *argument_list*is not used anymore and will always be- `None`. The argument is kept for backwards compatibility.
 - 
user_line(*frame*)[¶](#bdb.Bdb.user_line)
- Called from - `dispatch_line()`- `stop_here()`- `break_here()`- `True`.
 - 
user_return(*frame*,*return_value*)[¶](#bdb.Bdb.user_return)
- Called from - `dispatch_return()`- `stop_here()`- `True`.
 - 
user_exception(*frame*,*exc_info*)[¶](#bdb.Bdb.user_exception)
- Called from - `dispatch_exception()`- `stop_here()`- `True`.
 - 
do_clear(*arg*)[¶](#bdb.Bdb.do_clear)
- Handle how a breakpoint must be removed when it is a temporary one. - This method must be implemented by derived classes. 
 - Derived classes and clients can call the following methods to affect the stepping state. - 
set_step()[¶](#bdb.Bdb.set_step)
- Stop after one line of code. 
 - 
set_next(*frame*)[¶](#bdb.Bdb.set_next)
- Stop on the next line in or below the given frame. 
 - 
set_return(*frame*)[¶](#bdb.Bdb.set_return)
- Stop when returning from the given frame. 
 - 
set_until(*frame*,*lineno=None*)[¶](#bdb.Bdb.set_until)
- Stop when the line with the - *lineno*greater than the current one is reached or when returning from current frame.
 - 
set_trace([*frame*])[¶](#bdb.Bdb.set_trace)
- Start debugging from - *frame*. If- *frame*is not specified, debugging starts from caller’s frame.- Changed in version 3.13: - `set_trace()`
 - 
set_continue()[¶](#bdb.Bdb.set_continue)
- Stop only at breakpoints or when finished. If there are no breakpoints, set the system trace function to - `None`.
 - 
set_quit()[¶](#bdb.Bdb.set_quit)
- Set the - `quitting`attribute to- `True`. This raises- `BdbQuit`- `dispatch_*()`methods.
 - Derived classes and clients can call the following methods to manipulate breakpoints. These methods return a string containing an error message if something went wrong, or - `None`if all is well.- 
set_break(*filename*,*lineno*,*temporary=False*,*cond=None*,*funcname=None*)[¶](#bdb.Bdb.set_break)
- Set a new breakpoint. If the - *lineno*line doesn’t exist for the- *filename*passed as argument, return an error message. The- *filename*should be in canonical form, as described in the- `canonic()`
 - 
clear_break(*filename*,*lineno*)[¶](#bdb.Bdb.clear_break)
- Delete the breakpoints in - *filename*and- *lineno*. If none were set, return an error message.
 - 
clear_bpbynumber(*arg*)[¶](#bdb.Bdb.clear_bpbynumber)
- Delete the breakpoint which has the index - *arg*in the- `Breakpoint.bpbynumber`- *arg*is not numeric or out of range, return an error message.
 - 
clear_all_file_breaks(*filename*)[¶](#bdb.Bdb.clear_all_file_breaks)
- Delete all breakpoints in - *filename*. If none were set, return an error message.
 - 
clear_all_breaks()[¶](#bdb.Bdb.clear_all_breaks)
- Delete all existing breakpoints. If none were set, return an error message. 
 - 
get_bpbynumber(*arg*)[¶](#bdb.Bdb.get_bpbynumber)
- Return a breakpoint specified by the given number. If - *arg*is a string, it will be converted to a number. If- *arg*is a non-numeric string, if the given breakpoint never existed or has been deleted, a- `ValueError`- Added in version 3.2. 
 - 
get_break(*filename*,*lineno*)[¶](#bdb.Bdb.get_break)
- Return - `True`if there is a breakpoint for- *lineno*in- *filename*.
 - 
get_breaks(*filename*,*lineno*)[¶](#bdb.Bdb.get_breaks)
- Return all breakpoints for - *lineno*in- *filename*, or an empty list if none are set.
 - 
get_file_breaks(*filename*)[¶](#bdb.Bdb.get_file_breaks)
- Return all breakpoints in - *filename*, or an empty list if none are set.
 - 
get_all_breaks()[¶](#bdb.Bdb.get_all_breaks)
- Return all breakpoints that are set. 
 - Derived classes and clients can call the following methods to disable and restart events to achieve better performance. These methods only work when using the - `'monitoring'`backend.- 
disable_current_event()[¶](#bdb.Bdb.disable_current_event)
- Disable the current event until the next time - `restart_events()`- Added in version 3.14. 
 - 
restart_events()[¶](#bdb.Bdb.restart_events)
- Restart all the disabled events. This function is automatically called in - `dispatch_*`methods after- `user_*`methods are called. If the- `dispatch_*`methods are not overridden, the disabled events will be restarted after each user interaction.- Added in version 3.14. 
 - Derived classes and clients can call the following methods to get a data structure representing a stack trace. - 
get_stack(*f*,*t*)[¶](#bdb.Bdb.get_stack)
- Return a list of (frame, lineno) tuples in a stack trace, and a size. - The most recently called frame is last in the list. The size is the number of frames below the frame where the debugger was invoked. 
 - 
format_stack_entry(*frame_lineno*,*lprefix=': '*)[¶](#bdb.Bdb.format_stack_entry)
- Return a string with information about a stack entry, which is a - `(frame, lineno)`tuple. The return string contains:- The canonical filename which contains the frame. 
- The function name or - `"<lambda>"`.
- The input arguments. 
- The return value. 
- The line of code (if it exists). 
 
 - The following two methods can be called by clients to use a debugger to debug a - [statement](../glossary.html#term-statement), given as a string.- 
run(*cmd*,*globals=None*,*locals=None*)[¶](#bdb.Bdb.run)
- Debug a statement executed via the - `exec()`- *globals*defaults to- `__main__.__dict__`,- *locals*defaults to- *globals*.
 - 
runeval(*expr*,*globals=None*,*locals=None*)[¶](#bdb.Bdb.runeval)
- Debug an expression executed via the - `eval()`- *globals*and- *locals*have the same meaning as in- `run()`
 - 
runcall(*func*,*/*,**args*,***kwds*)[¶](#bdb.Bdb.runcall)
- Debug a single function call, and return its result. 
 
- 
canonic(

Finally, the module defines the following functions:

- 
bdb.checkfuncname(*b*,*frame*)[¶](#bdb.checkfuncname)
- Return - `True`if we should break here, depending on the way the- `Breakpoint`- *b*was set.- If it was set via line number, it checks if - `b.line`- *frame*. If the breakpoint was set via- `function name`- *frame*(the right function) and if we are on its first executable line.

- 
bdb.effective(*file*,*line*,*frame*)[¶](#bdb.effective)
- Return - `(active breakpoint, delete temporary flag)`or- `(None, None)`as the breakpoint to act upon.- The - *active breakpoint*is the first entry in- `bplist`- `file`- `line`- `enabled`- `checkfuncname()`- `condition`- `ignore`- *flag*, meaning that a temporary breakpoint should be deleted, is- `False`only when the- `cond`cannot be evaluated (in which case,- `ignore`count is ignored).- If no such entry exists, then - `(None, None)`is returned.