# fnmatch — Unix filename pattern matching — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/fnmatch.html](https://docs.python.org/3.13/library/fnmatch.html)

---

`fnmatch` — Unix filename pattern matching[¶](#module-fnmatch)

**Source code:** [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.13/Lib/fnmatch.py)

This module provides support for Unix shell-style wildcards, which are *not* the
same as regular expressions (which are documented in the [ re](re.html#module-re) module).  The
special characters used in shell-style wildcards are:

| Pattern | Meaning | 
|---|---|
| 
 | matches everything | 
| 
 | matches any single character | 
| 
 | matches any character in  | 
| 
 | matches any character not in  | 

For a literal match, wrap the meta-characters in brackets.
For example, `'[?]'` matches the character `'?'`.

Note that the filename separator (`'/'` on Unix) is *not* special to this
module.  See module [ glob](glob.html#module-glob) for pathname expansion (

`glob` uses
[to match pathname segments). Similarly, filenames starting with a period are not special for this module, and are matched by the](#fnmatch.filter)

`filter()``*` and `?`
patterns.Unless stated otherwise, “filename string” and “pattern string” either refer to
[ str](stdtypes.html#str) or 

`ISO-8859-1` encoded [objects. Note that the functions documented below do not allow to mix a](stdtypes.html#bytes)

`bytes``bytes` pattern with
a `str` filename, and vice-versa.Finally, note that [ functools.lru_cache()](functools.html#functools.lru_cache) with a 

*maxsize*of 32768 is used to cache the (typed) compiled regex patterns in the following functions:

[,](#module-fnmatch)

`fnmatch()`[,](#fnmatch.fnmatchcase)

`fnmatchcase()`[.](#fnmatch.filter)

`filter()`- 
fnmatch.fnmatch(*name*,*pat*)[¶](#fnmatch.fnmatch)
- Test whether the filename string - *name*matches the pattern string- *pat*, returning- `True`or- `False`. Both parameters are case-normalized using- `os.path.normcase()`- `fnmatchcase()`- This example will print all file names in the current directory with the extension - `.txt`:- import fnmatch import os for file in os.listdir('.'): if fnmatch.fnmatch(file, '*.txt'): print(file) 

- 
fnmatch.fnmatchcase(*name*,*pat*)[¶](#fnmatch.fnmatchcase)
- Test whether the filename string - *name*matches the pattern string- *pat*, returning- `True`or- `False`; the comparison is case-sensitive and does not apply- `os.path.normcase()`

- 
fnmatch.filter(*names*,*pat*)[¶](#fnmatch.filter)
- Construct a list from those elements of the - [iterable](../glossary.html#term-iterable)of filename strings- *names*that match the pattern string- *pat*. It is the same as- `[n for n in names if fnmatch(n, pat)]`, but implemented more efficiently.

- 
fnmatch.translate(*pat*)[¶](#fnmatch.translate)
- Return the shell-style pattern - *pat*converted to a regular expression for using with- `re.match()`- `str`- Example: - >>> import fnmatch, re >>> >>> regex = fnmatch.translate('*.txt') >>> regex '(?s:.*\\.txt)\\Z' >>> reobj = re.compile(regex) >>> reobj.match('foobar.txt') <re.Match object; span=(0, 10), match='foobar.txt'> 

See also

- Module `glob`
- Unix shell-style path expansion.