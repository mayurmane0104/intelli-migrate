# hmac — Keyed-Hashing for Message Authentication — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/hmac.html](https://docs.python.org/3.13/library/hmac.html)

---

`hmac` — Keyed-Hashing for Message Authentication[¶](#module-hmac)

**Source code:** [Lib/hmac.py](https://github.com/python/cpython/tree/3.13/Lib/hmac.py)

This module implements the HMAC algorithm as described by [ RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104.html).
The interface allows to use any hash function with a 

*fixed*digest size. In particular, extendable output functions such as SHAKE-128 or SHAKE-256 cannot be used with HMAC.

- 
hmac.new(*key*,*msg=None*,*digestmod*)[¶](#hmac.new)
- Return a new hmac object. - *key*is a bytes or bytearray object giving the secret key. If- *msg*is present, the method call- `update(msg)`is made.- *digestmod*is the digest name, digest constructor or module for the HMAC object to use. It may be any name suitable to- `hashlib.new()`- Changed in version 3.4: Parameter - *key*can be a bytes or bytearray object. Parameter- *msg*can be of any type supported by- `hashlib`- *digestmod*can be the name of a hash algorithm.- Changed in version 3.8: The - *digestmod*argument is now required. Pass it as a keyword argument to avoid awkwardness when you do not have an initial- *msg*.

- 
hmac.digest(*key*,*msg*,*digest*)[¶](#hmac.digest)
- Return digest of - *msg*for given secret- *key*and- *digest*. The function is equivalent to- `HMAC(key, msg, digest).digest()`, but uses an optimized C or inline implementation, which is faster for messages that fit into memory. The parameters- *key*,- *msg*, and- *digest*have the same meaning as in- `new()`- CPython implementation detail, the optimized C implementation is only used when - *digest*is a string and name of a digest algorithm, which is supported by OpenSSL.- Added in version 3.7. 

- 
*class*hmac.HMAC[¶](#hmac.HMAC)
- An HMAC object has the following methods: 

- 
HMAC.update(*msg*)[¶](#hmac.HMAC.update)
- Update the hmac object with - *msg*. Repeated calls are equivalent to a single call with the concatenation of all the arguments:- `m.update(a); m.update(b)`is equivalent to- `m.update(a + b)`.- Changed in version 3.4: Parameter - *msg*can be of any type supported by- `hashlib`

- 
HMAC.digest()[¶](#hmac.HMAC.digest)
- Return the digest of the bytes passed to the - `update()`- *digest_size*of the digest given to the constructor. It may contain non-ASCII bytes, including NUL bytes.- Warning - When comparing the output of - `digest()`to an externally supplied digest during a verification routine, it is recommended to use the- `compare_digest()`- `==`operator to reduce the vulnerability to timing attacks.

- 
HMAC.hexdigest()[¶](#hmac.HMAC.hexdigest)
- Like - `digest()`- Warning - When comparing the output of - `hexdigest()`to an externally supplied digest during a verification routine, it is recommended to use the- `compare_digest()`- `==`operator to reduce the vulnerability to timing attacks.

- 
HMAC.copy()[¶](#hmac.HMAC.copy)
- Return a copy (“clone”) of the hmac object. This can be used to efficiently compute the digests of strings that share a common initial substring. 

A hash object has the following attributes:

- 
HMAC.digest_size[¶](#hmac.HMAC.digest_size)
- The size of the resulting HMAC digest in bytes. 

- 
HMAC.block_size[¶](#hmac.HMAC.block_size)
- The internal block size of the hash algorithm in bytes. - Added in version 3.4. 

- 
HMAC.name[¶](#hmac.HMAC.name)
- The canonical name of this HMAC, always lowercase, e.g. - `hmac-md5`.- Added in version 3.4. 

Changed in version 3.10: Removed the undocumented attributes `HMAC.digest_cons`, `HMAC.inner`,
and `HMAC.outer`.

This module also provides the following helper function:

- 
hmac.compare_digest(*a*,*b*)[¶](#hmac.compare_digest)
- Return - `a == b`. This function uses an approach designed to prevent timing analysis by avoiding content-based short circuiting behaviour, making it appropriate for cryptography.- *a*and- *b*must both be of the same type: either- `str`- `HMAC.hexdigest()`- [bytes-like object](../glossary.html#term-bytes-like-object).- Note - If - *a*and- *b*are of different lengths, or if an error occurs, a timing attack could theoretically reveal information about the types and lengths of- *a*and- *b*—but not their values.- Added in version 3.3. - Changed in version 3.10: The function uses OpenSSL’s - `CRYPTO_memcmp()`internally when available.

See also

- Module `hashlib`
- The Python module providing secure hash functions.