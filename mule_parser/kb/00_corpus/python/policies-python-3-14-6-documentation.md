# Policies — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/asyncio-policy.html](https://docs.python.org/library/asyncio-policy.html)

---

# Policies[¶](#policies)

Warning

Policies are deprecated and will be removed in Python 3.16.
Users are encouraged to use the [ asyncio.run()](asyncio-runner.html#asyncio.run) function
or the 

[with](asyncio-runner.html#asyncio.Runner)

`asyncio.Runner`*loop_factory*to use the desired loop implementation.

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
- Return the current process-wide policy. - Deprecated since version 3.14: The - `get_event_loop_policy()`function is deprecated and will be removed in Python 3.16.

- 
asyncio.set_event_loop_policy(*policy*)[¶](#asyncio.set_event_loop_policy)
- Set the current process-wide policy to - *policy*.- If - *policy*is set to- `None`, the default policy is restored.- Deprecated since version 3.14: The - `set_event_loop_policy()`function is deprecated and will be removed in Python 3.16.

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
 - Deprecated since version 3.14: The - `AbstractEventLoopPolicy`class is deprecated and will be removed in Python 3.16.
- 
get_event_loop()

asyncio ships with the following built-in policies:

- 
*class*asyncio.DefaultEventLoopPolicy[¶](#asyncio.DefaultEventLoopPolicy)
- The default asyncio policy. Uses - `SelectorEventLoop`- `ProactorEventLoop`- There is no need to install the default policy manually. asyncio is configured to use the default policy automatically. - Changed in version 3.8: On Windows, - `ProactorEventLoop`- Changed in version 3.14: The - `get_event_loop()`- `RuntimeError`- Deprecated since version 3.14: The - `DefaultEventLoopPolicy`class is deprecated and will be removed in Python 3.16.

- 
*class*asyncio.WindowsSelectorEventLoopPolicy[¶](#asyncio.WindowsSelectorEventLoopPolicy)
- An alternative event loop policy that uses the - `SelectorEventLoop`- [Availability](intro.html#availability): Windows.- Deprecated since version 3.14: The - `WindowsSelectorEventLoopPolicy`class is deprecated and will be removed in Python 3.16.

- 
*class*asyncio.WindowsProactorEventLoopPolicy[¶](#asyncio.WindowsProactorEventLoopPolicy)
- An alternative event loop policy that uses the - `ProactorEventLoop`- [Availability](intro.html#availability): Windows.- Deprecated since version 3.14: The - `WindowsProactorEventLoopPolicy`class is deprecated and will be removed in Python 3.16.

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