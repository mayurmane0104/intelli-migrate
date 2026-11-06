# pprint — Data pretty printer — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/pprint.html](https://docs.python.org/3.13/library/pprint.html)

---

`pprint` — Data pretty printer[¶](#module-pprint)

**Source code:** [Lib/pprint.py](https://github.com/python/cpython/tree/3.13/Lib/pprint.py)

The `pprint` module provides a capability to “pretty-print” arbitrary
Python data structures in a form which can be used as input to the interpreter.
If the formatted structures include objects which are not fundamental Python
types, the representation may not be loadable.  This may be the case if objects
such as files, sockets or classes are included, as well as many other
objects which are not representable as Python literals.

The formatted representation keeps objects on a single line if it can, and
breaks them onto multiple lines if they don’t fit within the allowed width,
adjustable by the *width* parameter defaulting to 80 characters.

Changed in version 3.9: Added support for pretty-printing [ types.SimpleNamespace](types.html#types.SimpleNamespace).

Changed in version 3.10: Added support for pretty-printing [ dataclasses.dataclass](dataclasses.html#dataclasses.dataclass).

## Functions[¶](#functions)

- 
pprint.pp(*object*,*stream=None*,*indent=1*,*width=80*,*depth=None*,***,*compact=False*,*sort_dicts=False*,*underscore_numbers=False*)[¶](#pprint.pp)
- Prints the formatted representation of - *object*, followed by a newline. This function may be used in the interactive interpreter instead of the- `print()`- `print = pprint.pp`for use within a scope.- Parameters:
- **object**– The object to be printed.
- **stream**(- [file-like object](../glossary.html#term-file-like-object)| None) – A file-like object to which the output will be written by calling its- `write()`method. If- `None`(the default),- `sys.stdout`
- **indent**(- *int*
- **width**(- *int*
- **depth**(- *int*- *|*- *None*) – The number of nesting levels which may be printed. If the data structure being printed is too deep, the next contained level is replaced by- `...`. If- `None`(the default), there is no constraint on the depth of the objects being formatted.
- **compact**(- *bool*- [sequences](../glossary.html#term-sequence)are formatted. If- `False`(the default), each item of a sequence will be formatted on a separate line, otherwise as many items as will fit within the- *width*will be formatted on each output line.
- **sort_dicts**(- *bool*- `True`, dictionaries will be formatted with their keys sorted, otherwise they will be displayed in insertion order (the default).
- **underscore_numbers**(- *bool*- `True`, integers will be formatted with the- `_`character for a thousands separator, otherwise underscores are not displayed (the default).
 
 - >>> import pprint >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni'] >>> stuff.insert(0, stuff) >>> pprint.pp(stuff) [<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni'] - Added in version 3.8. 

- 
pprint.pprint(*object*,*stream=None*,*indent=1*,*width=80*,*depth=None*,***,*compact=False*,*sort_dicts=True*,*underscore_numbers=False*)[¶](#pprint.pprint)
- Alias for - `pp()`- *sort_dicts*set to- `True`by default, which would automatically sort the dictionaries’ keys, you might want to use- `pp()`instead where it is- `False`by default.

- 
pprint.pformat(*object*,*indent=1*,*width=80*,*depth=None*,***,*compact=False*,*sort_dicts=True*,*underscore_numbers=False*)[¶](#pprint.pformat)
- Return the formatted representation of - *object*as a string.- *indent*,- *width*,- *depth*,- *compact*,- *sort_dicts*and- *underscore_numbers*are passed to the- `PrettyPrinter`

- 
pprint.isreadable(*object*)[¶](#pprint.isreadable)
- Determine if the formatted representation of - *object*is “readable”, or can be used to reconstruct the value using- `eval()`- `False`for recursive objects.- >>> pprint.isreadable(stuff) False 

- 
pprint.isrecursive(*object*)[¶](#pprint.isrecursive)
- Determine if - *object*requires a recursive representation. This function is subject to the same limitations as noted in- `saferepr()`- `RecursionError`

- 
pprint.saferepr(*object*)[¶](#pprint.saferepr)
- Return a string representation of - *object*, protected against recursion in some common data structures, namely instances of- `dict`- `list`- `tuple`- `__repr__`has not been overridden. If the representation of object exposes a recursive entry, the recursive reference will be represented as- `<Recursion on typename with id=number>`. The representation is not otherwise formatted.- >>> pprint.saferepr(stuff) "[<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']" 

## PrettyPrinter Objects[¶](#prettyprinter-objects)

- 
*class*pprint.PrettyPrinter(*indent=1*,*width=80*,*depth=None*,*stream=None*,***,*compact=False*,*sort_dicts=True*,*underscore_numbers=False*)[¶](#pprint.PrettyPrinter)
- Construct a - `PrettyPrinter`instance.- Arguments have the same meaning as for - `pp()`- *sort_dicts*defaults to- `True`.- >>> import pprint >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni'] >>> stuff.insert(0, stuff[:]) >>> pp = pprint.PrettyPrinter(indent=4) >>> pp.pprint(stuff) [ ['spam', 'eggs', 'lumberjack', 'knights', 'ni'], 'spam', 'eggs', 'lumberjack', 'knights', 'ni'] >>> pp = pprint.PrettyPrinter(width=41, compact=True) >>> pp.pprint(stuff) [['spam', 'eggs', 'lumberjack', 'knights', 'ni'], 'spam', 'eggs', 'lumberjack', 'knights', 'ni'] >>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ... ('parrot', ('fresh fruit',)))))))) >>> pp = pprint.PrettyPrinter(depth=6) >>> pp.pprint(tup) ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...))))))) - Changed in version 3.4: Added the - *compact*parameter.- Changed in version 3.8: Added the - *sort_dicts*parameter.- Changed in version 3.10: Added the - *underscore_numbers*parameter.- Changed in version 3.11: No longer attempts to write to - `sys.stdout`if it is- `None`.

[ PrettyPrinter](#pprint.PrettyPrinter) instances have the following methods:

- 
PrettyPrinter.pformat(*object*)[¶](#pprint.PrettyPrinter.pformat)
- Return the formatted representation of - *object*. This takes into account the options passed to the- `PrettyPrinter`

- 
PrettyPrinter.pprint(*object*)[¶](#pprint.PrettyPrinter.pprint)
- Print the formatted representation of - *object*on the configured stream, followed by a newline.

The following methods provide the implementations for the corresponding
functions of the same names.  Using these methods on an instance is slightly
more efficient since new [ PrettyPrinter](#pprint.PrettyPrinter) objects don’t need to be
created.

- 
PrettyPrinter.isreadable(*object*)[¶](#pprint.PrettyPrinter.isreadable)
- Determine if the formatted representation of the object is “readable,” or can be used to reconstruct the value using - `eval()`- `False`for recursive objects. If the- *depth*parameter of the- `PrettyPrinter`- `False`.

- 
PrettyPrinter.isrecursive(*object*)[¶](#pprint.PrettyPrinter.isrecursive)
- Determine if the object requires a recursive representation. 

This method is provided as a hook to allow subclasses to modify the way objects
are converted to strings.  The default implementation uses the internals of the
[ saferepr()](#pprint.saferepr) implementation.

- 
PrettyPrinter.format(*object*,*context*,*maxlevels*,*level*)[¶](#pprint.PrettyPrinter.format)
- Returns three values: the formatted version of - *object*as a string, a flag indicating whether the result is readable, and a flag indicating whether recursion was detected. The first argument is the object to be presented. The second is a dictionary which contains the- `id()`- *object*that are affecting the presentation) as the keys; if an object needs to be presented which is already represented in- *context*, the third return value should be- `True`. Recursive calls to the- `format()`method should add additional entries for containers to this dictionary. The third argument,- *maxlevels*, gives the requested limit to recursion; this will be- `0`if there is no requested limit. This argument should be passed unmodified to recursive calls. The fourth argument,- *level*, gives the current level; recursive calls should be passed a value less than that of the current call.

## Example[¶](#example)

To demonstrate several uses of the [ pp()](#pprint.pp) function and its parameters,
let’s fetch information about a project from 

[PyPI](https://pypi.org):

```
>>> import json
>>> import pprint
>>> from urllib.request import urlopen
>>> with urlopen('https://pypi.org/pypi/sampleproject/1.2.0/json') as resp:
...     project_info = json.load(resp)['info']
```
In its basic form, [ pp()](#pprint.pp) shows the whole object:

```
>>> pprint.pp(project_info)
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': ['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Software Development :: Build Tools'],
 'description': 'A sample Python project\n'
                '=======================\n'
                '\n'
                'This is the description file for the project.\n'
                '\n'
                'The file should use UTF-8 encoding and be written using '
                'ReStructured Text. It\n'
                'will be used to generate the project webpage on PyPI, and '
                'should be written for\n'
                'that purpose.\n'
                '\n'
                'Typical contents for this file would include an overview of '
                'the project, basic\n'
                'usage examples, etc. Generally, including the project '
                'changelog in here is not\n'
                'a good idea, although a simple "What\'s New" section for the '
                'most recent version\n'
                'may be appropriate.',
 'description_content_type': None,
 'docs_url': None,
 'download_url': 'UNKNOWN',
 'downloads': {'last_day': -1, 'last_month': -1, 'last_week': -1},
 'home_page': 'https://github.com/pypa/sampleproject',
 'keywords': 'sample setuptools development',
 'license': 'MIT',
 'maintainer': None,
 'maintainer_email': None,
 'name': 'sampleproject',
 'package_url': 'https://pypi.org/project/sampleproject/',
 'platform': 'UNKNOWN',
 'project_url': 'https://pypi.org/project/sampleproject/',
 'project_urls': {'Download': 'UNKNOWN',
                  'Homepage': 'https://github.com/pypa/sampleproject'},
 'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
 'requires_dist': None,
 'requires_python': None,
 'summary': 'A sample Python project',
 'version': '1.2.0'}
```
The result can be limited to a certain *depth* (ellipsis is used for deeper
contents):

```
>>> pprint.pp(project_info, depth=1)
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': [...],
 'description': 'A sample Python project\n'
                '=======================\n'
                '\n'
                'This is the description file for the project.\n'
                '\n'
                'The file should use UTF-8 encoding and be written using '
                'ReStructured Text. It\n'
                'will be used to generate the project webpage on PyPI, and '
                'should be written for\n'
                'that purpose.\n'
                '\n'
                'Typical contents for this file would include an overview of '
                'the project, basic\n'
                'usage examples, etc. Generally, including the project '
                'changelog in here is not\n'
                'a good idea, although a simple "What\'s New" section for the '
                'most recent version\n'
                'may be appropriate.',
 'description_content_type': None,
 'docs_url': None,
 'download_url': 'UNKNOWN',
 'downloads': {...},
 'home_page': 'https://github.com/pypa/sampleproject',
 'keywords': 'sample setuptools development',
 'license': 'MIT',
 'maintainer': None,
 'maintainer_email': None,
 'name': 'sampleproject',
 'package_url': 'https://pypi.org/project/sampleproject/',
 'platform': 'UNKNOWN',
 'project_url': 'https://pypi.org/project/sampleproject/',
 'project_urls': {...},
 'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
 'requires_dist': None,
 'requires_python': None,
 'summary': 'A sample Python project',
 'version': '1.2.0'}
```
Additionally, maximum character *width* can be suggested. If a long object
cannot be split, the specified width will be exceeded:

```
>>> pprint.pp(project_info, depth=1, width=60)
{'author': 'The Python Packaging Authority',
 'author_email': 'pypa-dev@googlegroups.com',
 'bugtrack_url': None,
 'classifiers': [...],
 'description': 'A sample Python project\n'
                '=======================\n'
                '\n'
                'This is the description file for the '
                'project.\n'
                '\n'
                'The file should use UTF-8 encoding and be '
                'written using ReStructured Text. It\n'
                'will be used to generate the project '
                'webpage on PyPI, and should be written '
                'for\n'
                'that purpose.\n'
                '\n'
                'Typical contents for this file would '
                'include an overview of the project, '
                'basic\n'
                'usage examples, etc. Generally, including '
                'the project changelog in here is not\n'
                'a good idea, although a simple "What\'s '
                'New" section for the most recent version\n'
                'may be appropriate.',
 'description_content_type': None,
 'docs_url': None,
 'download_url': 'UNKNOWN',
 'downloads': {...},
 'home_page': 'https://github.com/pypa/sampleproject',
 'keywords': 'sample setuptools development',
 'license': 'MIT',
 'maintainer': None,
 'maintainer_email': None,
 'name': 'sampleproject',
 'package_url': 'https://pypi.org/project/sampleproject/',
 'platform': 'UNKNOWN',
 'project_url': 'https://pypi.org/project/sampleproject/',
 'project_urls': {...},
 'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
 'requires_dist': None,
 'requires_python': None,
 'summary': 'A sample Python project',
 'version': '1.2.0'}
```