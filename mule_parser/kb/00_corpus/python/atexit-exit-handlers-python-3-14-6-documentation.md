# atexit — Exit handlers — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/atexit.html](https://docs.python.org/library/atexit.html)

---

`atexit` — Exit handlers[¶](#module-atexit)

The `atexit` module defines functions to register and unregister cleanup
functions.  Functions thus registered are automatically executed upon normal
interpreter termination.  `atexit` runs these functions in the *reverse*
order in which they were registered; if you register `A`, `B`, and `C`,
at interpreter termination time they will be run in the order `C`, `B`,
`A`.

**Note:** The functions registered via this module are not called when the
program is killed by a signal not handled by Python, when a Python fatal
internal error is detected, or when [ os._exit()](os.html#os._exit) is called.

**Note:** The effect of registering or unregistering functions from within
a cleanup function is undefined.

Changed in version 3.7: When used with C-API subinterpreters, registered functions are local to the interpreter they were registered in.

- 
atexit.register(*func*,**args*,***kwargs*)[¶](#atexit.register)
- Register - *func*as a function to be executed at termination. Any optional arguments that are to be passed to- *func*must be passed as arguments to- `register()`. It is possible to register the same function and arguments more than once.- At normal program termination (for instance, if - `sys.exit()`- If an exception is raised during execution of the exit handlers, a traceback is printed (unless - `SystemExit`- This function returns - *func*, which makes it possible to use it as a decorator.- Warning - Starting new threads or calling - `os.fork()`- `threading`- Changed in version 3.12: Attempts to start a new thread or - `os.fork()`- `RuntimeError`

- 
atexit.unregister(*func*)[¶](#atexit.unregister)
- Remove - *func*from the list of functions to be run at interpreter shutdown.- `unregister()`silently does nothing if- *func*was not previously registered. If- *func*has been registered more than once, every occurrence of that function in the- `atexit`call stack will be removed. Equality comparisons (- `==`) are used internally during unregistration, so function references do not need to have matching identities.

`atexit` Example[¶](#atexit-example)

The following simple example demonstrates how a module can initialize a counter from a file when it is imported and save the counter’s updated value automatically when the program terminates without relying on the application making an explicit call into this module at termination.

```
try:
    with open('counterfile') as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0
def incrcounter(n):
    global _count
    _count = _count + n
def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % _count)
import atexit
atexit.register(savecounter)
```
Positional and keyword arguments may also be passed to [ register()](#atexit.register) to be
passed along to the registered function when it is called:

```
def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))
import atexit
atexit.register(goodbye, 'Donny', 'nice')
# or:
atexit.register(goodbye, adjective='nice', name='Donny')
```
Usage as a [decorator](../glossary.html#term-decorator):

```
import atexit
@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')
```
This only works with functions that can be called without arguments.