# uu — Encode and decode uuencode files — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/uu.html](https://docs.python.org/3.12/library/uu.html)

---

`uu`[¶](#module-uu)

`uu`**Source code:** [Lib/uu.py](https://github.com/python/cpython/tree/3.12/Lib/uu.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ uu](#module-uu) module is deprecated
(see 

[for details).](https://peps.python.org/pep-0594/#uu-and-the-uu-encoding)

**PEP 594**[is a modern alternative.](base64.html#module-base64)

`base64`This module encodes and decodes files in uuencode format, allowing arbitrary
binary data to be transferred over ASCII-only connections. Wherever a file
argument is expected, the methods accept a file-like object.  For backwards
compatibility, a string containing a pathname is also accepted, and the
corresponding file will be opened for reading and writing; the pathname `'-'`
is understood to mean the standard input or output.  However, this interface is
deprecated; it’s better for the caller to open the file itself, and be sure
that, when required, the mode is `'rb'` or `'wb'` on Windows.

This code was contributed by Lance Ellinghouse, and modified by Jack Jansen.

The [ uu](#module-uu) module defines the following functions:

- 
uu.encode(*in_file*,*out_file*,*name=None*,*mode=None*,***,*backtick=False*)[¶](#uu.encode)
- Uuencode file - *in_file*into file- *out_file*. The uuencoded file will have the header specifying- *name*and- *mode*as the defaults for the results of decoding the file. The default defaults are taken from- *in_file*, or- `'-'`and- `0o666`respectively. If- *backtick*is true, zeros are represented by- `'`'`instead of spaces.- Changed in version 3.7: Added the - *backtick*parameter.

- 
uu.decode(*in_file*,*out_file=None*,*mode=None*,*quiet=False*)[¶](#uu.decode)
- This call decodes uuencoded file - *in_file*placing the result on file- *out_file*. If- *out_file*is a pathname,- *mode*is used to set the permission bits if the file must be created. Defaults for- *out_file*and- *mode*are taken from the uuencode header. However, if the file specified in the header already exists, a- `uu.Error`- `decode()`- *quiet*to a true value silences this warning.

- 
*exception*uu.Error[¶](#uu.Error)
- Subclass of - `Exception`- `uu.decode()`

See also

- Module `binascii`
- Support module containing ASCII-to-binary and binary-to-ASCII conversions.