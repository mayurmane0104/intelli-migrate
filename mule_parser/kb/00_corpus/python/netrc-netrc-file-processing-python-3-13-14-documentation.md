# netrc — netrc file processing — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/netrc.html](https://docs.python.org/3.13/library/netrc.html)

---

`netrc` — netrc file processing[¶](#module-netrc)

**Source code:** [Lib/netrc.py](https://github.com/python/cpython/tree/3.13/Lib/netrc.py)

The [ netrc](#netrc.netrc) class parses and encapsulates the netrc file format used by
the Unix 

**ftp**program and other FTP clients.

- 
*class*netrc.netrc([*file*])[¶](#netrc.netrc)
- A - `netrc`instance or subclass instance encapsulates data from a netrc file. The initialization argument, if present, specifies the file to parse. If no argument is given, the file- `.netrc`in the user’s home directory – as determined by- `os.path.expanduser()`- `FileNotFoundError`- `NetrcParseError`- If no argument is specified on a POSIX system, the presence of passwords in the - `.netrc`file will raise a- `NetrcParseError`- `.netrc`. Such security checks are not available on platforms that do not support- `os.getuid()`- Changed in version 3.4: Added the POSIX permission check. - Changed in version 3.7: - `os.path.expanduser()`- `.netrc`file when- *file*is not passed as argument.- Changed in version 3.10: - `netrc`try UTF-8 encoding before using locale specific encoding. The entry in the netrc file no longer needs to contain all tokens. The missing tokens’ value default to an empty string. All the tokens and their values now can contain arbitrary characters, like whitespace and non-ASCII characters. If the login name is anonymous, it won’t trigger the security check.

- 
*exception*netrc.NetrcParseError[¶](#netrc.NetrcParseError)
- Exception raised by the - `netrc`- 
msg[¶](#netrc.NetrcParseError.msg)
- Textual explanation of the error. 
 - 
filename[¶](#netrc.NetrcParseError.filename)
- The name of the source file. 
 - 
lineno[¶](#netrc.NetrcParseError.lineno)
- The line number on which the error was found. 
 
- 
msg

## netrc Objects[¶](#netrc-objects)

A [ netrc](#netrc.netrc) instance has the following methods:

- 
netrc.authenticators(*host*)[¶](#netrc.netrc.authenticators)
- Return a 3-tuple - `(login, account, password)`of authenticators for- *host*. If the netrc file did not contain an entry for the given host, return the tuple associated with the ‘default’ entry. If neither matching host nor default entry is available, return- `None`.

- 
netrc.__repr__()[¶](#netrc.netrc.__repr__)
- Dump the class data as a string in the format of a netrc file. (This discards comments and may reorder the entries.) 

Instances of [ netrc](#netrc.netrc) have public instance variables:

- 
netrc.hosts[¶](#netrc.netrc.hosts)
- Dictionary mapping host names to - `(login, account, password)`tuples. The ‘default’ entry, if any, is represented as a pseudo-host by that name.

- 
netrc.macros[¶](#netrc.netrc.macros)
- Dictionary mapping macro names to string lists.