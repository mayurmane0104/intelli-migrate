# Security Considerations — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/security_warnings.html](https://docs.python.org/library/security_warnings.html)

---

# Security Considerations[¶](#security-considerations)

The following modules have specific security considerations:

- `hashlib`- [all constructors take a “usedforsecurity” keyword-only argument disabling known insecure and blocked algorithms](hashlib.html#hashlib-usedforsecurity)
- `http.server`- [security considerations](http.server.html#http-server-security).
- `random`- `secrets`
- `shelve`- [shelve is based on pickle and thus unsuitable for dealing with untrusted sources](shelve.html#shelve-security)
- `tempfile`- [mktemp is deprecated due to vulnerability to race conditions](tempfile.html#tempfile-mktemp-deprecated)
- `zipfile`- [maliciously prepared .zip files can cause disk volume exhaustion](zipfile.html#zipfile-resources-limitations)

The [ -I](../using/cmdline.html#cmdoption-I) command line option can be used to run Python in isolated
mode. When it cannot be used, the 

[option or the](../using/cmdline.html#cmdoption-P)

`-P`[environment variable can be used to not prepend a potentially unsafe path to](../using/cmdline.html#envvar-PYTHONSAFEPATH)

`PYTHONSAFEPATH`[such as the current directory, the script’s directory or an empty string.](sys.html#sys.path)

`sys.path`