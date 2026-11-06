# urllib.error — Exception classes raised by urllib.request — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/urllib.error.html](https://docs.python.org/3.13/library/urllib.error.html)

---

`urllib.error` — Exception classes raised by urllib.request[¶](#module-urllib.error)

**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.13/Lib/urllib/error.py)

The `urllib.error` module defines the exception classes for exceptions
raised by [ urllib.request](urllib.request.html#module-urllib.request).  The base exception class is 

[.](#urllib.error.URLError)

`URLError`The following exceptions are raised by `urllib.error` as appropriate:

- 
*exception*urllib.error.URLError[¶](#urllib.error.URLError)
- The handlers raise this exception (or derived exceptions) when they run into a problem. It is a subclass of - `OSError`- 
reason[¶](#urllib.error.URLError.reason)
- The reason for this error. It can be a message string or another exception instance. 
 
- 
reason

- 
*exception*urllib.error.HTTPError(*url*,*code*,*msg*,*hdrs*,*fp*)[¶](#urllib.error.HTTPError)
- Though being an exception (a subclass of - `URLError`- `HTTPError`can also function as a non-exceptional file-like return value (the same thing that- `urlopen()`- 
url[¶](#urllib.error.HTTPError.url)
- Contains the request URL. An alias for - *filename*attribute.
 - 
code[¶](#urllib.error.HTTPError.code)
- An HTTP status code as defined in - **RFC 2616**- `http.server.BaseHTTPRequestHandler.responses`
 - 
reason[¶](#urllib.error.HTTPError.reason)
- This is usually a string explaining the reason for this error. An alias for - *msg*attribute.
 - 
headers[¶](#urllib.error.HTTPError.headers)
- The HTTP response headers for the HTTP request that caused the - `HTTPError`. An alias for- *hdrs*attribute.- Added in version 3.4. 
 - 
fp[¶](#urllib.error.HTTPError.fp)
- A file-like object where the HTTP error body can be read from. 
 
- 
url

- 
*exception*urllib.error.ContentTooShortError(*msg*,*content*)[¶](#urllib.error.ContentTooShortError)
- This exception is raised when the - `urlretrieve()`- *Content-Length*header).- 
content[¶](#urllib.error.ContentTooShortError.content)
- The downloaded (and supposedly truncated) data. 
 
- 
content