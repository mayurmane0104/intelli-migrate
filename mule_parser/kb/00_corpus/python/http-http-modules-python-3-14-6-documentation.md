# http — HTTP modules — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/http.html](https://docs.python.org/library/http.html)

---

`http` — HTTP modules[¶](#module-http)

**Source code:** [Lib/http/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/http/__init__.py)

`http` is a package that collects several modules for working with the
HyperText Transfer Protocol:

- `http.client`- `urllib.request`
- `http.server`- `socketserver`
- `http.cookies`
- `http.cookiejar`

The `http` module also defines the following enums that help you work with http related code:

- 
*class*http.HTTPStatus[¶](#http.HTTPStatus)
- Added in version 3.5. - A subclass of - `enum.IntEnum`- Usage: - >>> from http import HTTPStatus >>> HTTPStatus.OK HTTPStatus.OK >>> HTTPStatus.OK == 200 True >>> HTTPStatus.OK.value 200 >>> HTTPStatus.OK.phrase 'OK' >>> HTTPStatus.OK.description 'Request fulfilled, document follows' >>> list(HTTPStatus) [HTTPStatus.CONTINUE, HTTPStatus.SWITCHING_PROTOCOLS, ...] 

## HTTP status codes[¶](#http-status-codes)

Supported,
[IANA-registered status codes](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
available in [ http.HTTPStatus](#http.HTTPStatus) are:

| Code | Enum Name | Details | 
|---|---|---|
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | WebDAV  | 
| 
 | 
 | An HTTP Status Code for Indicating Hints  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | WebDAV  | 
| 
 | 
 | WebDAV Binding Extensions  | 
| 
 | 
 | Delta Encoding in HTTP  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTCPCP/1.0  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | WebDAV  | 
| 
 | 
 | WebDAV  | 
| 
 | 
 | Using Early Data in HTTP  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | Additional HTTP Status Codes  | 
| 
 | 
 | Additional HTTP Status Codes  | 
| 
 | 
 | Additional HTTP Status Codes  | 
| 
 | 
 | An HTTP Status Code to Report Legal Obstacles  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | Transparent Content Negotiation in HTTP  | 
| 
 | 
 | WebDAV  | 
| 
 | 
 | WebDAV Binding Extensions  | 
| 
 | 
 | An HTTP Extension Framework  | 
| 
 | 
 | Additional HTTP Status Codes  | 

In order to preserve backwards compatibility, enum values are also present
in the [ http.client](http.client.html#module-http.client) module in the form of constants. The enum name is
equal to the constant name (i.e. 

`http.HTTPStatus.OK` is also available as
`http.client.OK`).Changed in version 3.7: Added `421 MISDIRECTED_REQUEST` status code.

Added in version 3.8: Added `451 UNAVAILABLE_FOR_LEGAL_REASONS` status code.

Added in version 3.9: Added `103 EARLY_HINTS`, `418 IM_A_TEAPOT` and `425 TOO_EARLY` status codes.

Changed in version 3.13: Implemented RFC9110 naming for status constants. Old constant names are preserved for
backwards compatibility: `413 REQUEST_ENTITY_TOO_LARGE`, `414 REQUEST_URI_TOO_LONG`,
`416 REQUESTED_RANGE_NOT_SATISFIABLE` and `422 UNPROCESSABLE_ENTITY`.

## HTTP status category[¶](#http-status-category)

Added in version 3.12.

The enum values have several properties to indicate the HTTP status category:

| Property | Indicates that | Details | 
|---|---|---|
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 

Usage:

>>> from http import HTTPStatus >>> HTTPStatus.OK.is_success True >>> HTTPStatus.OK.is_client_error False

- 
*class*http.HTTPMethod[¶](#http.HTTPMethod)
- Added in version 3.11. - A subclass of - `enum.StrEnum`- Usage: - >>> from http import HTTPMethod >>> >>> HTTPMethod.GET <HTTPMethod.GET> >>> HTTPMethod.GET == 'GET' True >>> HTTPMethod.GET.value 'GET' >>> HTTPMethod.GET.description 'Retrieve the target.' >>> list(HTTPMethod) [<HTTPMethod.CONNECT>, <HTTPMethod.DELETE>, <HTTPMethod.GET>, <HTTPMethod.HEAD>, <HTTPMethod.OPTIONS>, <HTTPMethod.PATCH>, <HTTPMethod.POST>, <HTTPMethod.PUT>, <HTTPMethod.TRACE>] 

## HTTP methods[¶](#http-methods)

Supported,
[IANA-registered methods](https://www.iana.org/assignments/http-methods/http-methods.xhtml)
available in [ http.HTTPMethod](#http.HTTPMethod) are:

| Method | Enum Name | Details | 
|---|---|---|
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP Semantics  | 
| 
 | 
 | HTTP/1.1  |