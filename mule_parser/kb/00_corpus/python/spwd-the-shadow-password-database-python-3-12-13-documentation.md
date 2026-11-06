# spwd — The shadow password database — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/spwd.html](https://docs.python.org/3.12/library/spwd.html)

---

`spwd`[¶](#module-spwd)

`spwd`Deprecated since version 3.11, will be removed in version 3.13: The [ spwd](#module-spwd) module is deprecated
(see 

[for details and alternatives).](https://peps.python.org/pep-0594/#spwd)

**PEP 594**This module provides access to the Unix shadow password database. It is available on various Unix versions.

[Availability](intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

You must have enough privileges to access the shadow password database (this usually means you have to be root).

Shadow password database entries are reported as a tuple-like object, whose
attributes correspond to the members of the `spwd` structure (Attribute field
below, see `<shadow.h>`):

| Index | Attribute | Meaning | 
|---|---|---|
| 0 | 
 | Login name | 
| 1 | 
 | Encrypted password | 
| 2 | 
 | Date of last change | 
| 3 | 
 | Minimal number of days between changes | 
| 4 | 
 | Maximum number of days between changes | 
| 5 | 
 | Number of days before password expires to warn user about it | 
| 6 | 
 | Number of days after password expires until account is disabled | 
| 7 | 
 | Number of days since 1970-01-01 when account expires | 
| 8 | 
 | Reserved | 

The sp_namp and sp_pwdp items are strings, all others are integers.
[ KeyError](exceptions.html#KeyError) is raised if the entry asked for cannot be found.

The following functions are defined:

- 
spwd.getspnam(*name*)[¶](#spwd.getspnam)
- Return the shadow password database entry for the given user name. - Changed in version 3.6: Raises a - `PermissionError`- `KeyError`

- 
spwd.getspall()[¶](#spwd.getspall)
- Return a list of all available shadow password database entries, in arbitrary order.