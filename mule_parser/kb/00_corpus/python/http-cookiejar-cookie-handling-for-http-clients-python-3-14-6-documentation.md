# http.cookiejar — Cookie handling for HTTP clients — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/http.cookiejar.html](https://docs.python.org/library/http.cookiejar.html)

---

`http.cookiejar` — Cookie handling for HTTP clients[¶](#module-http.cookiejar)

**Source code:** [Lib/http/cookiejar.py](https://github.com/python/cpython/tree/3.14/Lib/http/cookiejar.py)

The `http.cookiejar` module defines classes for automatic handling of HTTP
cookies.  It is useful for accessing websites that require small pieces of data
– *cookies* – to be set on the client machine by an HTTP response from a
web server, and then returned to the server in later HTTP requests.

Both the regular Netscape cookie protocol and the protocol defined by
[ RFC 2965](https://datatracker.ietf.org/doc/html/rfc2965.html) are handled.  RFC 2965 handling is switched off by default.

[cookies are parsed as Netscape cookies and subsequently treated either as Netscape or RFC 2965 cookies according to the ‘policy’ in effect. Note that the great majority of cookies on the internet are Netscape cookies.](https://datatracker.ietf.org/doc/html/rfc2109.html)

**RFC 2109**`http.cookiejar` attempts to follow the de-facto Netscape cookie protocol (which
differs substantially from that set out in the original Netscape specification),
including taking note of the `max-age` and `port` cookie-attributes
introduced with RFC 2965.Note

The various named parameters found in *Set-Cookie* and
*Set-Cookie2* headers (eg. `domain` and `expires`) are
conventionally referred to as *attributes*.  To distinguish them from
Python attributes, the documentation for this module uses the term
*cookie-attribute* instead.

The module defines the following exception:

- 
*exception*http.cookiejar.LoadError[¶](#http.cookiejar.LoadError)
- Instances of - `FileCookieJar`- `LoadError`is a subclass of- `OSError`

The following classes are provided:

- 
*class*http.cookiejar.CookieJar(*policy=None*)[¶](#http.cookiejar.CookieJar)
- *policy*is an object implementing the- `CookiePolicy`- The - `CookieJar`class stores HTTP cookies. It extracts cookies from HTTP requests, and returns them in HTTP responses.- `CookieJar`instances automatically expire contained cookies when necessary. Subclasses are also responsible for storing and retrieving cookies from a file or database.

- 
*class*http.cookiejar.FileCookieJar(*filename=None*,*delayload=None*,*policy=None*)[¶](#http.cookiejar.FileCookieJar)
- *policy*is an object implementing the- `CookiePolicy`- A - `CookieJar`- **NOT**loaded from the named file until either the- `load()`- `revert()`- [FileCookieJar subclasses and co-operation with web browsers](#file-cookie-jar-classes).- This should not be initialized directly – use its subclasses below instead. - Changed in version 3.8: The filename parameter supports a - [path-like object](../glossary.html#term-path-like-object).

- 
*class*http.cookiejar.CookiePolicy[¶](#http.cookiejar.CookiePolicy)
- This class is responsible for deciding whether each cookie should be accepted from / returned to the server. 

- 
*class*http.cookiejar.DefaultCookiePolicy(*blocked_domains=None*,*allowed_domains=None*,*netscape=True*,*rfc2965=False*,*rfc2109_as_netscape=None*,*hide_cookie2=False*,*strict_domain=False*,*strict_rfc2965_unverifiable=True*,*strict_ns_unverifiable=False*,*strict_ns_domain=DefaultCookiePolicy.DomainLiberal*,*strict_ns_set_initial_dollar=False*,*strict_ns_set_path=False*,*secure_protocols=('https', 'wss')*)[¶](#http.cookiejar.DefaultCookiePolicy)
- Constructor arguments should be passed as keyword arguments only. - *blocked_domains*is a sequence of domain names that we never accept cookies from, nor return cookies to.- *allowed_domains*if not- `None`- *secure_protocols*is a sequence of protocols for which secure cookies can be added to. By default- *https*and- *wss*(secure websocket) are considered secure protocols. For all other arguments, see the documentation for- `CookiePolicy`- `DefaultCookiePolicy`objects.- `DefaultCookiePolicy`implements the standard accept / reject rules for Netscape and- **RFC 2965**- **RFC 2109**- *Set-Cookie*header with a version cookie-attribute of 1) are treated according to the RFC 2965 rules. However, if RFC 2965 handling is turned off or- `rfc2109_as_netscape`- `True`, RFC 2109 cookies are ‘downgraded’ by the- `CookieJar`- `version`attribute of the- `Cookie`- `DefaultCookiePolicy`also provides some parameters to allow some fine-tuning of policy.

- 
*class*http.cookiejar.Cookie[¶](#http.cookiejar.Cookie)
- This class represents Netscape, - **RFC 2109**- **RFC 2965**- `http.cookiejar`construct their own- `Cookie`instances. Instead, if necessary, call- `make_cookies()`on a- `CookieJar`

See also

- Module `urllib.request`
- URL opening with automatic cookie handling. 
- Module `http.cookies`
- HTTP cookie classes, principally useful for server-side code. The - `http.cookiejar`and- `http.cookies`
- [https://curl.se/rfc/cookie_spec.html](https://curl.se/rfc/cookie_spec.html)
- The specification of the original Netscape cookie protocol. Though this is still the dominant protocol, the ‘Netscape cookie protocol’ implemented by all the major browsers (and - `http.cookiejar`) only bears a passing resemblance to the one sketched out in- `cookie_spec.html`.
- **RFC 2109**
- Obsoleted by - **RFC 2965**- *Set-Cookie*with version=1.
- **RFC 2965**
- The Netscape protocol with the bugs fixed. Uses - *Set-Cookie2*in place of- *Set-Cookie*. Not widely used.
- [https://kristol.org/cookie/errata.html](https://kristol.org/cookie/errata.html)
- Unfinished errata to - **RFC 2965**

[ RFC 2964](https://datatracker.ietf.org/doc/html/rfc2964.html) - Use of HTTP State Management

## CookieJar and FileCookieJar Objects[¶](#cookiejar-and-filecookiejar-objects)

[ CookieJar](#http.cookiejar.CookieJar) objects support the 

[iterator](../glossary.html#term-iterator)protocol for iterating over contained

[objects.](#http.cookiejar.Cookie)

`Cookie`[ CookieJar](#http.cookiejar.CookieJar) has the following methods:

- 
CookieJar.add_cookie_header(*request*)[¶](#http.cookiejar.CookieJar.add_cookie_header)
- Add correct - *Cookie*header to- *request*.- If policy allows (ie. the - `rfc2965`and- `hide_cookie2`attributes of the- `CookieJar`- `CookiePolicy`- *Cookie2*header is also added when appropriate.- The - *request*object (usually a- `urllib.request.Request`- `get_full_url()`,- `has_header()`,- `get_header()`,- `header_items()`,- `add_unredirected_header()`and the attributes- `host`,- `type`,- `unverifiable`and- `origin_req_host`as documented by- `urllib.request`- Changed in version 3.3: - *request*object needs- `origin_req_host`attribute. Dependency on a deprecated method- `get_origin_req_host()`has been removed.

- 
CookieJar.extract_cookies(*response*,*request*)[¶](#http.cookiejar.CookieJar.extract_cookies)
- Extract cookies from HTTP - *response*and store them in the- `CookieJar`- The - `CookieJar`- *Set-Cookie*and- *Set-Cookie2*headers in the- *response*argument, and store cookies as appropriate (subject to the- `CookiePolicy.set_ok()`- The - *response*object (usually the result of a call to- `urllib.request.urlopen()`- `info()`method, which returns an- `email.message.Message`- The - *request*object (usually a- `urllib.request.Request`- `get_full_url()`and the attributes- `host`,- `unverifiable`and- `origin_req_host`, as documented by- `urllib.request`- Changed in version 3.3: - *request*object needs- `origin_req_host`attribute. Dependency on a deprecated method- `get_origin_req_host()`has been removed.

- 
CookieJar.set_policy(*policy*)[¶](#http.cookiejar.CookieJar.set_policy)
- Set the - `CookiePolicy`

- 
CookieJar.make_cookies(*response*,*request*)[¶](#http.cookiejar.CookieJar.make_cookies)
- Return sequence of - `Cookie`- *response*object.- See the documentation for - `extract_cookies()`- *response*and- *request*arguments.

- 
CookieJar.set_cookie(*cookie*)[¶](#http.cookiejar.CookieJar.set_cookie)
- Set a - `Cookie`

- 
CookieJar.clear([*domain*[,*path*[,*name*]]])[¶](#http.cookiejar.CookieJar.clear)
- Clear some cookies. - If invoked without arguments, clear all cookies. If given a single argument, only cookies belonging to that - *domain*will be removed. If given two arguments, cookies belonging to the specified- *domain*and URL- *path*are removed. If given three arguments, then the cookie with the specified- *domain*,- *path*and- *name*is removed.- Raises - `KeyError`

- 
CookieJar.clear_session_cookies()[¶](#http.cookiejar.CookieJar.clear_session_cookies)
- Discard all session cookies. - Discards all contained cookies that have a true - `discard`attribute (usually because they had either no- `max-age`or- `expires`cookie-attribute, or an explicit- `discard`cookie-attribute). For interactive browsers, the end of a session usually corresponds to closing the browser window.- Note that the - `save()`method won’t save session cookies anyway, unless you ask otherwise by passing a true- *ignore_discard*argument.

[ FileCookieJar](#http.cookiejar.FileCookieJar) implements the following additional methods:

- 
FileCookieJar.save(*filename=None*,*ignore_discard=False*,*ignore_expires=False*)[¶](#http.cookiejar.FileCookieJar.save)
- Save cookies to a file. - This base class raises - `NotImplementedError`- *filename*is the name of file in which to save cookies. If- *filename*is not specified,- `self.filename`is used (whose default is the value passed to the constructor, if any); if- `self.filename`is- `None`- `ValueError`- *ignore_discard*: save even cookies set to be discarded.- *ignore_expires*: save even cookies that have expired- The file is overwritten if it already exists, thus wiping all the cookies it contains. Saved cookies can be restored later using the - `load()`- `revert()`

- 
FileCookieJar.load(*filename=None*,*ignore_discard=False*,*ignore_expires=False*)[¶](#http.cookiejar.FileCookieJar.load)
- Load cookies from a file. - Old cookies are kept unless overwritten by newly loaded ones. - Arguments are as for - `save()`- The named file must be in the format understood by the class, or - `LoadError`- `OSError`

- 
FileCookieJar.revert(*filename=None*,*ignore_discard=False*,*ignore_expires=False*)[¶](#http.cookiejar.FileCookieJar.revert)
- Clear all cookies and reload cookies from a saved file. - `revert()`can raise the same exceptions as- `load()`

[ FileCookieJar](#http.cookiejar.FileCookieJar) instances have the following public attributes:

- 
FileCookieJar.filename[¶](#http.cookiejar.FileCookieJar.filename)
- Filename of default file in which to keep cookies. This attribute may be assigned to. 

- 
FileCookieJar.delayload[¶](#http.cookiejar.FileCookieJar.delayload)
- If true, load cookies lazily from disk. This attribute should not be assigned to. This is only a hint, since this only affects performance, not behaviour (unless the cookies on disk are changing). A - `CookieJar`- `FileCookieJar`

## FileCookieJar subclasses and co-operation with web browsers[¶](#filecookiejar-subclasses-and-co-operation-with-web-browsers)

The following [ CookieJar](#http.cookiejar.CookieJar) subclasses are provided for reading and
writing.

- 
*class*http.cookiejar.MozillaCookieJar(*filename=None*,*delayload=None*,*policy=None*)[¶](#http.cookiejar.MozillaCookieJar)
- A - `FileCookieJar`- `cookies.txt`file format (which is also used by curl and the Lynx and Netscape browsers).- Note - This loses information about - **RFC 2965**- `port`.- Warning - Back up your cookies before saving if you have cookies whose loss / corruption would be inconvenient (there are some subtleties which may lead to slight changes in the file over a load / save round-trip). - Also note that cookies saved while Mozilla is running will get clobbered by Mozilla. 

- 
*class*http.cookiejar.LWPCookieJar(*filename=None*,*delayload=None*,*policy=None*)[¶](#http.cookiejar.LWPCookieJar)
- A - `FileCookieJar`- `Set-Cookie3`file format. This is convenient if you want to store cookies in a human-readable file.- Changed in version 3.8: The filename parameter supports a - [path-like object](../glossary.html#term-path-like-object).

## CookiePolicy Objects[¶](#cookiepolicy-objects)

Objects implementing the [ CookiePolicy](#http.cookiejar.CookiePolicy) interface have the following
methods:

- 
CookiePolicy.set_ok(*cookie*,*request*)[¶](#http.cookiejar.CookiePolicy.set_ok)
- Return boolean value indicating whether cookie should be accepted from server. - *cookie*is a- `Cookie`- *request*is an object implementing the interface defined by the documentation for- `CookieJar.extract_cookies()`

- 
CookiePolicy.return_ok(*cookie*,*request*)[¶](#http.cookiejar.CookiePolicy.return_ok)
- Return boolean value indicating whether cookie should be returned to server. - *cookie*is a- `Cookie`- *request*is an object implementing the interface defined by the documentation for- `CookieJar.add_cookie_header()`

- 
CookiePolicy.domain_return_ok(*domain*,*request*)[¶](#http.cookiejar.CookiePolicy.domain_return_ok)
- Return - `False`if cookies should not be returned, given cookie domain.- This method is an optimization. It removes the need for checking every cookie with a particular domain (which might involve reading many files). Returning true from - `domain_return_ok()`and- `path_return_ok()`- `return_ok()`- If - `domain_return_ok()`returns true for the cookie domain,- `path_return_ok()`- `path_return_ok()`and- `return_ok()`- `path_return_ok()`returns true,- `return_ok()`is called with the- `Cookie`- `return_ok()`is never called for that cookie path.- Note that - `domain_return_ok()`is called for every- *cookie*domain, not just for the- *request*domain. For example, the function might be called with both- `".example.com"`and- `"www.example.com"`if the request domain is- `"www.example.com"`. The same goes for- `path_return_ok()`- The - *request*argument is as documented for- `return_ok()`

- 
CookiePolicy.path_return_ok(*path*,*request*)[¶](#http.cookiejar.CookiePolicy.path_return_ok)
- Return - `False`if cookies should not be returned, given cookie path.- See the documentation for - `domain_return_ok()`

In addition to implementing the methods above, implementations of the
[ CookiePolicy](#http.cookiejar.CookiePolicy) interface must also supply the following attributes,
indicating which protocols should be used, and how.  All of these attributes may
be assigned to.

- 
CookiePolicy.netscape[¶](#http.cookiejar.CookiePolicy.netscape)
- Implement Netscape protocol. 

- 
CookiePolicy.hide_cookie2[¶](#http.cookiejar.CookiePolicy.hide_cookie2)
- Don’t add - *Cookie2*header to requests (the presence of this header indicates to the server that we understand- **RFC 2965**

The most useful way to define a [ CookiePolicy](#http.cookiejar.CookiePolicy) class is by subclassing
from 

[and overriding some or all of the methods above.](#http.cookiejar.DefaultCookiePolicy)

`DefaultCookiePolicy``CookiePolicy` itself may be used as a ‘null policy’ to allow
setting and receiving any and all cookies (this is unlikely to be useful).## DefaultCookiePolicy Objects[¶](#defaultcookiepolicy-objects)

Implements the standard rules for accepting and returning cookies.

Both [ RFC 2965](https://datatracker.ietf.org/doc/html/rfc2965.html) and Netscape cookies are covered.  RFC 2965 handling is switched
off by default.

The easiest way to provide your own policy is to override this class and call its methods in your overridden implementations before adding your own additional checks:

```
import http.cookiejar
class MyCookiePolicy(http.cookiejar.DefaultCookiePolicy):
    def set_ok(self, cookie, request):
        if not http.cookiejar.DefaultCookiePolicy.set_ok(self, cookie, request):
            return False
        if i_dont_want_to_store_this_cookie(cookie):
            return False
        return True
```
In addition to the features required to implement the [ CookiePolicy](#http.cookiejar.CookiePolicy)
interface, this class allows you to block and allow domains from setting and
receiving cookies.  There are also some strictness switches that allow you to
tighten up the rather loose Netscape protocol rules a little bit (at the cost of
blocking some benign cookies).

A domain blocklist and allowlist is provided (both off by default). Only domains
not in the blocklist and present in the allowlist (if the allowlist is active)
participate in cookie setting and returning.  Use the *blocked_domains*
constructor argument, and `blocked_domains()` and
`set_blocked_domains()` methods (and the corresponding argument and methods
for *allowed_domains*).  If you set an allowlist, you can turn it off again by
setting it to [ None](constants.html#None).

Domains in block or allow lists that do not start with a dot must equal the
cookie domain to be matched.  For example, `"example.com"` matches a blocklist
entry of `"example.com"`, but `"www.example.com"` does not.  Domains that do
start with a dot are matched by more specific domains too. For example, both
`"www.example.com"` and `"www.coyote.example.com"` match `".example.com"`
(but `"example.com"` itself does not).  IP addresses are an exception, and
must match exactly.  For example, if blocked_domains contains `"192.168.1.2"`
and `".168.1.2"`, 192.168.1.2 is blocked, but 193.168.1.2 is not.

[ DefaultCookiePolicy](#http.cookiejar.DefaultCookiePolicy) implements the following additional methods:

- 
DefaultCookiePolicy.blocked_domains()[¶](#http.cookiejar.DefaultCookiePolicy.blocked_domains)
- Return the sequence of blocked domains (as a tuple). 

- 
DefaultCookiePolicy.set_blocked_domains(*blocked_domains*)[¶](#http.cookiejar.DefaultCookiePolicy.set_blocked_domains)
- Set the sequence of blocked domains. 

- 
DefaultCookiePolicy.is_blocked(*domain*)[¶](#http.cookiejar.DefaultCookiePolicy.is_blocked)
- Return - `True`if- *domain*is on the blocklist for setting or receiving cookies.

- 
DefaultCookiePolicy.allowed_domains()[¶](#http.cookiejar.DefaultCookiePolicy.allowed_domains)
- Return - `None`

- 
DefaultCookiePolicy.set_allowed_domains(*allowed_domains*)[¶](#http.cookiejar.DefaultCookiePolicy.set_allowed_domains)
- Set the sequence of allowed domains, or - `None`

- 
DefaultCookiePolicy.is_not_allowed(*domain*)[¶](#http.cookiejar.DefaultCookiePolicy.is_not_allowed)
- Return - `True`if- *domain*is not on the allowlist for setting or receiving cookies.

[ DefaultCookiePolicy](#http.cookiejar.DefaultCookiePolicy) instances have the following attributes, which are
all initialised from the constructor arguments of the same name, and which may
all be assigned to.

- 
DefaultCookiePolicy.rfc2109_as_netscape[¶](#http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape)
- If true, request that the - `CookieJar`- **RFC 2109**- *Set-Cookie*header with a version cookie-attribute of 1) to Netscape cookies by setting the version attribute of the- `Cookie`- `None`- **RFC 2965**

General strictness switches:

- 
DefaultCookiePolicy.strict_domain[¶](#http.cookiejar.DefaultCookiePolicy.strict_domain)
- Don’t allow sites to set two-component domains with country-code top-level domains like - `.co.uk`,- `.gov.uk`,- `.co.nz`.etc. This is far from perfect and isn’t guaranteed to work!

[ RFC 2965](https://datatracker.ietf.org/doc/html/rfc2965.html) protocol strictness switches:

- 
DefaultCookiePolicy.strict_rfc2965_unverifiable[¶](#http.cookiejar.DefaultCookiePolicy.strict_rfc2965_unverifiable)
- Follow - **RFC 2965**- *never*blocked on the basis of verifiability

Netscape protocol strictness switches:

- 
DefaultCookiePolicy.strict_ns_unverifiable[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_unverifiable)
- Apply - **RFC 2965**

- 
DefaultCookiePolicy.strict_ns_domain[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_domain)
- Flags indicating how strict to be with domain-matching rules for Netscape cookies. See below for acceptable values. 

- 
DefaultCookiePolicy.strict_ns_set_initial_dollar[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_set_initial_dollar)
- Ignore cookies in Set-Cookie: headers that have names starting with - `'$'`.

- 
DefaultCookiePolicy.strict_ns_set_path[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_set_path)
- Don’t allow setting cookies whose path doesn’t path-match request URI. 

[ strict_ns_domain](#http.cookiejar.DefaultCookiePolicy.strict_ns_domain) is a collection of flags.  Its value is constructed by
or-ing together (for example, 

`DomainStrictNoDots|DomainStrictNonDomain` means
both flags are set).- 
DefaultCookiePolicy.DomainStrictNoDots[¶](#http.cookiejar.DefaultCookiePolicy.DomainStrictNoDots)
- When setting cookies, the ‘host prefix’ must not contain a dot (eg. - `www.foo.bar.com`can’t set a cookie for- `.bar.com`, because- `www.foo`contains a dot).

- 
DefaultCookiePolicy.DomainStrictNonDomain[¶](#http.cookiejar.DefaultCookiePolicy.DomainStrictNonDomain)
- Cookies that did not explicitly specify a - `domain`cookie-attribute can only be returned to a domain equal to the domain that set the cookie (eg.- `spam.example.com`won’t be returned cookies from- `example.com`that had no- `domain`cookie-attribute).

The following attributes are provided for convenience, and are the most useful combinations of the above flags:

- 
DefaultCookiePolicy.DomainLiberal[¶](#http.cookiejar.DefaultCookiePolicy.DomainLiberal)
- Equivalent to 0 (ie. all of the above Netscape domain strictness flags switched off). 

- 
DefaultCookiePolicy.DomainStrict[¶](#http.cookiejar.DefaultCookiePolicy.DomainStrict)
- Equivalent to - `DomainStrictNoDots|DomainStrictNonDomain`.

## Cookie Objects[¶](#cookie-objects)

[ Cookie](#http.cookiejar.Cookie) instances have Python attributes roughly corresponding to the
standard cookie-attributes specified in the various cookie standards.  The
correspondence is not one-to-one, because there are complicated rules for
assigning default values, because the 

`max-age` and `expires`
cookie-attributes contain equivalent information, and because [cookies may be ‘downgraded’ by](https://datatracker.ietf.org/doc/html/rfc2109.html)

**RFC 2109**`http.cookiejar` from version 1 to version 0 (Netscape)
cookies.Assignment to these attributes should not be necessary other than in rare
circumstances in a [ CookiePolicy](#http.cookiejar.CookiePolicy) method.  The class does not enforce
internal consistency, so you should know what you’re doing if you do that.

- 
Cookie.version[¶](#http.cookiejar.Cookie.version)
- Integer or - `None`- `version`- **RFC 2965**- **RFC 2109**- `version`cookie-attribute of 1. However, note that- `http.cookiejar`may ‘downgrade’ RFC 2109 cookies to Netscape cookies, in which case- `version`is 0.

- 
Cookie.name[¶](#http.cookiejar.Cookie.name)
- Cookie name (a string). 

- 
Cookie.domain[¶](#http.cookiejar.Cookie.domain)
- Cookie domain (a string). 

- 
Cookie.path[¶](#http.cookiejar.Cookie.path)
- Cookie path (a string, eg. - `'/acme/rocket_launchers'`).

- 
Cookie.secure[¶](#http.cookiejar.Cookie.secure)
- `True`if cookie should only be returned over a secure connection.

- 
Cookie.expires[¶](#http.cookiejar.Cookie.expires)
- Integer expiry date in seconds since epoch, or - `None`- `is_expired()`

- 
Cookie.discard[¶](#http.cookiejar.Cookie.discard)
- `True`if this is a session cookie.

- 
Cookie.comment_url[¶](#http.cookiejar.Cookie.comment_url)
- URL linking to a comment from the server explaining the function of this cookie, or - `None`

- 
Cookie.rfc2109[¶](#http.cookiejar.Cookie.rfc2109)
- `True`if this cookie was received as an- **RFC 2109**- *Set-Cookie*header, and the value of the Version cookie-attribute in that header was 1). This attribute is provided because- `http.cookiejar`may ‘downgrade’ RFC 2109 cookies to Netscape cookies, in which case- `version`

- 
Cookie.port_specified[¶](#http.cookiejar.Cookie.port_specified)
- `True`if a port or set of ports was explicitly specified by the server (in the- *Set-Cookie*/- *Set-Cookie2*header).

- 
Cookie.domain_specified[¶](#http.cookiejar.Cookie.domain_specified)
- `True`if a domain was explicitly specified by the server.

- 
Cookie.domain_initial_dot[¶](#http.cookiejar.Cookie.domain_initial_dot)
- `True`if the domain explicitly specified by the server began with a dot (- `'.'`).

Cookies may have additional non-standard cookie-attributes. These may be accessed using the following methods:

- 
Cookie.has_nonstandard_attr(*name*)[¶](#http.cookiejar.Cookie.has_nonstandard_attr)
- Return - `True`if cookie has the named cookie-attribute.

- 
Cookie.get_nonstandard_attr(*name*,*default=None*)[¶](#http.cookiejar.Cookie.get_nonstandard_attr)
- If cookie has the named cookie-attribute, return its value. Otherwise, return - *default*.

- 
Cookie.set_nonstandard_attr(*name*,*value*)[¶](#http.cookiejar.Cookie.set_nonstandard_attr)
- Set the value of the named cookie-attribute. 

The [ Cookie](#http.cookiejar.Cookie) class also defines the following method:

- 
Cookie.is_expired(*now=None*)[¶](#http.cookiejar.Cookie.is_expired)
- `True`if cookie has passed the time at which the server requested it should expire. If- *now*is given (in seconds since the epoch), return whether the cookie has expired at the specified time.

## Examples[¶](#examples)

The first example shows the most common usage of `http.cookiejar`:

```
import http.cookiejar, urllib.request
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
```
This example illustrates how to open a URL using your Netscape, Mozilla, or Lynx cookies (assumes Unix/Netscape convention for location of the cookies file):

```
import os, http.cookiejar, urllib.request
cj = http.cookiejar.MozillaCookieJar()
cj.load(os.path.join(os.path.expanduser("~"), ".netscape", "cookies.txt"))
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
```
The next example illustrates the use of [ DefaultCookiePolicy](#http.cookiejar.DefaultCookiePolicy). Turn on

[cookies, be more strict about domains when setting and returning Netscape cookies, and block some domains from setting cookies or having them returned:](https://datatracker.ietf.org/doc/html/rfc2965.html)

**RFC 2965**```
import urllib.request
from http.cookiejar import CookieJar, DefaultCookiePolicy
policy = DefaultCookiePolicy(
    rfc2965=True, strict_ns_domain=Policy.DomainStrict,
    blocked_domains=["ads.net", ".ads.net"])
cj = CookieJar(policy)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
```