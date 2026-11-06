# Policies — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/asyncio-policy.html](https://docs.python.org/3.13/library/asyncio-policy.html)

---

# Policies[¶](#policies)

An event loop policy is a global object
used to get and set the current [event loop](asyncio-eventloop.html#asyncio-event-loop),
as well as create new event loops.
The default policy can be [replaced](#asyncio-policy-get-set) with
[built-in alternatives](#asyncio-policy-builtin)
to use different event loop implementations,
or substituted by a [custom policy](#asyncio-custom-policies)
that can override these behaviors.

The [policy object](#asyncio-policy-objects)
gets and sets a separate event loop per *context*.
This is per-thread by default,
though custom policies could define *context* differently.

Custom event loop policies can control the behavior of
[ get_event_loop()](asyncio-eventloop.html#asyncio.get_event_loop), 

[, and](asyncio-eventloop.html#asyncio.set_event_loop)

`set_event_loop()`[.](asyncio-eventloop.html#asyncio.new_event_loop)

`new_event_loop()`Policy objects should implement the APIs defined
in the [ AbstractEventLoopPolicy](#asyncio.AbstractEventLoopPolicy) abstract base class.

## Getting and Setting the Policy[¶](#getting-and-setting-the-policy)

The following functions can be used to get and set the policy for the current process:

- 
asyncio.get_event_loop_policy()[¶](#asyncio.get_event_loop_policy)
- Return the current process-wide policy. 

- 
asyncio.set_event_loop_policy(*policy*)[¶](#asyncio.set_event_loop_policy)
- Set the current process-wide policy to - *policy*.- If - *policy*is set to- `None`, the default policy is restored.

## Policy Objects[¶](#policy-objects)

The abstract event loop policy base class is defined as follows:

- 
*class*asyncio.AbstractEventLoopPolicy[¶](#asyncio.AbstractEventLoopPolicy)
- An abstract base class for asyncio policies. - 
get_event_loop()[¶](#asyncio.AbstractEventLoopPolicy.get_event_loop)
- Get the event loop for the current context. - Return an event loop object implementing the - `AbstractEventLoop`- This method should never return - `None`.- Changed in version 3.6. 
 - 
set_event_loop(*loop*)[¶](#asyncio.AbstractEventLoopPolicy.set_event_loop)
- Set the event loop for the current context to - *loop*.
 - 
new_event_loop()[¶](#asyncio.AbstractEventLoopPolicy.new_event_loop)
- Create and return a new event loop object. - This method should never return - `None`.
 - 
get_child_watcher()[¶](#asyncio.AbstractEventLoopPolicy.get_child_watcher)
- Get a child process watcher object. - Return a watcher object implementing the - `AbstractChildWatcher`- This function is Unix specific. - Deprecated since version 3.12. 
 - 
set_child_watcher(*watcher*)[¶](#asyncio.AbstractEventLoopPolicy.set_child_watcher)
- Set the current child process watcher to - *watcher*.- This function is Unix specific. - Deprecated since version 3.12. 
 
- 
get_event_loop()

asyncio ships with the following built-in policies:

- 
*class*asyncio.DefaultEventLoopPolicy[¶](#asyncio.DefaultEventLoopPolicy)
- The default asyncio policy. Uses - `SelectorEventLoop`- `ProactorEventLoop`- There is no need to install the default policy manually. asyncio is configured to use the default policy automatically. - Changed in version 3.8: On Windows, - `ProactorEventLoop`- Deprecated since version 3.12: The - `get_event_loop()`- `DeprecationWarning`

- 
*class*asyncio.WindowsSelectorEventLoopPolicy[¶](#asyncio.WindowsSelectorEventLoopPolicy)
- An alternative event loop policy that uses the - `SelectorEventLoop`- [Availability](intro.html#availability): Windows.

- 
*class*asyncio.WindowsProactorEventLoopPolicy[¶](#asyncio.WindowsProactorEventLoopPolicy)
- An alternative event loop policy that uses the - `ProactorEventLoop`- [Availability](intro.html#availability): Windows.

## Process Watchers[¶](#process-watchers)

A process watcher allows customization of how an event loop monitors child processes on Unix. Specifically, the event loop needs to know when a child process has exited.

In asyncio, child processes are created with
[ create_subprocess_exec()](asyncio-subprocess.html#asyncio.create_subprocess_exec) and 

[functions.](asyncio-eventloop.html#asyncio.loop.subprocess_exec)

`loop.subprocess_exec()`asyncio defines the [ AbstractChildWatcher](#asyncio.AbstractChildWatcher) abstract base class, which child
watchers should implement, and has four different implementations:

[(configured to be used by default),](#asyncio.ThreadedChildWatcher)

`ThreadedChildWatcher`[,](#asyncio.MultiLoopChildWatcher)

`MultiLoopChildWatcher`[, and](#asyncio.SafeChildWatcher)

`SafeChildWatcher`[.](#asyncio.FastChildWatcher)

`FastChildWatcher`See also the [Subprocess and Threads](asyncio-subprocess.html#asyncio-subprocess-threads)
section.

The following two functions can be used to customize the child process watcher implementation used by the asyncio event loop:

- 
asyncio.get_child_watcher()[¶](#asyncio.get_child_watcher)
- Return the current child watcher for the current policy. - Deprecated since version 3.12. 

- 
asyncio.set_child_watcher(*watcher*)[¶](#asyncio.set_child_watcher)
- Set the current child watcher to - *watcher*for the current policy.- *watcher*must implement methods defined in the- `AbstractChildWatcher`- Deprecated since version 3.12. 

Note

Third-party event loops implementations might not support
custom child watchers.  For such event loops, using
[ set_child_watcher()](#asyncio.set_child_watcher) might be prohibited or have no effect.

- 
*class*asyncio.AbstractChildWatcher[¶](#asyncio.AbstractChildWatcher)
- 
add_child_handler(*pid*,*callback*,**args*)[¶](#asyncio.AbstractChildWatcher.add_child_handler)
- Register a new child handler. - Arrange for - `callback(pid, returncode, *args)`to be called when a process with PID equal to- *pid*terminates. Specifying another callback for the same process replaces the previous handler.- The - *callback*callable must be thread-safe.
 - 
remove_child_handler(*pid*)[¶](#asyncio.AbstractChildWatcher.remove_child_handler)
- Removes the handler for process with PID equal to - *pid*.- The function returns - `True`if the handler was successfully removed,- `False`if there was nothing to remove.
 - 
attach_loop(*loop*)[¶](#asyncio.AbstractChildWatcher.attach_loop)
- Attach the watcher to an event loop. - If the watcher was previously attached to an event loop, then it is first detached before attaching to the new loop. - Note: loop may be - `None`.
 - 
is_active()[¶](#asyncio.AbstractChildWatcher.is_active)
- Return - `True`if the watcher is ready to use.- Spawning a subprocess with - *inactive*current child watcher raises- `RuntimeError`- Added in version 3.8. 
 - 
close()[¶](#asyncio.AbstractChildWatcher.close)
- Close the watcher. - This method has to be called to ensure that underlying resources are cleaned-up. 
 - Deprecated since version 3.12. 
- 
add_child_handler(

- 
*class*asyncio.ThreadedChildWatcher[¶](#asyncio.ThreadedChildWatcher)
- This implementation starts a new waiting thread for every subprocess spawn. - It works reliably even when the asyncio event loop is run in a non-main OS thread. - There is no noticeable overhead when handling a big number of children ( - *O*(1) each time a child terminates), but starting a thread per process requires extra memory.- This watcher is used by default. - Added in version 3.8. 

- 
*class*asyncio.MultiLoopChildWatcher[¶](#asyncio.MultiLoopChildWatcher)
- This implementation registers a - `SIGCHLD`signal handler on instantiation. That can break third-party code that installs a custom handler for- `SIGCHLD`signal.- The watcher avoids disrupting other code spawning processes by polling every process explicitly on a - `SIGCHLD`signal.- There is no limitation for running subprocesses from different threads once the watcher is installed. - The solution is safe but it has a significant overhead when handling a big number of processes ( - *O*(- *n*) each time a- `SIGCHLD`is received).- Added in version 3.8. - Deprecated since version 3.12. 

- 
*class*asyncio.SafeChildWatcher[¶](#asyncio.SafeChildWatcher)
- This implementation uses active event loop from the main thread to handle - `SIGCHLD`signal. If the main thread has no running event loop another thread cannot spawn a subprocess (- `RuntimeError`- The watcher avoids disrupting other code spawning processes by polling every process explicitly on a - `SIGCHLD`signal.- This solution is as safe as - `MultiLoopChildWatcher`- *O*(- *n*) complexity but requires a running event loop in the main thread to work.- Deprecated since version 3.12. 

- 
*class*asyncio.FastChildWatcher[¶](#asyncio.FastChildWatcher)
- This implementation reaps every terminated processes by calling - `os.waitpid(-1)`directly, possibly breaking other code spawning processes and waiting for their termination.- There is no noticeable overhead when handling a big number of children ( - *O*(1) each time a child terminates).- This solution requires a running event loop in the main thread to work, as - `SafeChildWatcher`- Deprecated since version 3.12. 

- 
*class*asyncio.PidfdChildWatcher[¶](#asyncio.PidfdChildWatcher)
- This implementation polls process file descriptors (pidfds) to await child process termination. In some respects, - `PidfdChildWatcher`is a “Goldilocks” child watcher implementation. It doesn’t require signals or threads, doesn’t interfere with any processes launched outside the event loop, and scales linearly with the number of subprocesses launched by the event loop. The main disadvantage is that pidfds are specific to Linux, and only work on recent (5.3+) kernels.- Added in version 3.9. 

## Custom Policies[¶](#custom-policies)

To implement a new event loop policy, it is recommended to subclass
[ DefaultEventLoopPolicy](#asyncio.DefaultEventLoopPolicy) and override the methods for which
custom behavior is wanted, e.g.:

```
class MyEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
    def get_event_loop(self):
        """Get the event loop.
        This may be None or an instance of EventLoop.
        """
        loop = super().get_event_loop()
        # Do something with loop ...
        return loop
asyncio.set_event_loop_policy(MyEventLoopPolicy())
```