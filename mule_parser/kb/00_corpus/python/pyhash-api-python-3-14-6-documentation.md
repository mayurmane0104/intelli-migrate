# PyHash API — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/hash.html](https://docs.python.org/c-api/hash.html)

---

# PyHash API[¶](#pyhash-api)

See also the [ PyTypeObject.tp_hash](typeobj.html#c.PyTypeObject.tp_hash) member and 

[Hashing of numeric types](../library/stdtypes.html#numeric-hash).

- 
type Py_hash_t[¶](#c.Py_hash_t)
- Hash value type: signed integer. - Added in version 3.2. 

- 
type Py_uhash_t[¶](#c.Py_uhash_t)
- Hash value type: unsigned integer. - Added in version 3.2. 

- 
Py_HASH_ALGORITHM[¶](#c.Py_HASH_ALGORITHM)
- A numerical value indicating the algorithm for hashing of - `str`- `bytes`- `memoryview`- The algorithm name is exposed by - `sys.hash_info.algorithm`- Added in version 3.4. 

- 
Py_HASH_FNV[¶](#c.Py_HASH_FNV)
- 
Py_HASH_SIPHASH24[¶](#c.Py_HASH_SIPHASH24)
- 
Py_HASH_SIPHASH13[¶](#c.Py_HASH_SIPHASH13)
- Numerical values to compare to - `Py_HASH_ALGORITHM`- `--with-hash-algorithm`- Added in version 3.4: Add - `Py_HASH_FNV`and- `Py_HASH_SIPHASH24`.- Added in version 3.11: Add - `Py_HASH_SIPHASH13`.

- 
Py_HASH_CUTOFF[¶](#c.Py_HASH_CUTOFF)
- Buffers of length in range - `[1, Py_HASH_CUTOFF)`are hashed using DJBX33A instead of the algorithm described by- `Py_HASH_ALGORITHM`- A - `Py_HASH_CUTOFF`of 0 disables the optimization.
- `Py_HASH_CUTOFF`must be non-negative and less or equal than 7.
 - 32-bit platforms should use a cutoff smaller than 64-bit platforms because it is easier to create colliding strings. A cutoff of 7 on 64-bit platforms and 5 on 32-bit platforms should provide a decent safety margin. - This corresponds to the - `sys.hash_info.cutoff`- Added in version 3.4. 

- 
PyHASH_MODULUS[¶](#c.PyHASH_MODULUS)
- The - [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime)- `P = 2**n -1`, used for numeric hash scheme.- This corresponds to the - `sys.hash_info.modulus`- Added in version 3.13. 

- 
PyHASH_BITS[¶](#c.PyHASH_BITS)
- The exponent - `n`of- `P`in- `PyHASH_MODULUS`- Added in version 3.13. 

- 
PyHASH_MULTIPLIER[¶](#c.PyHASH_MULTIPLIER)
- Prime multiplier used in string and various other hashes. - Added in version 3.13. 

- 
PyHASH_INF[¶](#c.PyHASH_INF)
- The hash value returned for a positive infinity. - This corresponds to the - `sys.hash_info.inf`- Added in version 3.13. 

- 
PyHASH_IMAG[¶](#c.PyHASH_IMAG)
- The multiplier used for the imaginary part of a complex number. - This corresponds to the - `sys.hash_info.imag`- Added in version 3.13. 

- 
type PyHash_FuncDef[¶](#c.PyHash_FuncDef)
- Hash function definition used by - `PyHash_GetFuncDef()`- 
[Py_hash_t](#c.Py_hash_t)(*const hash)(const void*,[Py_ssize_t](intro.html#c.Py_ssize_t))[¶](#c.PyHash_FuncDef.hash)
- Hash function. 
 - 
const char *name[¶](#c.PyHash_FuncDef.name)
- Hash function name (UTF-8 encoded string). - This corresponds to the - `sys.hash_info.algorithm`
 - 
const int hash_bits[¶](#c.PyHash_FuncDef.hash_bits)
- Internal size of the hash value in bits. - This corresponds to the - `sys.hash_info.hash_bits`
 - 
const int seed_bits[¶](#c.PyHash_FuncDef.seed_bits)
- Size of seed input in bits. - This corresponds to the - `sys.hash_info.seed_bits`
 - Added in version 3.4. 
- 

- 
[PyHash_FuncDef](#c.PyHash_FuncDef)*PyHash_GetFuncDef(void)[¶](#c.PyHash_GetFuncDef)
- Get the hash function definition. - See also - **PEP 456**- Added in version 3.4. 

- 
[Py_hash_t](#c.Py_hash_t)Py_HashPointer(const void *ptr)[¶](#c.Py_HashPointer)
- Hash a pointer value: process the pointer value as an integer (cast it to - `uintptr_t`internally). The pointer is not dereferenced.- The function cannot fail: it cannot return - `-1`.- Added in version 3.13. 

- 
[Py_hash_t](#c.Py_hash_t)Py_HashBuffer(const void *ptr,[Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.Py_HashBuffer)
- Compute and return the hash value of a buffer of - *len*bytes starting at address- *ptr*. The hash is guaranteed to match that of- `bytes`- `memoryview`- [buffer protocol](buffer.html#bufferobjects).- Use this function to implement hashing for immutable objects whose - `tp_richcompare`- *len*must be greater than or equal to- `0`.- This function always succeeds. - Added in version 3.14. 

- 
[Py_hash_t](#c.Py_hash_t)PyObject_GenericHash([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyObject_GenericHash)
- Generic hashing function that is meant to be put into a type object’s - `tp_hash`slot. Its result only depends on the object’s identity.- **CPython implementation detail:**In CPython, it is equivalent to- `Py_HashPointer()`- Added in version 3.13.