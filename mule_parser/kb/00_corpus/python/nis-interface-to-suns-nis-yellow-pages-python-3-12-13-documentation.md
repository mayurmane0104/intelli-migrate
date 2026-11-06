# nis — Interface to Sun’s NIS (Yellow Pages) — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/nis.html](https://docs.python.org/3.12/library/nis.html)

---

`nis`[¶](#module-nis)

`nis`Deprecated since version 3.11, will be removed in version 3.13: The [ nis](#module-nis) module is deprecated
(see 

[for details).](https://peps.python.org/pep-0594/#nis)

**PEP 594**The [ nis](#module-nis) module gives a thin wrapper around the NIS library, useful for
central administration of several hosts.

Because NIS exists only on Unix systems, this module is only available for Unix.

[Availability](intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

The [ nis](#module-nis) module defines the following functions:

- 
nis.match(*key*,*mapname*,*domain=default_domain*)[¶](#nis.match)
- Return the match for - *key*in map- *mapname*, or raise an error (- `nis.error`- *key*is 8-bit clean. Return value is an arbitrary array of bytes (may contain- `NULL`and other joys).- Note that - *mapname*is first checked if it is an alias to another name.- The - *domain*argument allows overriding the NIS domain used for the lookup. If unspecified, lookup is in the default NIS domain.

- 
nis.cat(*mapname*,*domain=default_domain*)[¶](#nis.cat)
- Return a dictionary mapping - *key*to- *value*such that- `match(key, mapname)==value`. Note that both keys and values of the dictionary are arbitrary arrays of bytes.- Note that - *mapname*is first checked if it is an alias to another name.- The - *domain*argument allows overriding the NIS domain used for the lookup. If unspecified, lookup is in the default NIS domain.

- 
nis.maps(*domain=default_domain*)[¶](#nis.maps)
- Return a list of all valid maps. - The - *domain*argument allows overriding the NIS domain used for the lookup. If unspecified, lookup is in the default NIS domain.

- 
nis.get_default_domain()[¶](#nis.get_default_domain)
- Return the system default NIS domain. 

The [ nis](#module-nis) module defines the following exception:

- 
*exception*nis.error[¶](#nis.error)
- An error raised when a NIS function returns an error code.