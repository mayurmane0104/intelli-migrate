# http.cookies — HTTP state management — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/http.cookies.html](https://docs.python.org/3.13/library/http.cookies.html)

---

`http.cookies` — HTTP state management[¶](#module-http.cookies)

**Source code:** [Lib/http/cookies.py](https://github.com/python/cpython/tree/3.13/Lib/http/cookies.py)

The `http.cookies` module defines classes for abstracting the concept of
cookies, an HTTP state management mechanism. It supports both simple string-only
cookies, and provides an abstraction for having any serializable data-type as
cookie value.

The module formerly strictly applied the parsing rules described in the
[ RFC 2109](https://datatracker.ietf.org/doc/html/rfc2109.html) and 

[specifications. It has since been discovered that MSIE 3.0x didn’t follow the character rules outlined in those specs; many current-day browsers and servers have also relaxed parsing rules when it comes to cookie handling. As a result, this module now uses parsing rules that are a bit less strict than they once were.](https://datatracker.ietf.org/doc/html/rfc2068.html)

**RFC 2068**The character set, [ string.ascii_letters](string.html#string.ascii_letters), 

[and](string.html#string.digits)

`string.digits``!#$%&'*+-.^_`|~:` denote the set of valid characters allowed by this module
in a cookie name (as [).](#http.cookies.Morsel.key)

`key`Changed in version 3.3: Allowed ‘:’ as a valid cookie name character.

Note

On encountering an invalid cookie, [ CookieError](#http.cookies.CookieError) is raised, so if your
cookie data comes from a browser you should always prepare for invalid data
and catch 

`CookieError` on parsing.- 
*exception*http.cookies.CookieError[¶](#http.cookies.CookieError)
- Exception failing because of - **RFC 2109**- *Set-Cookie*header, etc.

- 
*class*http.cookies.BaseCookie([*input*])[¶](#http.cookies.BaseCookie)
- This class is a dictionary-like object whose keys are strings and whose values are - `Morsel`- `Morsel`containing the key and the value.- If - *input*is given, it is passed to the- `load()`

- 
*class*http.cookies.SimpleCookie([*input*])[¶](#http.cookies.SimpleCookie)
- This class derives from - `BaseCookie`- `value_decode()`- `value_encode()`- `SimpleCookie`supports strings as cookie values. When setting the value,- `SimpleCookie`calls the builtin- `str()`

See also

- Module `http.cookiejar`
- HTTP cookie handling for web - *clients*. The- `http.cookiejar`- `http.cookies`modules do not depend on each other.
- **RFC 2109**
- This is the state management specification implemented by this module. 

## Cookie Objects[¶](#cookie-objects)

- 
BaseCookie.value_decode(*val*)[¶](#http.cookies.BaseCookie.value_decode)
- Return a tuple - `(real_value, coded_value)`from a string representation.- `real_value`can be any type. This method does no decoding in- `BaseCookie`

- 
BaseCookie.value_encode(*val*)[¶](#http.cookies.BaseCookie.value_encode)
- Return a tuple - `(real_value, coded_value)`.- *val*can be any type, but- `coded_value`will always be converted to a string. This method does no encoding in- `BaseCookie`- In general, it should be the case that - `value_encode()`and- `value_decode()`- *value_decode*.

- 
BaseCookie.output(*attrs=None*,*header='Set-Cookie:'*,*sep='\r\n'*)[¶](#http.cookies.BaseCookie.output)
- Return a string representation suitable to be sent as HTTP headers. - *attrs*and- *header*are sent to each- `Morsel`- `output()`- *sep*is used to join the headers together, and is by default the combination- `'\r\n'`(CRLF).

## Morsel Objects[¶](#morsel-objects)

- 
*class*http.cookies.Morsel[¶](#http.cookies.Morsel)
- Abstract a key/value pair, which has some - **RFC 2109**- Morsels are dictionary-like objects, whose set of keys is constant — the valid - **RFC 2109**- The attribute - `httponly`- The attribute - `samesite`- The keys are case-insensitive and their default value is - `''`.- Changed in version 3.7: Attributes - `key`- `value`- `coded_value`- `set()`- Changed in version 3.8: Added support for the - `samesite`

- 
Morsel.value[¶](#http.cookies.Morsel.value)
- The value of the cookie. 

- 
Morsel.coded_value[¶](#http.cookies.Morsel.coded_value)
- The encoded value of the cookie — this is what should be sent. 

- 
Morsel.key[¶](#http.cookies.Morsel.key)
- The name of the cookie. 

- 
Morsel.set(*key*,*value*,*coded_value*)[¶](#http.cookies.Morsel.set)
- Set the - *key*,- *value*and- *coded_value*attributes.

- 
Morsel.output(*attrs=None*,*header='Set-Cookie:'*)[¶](#http.cookies.Morsel.output)
- Return a string representation of the Morsel, suitable to be sent as an HTTP header. By default, all the attributes are included, unless - *attrs*is given, in which case it should be a list of attributes to use.- *header*is by default- `"Set-Cookie:"`.

- 
Morsel.js_output(*attrs=None*)[¶](#http.cookies.Morsel.js_output)
- Return an embeddable JavaScript snippet, which, if run on a browser which supports JavaScript, will act the same as if the HTTP header was sent. - The meaning for - *attrs*is the same as in- `output()`

- 
Morsel.OutputString(*attrs=None*)[¶](#http.cookies.Morsel.OutputString)
- Return a string representing the Morsel, without any surrounding HTTP or JavaScript. - The meaning for - *attrs*is the same as in- `output()`

- 
Morsel.update(*values*)[¶](#http.cookies.Morsel.update)
- Update the values in the Morsel dictionary with the values in the dictionary - *values*. Raise an error if any of the keys in the- *values*dict is not a valid- **RFC 2109**- Changed in version 3.5: an error is raised for invalid keys. 

- 
Morsel.copy(*value*)[¶](#http.cookies.Morsel.copy)
- Return a shallow copy of the Morsel object. - Changed in version 3.5: return a Morsel object instead of a dict. 

- 
Morsel.setdefault(*key*,*value=None*)[¶](#http.cookies.Morsel.setdefault)
- Raise an error if key is not a valid - **RFC 2109**- `dict.setdefault()`

## Example[¶](#example)

The following example demonstrates how to use the `http.cookies` module.

```
>>> from http import cookies
>>> C = cookies.SimpleCookie()
>>> C["fig"] = "newton"
>>> C["sugar"] = "wafer"
>>> print(C) # generate HTTP headers
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
>>> print(C.output()) # same thing
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
>>> C = cookies.SimpleCookie()
>>> C["rocky"] = "road"
>>> C["rocky"]["path"] = "/cookie"
>>> print(C.output(header="Cookie:"))
Cookie: rocky=road; Path=/cookie
>>> print(C.output(attrs=[], header="Cookie:"))
Cookie: rocky=road
>>> C = cookies.SimpleCookie()
>>> C.load("chips=ahoy; vienna=finger") # load from a string (HTTP header)
>>> print(C)
Set-Cookie: chips=ahoy
Set-Cookie: vienna=finger
>>> C = cookies.SimpleCookie()
>>> C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=;";')
>>> print(C)
Set-Cookie: keebler="E=everybody; L=\"Loves\"; fudge=;"
>>> C = cookies.SimpleCookie()
>>> C["oreo"] = "doublestuff"
>>> C["oreo"]["path"] = "/"
>>> print(C)
Set-Cookie: oreo=doublestuff; Path=/
>>> C = cookies.SimpleCookie()
>>> C["twix"] = "none for you"
>>> C["twix"].value
'none for you'
>>> C = cookies.SimpleCookie()
>>> C["number"] = 7 # equivalent to C["number"] = str(7)
>>> C["string"] = "seven"
>>> C["number"].value
'7'
>>> C["string"].value
'seven'
>>> print(C)
Set-Cookie: number=7
Set-Cookie: string=seven
```