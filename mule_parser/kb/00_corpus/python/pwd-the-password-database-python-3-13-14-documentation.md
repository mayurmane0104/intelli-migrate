# pwd — The password database — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/pwd.html](https://docs.python.org/3.13/library/pwd.html)

---

`pwd` — The password database[¶](#module-pwd)

This module provides access to the Unix user account and password database. It is available on all Unix versions.

[Availability](intro.html#availability): Unix, not WASI, not iOS.

Password database entries are reported as a tuple-like object, whose attributes
correspond to the members of the `passwd` structure (Attribute field below,
see `<pwd.h>`):

| Index | Attribute | Meaning | 
|---|---|---|
| 0 | 
 | Login name | 
| 1 | 
 | Optional encrypted password | 
| 2 | 
 | Numerical user ID | 
| 3 | 
 | Numerical group ID | 
| 4 | 
 | User name or comment field | 
| 5 | 
 | User home directory | 
| 6 | 
 | User command interpreter | 

The uid and gid items are integers, all others are strings. [ KeyError](exceptions.html#KeyError) is
raised if the entry asked for cannot be found.

Note

In traditional Unix the field `pw_passwd` usually contains a password
encrypted with a DES derived algorithm.  However most
modern unices  use a so-called *shadow password* system.  On those unices the
*pw_passwd* field only contains an asterisk (`'*'`) or the  letter `'x'`
where the encrypted password is stored in a file `/etc/shadow` which is
not world readable.  Whether the *pw_passwd* field contains anything useful is
system-dependent.

It defines the following items:

- 
pwd.getpwuid(*uid*)[¶](#pwd.getpwuid)
- Return the password database entry for the given numeric user ID. 

- 
pwd.getpwnam(*name*)[¶](#pwd.getpwnam)
- Return the password database entry for the given user name. 

- 
pwd.getpwall()[¶](#pwd.getpwall)
- Return a list of all available password database entries, in arbitrary order. 

See also

- Module `grp`
- An interface to the group database, similar to this.