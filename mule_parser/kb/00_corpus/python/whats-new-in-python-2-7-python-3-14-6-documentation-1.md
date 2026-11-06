# What’s New in Python 2.7 — Python 3.14.6 documentation

**Source:** [http://docs.python.org/whatsnew/2.7.html](http://docs.python.org/whatsnew/2.7.html)

---

# What’s New in Python 2.7[¶](#what-s-new-in-python-2-7)

- Author:
- A.M. Kuchling (amk at amk.ca) 

This article explains the new features in Python 2.7. Python 2.7 was released on July 3, 2010.

Numeric handling has been improved in many ways, for both
floating-point numbers and for the [ Decimal](../library/decimal.html#decimal.Decimal) class.
There are some useful additions to the standard library, such as a
greatly enhanced 

[module, the](../library/unittest.html#module-unittest)

`unittest`[module for parsing command-line options, convenient](../library/argparse.html#module-argparse)

`argparse`[and](../library/collections.html#collections.OrderedDict)

`OrderedDict`[classes in the](../library/collections.html#collections.Counter)

`Counter`[module, and many other improvements.](../library/collections.html#module-collections)

`collections`Python 2.7 is planned to be the last of the 2.x releases, so we worked on making it a good release for the long term. To help with porting to Python 3, several new features from the Python 3.x series have been included in 2.7.

This article doesn’t attempt to provide a complete specification of
the new features, but instead provides a convenient overview.  For
full details, you should refer to the documentation for Python 2.7 at
[https://docs.python.org](https://docs.python.org). If you want to understand the rationale for
the design and implementation, refer to the PEP for a particular new
feature or the issue on [https://bugs.python.org](https://bugs.python.org) in which a change was
discussed.  Whenever possible, “What’s New in Python” links to the
bug/patch item for each change.

## The Future for Python 2.x[¶](#the-future-for-python-2-x)

Python 2.7 is the last major release in the 2.x series, as the Python maintainers have shifted the focus of their new feature development efforts to the Python 3.x series. This means that while Python 2 continues to receive bug fixes, and to be updated to build correctly on new hardware and versions of supported operated systems, there will be no new full feature releases for the language or standard library.

However, while there is a large common subset between Python 2.7 and Python 3, and many of the changes involved in migrating to that common subset, or directly to Python 3, can be safely automated, some other changes (notably those associated with Unicode handling) may require careful consideration, and preferably robust automated regression test suites, to migrate effectively.

This means that Python 2.7 will remain in place for a long time, providing a
stable and supported base platform for production systems that have not yet
been ported to Python 3. The full expected lifecycle of the Python 2.7
series is detailed in [ PEP 373](https://peps.python.org/pep-0373/).

Some key consequences of the long-term significance of 2.7 are:

- As noted above, the 2.7 release has a much longer period of maintenance when compared to earlier 2.x versions. Python 2.7 is currently expected to remain supported by the core development team (receiving security updates and other bug fixes) until at least 2020 (10 years after its initial release, compared to the more typical support period of 18–24 months). 
- As the Python 2.7 standard library ages, making effective use of the Python Package Index (either directly or via a redistributor) becomes more important for Python 2 users. In addition to a wide variety of third party packages for various tasks, the available packages include backports of new modules and features from the Python 3 standard library that are compatible with Python 2, as well as various tools and libraries that can make it easier to migrate to Python 3. The - [Python Packaging User Guide](https://packaging.python.org)provides guidance on downloading and installing software from the Python Package Index.
- While the preferred approach to enhancing Python 2 is now the publication of new packages on the Python Package Index, this approach doesn’t necessarily work in all cases, especially those related to network security. In exceptional cases that cannot be handled adequately by publishing new or updated packages on PyPI, the Python Enhancement Proposal process may be used to make the case for adding new features directly to the Python 2 standard library. Any such additions, and the maintenance releases where they were added, will be noted in the - [New Features Added to Python 2.7 Maintenance Releases](#py27-maintenance-enhancements)section below.

For projects wishing to migrate from Python 2 to Python 3, or for library
and framework developers wishing to support users on both Python 2 and
Python 3, there are a variety of tools and guides available to help decide
on a suitable approach and manage some of the technical details involved.
The recommended starting point is the [How to port Python 2 Code to Python 3](../howto/pyporting.html#pyporting-howto) HOWTO guide.

## Changes to the Handling of Deprecation Warnings[¶](#changes-to-the-handling-of-deprecation-warnings)

For Python 2.7, a policy decision was made to silence warnings only of
interest to developers by default.  [ DeprecationWarning](../library/exceptions.html#DeprecationWarning) and its
descendants are now ignored unless otherwise requested, preventing
users from seeing warnings triggered by an application.  This change
was also made in the branch that became Python 3.2. (Discussed
on stdlib-sig and carried out in 

[bpo-7319](https://bugs.python.org/issue?@action=redirect&bpo=7319).)

In previous releases, [ DeprecationWarning](../library/exceptions.html#DeprecationWarning) messages were
enabled by default, providing Python developers with a clear
indication of where their code may break in a future major version
of Python.

However, there are increasingly many users of Python-based
applications who are not directly involved in the development of
those applications.  [ DeprecationWarning](../library/exceptions.html#DeprecationWarning) messages are
irrelevant to such users, making them worry about an application
that’s actually working correctly and burdening application developers
with responding to these concerns.

You can re-enable display of [ DeprecationWarning](../library/exceptions.html#DeprecationWarning) messages by
running Python with the 

[(short form:](../using/cmdline.html#cmdoption-W)

`-Wdefault``-Wd`) switch, or by setting the [environment variable to](../using/cmdline.html#envvar-PYTHONWARNINGS)

`PYTHONWARNINGS``"default"` (or `"d"`) before running
Python.  Python code can also re-enable them
by calling `warnings.simplefilter('default')`.The `unittest` module also automatically reenables deprecation warnings
when running tests.

## Python 3.1 Features[¶](#python-3-1-features)

Much as Python 2.6 incorporated features from Python 3.0, version 2.7 incorporates some of the new features in Python 3.1. The 2.x series continues to provide tools for migrating to the 3.x series.

A partial list of 3.1 features that were backported to 2.7:

- The syntax for set literals ( - `{1,2,3}`is a mutable set).
- Dictionary and set comprehensions ( - `{i: i*2 for i in range(3)}`).
- Multiple context managers in a single - `with`
- A new version of the - `io`
- The ordered-dictionary type described in - [PEP 372: Adding an Ordered Dictionary to collections](#pep-0372).
- The new - `","`format specifier described in- [PEP 378: Format Specifier for Thousands Separator](#pep-0378).
- The - `memoryview`
- A small subset of the - `importlib`- [described below](#importlib-section).
- The - `repr()`- `x`is shorter in many cases: it’s now based on the shortest decimal string that’s guaranteed to round back to- `x`. As in previous versions of Python, it’s guaranteed that- `float(repr(x))`recovers- `x`.
- Float-to-string and string-to-float conversions are correctly rounded. The - `round()`
- The - `PyCapsule`
- The - `PyLong_AsLongAndOverflow()`

Other new Python3-mode warnings include:

- `operator.isCallable()`and- `operator.sequenceIncludes()`, which are not supported in 3.x, now trigger warnings.
- The - `-3`switch now automatically enables the- `-Qwarn`switch that causes warnings about using classic division with integers and long integers.

## PEP 372: Adding an Ordered Dictionary to collections[¶](#pep-372-adding-an-ordered-dictionary-to-collections)

Regular Python dictionaries iterate over key/value pairs in arbitrary order.
Over the years, a number of authors have written alternative implementations
that remember the order that the keys were originally inserted.  Based on
the experiences from those implementations, 2.7 introduces a new
[ OrderedDict](../library/collections.html#collections.OrderedDict) class in the 

[module.](../library/collections.html#module-collections)

`collections`The [ OrderedDict](../library/collections.html#collections.OrderedDict) API provides the same interface as regular
dictionaries but iterates over keys and values in a guaranteed order
depending on when a key was first inserted:

```
>>> from collections import OrderedDict
>>> d = OrderedDict([('first', 1),
...                  ('second', 2),
...                  ('third', 3)])
>>> d.items()
[('first', 1), ('second', 2), ('third', 3)]
```
If a new entry overwrites an existing entry, the original insertion position is left unchanged:

```
>>> d['second'] = 4
>>> d.items()
[('first', 1), ('second', 4), ('third', 3)]
```
Deleting an entry and reinserting it will move it to the end:

```
>>> del d['second']
>>> d['second'] = 5
>>> d.items()
[('first', 1), ('third', 3), ('second', 5)]
```
The [ popitem()](../library/collections.html#collections.OrderedDict.popitem) method has an optional 

*last*argument that defaults to

`True`.  If *last*is true, the most recently added key is returned and removed; if it’s false, the oldest key is selected:

```
>>> od = OrderedDict([(x,0) for x in range(20)])
>>> od.popitem()
(19, 0)
>>> od.popitem()
(18, 0)
>>> od.popitem(last=False)
(0, 0)
>>> od.popitem(last=False)
(1, 0)
```
Comparing two ordered dictionaries checks both the keys and values, and requires that the insertion order was the same:

```
>>> od1 = OrderedDict([('first', 1),
...                    ('second', 2),
...                    ('third', 3)])
>>> od2 = OrderedDict([('third', 3),
...                    ('first', 1),
...                    ('second', 2)])
>>> od1 == od2
False
>>> # Move 'third' key to the end
>>> del od2['third']; od2['third'] = 3
>>> od1 == od2
True
```
Comparing an [ OrderedDict](../library/collections.html#collections.OrderedDict) with a regular dictionary
ignores the insertion order and just compares the keys and values.

How does the [ OrderedDict](../library/collections.html#collections.OrderedDict) work?  It maintains a
doubly linked list of keys, appending new keys to the list as they’re inserted.
A secondary dictionary maps keys to their corresponding list node, so
deletion doesn’t have to traverse the entire linked list and therefore
remains 

*O*(1).

The standard library now supports use of ordered dictionaries in several modules.

- The - `ConfigParser`
- The - `_asdict()`- `collections.namedtuple()`
- The - `json`- `JSONDecoder`- *object_pairs_hook*parameter to allow- `OrderedDict`instances to be built by the decoder. Support was also added for third-party tools like- [PyYAML](https://pyyaml.org/).

See also

- **PEP 372**
- PEP written by Armin Ronacher and Raymond Hettinger; implemented by Raymond Hettinger. 

## PEP 378: Format Specifier for Thousands Separator[¶](#pep-378-format-specifier-for-thousands-separator)

To make program output more readable, it can be useful to add separators to large numbers, rendering them as 18,446,744,073,709,551,616 instead of 18446744073709551616.

The fully general solution for doing this is the [ locale](../library/locale.html#module-locale) module,
which can use different separators (“,” in North America, “.” in
Europe) and different grouping sizes, but 

`locale` is complicated
to use and unsuitable for multi-threaded applications where different
threads are producing output for different locales.Therefore, a simple comma-grouping mechanism has been added to the
mini-language used by the [ str.format()](../library/stdtypes.html#str.format) method.  When
formatting a floating-point number, simply include a comma between the
width and the precision:

```
>>> '{:20,.2f}'.format(18446744073709551616.0)
'18,446,744,073,709,551,616.00'
```
When formatting an integer, include the comma after the width:

```
>>> '{:20,d}'.format(18446744073709551616)
'18,446,744,073,709,551,616'
```
This mechanism is not adaptable at all; commas are always used as the
separator and the grouping is always into three-digit groups.  The
comma-formatting mechanism isn’t as general as the [ locale](../library/locale.html#module-locale)
module, but it’s easier to use.

See also

- **PEP 378**
- PEP written by Raymond Hettinger; implemented by Eric Smith. 

## PEP 389: The argparse Module for Parsing Command Lines[¶](#pep-389-the-argparse-module-for-parsing-command-lines)

The [ argparse](../library/argparse.html#module-argparse) module for parsing command-line arguments was
added as a more powerful replacement for the

[module.](../library/optparse.html#module-optparse)

`optparse`This means Python now supports three different modules for parsing
command-line arguments: [ getopt](../library/getopt.html#module-getopt), 

[, and](../library/optparse.html#module-optparse)

`optparse`[. The](../library/argparse.html#module-argparse)

`argparse``getopt` module closely resembles the C
library’s `getopt()` function, so it remains useful if you’re writing a
Python prototype that will eventually be rewritten in C.
`optparse` becomes redundant, but there are no plans to remove it
because there are many scripts still using it, and there’s no
automated way to update these scripts.  (Making the `argparse`
API consistent with `optparse`’s interface was discussed but
rejected as too messy and difficult.)In short, if you’re writing a new script and don’t need to worry
about compatibility with earlier versions of Python, use
[ argparse](../library/argparse.html#module-argparse) instead of 

[.](../library/optparse.html#module-optparse)

`optparse`Here’s an example:

```
import argparse
parser = argparse.ArgumentParser(description='Command-line example.')
# Add optional switches
parser.add_argument('-v', action='store_true', dest='is_verbose',
                    help='produce verbose output')
parser.add_argument('-o', action='store', dest='output',
                    metavar='FILE',
                    help='direct output to FILE instead of stdout')
parser.add_argument('-C', action='store', type=int, dest='context',
                    metavar='NUM', default=0,
                    help='display NUM lines of added context')
# Allow any number of additional arguments.
parser.add_argument(nargs='*', action='store', dest='inputs',
                    help='input filenames (default is stdin)')
args = parser.parse_args()
print args.__dict__
```
Unless you override it, `-h` and `--help` switches
are automatically added, and produce neatly formatted output:

```
-> ./python.exe argparse-example.py --help
usage: argparse-example.py [-h] [-v] [-o FILE] [-C NUM] [inputs [inputs ...]]
Command-line example.
positional arguments:
  inputs      input filenames (default is stdin)
optional arguments:
  -h, --help  show this help message and exit
  -v          produce verbose output
  -o FILE     direct output to FILE instead of stdout
  -C NUM      display NUM lines of added context
```
As with [ optparse](../library/optparse.html#module-optparse), the command-line switches and arguments
are returned as an object with attributes named by the 

*dest*parameters:

```
-> ./python.exe argparse-example.py -v
{'output': None,
 'is_verbose': True,
 'context': 0,
 'inputs': []}
-> ./python.exe argparse-example.py -v -o /tmp/output -C 4 file1 file2
{'output': '/tmp/output',
 'is_verbose': True,
 'context': 4,
 'inputs': ['file1', 'file2']}
```
[ argparse](../library/argparse.html#module-argparse) has much fancier validation than 

[; you can specify an exact number of arguments as an integer, 0 or more arguments by passing](../library/optparse.html#module-optparse)

`optparse``'*'`, 1 or more by passing `'+'`, or an
optional argument with `'?'`.  A top-level parser can contain
sub-parsers to define subcommands that have different sets of
switches, as in `svn commit`, `svn checkout`, etc.  You can
specify an argument’s type as [, which will automatically open files for you and understands that](../library/argparse.html#argparse.FileType)

`FileType``'-'` means
standard input or output.See also

- `argparse`
- The documentation page of the argparse module. 
- [Migrating optparse code to argparse](../howto/argparse-optparse.html#upgrading-optparse-code)
- Part of the Python documentation, describing how to convert code that uses - `optparse`
- **PEP 389**
- PEP written and implemented by Steven Bethard. 

## PEP 391: Dictionary-Based Configuration For Logging[¶](#pep-391-dictionary-based-configuration-for-logging)

The [ logging](../library/logging.html#module-logging) module is very flexible; applications can define
a tree of logging subsystems, and each logger in this tree can filter
out certain messages, format them differently, and direct messages to
a varying number of handlers.

All this flexibility can require a lot of configuration.  You can
write Python statements to create objects and set their properties,
but a complex set-up requires verbose but boring code.
[ logging](../library/logging.html#module-logging) also supports a 

[function that parses a file, but the file format doesn’t support configuring filters, and it’s messier to generate programmatically.](../library/logging.config.html#logging.config.fileConfig)

`fileConfig()`Python 2.7 adds a [ dictConfig()](../library/logging.config.html#logging.config.dictConfig) function that
uses a dictionary to configure logging.  There are many ways to
produce a dictionary from different sources: construct one with code;
parse a file containing JSON; or use a YAML parsing library if one is
installed.  For more information see 

[Configuration functions](../library/logging.config.html#logging-config-api).

The following example configures two loggers, the root logger and a
logger named “network”.  Messages sent to the root logger will be
sent to the system log using the syslog protocol, and messages
to the “network” logger will be written to a `network.log` file
that will be rotated once the log reaches 1MB.

```
import logging
import logging.config
configdict = {
 'version': 1,    # Configuration schema in use; must be 1 for now
 'formatters': {
     'standard': {
         'format': ('%(asctime)s %(name)-15s '
                    '%(levelname)-8s %(message)s')}},
 'handlers': {'netlog': {'backupCount': 10,
                     'class': 'logging.handlers.RotatingFileHandler',
                     'filename': '/logs/network.log',
                     'formatter': 'standard',
                     'level': 'INFO',
                     'maxBytes': 1000000},
              'syslog': {'class': 'logging.handlers.SysLogHandler',
                         'formatter': 'standard',
                         'level': 'ERROR'}},
 # Specify all the subordinate loggers
 'loggers': {
             'network': {
                         'handlers': ['netlog']
             }
 },
 # Specify properties of the root logger
 'root': {
          'handlers': ['syslog']
 },
}
# Set up configuration
logging.config.dictConfig(configdict)
# As an example, log two error messages
logger = logging.getLogger('/')
logger.error('Database not found')
netlogger = logging.getLogger('network')
netlogger.error('Connection failed')
```
Three smaller enhancements to the [ logging](../library/logging.html#module-logging) module, all
implemented by Vinay Sajip, are:

- The - `SysLogHandler`- *socktype*parameter giving the type of socket to use, either- `socket.SOCK_DGRAM`- `socket.SOCK_STREAM`
- `Logger`- `getChild()`- `log = getLogger('app')`, calling- `log.getChild('network.listen')`is equivalent to- `getLogger('app.network.listen')`.
- The - `LoggerAdapter`- `isEnabledFor()`- *level*and returns whether the underlying logger would process a message of that level of importance.

See also

- **PEP 391**
- PEP written and implemented by Vinay Sajip. 

## PEP 3106: Dictionary Views[¶](#pep-3106-dictionary-views)

The dictionary methods [ keys()](../library/stdtypes.html#dict.keys), 

[, and](../library/stdtypes.html#dict.values)

`values()`[are different in Python 3.x. They return an object called a](../library/stdtypes.html#dict.items)

`items()`*view*instead of a fully materialized list.

It’s not possible to change the return values of [ keys()](../library/stdtypes.html#dict.keys),

[, and](../library/stdtypes.html#dict.values)

`values()`[in Python 2.7 because too much code would break. Instead the 3.x versions were added under the new names](../library/stdtypes.html#dict.items)

`items()``viewkeys()`, `viewvalues()`,
and `viewitems()`.```
>>> d = dict((i*10, chr(65+i)) for i in range(26))
>>> d
{0: 'A', 130: 'N', 10: 'B', 140: 'O', 20: ..., 250: 'Z'}
>>> d.viewkeys()
dict_keys([0, 130, 10, 140, 20, 150, 30, ..., 250])
```
Views can be iterated over, but the key and item views also behave
like sets.  The `&` operator performs intersection, and `|`
performs a union:

```
>>> d1 = dict((i*10, chr(65+i)) for i in range(26))
>>> d2 = dict((i**.5, i) for i in range(1000))
>>> d1.viewkeys() & d2.viewkeys()
set([0.0, 10.0, 20.0, 30.0])
>>> d1.viewkeys() | range(0, 30)
set([0, 1, 130, 3, 4, 5, 6, ..., 120, 250])
```
The view keeps track of the dictionary and its contents change as the dictionary is modified:

```
>>> vk = d.viewkeys()
>>> vk
dict_keys([0, 130, 10, ..., 250])
>>> d[260] = '&'
>>> vk
dict_keys([0, 130, 260, 10, ..., 250])
```
However, note that you can’t add or remove keys while you’re iterating over the view:

```
>>> for k in vk:
...     d[k*2] = k
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
```
You can use the view methods in Python 2.x code, and the 2to3
converter will change them to the standard [ keys()](../library/stdtypes.html#dict.keys),

[, and](../library/stdtypes.html#dict.values)

`values()`[methods.](../library/stdtypes.html#dict.items)

`items()`## PEP 3137: The memoryview Object[¶](#pep-3137-the-memoryview-object)

The [ memoryview](../library/stdtypes.html#memoryview) object provides a view of another object’s
memory content that matches the 

[type’s interface.](../library/stdtypes.html#bytes)

`bytes````
>>> import string
>>> m = memoryview(string.letters)
>>> m
<memory at 0x37f850>
>>> len(m)           # Returns length of underlying object
52
>>> m[0], m[25], m[26]   # Indexing returns one byte
('a', 'z', 'A')
>>> m2 = m[0:26]         # Slicing returns another memoryview
>>> m2
<memory at 0x37f080>
```
The content of the view can be converted to a string of bytes or a list of integers:

```
>>> m2.tobytes()
'abcdefghijklmnopqrstuvwxyz'
>>> m2.tolist()
[97, 98, 99, 100, 101, 102, 103, ... 121, 122]
>>>
```
[ memoryview](../library/stdtypes.html#memoryview) objects allow modifying the underlying object if
it’s a mutable object.

```
>>> m2[0] = 75
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot modify read-only memory
>>> b = bytearray(string.letters)  # Creating a mutable object
>>> b
bytearray(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
>>> mb = memoryview(b)
>>> mb[0] = '*'         # Assign to view, changing the bytearray.
>>> b[0:5]              # The bytearray has been changed.
bytearray(b'*bcde')
>>>
```
## Other Language Changes[¶](#other-language-changes)

Some smaller changes made to the core Python language are:

- The syntax for set literals has been backported from Python 3.x. Curly brackets are used to surround the contents of the resulting mutable set; set literals are distinguished from dictionaries by not containing colons and values. - `{}`continues to represent an empty dictionary; use- `set()`for an empty set.- >>> {1, 2, 3, 4, 5} set([1, 2, 3, 4, 5]) >>> set() # empty set set([]) >>> {} # empty dict {} - Backported by Alexandre Vassalotti; - [bpo-2335](https://bugs.python.org/issue?@action=redirect&bpo=2335).
- Dictionary and set comprehensions are another feature backported from 3.x, generalizing list/generator comprehensions to use the literal syntax for sets and dictionaries. - >>> {x: x*x for x in range(6)} {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25} >>> {('a'*x) for x in range(6)} set(['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa']) - Backported by Alexandre Vassalotti; - [bpo-2333](https://bugs.python.org/issue?@action=redirect&bpo=2333).
- The - `with`- `with`statement. This means that:- with A() as a, B() as b: ... suite of statements ... - is equivalent to: - with A() as a: with B() as b: ... suite of statements ... - The - `contextlib.nested()`function provides a very similar function, so it’s no longer necessary and has been deprecated.- (Proposed in - [https://codereview.appspot.com/53094](https://codereview.appspot.com/53094); implemented by Georg Brandl.)
- Conversions between floating-point numbers and strings are now correctly rounded on most platforms. These conversions occur in many different places: - `str()`- `float`- `complex`- `marshal`- `pickle`- `json`- `Decimal`- Related to this, the - `repr()`- *x*now returns a result based on the shortest decimal string that’s guaranteed to round back to- *x*under correct rounding (with round-half-to-even rounding mode). Previously it gave a string based on rounding x to 17 decimal digits.- The rounding library responsible for this improvement works on Windows and on Unix platforms using the gcc, icc, or suncc compilers. There may be a small number of platforms where correct operation of this code cannot be guaranteed, so the code is not used on such systems. You can find out which code is being used by checking - `sys.float_repr_style`- `short`if the new code is in use and- `legacy`if it isn’t.- Implemented by Eric Smith and Mark Dickinson, using David Gay’s - `dtoa.c`library;- [bpo-7117](https://bugs.python.org/issue?@action=redirect&bpo=7117).
- Conversions from long integers and regular integers to floating point now round differently, returning the floating-point number closest to the number. This doesn’t matter for small integers that can be converted exactly, but for large numbers that will unavoidably lose precision, Python 2.7 now approximates more closely. For example, Python 2.6 computed the following: - >>> n = 295147905179352891391 >>> float(n) 2.9514790517935283e+20 >>> n - long(float(n)) 65535L - Python 2.7’s floating-point result is larger, but much closer to the true value: - >>> n = 295147905179352891391 >>> float(n) 2.9514790517935289e+20 >>> n - long(float(n)) -1L - (Implemented by Mark Dickinson; - [bpo-3166](https://bugs.python.org/issue?@action=redirect&bpo=3166).)- Integer division is also more accurate in its rounding behaviours. (Also implemented by Mark Dickinson; - [bpo-1811](https://bugs.python.org/issue?@action=redirect&bpo=1811).)
- Implicit coercion for complex numbers has been removed; the interpreter will no longer ever attempt to call a - `__coerce__()`method on complex objects. (Removed by Meador Inge and Mark Dickinson;- [bpo-5211](https://bugs.python.org/issue?@action=redirect&bpo=5211).)
- The - `str.format()`- `str.format()`more closely resemble using- `%s`formatting:- >>> '{}:{}:{}'.format(2009, 04, 'Sunday') '2009:4:Sunday' >>> '{}:{}:{day}'.format(2009, 4, day='Sunday') '2009:4:Sunday' - The auto-numbering takes the fields from left to right, so the first - `{...}`specifier will use the first argument to- `str.format()`- [bpo-5237](https://bugs.python.org/issue?@action=redirect&bpo=5237).)- Complex numbers now correctly support usage with - `format()`- `1.5+3j`output. (Contributed by Eric Smith;- [bpo-1588](https://bugs.python.org/issue?@action=redirect&bpo=1588)and- [bpo-7988](https://bugs.python.org/issue?@action=redirect&bpo=7988).)- The ‘F’ format code now always formats its output using uppercase characters, so it will now produce ‘INF’ and ‘NAN’. (Contributed by Eric Smith; - [bpo-3382](https://bugs.python.org/issue?@action=redirect&bpo=3382).)- A low-level change: the - `object.__format__()`- `PendingDeprecationWarning`- `__format__()`method for- `object`- [bpo-7994](https://bugs.python.org/issue?@action=redirect&bpo=7994).)
- The - `int()`- `long()`types gained a- `bit_length`method that returns the number of bits necessary to represent its argument in binary:- >>> n = 37 >>> bin(n) '0b100101' >>> n.bit_length() 6 >>> n = 2**123-1 >>> n.bit_length() 123 >>> (n+1).bit_length() 124 - (Contributed by Fredrik Johansson and Victor Stinner; - [bpo-3439](https://bugs.python.org/issue?@action=redirect&bpo=3439).)
- The - `import`- `from .os import sep`) fails. This fixes a bug, but could possibly break certain- `import`statements that were only working by accident. (Fixed by Meador Inge;- [bpo-7902](https://bugs.python.org/issue?@action=redirect&bpo=7902).)
- It’s now possible for a subclass of the built-in - `unicode`type to override the- `__unicode__()`method. (Implemented by Victor Stinner;- [bpo-1583863](https://bugs.python.org/issue?@action=redirect&bpo=1583863).)
- The - `bytearray`- `translate()`- `None`as its first argument. (Fixed by Georg Brandl;- [bpo-4759](https://bugs.python.org/issue?@action=redirect&bpo=4759).)
- When using - `@classmethod`- `@staticmethod`- `__func__`- [bpo-5982](https://bugs.python.org/issue?@action=redirect&bpo=5982).)
- When a restricted set of attributes were set using - `__slots__`, deleting an unset attribute would not raise- `AttributeError`- [bpo-7604](https://bugs.python.org/issue?@action=redirect&bpo=7604).)
- Two new encodings are now supported: “cp720”, used primarily for Arabic text; and “cp858”, a variant of CP 850 that adds the euro symbol. (CP720 contributed by Alexander Belchenko and Amaury Forgeot d’Arc in - [bpo-1616979](https://bugs.python.org/issue?@action=redirect&bpo=1616979); CP858 contributed by Tim Hatch in- [bpo-8016](https://bugs.python.org/issue?@action=redirect&bpo=8016).)
- The - `file`object will now set the- `filename`attribute on the- `IOError`- [bpo-4764](https://bugs.python.org/issue?@action=redirect&bpo=4764)), and now explicitly checks for and forbids writing to read-only file objects instead of trusting the C library to catch and report the error (fixed by Stefan Krah;- [bpo-5677](https://bugs.python.org/issue?@action=redirect&bpo=5677)).
- The Python tokenizer now translates line endings itself, so the - `compile()`
- Extra parentheses in function definitions are illegal in Python 3.x, meaning that you get a syntax error from - `def f((x)): pass`. In Python3-warning mode, Python 2.7 will now warn about this odd usage. (Noted by James Lingard;- [bpo-7362](https://bugs.python.org/issue?@action=redirect&bpo=7362).)
- It’s now possible to create weak references to old-style class objects. New-style classes were always weak-referenceable. (Fixed by Antoine Pitrou; - [bpo-8268](https://bugs.python.org/issue?@action=redirect&bpo=8268).)
- When a module object is garbage-collected, the module’s dictionary is now only cleared if no one else is holding a reference to the dictionary ( - [bpo-7140](https://bugs.python.org/issue?@action=redirect&bpo=7140)).

### Interpreter Changes[¶](#interpreter-changes)

A new environment variable, [ PYTHONWARNINGS](../using/cmdline.html#envvar-PYTHONWARNINGS),
allows controlling warnings.  It should be set to a string
containing warning settings, equivalent to those
used with the 

[switch, separated by commas. (Contributed by Brian Curtin;](../using/cmdline.html#cmdoption-W)

`-W`[bpo-7301](https://bugs.python.org/issue?@action=redirect&bpo=7301).)

For example, the following setting will print warnings every time
they occur, but turn warnings from the [ Cookie](../library/http.cookies.html#module-http.cookies) module into an
error.  (The exact syntax for setting an environment variable varies
across operating systems and shells.)

```
export PYTHONWARNINGS=all,error:::Cookie:0
```
### Optimizations[¶](#optimizations)

Several performance enhancements have been added:

- A new opcode was added to perform the initial setup for - `with`- `__enter__()`- `__exit__()`
- The garbage collector now performs better for one common usage pattern: when many objects are being allocated without deallocating any of them. This would previously take quadratic time for garbage collection, but now the number of full garbage collections is reduced as the number of objects on the heap grows. The new logic only performs a full garbage collection pass when the middle generation has been collected 10 times and when the number of survivor objects from the middle generation exceeds 10% of the number of objects in the oldest generation. (Suggested by Martin von Löwis and implemented by Antoine Pitrou; - [bpo-4074](https://bugs.python.org/issue?@action=redirect&bpo=4074).)
- The garbage collector tries to avoid tracking simple containers which can’t be part of a cycle. In Python 2.7, this is now true for tuples and dicts containing atomic types (such as ints, strings, etc.). Transitively, a dict containing tuples of atomic types won’t be tracked either. This helps reduce the cost of each garbage collection by decreasing the number of objects to be considered and traversed by the collector. (Contributed by Antoine Pitrou; - [bpo-4688](https://bugs.python.org/issue?@action=redirect&bpo=4688).)
- Long integers are now stored internally either in base - `2**15`or in base- `2**30`, the base being determined at build time. Previously, they were always stored in base- `2**15`. Using base- `2**30`gives significant performance improvements on 64-bit machines, but benchmark results on 32-bit machines have been mixed. Therefore, the default is to use base- `2**30`on 64-bit machines and base- `2**15`on 32-bit machines; on Unix, there’s a new configure option- `--enable-big-digits`that can be used to override this default.- Apart from the performance improvements this change should be invisible to end users, with one exception: for testing and debugging purposes there’s a new structseq - `sys.long_info`that provides information about the internal format, giving the number of bits per digit and the size in bytes of the C type used to store each digit:- >>> import sys >>> sys.long_info sys.long_info(bits_per_digit=30, sizeof_digit=4) - (Contributed by Mark Dickinson; - [bpo-4258](https://bugs.python.org/issue?@action=redirect&bpo=4258).)- Another set of changes made long objects a few bytes smaller: 2 bytes smaller on 32-bit systems and 6 bytes on 64-bit. (Contributed by Mark Dickinson; - [bpo-5260](https://bugs.python.org/issue?@action=redirect&bpo=5260).)
- The division algorithm for long integers has been made faster by tightening the inner loop, doing shifts instead of multiplications, and fixing an unnecessary extra iteration. Various benchmarks show speedups of between 50% and 150% for long integer divisions and modulo operations. (Contributed by Mark Dickinson; - [bpo-5512](https://bugs.python.org/issue?@action=redirect&bpo=5512).) Bitwise operations are also significantly faster (initial patch by Gregory Smith;- [bpo-1087418](https://bugs.python.org/issue?@action=redirect&bpo=1087418)).
- The implementation of - `%`checks for the left-side operand being a Python string and special-cases it; this results in a 1–3% performance increase for applications that frequently use- `%`with strings, such as templating libraries. (Implemented by Collin Winter;- [bpo-5176](https://bugs.python.org/issue?@action=redirect&bpo=5176).)
- List comprehensions with an - `if`condition are compiled into faster bytecode. (Patch by Antoine Pitrou, back-ported to 2.7 by Jeffrey Yasskin;- [bpo-4715](https://bugs.python.org/issue?@action=redirect&bpo=4715).)
- Converting an integer or long integer to a decimal string was made faster by special-casing base 10 instead of using a generalized conversion function that supports arbitrary bases. (Patch by Gawain Bolton; - [bpo-6713](https://bugs.python.org/issue?@action=redirect&bpo=6713).)
- The - `split()`,- `replace()`,- `rindex()`,- `rpartition()`, and- `rsplit()`methods of string-like types (strings, Unicode strings, and- `bytearray`- [bpo-7462](https://bugs.python.org/issue?@action=redirect&bpo=7462)and- [bpo-7622](https://bugs.python.org/issue?@action=redirect&bpo=7622).)
- The - `pickle`- `cPickle`modules now automatically intern the strings used for attribute names, reducing memory usage of the objects resulting from unpickling. (Contributed by Jake McGuire;- [bpo-5084](https://bugs.python.org/issue?@action=redirect&bpo=5084).)
- The - `cPickle`module now special-cases dictionaries, nearly halving the time required to pickle them. (Contributed by Collin Winter;- [bpo-5670](https://bugs.python.org/issue?@action=redirect&bpo=5670).)

## New and Improved Modules[¶](#new-and-improved-modules)

As in every release, Python’s standard library received a number of
enhancements and bug fixes.  Here’s a partial list of the most notable
changes, sorted alphabetically by module name. Consult the
`Misc/NEWS` file in the source tree for a more complete list of
changes, or look through the Subversion logs for all the details.

- The - `bdb`- `Bdb`- `django.*`; the debugger will not step into stack frames from a module that matches one of these patterns. (Contributed by Maru Newby after a suggestion by Senthil Kumaran;- [bpo-5142](https://bugs.python.org/issue?@action=redirect&bpo=5142).)
- The - `binascii`- `memoryview`- [bpo-7703](https://bugs.python.org/issue?@action=redirect&bpo=7703).)
- Updated module: the - `bsddb`module has been updated from 4.7.2devel9 to version 4.8.4 of- [the pybsddb package](https://www.jcea.es/programacion/pybsddb.htm). The new version features better Python 3.x compatibility, various bug fixes, and adds several new BerkeleyDB flags and methods. (Updated by Jesús Cea Avión;- [bpo-8156](https://bugs.python.org/issue?@action=redirect&bpo=8156). The pybsddb changelog can be read at- [https://hg.jcea.es/pybsddb/file/tip/ChangeLog](https://hg.jcea.es/pybsddb/file/tip/ChangeLog).)
- The - `bz2`- `BZ2File`- `with bz2.BZ2File(...) as f:`. (Contributed by Hagen Fürstenau;- [bpo-3860](https://bugs.python.org/issue?@action=redirect&bpo=3860).)
- New class: the - `Counter`- `collections`- `Counter`instances behave mostly like dictionaries but return zero for missing keys instead of raising a- `KeyError`- >>> from collections import Counter >>> c = Counter() >>> for letter in 'here is a sample of english text': ... c[letter] += 1 ... >>> c Counter({' ': 6, 'e': 5, 's': 3, 'a': 2, 'i': 2, 'h': 2, 'l': 2, 't': 2, 'g': 1, 'f': 1, 'm': 1, 'o': 1, 'n': 1, 'p': 1, 'r': 1, 'x': 1}) >>> c['e'] 5 >>> c['z'] 0 - There are three additional - `Counter`- `most_common()`- `elements()`- `subtract()`- `Counter`, the counts are subtracted.- >>> c.most_common(5) [(' ', 6), ('e', 5), ('s', 3), ('a', 2), ('i', 2)] >>> c.elements() -> 'a', 'a', ' ', ' ', ' ', ' ', ' ', ' ', 'e', 'e', 'e', 'e', 'e', 'g', 'f', 'i', 'i', 'h', 'h', 'm', 'l', 'l', 'o', 'n', 'p', 's', 's', 's', 'r', 't', 't', 'x' >>> c['e'] 5 >>> c.subtract('very heavy on the letter e') >>> c['e'] # Count is now lower -1 - Contributed by Raymond Hettinger; - [bpo-1696199](https://bugs.python.org/issue?@action=redirect&bpo=1696199).- New class: - `OrderedDict`- [PEP 372: Adding an Ordered Dictionary to collections](#pep-0372).- New method: The - `deque`- `count()`- *x*, and a- `reverse()`- `deque`also exposes its maximum length as the read-only- `maxlen`- The - `namedtuple`- *rename*parameter. If- *rename*is true, field names that are invalid because they’ve been repeated or aren’t legal Python identifiers will be renamed to legal names that are derived from the field’s position within the list of fields:- >>> from collections import namedtuple >>> T = namedtuple('T', ['field1', '$illegal', 'for', 'field2'], rename=True) >>> T._fields ('field1', '_1', '_2', 'field2') - (Added by Raymond Hettinger; - [bpo-1818](https://bugs.python.org/issue?@action=redirect&bpo=1818).)- Finally, the - `Mapping`- `NotImplemented`- `Mapping`. (Fixed by Daniel Stutzbach;- [bpo-8729](https://bugs.python.org/issue?@action=redirect&bpo=8729).)
- Constructors for the parsing classes in the - `ConfigParser`- *allow_no_value*parameter, defaulting to false; if true, options without values will be allowed. For example:- >>> import ConfigParser, StringIO >>> sample_config = """ ... [mysqld] ... user = mysql ... pid-file = /var/run/mysqld/mysqld.pid ... skip-bdb ... """ >>> config = ConfigParser.RawConfigParser(allow_no_value=True) >>> config.readfp(StringIO.StringIO(sample_config)) >>> config.get('mysqld', 'user') 'mysql' >>> print config.get('mysqld', 'skip-bdb') None >>> print config.get('mysqld', 'unknown') Traceback (most recent call last): ... NoOptionError: No option 'unknown' in section: 'mysqld' - (Contributed by Mats Kindahl; - [bpo-7005](https://bugs.python.org/issue?@action=redirect&bpo=7005).)
- Deprecated function: - `contextlib.nested()`, which allows handling more than one context manager with a single- `with`- `with`statement now supports multiple context managers.
- The - `cookielib`- [bpo-3924](https://bugs.python.org/issue?@action=redirect&bpo=3924).)
- The - `copy`- `deepcopy()`- [bpo-1515](https://bugs.python.org/issue?@action=redirect&bpo=1515).)
- The - `ctypes`- `None`to a C- `NULL`pointer for arguments declared as pointers. (Changed by Thomas Heller;- [bpo-4606](https://bugs.python.org/issue?@action=redirect&bpo=4606).) The underlying- [libffi library](https://sourceware.org/libffi/)has been updated to version 3.0.9, containing various fixes for different platforms. (Updated by Matthias Klose;- [bpo-8142](https://bugs.python.org/issue?@action=redirect&bpo=8142).)
- New method: the - `datetime`- `timedelta`- `total_seconds()`- [bpo-5788](https://bugs.python.org/issue?@action=redirect&bpo=5788).)
- New method: the - `Decimal`- `from_float()`- `Decimal`. This exact conversion strives for the closest decimal approximation to the floating-point representation’s value; the resulting decimal value will therefore still include the inaccuracy, if any. For example,- `Decimal.from_float(0.1)`returns- `Decimal('0.1000000000000000055511151231257827021181583404541015625')`. (Implemented by Raymond Hettinger;- [bpo-4796](https://bugs.python.org/issue?@action=redirect&bpo=4796).)- Comparing instances of - `Decimal`- `Decimal`and floating point in other operations such as addition, since you should be explicitly choosing how to convert between float and- `Decimal`. (Fixed by Mark Dickinson;- [bpo-2531](https://bugs.python.org/issue?@action=redirect&bpo=2531).)- The constructor for - `Decimal`- [bpo-8257](https://bugs.python.org/issue?@action=redirect&bpo=8257)) and non-European Unicode characters such as Arabic-Indic digits (contributed by Mark Dickinson;- [bpo-6595](https://bugs.python.org/issue?@action=redirect&bpo=6595)).- Most of the methods of the - `Context`- `Decimal`- `canonical()`- `is_canonical()`- [bpo-7633](https://bugs.python.org/issue?@action=redirect&bpo=7633).)- When using - `Decimal`- `format()`- [bpo-6857](https://bugs.python.org/issue?@action=redirect&bpo=6857).)- Comparisons involving a signaling NaN value (or - `sNAN`) now signal- `InvalidOperation`- `NaN`) are now hashable. (Fixed by Mark Dickinson;- [bpo-7279](https://bugs.python.org/issue?@action=redirect&bpo=7279).)
- The - `difflib`- **diff**/- **patch**tools through one small change, using a tab character instead of spaces as a separator in the header giving the filename. (Fixed by Anatoly Techtonik;- [bpo-7585](https://bugs.python.org/issue?@action=redirect&bpo=7585).)
- The Distutils - `sdist`command now always regenerates the- `MANIFEST`file, since even if the- `MANIFEST.in`or- `setup.py`files haven’t been modified, the user might have created some new files that should be included. (Fixed by Tarek Ziadé;- [bpo-8688](https://bugs.python.org/issue?@action=redirect&bpo=8688).)
- The - `doctest`- `IGNORE_EXCEPTION_DETAIL`- [bpo-7490](https://bugs.python.org/issue?@action=redirect&bpo=7490).)
- The - `email`- `Message`- `output_charset`. (Added by R. David Murray;- [bpo-1368247](https://bugs.python.org/issue?@action=redirect&bpo=1368247).)
- The - `Fraction`- `Decimal`- [bpo-5812](https://bugs.python.org/issue?@action=redirect&bpo=5812), and float/decimal in- [bpo-8294](https://bugs.python.org/issue?@action=redirect&bpo=8294).)- Ordering comparisons ( - `<`,- `<=`,- `>`,- `>=`) between fractions and complex numbers now raise a- `TypeError`- `Fraction`
- New class: - `FTP_TLS`- `ftplib`- [bpo-2054](https://bugs.python.org/issue?@action=redirect&bpo=2054).)- The - `storbinary()`- *rest*parameter (patch by Pablo Mouzo;- [bpo-6845](https://bugs.python.org/issue?@action=redirect&bpo=6845).)
- New class decorator: - `total_ordering()`- `functools`- `__eq__()`- `__lt__()`- `__le__()`- `__gt__()`- `__ge__()`- `__cmp__()`method is being deprecated in Python 3.x, this decorator makes it easier to define ordered classes. (Added by Raymond Hettinger;- [bpo-5479](https://bugs.python.org/issue?@action=redirect&bpo=5479).)- New function: - `cmp_to_key()`- *key*parameter to functions such as- `sorted()`- `min()`- `max()`
- New function: the - `gc`- `is_tracked()`- [bpo-4688](https://bugs.python.org/issue?@action=redirect&bpo=4688).)
- The - `gzip`- `GzipFile`- `with gzip.GzipFile(...) as f:`(contributed by Hagen Fürstenau;- [bpo-3860](https://bugs.python.org/issue?@action=redirect&bpo=3860)), and it now implements the- `io.BufferedIOBase`- `io.BufferedReader`- [bpo-7471](https://bugs.python.org/issue?@action=redirect&bpo=7471)). It’s also now possible to override the modification time recorded in a gzipped file by providing an optional timestamp to the constructor. (Contributed by Jacques Frechet;- [bpo-4272](https://bugs.python.org/issue?@action=redirect&bpo=4272).)- Files in gzip format can be padded with trailing zero bytes; the - `gzip`- [bpo-2846](https://bugs.python.org/issue?@action=redirect&bpo=2846).)
- New attribute: the - `hashlib`- `algorithms`attribute containing a tuple naming the supported algorithms. In Python 2.7,- `hashlib.algorithms`contains- `('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')`. (Contributed by Carl Chenet;- [bpo-7418](https://bugs.python.org/issue?@action=redirect&bpo=7418).)
- The default - `HTTPResponse`- `httplib`- [bpo-4879](https://bugs.python.org/issue?@action=redirect&bpo=4879).)- The - `HTTPConnection`- `HTTPSConnection`- *source_address*parameter, a- `(host, port)`2-tuple giving the source address that will be used for the connection. (Contributed by Eldon Ziegler;- [bpo-3972](https://bugs.python.org/issue?@action=redirect&bpo=3972).)
- The - `ihooks`module now supports relative imports. Note that- `ihooks`is an older module for customizing imports, superseded by the- `imputil`module added in Python 2.0. (Relative import support added by Neil Schemenauer.)
- The - `imaplib`- [bpo-1655](https://bugs.python.org/issue?@action=redirect&bpo=1655).)
- New function: the - `inspect`- `getcallargs()`- >>> from inspect import getcallargs >>> def f(a, b=1, *pos, **named): ... pass ... >>> getcallargs(f, 1, 2, 3) {'a': 1, 'b': 2, 'pos': (3,), 'named': {}} >>> getcallargs(f, a=2, x=4) {'a': 2, 'b': 1, 'pos': (), 'named': {'x': 4}} >>> getcallargs(f) Traceback (most recent call last): ... TypeError: f() takes at least 1 argument (0 given) - Contributed by George Sakkis; - [bpo-3135](https://bugs.python.org/issue?@action=redirect&bpo=3135).
- Updated module: The - `io`- `_pyio`module.- One minor resulting change: the - `io.TextIOBase`- `errors`- `'strict'`,- `'replace'`,- `'ignore'`).- The - `io.FileIO`- `OSError`- [bpo-4991](https://bugs.python.org/issue?@action=redirect&bpo=4991).) The- `truncate()`- [bpo-6939](https://bugs.python.org/issue?@action=redirect&bpo=6939).)
- New function: - `itertools.compress(data, selectors)`takes two iterators. Elements of- *data*are returned if the corresponding value in- *selectors*is true:- itertools.compress('ABCDEF', [1,0,1,0,1,1]) => A, C, E, F - New function: - `itertools.combinations_with_replacement(iter, r)`returns all the possible- *r*-length combinations of elements from the iterable- *iter*. Unlike- `combinations()`- itertools.combinations_with_replacement('abc', 2) => ('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c') - Note that elements are treated as unique depending on their position in the input, not their actual values. - The - `itertools.count()`- *step*argument that allows incrementing by values other than 1.- `count()`also now allows keyword arguments, and using non-integer values such as floats or- `Decimal`- [bpo-5032](https://bugs.python.org/issue?@action=redirect&bpo=5032).)- `itertools.combinations()`- `itertools.product()`- `ValueError`- *r*larger than the input iterable. This was deemed a specification error, so they now return an empty iterator. (Fixed by Raymond Hettinger;- [bpo-4816](https://bugs.python.org/issue?@action=redirect&bpo=4816).)
- Updated module: The - `json`- [bpo-4136](https://bugs.python.org/issue?@action=redirect&bpo=4136).)- To support the new - `collections.OrderedDict`- `json.load()`- *object_pairs_hook*parameter that will be called with any object literal that decodes to a list of pairs. (Contributed by Raymond Hettinger;- [bpo-5381](https://bugs.python.org/issue?@action=redirect&bpo=5381).)
- The - `mailbox`- `Maildir`- [bpo-1607951](https://bugs.python.org/issue?@action=redirect&bpo=1607951),- [bpo-6896](https://bugs.python.org/issue?@action=redirect&bpo=6896).)
- New functions: the - `math`- `erf()`- `erfc()`- `expm1()`- `e**x - 1`with more precision than using- `exp()`- `gamma()`- `lgamma()`- [bpo-3366](https://bugs.python.org/issue?@action=redirect&bpo=3366).)
- The - `multiprocessing`- `Manager*`classes can now be passed a callable that will be called whenever a subprocess is started, along with a set of arguments that will be passed to the callable. (Contributed by lekma;- [bpo-5585](https://bugs.python.org/issue?@action=redirect&bpo=5585).)- The - `Pool`- *maxtasksperchild*parameter. Worker processes will perform the specified number of tasks and then exit, causing the- `Pool`to start a new worker. This is useful if tasks may leak memory or other resources, or if some tasks will cause the worker to become very large. (Contributed by Charles Cazabon;- [bpo-6963](https://bugs.python.org/issue?@action=redirect&bpo=6963).)
- The - `nntplib`module now supports IPv6 addresses. (Contributed by Derek Morr;- [bpo-1664](https://bugs.python.org/issue?@action=redirect&bpo=1664).)
- New functions: the - `os`- `getresgid()`- `getresuid()`- `setresgid()`- `setresuid()`- `initgroups()`- [bpo-6508](https://bugs.python.org/issue?@action=redirect&bpo=6508). Support for initgroups added by Jean-Paul Calderone;- [bpo-7333](https://bugs.python.org/issue?@action=redirect&bpo=7333).)- The - `os.fork()`- `fork()`is called from a thread. (Fixed by Zsolt Cserna;- [bpo-7242](https://bugs.python.org/issue?@action=redirect&bpo=7242).)
- In the - `os.path`- `normpath()`- `abspath()`- `normpath()`- [bpo-5827](https://bugs.python.org/issue?@action=redirect&bpo=5827);- `abspath()`- [bpo-3426](https://bugs.python.org/issue?@action=redirect&bpo=3426).)
- The - `pydoc`- `help('<<')`or- `help('@')`, for example. (Contributed by David Laban;- [bpo-4739](https://bugs.python.org/issue?@action=redirect&bpo=4739).)
- The - `re`- `split()`- `sub()`- `subn()`- *flags*argument, for consistency with the other functions in the module. (Added by Gregory P. Smith.)
- New function: - `run_path()`- `runpy`- *path*argument.- *path*can be the path of a Python source file (- `example.py`), a compiled bytecode file (- `example.pyc`), a directory (- `./package/`), or a zip archive (- `example.zip`). If a directory or zip path is provided, it will be added to the front of- `sys.path`and the module- `__main__`- `__main__.py`; if it doesn’t, some other- `__main__.py`might be imported from a location later in- `sys.path`. This makes more of the machinery of- `runpy`available to scripts that want to mimic the way Python’s command line processes an explicit path name. (Added by Nick Coghlan;- [bpo-6816](https://bugs.python.org/issue?@action=redirect&bpo=6816).)
- New function: in the - `shutil`- `make_archive()`- `shutil`- `copyfile()`- `copytree()`- `SpecialFileError`- [bpo-3002](https://bugs.python.org/issue?@action=redirect&bpo=3002).)
- The - `signal`- [bpo-8354](https://bugs.python.org/issue?@action=redirect&bpo=8354).)
- New functions: in the - `site`- `getsitepackages()`- `getusersitepackages()`- `getuserbase()`- `USER_BASE`- [bpo-6693](https://bugs.python.org/issue?@action=redirect&bpo=6693).)- The - `site`- `sitecustomize`- `KeyboardInterrupt`- [bpo-3137](https://bugs.python.org/issue?@action=redirect&bpo=3137).)
- The - `create_connection()`- *source_address*parameter, a- `(host, port)`2-tuple giving the source address that will be used for the connection. (Contributed by Eldon Ziegler;- [bpo-3972](https://bugs.python.org/issue?@action=redirect&bpo=3972).)- The - `recv_into()`- `recvfrom_into()`- `bytearray`- `memoryview`- [bpo-8104](https://bugs.python.org/issue?@action=redirect&bpo=8104).)
- The - `SocketServer`- `TCPServer`- `disable_nagle_algorithm`class attribute defaults to- `False`; if overridden to be true, new request connections will have the TCP_NODELAY option set to prevent buffering many small sends into a single TCP packet. The- `timeout`- `handle_timeout()`- `handle_request()`- [bpo-6192](https://bugs.python.org/issue?@action=redirect&bpo=6192)and- [bpo-6267](https://bugs.python.org/issue?@action=redirect&bpo=6267).)
- Updated module: the - `sqlite3`- [pysqlite package](https://github.com/ghaering/pysqlite). Version 2.6.0 includes a number of bugfixes, and adds the ability to load SQLite extensions from shared libraries. Call the- `enable_load_extension(True)`method to enable extensions, and then call- `load_extension()`
- The - `ssl`- `SSLSocket`- [bpo-7133](https://bugs.python.org/issue?@action=redirect&bpo=7133)) and automatically set OpenSSL’s- `SSL_MODE_AUTO_RETRY`, which will prevent an error code being returned from- `recv()`operations that trigger an SSL renegotiation (fix by Antoine Pitrou;- [bpo-8222](https://bugs.python.org/issue?@action=redirect&bpo=8222)).- The - `wrap_socket()`- *ciphers*argument that’s a string listing the encryption algorithms to be allowed; the format of the string is described- [in the OpenSSL documentation](https://docs.openssl.org/1.0.2/man1/ciphers/). (Added by Antoine Pitrou;- [bpo-8322](https://bugs.python.org/issue?@action=redirect&bpo=8322).)- Another change makes the extension load all of OpenSSL’s ciphers and digest algorithms so that they’re all available. Some SSL certificates couldn’t be verified, reporting an “unknown algorithm” error. (Reported by Beda Kosata, and fixed by Antoine Pitrou; - [bpo-8484](https://bugs.python.org/issue?@action=redirect&bpo=8484).)- The version of OpenSSL being used is now available as the module attributes - `ssl.OPENSSL_VERSION`- `ssl.OPENSSL_VERSION_INFO`- `ssl.OPENSSL_VERSION_NUMBER`- [bpo-8321](https://bugs.python.org/issue?@action=redirect&bpo=8321).)
- The - `struct`- `bBhHiIlLqQ`); it now always raises a- `struct.error`- [bpo-1523](https://bugs.python.org/issue?@action=redirect&bpo=1523).) The- `pack()`- `__index__()`- `__int__()`- [bpo-8300](https://bugs.python.org/issue?@action=redirect&bpo=8300).)
- New function: the - `subprocess`- `check_output()`- `CalledProcessError`- >>> subprocess.check_output(['df', '-h', '.']) 'Filesystem Size Used Avail Capacity Mounted on\n /dev/disk0s2 52G 49G 3.0G 94% /\n' >>> subprocess.check_output(['df', '-h', '/bogus']) ... subprocess.CalledProcessError: Command '['df', '-h', '/bogus']' returned non-zero exit status 1 - (Contributed by Gregory P. Smith.) - The - `subprocess`- `EINTR`- [bpo-1068268](https://bugs.python.org/issue?@action=redirect&bpo=1068268).)
- New function: - `is_declared_global()`- `symtable`
- The - `syslog`- `sys.argv[0]`as the identifier instead of the previous default value of- `'python'`. (Changed by Sean Reifschneider;- [bpo-8451](https://bugs.python.org/issue?@action=redirect&bpo=8451).)
- The - `sys.version_info`- `major`,- `minor`,- `micro`,- `releaselevel`, and- `serial`. (Contributed by Ross Light;- [bpo-4285](https://bugs.python.org/issue?@action=redirect&bpo=4285).)- `sys.getwindowsversion()`- `major`,- `minor`,- `build`,- `platform`,- `service_pack`,- `service_pack_major`,- `service_pack_minor`,- `suite_mask`, and- `product_type`. (Contributed by Brian Curtin;- [bpo-7766](https://bugs.python.org/issue?@action=redirect&bpo=7766).)
- The - `tarfile`- [bpo-7357](https://bugs.python.org/issue?@action=redirect&bpo=7357).)- `tarfile`- `TarInfo`- `add()`- *filter*argument that’s a callable. The- *filter*callable will be passed the- `TarInfo`for every file being added, and can modify and return it. If the callable returns- `None`, the file will be excluded from the resulting archive. This is more powerful than the existing- *exclude*argument, which has therefore been deprecated. (Added by Lars Gustäbel;- [bpo-6856](https://bugs.python.org/issue?@action=redirect&bpo=6856).) The- `TarFile`- [bpo-7232](https://bugs.python.org/issue?@action=redirect&bpo=7232).)
- The - `wait()`- `threading.Event`- `wait()`is supposed to block until the internal flag becomes true. The return value will only be false if a timeout was provided and the operation timed out. (Contributed by Tim Lesher;- [bpo-1674032](https://bugs.python.org/issue?@action=redirect&bpo=1674032).)
- The Unicode database provided by the - `unicodedata`- `Unihan.txt`data file (patch by Anders Chrigström and Amaury Forgeot d’Arc;- [bpo-1571184](https://bugs.python.org/issue?@action=redirect&bpo=1571184)) and has been updated to version 5.2.0 (updated by Florent Xicluna;- [bpo-8024](https://bugs.python.org/issue?@action=redirect&bpo=8024)).
- The - `urlparse`- `urlsplit()`- **RFC 3986**- `"<something>://..."`, the text before the- `://`is treated as the scheme, even if it’s a made-up scheme that the module doesn’t know about. This change may break code that worked around the old behaviour. For example, Python 2.6.4 or 2.5 will return the following:- >>> import urlparse >>> urlparse.urlsplit('invented://host/filename?query') ('invented', '', '//host/filename?query', '', '') - Python 2.7 (and Python 2.6.5) will return: - >>> import urlparse >>> urlparse.urlsplit('invented://host/filename?query') ('invented', 'host', '/filename?query', '', '') - (Python 2.7 actually produces slightly different output, since it returns a named tuple instead of a standard tuple.) - The - `urlparse`- **RFC 2732**- [bpo-2987](https://bugs.python.org/issue?@action=redirect&bpo=2987)).- >>> urlparse.urlparse('http://[1080::8:800:200C:417A]/foo') ParseResult(scheme='http', netloc='[1080::8:800:200C:417A]', path='/foo', params='', query='', fragment='') 
- New class: the - `WeakSet`- `weakref`
- The - `xml.etree.ElementTree`- `<?xml-stylesheet href="#style1"?>`) or comment (which looks like- `<!-- comment -->`). (Patch by Neil Muller;- [bpo-2746](https://bugs.python.org/issue?@action=redirect&bpo=2746).)
- The XML-RPC client and server, provided by the - `xmlrpclib`- `SimpleXMLRPCServer`- `encode_threshold`attribute of- `SimpleXMLRPCRequestHandler`- [bpo-6267](https://bugs.python.org/issue?@action=redirect&bpo=6267).)
- The - `zipfile`- `ZipFile`- `with zipfile.ZipFile(...) as f:`. (Contributed by Brian Curtin;- [bpo-5511](https://bugs.python.org/issue?@action=redirect&bpo=5511).)- `zipfile`- [bpo-4710](https://bugs.python.org/issue?@action=redirect&bpo=4710).) Reading files out of an archive is faster, and interleaving- `read()`- `readline()`- [bpo-7610](https://bugs.python.org/issue?@action=redirect&bpo=7610).)- The - `is_zipfile()`- [bpo-4756](https://bugs.python.org/issue?@action=redirect&bpo=4756).)- The - `writestr()`- *compress_type*parameter that lets you override the default compression method specified in the- `ZipFile`- [bpo-6003](https://bugs.python.org/issue?@action=redirect&bpo=6003).)

### New module: importlib[¶](#new-module-importlib)

Python 3.1 includes the [ importlib](../library/importlib.html#module-importlib) package, a re-implementation
of the logic underlying Python’s 

[statement.](../reference/simple_stmts.html#import)

`import``importlib` is useful for implementers of Python interpreters and
to users who wish to write new importers that can participate in the
import process.  Python 2.7 doesn’t contain the complete
`importlib` package, but instead has a tiny subset that contains
a single function, [.](../library/importlib.html#importlib.import_module)

`import_module()``import_module(name, package=None)` imports a module.  *name* is
a string containing the module or package’s name.  It’s possible to do
relative imports by providing a string that begins with a `.`
character, such as `..utils.errors`.  For relative imports, the
*package* argument must be provided and is the name of the package that
will be used as the anchor for
the relative import.  [ import_module()](../library/importlib.html#importlib.import_module) both inserts the imported
module into 

`sys.modules` and returns the module object.Here are some examples:

```
>>> from importlib import import_module
>>> anydbm = import_module('anydbm')  # Standard absolute import
>>> anydbm
<module 'anydbm' from '/p/python/Lib/anydbm.py'>
>>> # Relative import
>>> file_util = import_module('..file_util', 'distutils.command')
>>> file_util
<module 'distutils.file_util' from '/python/Lib/distutils/file_util.pyc'>
```
[ importlib](../library/importlib.html#module-importlib) was implemented by Brett Cannon and introduced in
Python 3.1.

### New module: sysconfig[¶](#new-module-sysconfig)

The [ sysconfig](../library/sysconfig.html#module-sysconfig) module has been pulled out of the Distutils
package, becoming a new top-level module in its own right.

`sysconfig` provides functions for getting information about
Python’s build process: compiler switches, installation paths, the
platform name, and whether Python is running from its source
directory.Some of the functions in the module are:

- `get_config_var()`- `pyconfig.h`file.
- `get_config_vars()`
- `get_path()`
- `is_python_build()`

Consult the [ sysconfig](../library/sysconfig.html#module-sysconfig) documentation for more details and for
a complete list of functions.

The Distutils package and [ sysconfig](../library/sysconfig.html#module-sysconfig) are now maintained by Tarek
Ziadé, who has also started a Distutils2 package (source repository at

[https://hg.python.org/distutils2/](https://hg.python.org/distutils2/)) for developing a next-generation version of Distutils.

### ttk: Themed Widgets for Tk[¶](#ttk-themed-widgets-for-tk)

Tcl/Tk 8.5 includes a set of themed widgets that re-implement basic Tk widgets but have a more customizable appearance and can therefore more closely resemble the native platform’s widgets. This widget set was originally called Tile, but was renamed to Ttk (for “themed Tk”) on being added to Tcl/Tck release 8.5.

To learn more, read the [ ttk](../library/tkinter.ttk.html#module-tkinter.ttk) module documentation.  You may also
wish to read the Tcl/Tk manual page describing the
Ttk theme engine, available at

[https://www.tcl.tk/man/tcl8.5/TkCmd/ttk_intro.html](https://www.tcl.tk/man/tcl8.5/TkCmd/ttk_intro.html). Some screenshots of the Python/Ttk code in use are at

[https://code.google.com/archive/p/python-ttk/wikis/Screenshots.wiki](https://code.google.com/archive/p/python-ttk/wikis/Screenshots.wiki).

The [ tkinter.ttk](../library/tkinter.ttk.html#module-tkinter.ttk) module was written by Guilherme Polo and added in

[bpo-2983](https://bugs.python.org/issue?@action=redirect&bpo=2983). An alternate version called

`Tile.py`, written by
Martin Franklin and maintained by Kevin Walzer, was proposed for
inclusion in [bpo-2618](https://bugs.python.org/issue?@action=redirect&bpo=2618), but the authors argued that Guilherme Polo’s work was more comprehensive.

### Updated module: unittest[¶](#updated-module-unittest)

The [ unittest](../library/unittest.html#module-unittest) module was greatly enhanced; many
new features were added.  Most of these features were implemented
by Michael Foord, unless otherwise noted.  The enhanced version of
the module is downloadable separately for use with Python versions 2.4 to 2.6,
packaged as the 

`unittest2` package, from [unittest2](https://pypi.org/project/unittest2/).

When used from the command line, the module can automatically discover
tests.  It’s not as fancy as [py.test](https://pytest.org) or
[nose](https://nose.readthedocs.io/), but provides a
simple way to run tests kept within a set of package directories.  For example,
the following command will search the `test/` subdirectory for
any importable test files named `test*.py`:

```
python -m unittest discover -s test
```
Consult the [ unittest](../library/unittest.html#module-unittest) module documentation for more details.
(Developed in 

[bpo-6001](https://bugs.python.org/issue?@action=redirect&bpo=6001).)

The [ main()](../library/unittest.html#unittest.main) function supports some other new options:

- `-b`- `--buffer`will buffer the standard output and standard error streams during each test. If the test passes, any resulting output will be discarded; on failure, the buffered output will be displayed.
- `-c`- `--catch`will cause the control-C interrupt to be handled more gracefully. Instead of interrupting the test process immediately, the currently running test will be completed and then the partial results up to the interruption will be reported. If you’re impatient, a second press of control-C will cause an immediate interruption.- This control-C handler tries to avoid causing problems when the code being tested or the tests being run have defined a signal handler of their own, by noticing that a signal handler was already set and calling it. If this doesn’t work for you, there’s a - `removeHandler()`
- `-f`- `--failfast`makes test execution stop immediately when a test fails instead of continuing to execute further tests. (Suggested by Cliff Dyer and implemented by Michael Foord;- [bpo-8074](https://bugs.python.org/issue?@action=redirect&bpo=8074).)

The progress messages now show ‘x’ for expected failures and ‘u’ for unexpected successes when run in verbose mode. (Contributed by Benjamin Peterson.)

Test cases can raise the [ SkipTest](../library/unittest.html#unittest.SkipTest) exception to skip a
test (

[bpo-1034053](https://bugs.python.org/issue?@action=redirect&bpo=1034053)).

The error messages for [ assertEqual()](../library/unittest.html#unittest.TestCase.assertEqual),

[, and](../library/unittest.html#unittest.TestCase.assertTrue)

`assertTrue()`[failures now provide more information. If you set the](../library/unittest.html#unittest.TestCase.assertFalse)

`assertFalse()`[attribute of your](../library/unittest.html#unittest.TestCase.longMessage)

`longMessage`[classes to true, both the standard error message and any additional message you provide will be printed for failures. (Added by Michael Foord;](../library/unittest.html#unittest.TestCase)

`TestCase`[bpo-5663](https://bugs.python.org/issue?@action=redirect&bpo=5663).)

The [ assertRaises()](../library/unittest.html#unittest.TestCase.assertRaises) method now
returns a context handler when called without providing a callable
object to run.  For example, you can write this:

```
with self.assertRaises(KeyError):
    {}['foo']
```
(Implemented by Antoine Pitrou; [bpo-4444](https://bugs.python.org/issue?@action=redirect&bpo=4444).)

Module- and class-level setup and teardown fixtures are now supported.
Modules can contain [ setUpModule()](../library/unittest.html#unittest.setUpModule) and 

[functions. Classes can have](../library/unittest.html#unittest.tearDownModule)

`tearDownModule()`[and](../library/unittest.html#unittest.TestCase.setUpClass)

`setUpClass()`[methods that must be defined as class methods (using](../library/unittest.html#unittest.TestCase.tearDownClass)

`tearDownClass()``@classmethod` or equivalent).  These functions and
methods are invoked when the test runner switches to a test case in a
different module or class.The methods [ addCleanup()](../library/unittest.html#unittest.TestCase.addCleanup) and

[were added.](../library/unittest.html#unittest.TestCase.doCleanups)

`doCleanups()``addCleanup()` lets you add cleanup functions that
will be called unconditionally (after [if](../library/unittest.html#unittest.TestCase.setUp)

`setUp()``setUp()` fails, otherwise after [). This allows for much simpler resource allocation and deallocation during tests (](../library/unittest.html#unittest.TestCase.tearDown)

`tearDown()`[bpo-5679](https://bugs.python.org/issue?@action=redirect&bpo=5679)).

A number of new methods were added that provide more specialized
tests.  Many of these methods were written by Google engineers
for use in their test suites; Gregory P. Smith, Michael Foord, and
GvR worked on merging them into Python’s version of [ unittest](../library/unittest.html#module-unittest).

- `assertIsNone()`- `assertIsNotNone()`- `None`.
- `assertIs()`- `assertIsNot()`- [bpo-2578](https://bugs.python.org/issue?@action=redirect&bpo=2578).)
- `assertIsInstance()`- `assertNotIsInstance()`- [bpo-7031](https://bugs.python.org/issue?@action=redirect&bpo=7031).)
- `assertGreater()`- `assertGreaterEqual()`- `assertLess()`- `assertLessEqual()`
- `assertMultiLineEqual()`- `assertEqual()`
- `assertRegexpMatches()`- `assertNotRegexpMatches()`- [bpo-8038](https://bugs.python.org/issue?@action=redirect&bpo=8038)).
- `assertRaisesRegexp()`
- `assertIn()`- `assertNotIn()`- *first*is or is not in- *second*.
- `assertItemsEqual()`
- `assertSetEqual()`
- Similarly, - `assertListEqual()`- `assertTupleEqual()`- `assertEqual()`- `assertSequenceEqual()`
- `assertDictEqual()`- `assertEqual()`- `assertDictContainsSubset()`checks whether all of the key/value pairs in- *first*are found in- *second*.
- `assertAlmostEqual()`- `assertNotAlmostEqual()`- *first*and- *second*are approximately equal. This method can either round their difference to an optionally specified number of- *places*(the default is 7) and compare it to zero, or require the difference to be smaller than a supplied- *delta*value.
- `loadTestsFromName()`- `suiteClass`- `TestLoader`- [bpo-6866](https://bugs.python.org/issue?@action=redirect&bpo=6866).)
- A new hook lets you extend the - `assertEqual()`- `addTypeEqualityFunc()`

[ unittest.main()](../library/unittest.html#unittest.main) now takes an optional 

`exit` argument.  If
false, `main()` doesn’t call [, allowing](../library/sys.html#sys.exit)

`sys.exit()``main()` to be used from the interactive interpreter.
(Contributed by J. Pablo Fernández; [bpo-3379](https://bugs.python.org/issue?@action=redirect&bpo=3379).)

[ TestResult](../library/unittest.html#unittest.TestResult) has new 

[and](../library/unittest.html#unittest.TestResult.startTestRun)

`startTestRun()`[methods that are called immediately before and after a test run. (Contributed by Robert Collins;](../library/unittest.html#unittest.TestResult.stopTestRun)

`stopTestRun()`[bpo-5728](https://bugs.python.org/issue?@action=redirect&bpo=5728).)

With all these changes, the `unittest.py` was becoming awkwardly
large, so the module was turned into a package and the code split into
several files (by Benjamin Peterson).  This doesn’t affect how the
module is imported or used.

See also

- [https://web.archive.org/web/20210619163128/http://www.voidspace.org.uk/python/articles/unittest2.shtml](https://web.archive.org/web/20210619163128/http://www.voidspace.org.uk/python/articles/unittest2.shtml)
- Describes the new features, how to use them, and the rationale for various design decisions. (By Michael Foord.) 

### Updated module: ElementTree 1.3[¶](#updated-module-elementtree-1-3)

The version of the ElementTree library included with Python was updated to version 1.3. Some of the new features are:

- The various parsing functions now take a - *parser*keyword argument giving an- `XMLParser`- p = ET.XMLParser(encoding='utf-8') t = ET.XML("""<root/>""", parser=p) - Errors in parsing XML now raise a - `ParseError`- `position`attribute containing a (- *line*,- *column*) tuple giving the location of the problem.
- ElementTree’s code for converting trees to a string has been significantly reworked, making it roughly twice as fast in many cases. The - `ElementTree.write()`- `Element.write()`methods now have a- *method*parameter that can be “xml” (the default), “html”, or “text”. HTML mode will output empty elements as- `<empty></empty>`instead of- `<empty/>`, and text mode will skip over elements and only output the text chunks. If you set the- `tag`- `None`but leave its children in place, the element will be omitted when the tree is written out, so you don’t need to do more extensive rearrangement to remove a single element.- Namespace handling has also been improved. All - `xmlns:<whatever>`declarations are now output on the root element, not scattered throughout the resulting XML. You can set the default namespace for a tree by setting the- `default_namespace`attribute and can register new prefixes with- `register_namespace()`- *xml_declaration*parameter to suppress the XML declaration.
- New - `Element`- `extend()`- from xml.etree import ElementTree as ET t = ET.XML("""<list> <item>1</item> <item>2</item> <item>3</item> </list>""") new = ET.XML('<root/>') new.extend(t) # Outputs <root><item>1</item>...</root> print ET.tostring(new) 
- New - `Element`- `iter()`- `for child in elem:`to loop over an element’s children. The existing method- `getiterator()`is now deprecated, as is- `getchildren()`which constructs and returns a list of children.
- New - `Element`- `itertext()`- t = ET.XML("""<list> <item>1</item> <item>2</item> <item>3</item> </list>""") # Outputs ['\n ', '1', ' ', '2', ' ', '3', '\n'] print list(t.itertext()) 
- Deprecated: using an element as a Boolean (i.e., - `if elem:`) would return true if the element had any children, or false if there were no children. This behaviour is confusing –- `None`is false, but so is a childless element? – so it will now trigger a- `FutureWarning`- `len(elem) != 0`if you’re interested in the number of children, or- `elem is not None`.

Fredrik Lundh develops ElementTree and produced the 1.3 version;
you can read his article describing 1.3 at
[https://web.archive.org/web/20200703234532/http://effbot.org/zone/elementtree-13-intro.htm](https://web.archive.org/web/20200703234532/http://effbot.org/zone/elementtree-13-intro.htm).
Florent Xicluna updated the version included with
Python, after discussions on python-dev and in [bpo-6472](https://bugs.python.org/issue?@action=redirect&bpo=6472).)

## Build and C API Changes[¶](#build-and-c-api-changes)

Changes to Python’s build process and to the C API include:

- The latest release of the GNU Debugger, GDB 7, can be - [scripted using Python](https://web.archive.org/web/20110715084810/http://sourceware.org/gdb/current/onlinedocs/gdb/Python.html). When you begin debugging an executable program P, GDB will look for a file named- `P-gdb.py`and automatically read it. Dave Malcolm contributed a- `python-gdb.py`that adds a number of commands useful when debugging Python itself. For example,- `py-up`and- `py-down`go up or down one Python stack frame, which usually corresponds to several C stack frames.- `py-print`prints the value of a Python variable, and- `py-bt`prints the Python stack trace. (Added as a result of- [bpo-8032](https://bugs.python.org/issue?@action=redirect&bpo=8032).)
- If you use the - `.gdbinit`file provided with Python, the “pyo” macro in the 2.7 version now works correctly when the thread being debugged doesn’t hold the GIL; the macro now acquires it before printing. (Contributed by Victor Stinner;- [bpo-3632](https://bugs.python.org/issue?@action=redirect&bpo=3632).)
- `Py_AddPendingCall()`- [bpo-4293](https://bugs.python.org/issue?@action=redirect&bpo=4293).)
- New function: - `PyCode_NewEmpty()`- `PyCode_New()`, which had many more arguments. (Added by Jeffrey Yasskin.)
- New function: - `PyErr_NewExceptionWithDoc()`- `PyErr_NewException()`- `char *`argument containing the docstring for the new exception class. (Added by ‘lekma’ on the Python bug tracker;- [bpo-7033](https://bugs.python.org/issue?@action=redirect&bpo=7033).)
- New function: - `PyFrame_GetLineNumber()`
- New functions: - `PyLong_AsLongAndOverflow()`- `PyLong_AsLongLongAndOverflow()`- *overflow*flag is set and returned to the caller. (Contributed by Case Van Horsen;- [bpo-7528](https://bugs.python.org/issue?@action=redirect&bpo=7528)and- [bpo-7767](https://bugs.python.org/issue?@action=redirect&bpo=7767).)
- New function: stemming from the rewrite of string-to-float conversion, a new - `PyOS_string_to_double()`- `PyOS_ascii_strtod()`and- `PyOS_ascii_atof()`functions are now deprecated.
- New function: - `PySys_SetArgvEx()`sets the value of- `sys.argv`and can optionally update- `sys.path`to include the directory containing the script named by- `sys.argv[0]`depending on the value of an- *updatepath*parameter.- This function was added to close a security hole for applications that embed Python. The old function, - `PySys_SetArgv()`, would always update- `sys.path`, and sometimes it would add the current directory. This meant that, if you ran an application embedding Python in a directory controlled by someone else, attackers could put a Trojan-horse module in the directory (say, a file named- `os.py`) that your application would then import and run.- If you maintain a C/C++ application that embeds Python, check whether you’re calling - `PySys_SetArgv()`and carefully consider whether the application should be using- `PySys_SetArgvEx()`with- *updatepath*set to false.- Security issue reported as - **CVE 2008-5983**- [bpo-5753](https://bugs.python.org/issue?@action=redirect&bpo=5753), and fixed by Antoine Pitrou.
- New macros: the Python header files now define the following macros: - `Py_ISALNUM`- `Py_ISALPHA`- `Py_ISDIGIT`- `Py_ISLOWER`- `Py_ISSPACE`- `Py_ISUPPER`- `Py_ISXDIGIT`- `Py_TOLOWER`- `Py_TOUPPER`- [bpo-5793](https://bugs.python.org/issue?@action=redirect&bpo=5793).)
- Removed function: - `PyEval_CallObject()`is now only available as a macro. A function version was being kept around to preserve ABI linking compatibility, but that was in 1997; it can certainly be deleted by now. (Removed by Antoine Pitrou;- [bpo-8276](https://bugs.python.org/issue?@action=redirect&bpo=8276).)
- New format codes: the - `PyString_FromFormat()`,- `PyString_FromFormatV()`, and- `PyErr_Format()`- `%lld`and- `%llu`format codes for displaying C’s long long types. (Contributed by Mark Dickinson;- [bpo-7228](https://bugs.python.org/issue?@action=redirect&bpo=7228).)
- The complicated interaction between threads and process forking has been changed. Previously, the child process created by - `os.fork()`- `os.fork()`. If other threads were holding a lock, such as Python’s import lock, when the fork was performed, the lock would still be marked as “held” in the new process. But in the child process nothing would ever release the lock, since the other threads weren’t replicated, and the child process would no longer be able to perform imports.- Python 2.7 acquires the import lock before performing an - `os.fork()`- `threading`- `fork()`themselves, will not benefit from this clean-up.- (Fixed by Thomas Wouters; - [bpo-1590864](https://bugs.python.org/issue?@action=redirect&bpo=1590864).)
- The - `Py_Finalize()`- `threading._shutdown()`function; this prevents some exceptions from being raised when an interpreter shuts down. (Patch by Adam Olsen;- [bpo-1722344](https://bugs.python.org/issue?@action=redirect&bpo=1722344).)
- When using the - `PyMemberDef`- `T_STRING_INPLACE`attribute.
- Global symbols defined by the - `ctypes`- `Py`, or with- `_ctypes`. (Implemented by Thomas Heller;- [bpo-3102](https://bugs.python.org/issue?@action=redirect&bpo=3102).)
- New configure option: the - `--with-system-expat`switch allows building the- `pyexpat`- [bpo-7609](https://bugs.python.org/issue?@action=redirect&bpo=7609).)
- New configure option: the - `--with-valgrind`option will now disable the pymalloc allocator, which is difficult for the Valgrind memory-error detector to analyze correctly. Valgrind will therefore be better at detecting memory leaks and overruns. (Contributed by James Henstridge;- [bpo-2422](https://bugs.python.org/issue?@action=redirect&bpo=2422).)
- New configure option: you can now supply an empty string to - `--with-dbmliborder=`in order to disable all of the various DBM modules. (Added by Arfrever Frehtes Taifersar Arahesis;- [bpo-6491](https://bugs.python.org/issue?@action=redirect&bpo=6491).)
- The - **configure**script now checks for floating-point rounding bugs on certain 32-bit Intel chips and defines a- `X87_DOUBLE_ROUNDING`preprocessor definition. No code currently uses this definition, but it’s available if anyone wishes to use it. (Added by Mark Dickinson;- [bpo-2937](https://bugs.python.org/issue?@action=redirect&bpo=2937).)- **configure**also now sets a- `LDCXXSHARED`Makefile variable for supporting C++ linking. (Contributed by Arfrever Frehtes Taifersar Arahesis;- [bpo-1222585](https://bugs.python.org/issue?@action=redirect&bpo=1222585).)
- The build process now creates the necessary files for pkg-config support. (Contributed by Clinton Roy; - [bpo-3585](https://bugs.python.org/issue?@action=redirect&bpo=3585).)
- The build process now supports Subversion 1.7. (Contributed by Arfrever Frehtes Taifersar Arahesis; - [bpo-6094](https://bugs.python.org/issue?@action=redirect&bpo=6094).)

### Capsules[¶](#capsules)

Python 3.1 adds a new C datatype, [ PyCapsule](../c-api/capsule.html#c.PyCapsule), for providing a
C API to an extension module.  A capsule is essentially the holder of
a C 

`void *` pointer, and is made available as a module attribute; for
example, the [module’s API is exposed as](../library/socket.html#module-socket)

`socket``socket.CAPI`,
and [exposes](../library/unicodedata.html#module-unicodedata)

`unicodedata``ucnhash_CAPI`.  Other extensions
can import the module, access its dictionary to get the capsule
object, and then get the `void *` pointer, which will usually point
to an array of pointers to the module’s various API functions.There is an existing data type already used for this,
`PyCObject`, but it doesn’t provide type safety.  Evil code
written in pure Python could cause a segmentation fault by taking a
`PyCObject` from module A and somehow substituting it for the
`PyCObject` in module B.   Capsules know their own name,
and getting the pointer requires providing the name:

```
void *vtable;
if (!PyCapsule_IsValid(capsule, "mymodule.CAPI") {
        PyErr_SetString(PyExc_ValueError, "argument type invalid");
        return NULL;
}
vtable = PyCapsule_GetPointer(capsule, "mymodule.CAPI");
```
You are assured that `vtable` points to whatever you’re expecting.
If a different capsule was passed in, [ PyCapsule_IsValid()](../c-api/capsule.html#c.PyCapsule_IsValid) would
detect the mismatched name and return false.  Refer to

[Providing a C API for an Extension Module](../extending/extending.html#using-capsules)for more information on using these objects.

Python 2.7 now uses capsules internally to provide various
extension-module APIs, but the `PyCObject_AsVoidPtr()` was
modified to handle capsules, preserving compile-time compatibility
with the `PyCObject` interface.  Use of
`PyCObject_AsVoidPtr()` will signal a
[ PendingDeprecationWarning](../library/exceptions.html#PendingDeprecationWarning), which is silent by default.

Implemented in Python 3.1 and backported to 2.7 by Larry Hastings;
discussed in [bpo-5630](https://bugs.python.org/issue?@action=redirect&bpo=5630).

### Port-Specific Changes: Windows[¶](#port-specific-changes-windows)

- The - `msvcrt`- `crtassem.h`header file:- `CRT_ASSEMBLY_VERSION`- `VC_ASSEMBLY_PUBLICKEYTOKEN`- `LIBRARIES_ASSEMBLY_NAME_PREFIX`- [bpo-4365](https://bugs.python.org/issue?@action=redirect&bpo=4365).)
- The - `_winreg`- `CreateKeyEx()`- `DeleteKeyEx()`- `DisableReflectionKey()`- `EnableReflectionKey()`- `QueryReflectionKey()`- [bpo-7347](https://bugs.python.org/issue?@action=redirect&bpo=7347).)
- The new - `_beginthreadex()`API is used to start threads, and the native thread-local storage functions are now used. (Contributed by Kristján Valur Jónsson;- [bpo-3582](https://bugs.python.org/issue?@action=redirect&bpo=3582).)
- The - `os.kill()`- `CTRL_C_EVENT`- `CTRL_BREAK_EVENT`- `Control`-- `C`and- `Control`-- `Break`keystroke events to subprocesses; any other value will use the- `TerminateProcess()`API. (Contributed by Miki Tebeka;- [bpo-1220212](https://bugs.python.org/issue?@action=redirect&bpo=1220212).)
- The - `os.listdir()`- [bpo-5913](https://bugs.python.org/issue?@action=redirect&bpo=5913).)
- The - `mimetypes`- [bpo-4969](https://bugs.python.org/issue?@action=redirect&bpo=4969).)

### Port-Specific Changes: Mac OS X[¶](#port-specific-changes-mac-os-x)

- The path - `/Library/Python/2.7/site-packages`is now appended to- `sys.path`, in order to share added packages between the system installation and a user-installed copy of the same version. (Changed by Ronald Oussoren;- [bpo-4865](https://bugs.python.org/issue?@action=redirect&bpo=4865).)- Changed in version 2.7.13: As of 2.7.13, this change was removed. - `/Library/Python/2.7/site-packages`, the site-packages directory used by the Apple-supplied system Python 2.7 is no longer appended to- `sys.path`for user-installed Pythons such as from the python.org installers. As of macOS 10.12, Apple changed how the system site-packages directory is configured, which could cause installation of pip components, like setuptools, to fail. Packages installed for the system Python will no longer be shared with user-installed Pythons. (- [bpo-28440](https://bugs.python.org/issue?@action=redirect&bpo=28440))

### Port-Specific Changes: FreeBSD[¶](#port-specific-changes-freebsd)

- FreeBSD 7.1’s - `SO_SETFIB`constant, used with the- `socket()`- `getsockopt()`- `setsockopt()`- `socket`- [bpo-8235](https://bugs.python.org/issue?@action=redirect&bpo=8235).)

## Other Changes and Fixes[¶](#other-changes-and-fixes)

- Two benchmark scripts, - `iobench`and- `ccbench`, were added to the- `Tools`directory.- `iobench`measures the speed of the built-in file I/O objects returned by- `open()`- `ccbench`is a concurrency benchmark that tries to measure computing throughput, thread switching latency, and IO processing bandwidth when performing several tasks using a varying number of threads.
- The - `Tools/i18n/msgfmt.py`script now understands plural forms in- `.po`files. (Fixed by Martin von Löwis;- [bpo-5464](https://bugs.python.org/issue?@action=redirect&bpo=5464).)
- When importing a module from a - `.pyc`or- `.pyo`file with an existing- `.py`counterpart, the- `co_filename`- [bpo-1180193](https://bugs.python.org/issue?@action=redirect&bpo=1180193).)
- The - `regrtest.py`script now takes a- `--randseed=`switch that takes an integer that will be used as the random seed for the- `-r`option that executes tests in random order. The- `-r`option also reports the seed that was used (Added by Collin Winter.)
- Another - `regrtest.py`switch is- `-j`, which takes an integer specifying how many tests run in parallel. This allows reducing the total runtime on multi-core machines. This option is compatible with several other options, including the- `-R`switch which is known to produce long runtimes. (Added by Antoine Pitrou,- [bpo-6152](https://bugs.python.org/issue?@action=redirect&bpo=6152).) This can also be used with a new- `-F`switch that runs selected tests in a loop until they fail. (Added by Antoine Pitrou;- [bpo-7312](https://bugs.python.org/issue?@action=redirect&bpo=7312).)
- When executed as a script, the - `py_compile.py`module now accepts- `'-'`as an argument, which will read standard input for the list of filenames to be compiled. (Contributed by Piotr Ożarowski;- [bpo-8233](https://bugs.python.org/issue?@action=redirect&bpo=8233).)

## Porting to Python 2.7[¶](#porting-to-python-2-7)

This section lists previously described changes and other bugfixes that may require changes to your code:

- The - `range()`- `__int__()`- [bpo-1533](https://bugs.python.org/issue?@action=redirect&bpo=1533).)
- The string - `format()`- `str()`- [bpo-5920](https://bugs.python.org/issue?@action=redirect&bpo=5920).)
- Because of an optimization for the - `with`- `__enter__()`- `__exit__()`- `object`- [bpo-6101](https://bugs.python.org/issue?@action=redirect&bpo=6101).)
- Due to a bug in Python 2.6, the - *exc_value*parameter to- `__exit__()`- *exc_value*will be an instance as expected. (Fixed by Florent Xicluna;- [bpo-7853](https://bugs.python.org/issue?@action=redirect&bpo=7853).)
- When a restricted set of attributes were set using - `__slots__`, deleting an unset attribute would not raise- `AttributeError`- [bpo-7604](https://bugs.python.org/issue?@action=redirect&bpo=7604).)

In the standard library:

- Operations with - `datetime`- `OverflowError`- [bpo-7150](https://bugs.python.org/issue?@action=redirect&bpo=7150).)
- When using - `Decimal`- `format()`- [bpo-6857](https://bugs.python.org/issue?@action=redirect&bpo=6857).)- Comparisons involving a signaling NaN value (or - `sNAN`) now signal- `InvalidOperation`- `NaN`) are now hashable. (Fixed by Mark Dickinson;- [bpo-7279](https://bugs.python.org/issue?@action=redirect&bpo=7279).)
- The - `xml.etree.ElementTree`- `<?xml-stylesheet href="#style1"?>`) or comment (which looks like- `<!-- comment -->`). (Patch by Neil Muller;- [bpo-2746](https://bugs.python.org/issue?@action=redirect&bpo=2746).)
- The - `readline()`method of- `StringIO`- [bpo-7348](https://bugs.python.org/issue?@action=redirect&bpo=7348)).
- The - `syslog`- `sys.argv[0]`as the identifier instead of the previous default value of- `'python'`. (Changed by Sean Reifschneider;- [bpo-8451](https://bugs.python.org/issue?@action=redirect&bpo=8451).)
- The - `tarfile`- [bpo-7357](https://bugs.python.org/issue?@action=redirect&bpo=7357).)
- The - `urlparse`- `urlsplit()`- **RFC 3986**- `"<something>://..."`, the text before the- `://`is treated as the scheme, even if it’s a made-up scheme that the module doesn’t know about. This change may break code that worked around the old behaviour. For example, Python 2.6.4 or 2.5 will return the following:- >>> import urlparse >>> urlparse.urlsplit('invented://host/filename?query') ('invented', '', '//host/filename?query', '', '') - Python 2.7 (and Python 2.6.5) will return: - >>> import urlparse >>> urlparse.urlsplit('invented://host/filename?query') ('invented', 'host', '/filename?query', '', '') - (Python 2.7 actually produces slightly different output, since it returns a named tuple instead of a standard tuple.) 

For C extensions:

- C extensions that use integer format codes with the - `PyArg_Parse*`family of functions will now raise a- `TypeError`- `DeprecationWarning`- [bpo-5080](https://bugs.python.org/issue?@action=redirect&bpo=5080)).
- Use the new - `PyOS_string_to_double()`- `PyOS_ascii_strtod()`and- `PyOS_ascii_atof()`functions, which are now deprecated.

For applications that embed Python:

- The - `PySys_SetArgvEx()`function was added, letting applications close a security hole when the existing- `PySys_SetArgv()`function was used. Check whether you’re calling- `PySys_SetArgv()`and carefully consider whether the application should be using- `PySys_SetArgvEx()`with- *updatepath*set to false.

## New Features Added to Python 2.7 Maintenance Releases[¶](#new-features-added-to-python-2-7-maintenance-releases)

New features may be added to Python 2.7 maintenance releases when the situation genuinely calls for it. Any such additions must go through the Python Enhancement Proposal process, and make a compelling case for why they can’t be adequately addressed by either adding the new feature solely to Python 3, or else by publishing it on the Python Package Index.

In addition to the specific proposals listed below, there is a general
exemption allowing new `-3` warnings to be added in any Python 2.7
maintenance release.

### Two new environment variables for debug mode[¶](#two-new-environment-variables-for-debug-mode)

In debug mode, the `[xxx refs]` statistic is not written by default, the
`PYTHONSHOWREFCOUNT` environment variable now must also be set.
(Contributed by Victor Stinner; [bpo-31733](https://bugs.python.org/issue?@action=redirect&bpo=31733).)

When Python is compiled with `COUNT_ALLOC` defined, allocation counts are no
longer dumped by default anymore: the `PYTHONSHOWALLOCCOUNT` environment
variable must now also be set. Moreover, allocation counts are now dumped into
stderr, rather than stdout. (Contributed by Victor Stinner; [bpo-31692](https://bugs.python.org/issue?@action=redirect&bpo=31692).)

Added in version 2.7.15.

### PEP 434: IDLE Enhancement Exception for All Branches[¶](#pep-434-idle-enhancement-exception-for-all-branches)

[ PEP 434](https://peps.python.org/pep-0434/) describes a general exemption for changes made to the IDLE
development environment shipped along with Python. This exemption makes it
possible for the IDLE developers to provide a more consistent user
experience across all supported versions of Python 2 and 3.

For details of any IDLE changes, refer to the NEWS file for the specific release.

### PEP 466: Network Security Enhancements for Python 2.7[¶](#pep-466-network-security-enhancements-for-python-2-7)

[ PEP 466](https://peps.python.org/pep-0466/) describes a number of network security enhancement proposals
that have been approved for inclusion in Python 2.7 maintenance releases,
with the first of those changes appearing in the Python 2.7.7 release.

[ PEP 466](https://peps.python.org/pep-0466/) related features added in Python 2.7.7:

- `hmac.compare_digest()`- [bpo-21306](https://bugs.python.org/issue?@action=redirect&bpo=21306).)
- OpenSSL 1.0.1g was upgraded in the official Windows installers published on python.org. (Contributed by Zachary Ware; - [bpo-21462](https://bugs.python.org/issue?@action=redirect&bpo=21462).)

[ PEP 466](https://peps.python.org/pep-0466/) related features added in Python 2.7.8:

- `hashlib.pbkdf2_hmac()`- [bpo-21304](https://bugs.python.org/issue?@action=redirect&bpo=21304).)
- OpenSSL 1.0.1h was upgraded for the official Windows installers published on python.org. (Contributed by Zachary Ware in - [bpo-21671](https://bugs.python.org/issue?@action=redirect&bpo=21671)for- **CVE 2014-0224**

[ PEP 466](https://peps.python.org/pep-0466/) related features added in Python 2.7.9:

- Most of Python 3.4’s - `ssl`- `ssl`now supports Server Name Indication, TLS1.x settings, access to the platform certificate store, the- `SSLContext`- [bpo-21308](https://bugs.python.org/issue?@action=redirect&bpo=21308).)- Refer to the “Version added: 2.7.9” notes in the module documentation for specific details. 
- `os.urandom()`- `/dev/urandom`instead of reopening- `/dev/urandom`on every call. (Contributed by Alex Gaynor;- [bpo-21305](https://bugs.python.org/issue?@action=redirect&bpo=21305).)
- `hashlib.algorithms_guaranteed`- `hashlib.algorithms_available`- [bpo-21307](https://bugs.python.org/issue?@action=redirect&bpo=21307))

### PEP 477: Backport ensurepip (PEP 453) to Python 2.7[¶](#pep-477-backport-ensurepip-pep-453-to-python-2-7)

[ PEP 477](https://peps.python.org/pep-0477/) approves the inclusion of the 

[ensurepip module and the improved documentation that was enabled by it in the Python 2.7 maintenance releases, appearing first in the Python 2.7.9 release.](https://peps.python.org/pep-0453/)

**PEP 453**#### Bootstrapping pip By Default[¶](#bootstrapping-pip-by-default)

The new [ ensurepip](../library/ensurepip.html#module-ensurepip) module (defined in 

[) provides a standard cross-platform mechanism to bootstrap the pip installer into Python installations. The version of](https://peps.python.org/pep-0453/)

**PEP 453**`pip` included with Python 2.7.9 is `pip`
1.5.6, and future 2.7.x maintenance releases will update the bundled version to
the latest version of `pip` that is available at the time of creating the
release candidate.By default, the commands `pip`, `pipX` and `pipX.Y` will be installed on
all platforms (where X.Y stands for the version of the Python installation),
along with the `pip` Python package and its dependencies.

For CPython [source builds on POSIX systems](../using/unix.html#building-python-on-unix),
the `make install` and `make altinstall` commands do not bootstrap `pip`
by default.  This behaviour can be controlled through configure options, and
overridden through Makefile options.

On Windows and Mac OS X, the CPython installers now default to installing
`pip` along with CPython itself (users may opt out of installing it
during the installation process). Window users will need to opt in to the
automatic `PATH` modifications to have `pip` available from the command
line by default, otherwise it can still be accessed through the Python
launcher for Windows as `py -m pip`.

As [ discussed in the PEP](https://peps.python.org/pep-0477/#disabling-ensurepip-by-downstream-distributors),
platform packagers may choose not to install
these commands by default, as long as, when invoked, they provide clear and
simple directions on how to install them on that platform (usually using
the system package manager).

#### Documentation Changes[¶](#documentation-changes)

As part of this change, the [Installing Python modules](../installing/index.html#installing-index) and
[Distributing Python Modules](../distributing/index.html#distributing-index) sections of the documentation have been
completely redesigned as short getting started and FAQ documents. Most
packaging documentation has now been moved out to the Python Packaging
Authority maintained [Python Packaging User Guide](https://packaging.python.org) and the documentation of the individual
projects.

However, as this migration is currently still incomplete, the legacy
versions of those guides remaining available as [Building C and C++ Extensions with setuptools](../extending/building.html#install-index)
and [Building C and C++ Extensions with setuptools](../extending/building.html#setuptools-index).

See also

- **PEP 453**
- PEP written by Donald Stufft and Nick Coghlan, implemented by Donald Stufft, Nick Coghlan, Martin von Löwis and Ned Deily. 

### PEP 476: Enabling certificate verification by default for stdlib http clients[¶](#pep-476-enabling-certificate-verification-by-default-for-stdlib-http-clients)

[ PEP 476](https://peps.python.org/pep-0476/) updated 

[and modules which use it, such as](../library/http.html#module-http)

`httplib`[and](../library/urllib.request.html#module-urllib.request)

`urllib2`[, to now verify that the server presents a certificate which is signed by a Certificate Authority in the platform trust store and whose hostname matches the hostname being requested by default, significantly improving security for many applications. This change was made in the Python 2.7.9 release.](../library/xmlrpc.client.html#module-xmlrpc.client)

`xmlrpclib`For applications which require the old previous behavior, they can pass an alternate context:

```
import urllib2
import ssl
# This disables all verification
context = ssl._create_unverified_context()
# This allows using a specific certificate for the host, which doesn't need
# to be in the trust store
context = ssl.create_default_context(cafile="/path/to/file.crt")
urllib2.urlopen("https://invalid-cert", context=context)
```
### PEP 493: HTTPS verification migration tools for Python 2.7[¶](#pep-493-https-verification-migration-tools-for-python-2-7)

[ PEP 493](https://peps.python.org/pep-0493/) provides additional migration tools to support a more incremental
infrastructure upgrade process for environments containing applications and
services relying on the historically permissive processing of server
certificates when establishing client HTTPS connections.  These additions were
made in the Python 2.7.12 release.

These tools are intended for use in cases where affected applications and services can’t be modified to explicitly pass a more permissive SSL context when establishing the connection.

For applications and services which can’t be modified at all, the new
`PYTHONHTTPSVERIFY` environment variable may be set to `0` to revert an
entire Python process back to the default permissive behaviour of Python 2.7.8
and earlier.

For cases where the connection establishment code can’t be modified, but the
overall application can be, the new `ssl._https_verify_certificates()`
function can be used to adjust the default behaviour at runtime.

### New `make regen-all` build target[¶](#new-make-regen-all-build-target)

To simplify cross-compilation, and to ensure that CPython can reliably be compiled without requiring an existing version of Python to already be available, the autotools-based build system no longer attempts to implicitly recompile generated files based on file modification times.

Instead, a new `make regen-all` command has been added to force regeneration
of these files when desired (e.g. after an initial version of Python has
already been built based on the pregenerated versions).

More selective regeneration targets are also defined - see
[Makefile.pre.in](https://github.com/python/cpython/tree/3.14/Makefile.pre.in) for details.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 2.7.14.

### Removal of `make touch` build target[¶](#removal-of-make-touch-build-target)

The `make touch` build target previously used to request implicit regeneration
of generated files by updating their modification times has been removed.

It has been replaced by the new `make regen-all` target.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 2.7.14.

## Acknowledgements[¶](#acknowledgements)

The author would like to thank the following people for offering suggestions, corrections and assistance with various drafts of this article: Nick Coghlan, Philip Jenvey, Ryan Lovett, R. David Murray, Hugh Secker-Walker.