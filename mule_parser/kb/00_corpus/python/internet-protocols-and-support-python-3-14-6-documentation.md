# Internet Protocols and Support — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/internet.html](https://docs.python.org/library/internet.html)

---

# Internet Protocols and Support[¶](#internet-protocols-and-support)

The modules described in this chapter implement internet protocols and  support
for related technology.  They are all implemented in Python. Most of these
modules require the presence of the system-dependent module [ socket](socket.html#module-socket), which
is currently supported on most popular platforms.  Here is an overview:

- `webbrowser`— Convenient web-browser controller
- `wsgiref`— WSGI Utilities and Reference Implementation
- `urllib`— URL handling modules
- `urllib.request`— Extensible library for opening URLs- [Request Objects](urllib.request.html#request-objects)
- [OpenerDirector Objects](urllib.request.html#openerdirector-objects)
- [BaseHandler Objects](urllib.request.html#basehandler-objects)
- [HTTPRedirectHandler Objects](urllib.request.html#httpredirecthandler-objects)
- [HTTPCookieProcessor Objects](urllib.request.html#httpcookieprocessor-objects)
- [ProxyHandler Objects](urllib.request.html#proxyhandler-objects)
- [HTTPPasswordMgr Objects](urllib.request.html#httppasswordmgr-objects)
- [HTTPPasswordMgrWithPriorAuth Objects](urllib.request.html#httppasswordmgrwithpriorauth-objects)
- [AbstractBasicAuthHandler Objects](urllib.request.html#abstractbasicauthhandler-objects)
- [HTTPBasicAuthHandler Objects](urllib.request.html#httpbasicauthhandler-objects)
- [ProxyBasicAuthHandler Objects](urllib.request.html#proxybasicauthhandler-objects)
- [AbstractDigestAuthHandler Objects](urllib.request.html#abstractdigestauthhandler-objects)
- [HTTPDigestAuthHandler Objects](urllib.request.html#httpdigestauthhandler-objects)
- [ProxyDigestAuthHandler Objects](urllib.request.html#proxydigestauthhandler-objects)
- [HTTPHandler Objects](urllib.request.html#httphandler-objects)
- [HTTPSHandler Objects](urllib.request.html#httpshandler-objects)
- [FileHandler Objects](urllib.request.html#filehandler-objects)
- [DataHandler Objects](urllib.request.html#datahandler-objects)
- [FTPHandler Objects](urllib.request.html#ftphandler-objects)
- [CacheFTPHandler Objects](urllib.request.html#cacheftphandler-objects)
- [UnknownHandler Objects](urllib.request.html#unknownhandler-objects)
- [HTTPErrorProcessor Objects](urllib.request.html#httperrorprocessor-objects)
- [Examples](urllib.request.html#examples)
- [Legacy interface](urllib.request.html#legacy-interface)
- `urllib.request`Restrictions
 
- `urllib.response`— Response classes used by urllib
- `urllib.parse`— Parse URLs into components
- `urllib.error`— Exception classes raised by urllib.request
- `urllib.robotparser`— Parser for robots.txt
- `http`— HTTP modules
- `http.client`— HTTP protocol client
- `ftplib`— FTP protocol client
- `poplib`— POP3 protocol client
- `imaplib`— IMAP4 protocol client
- `smtplib`— SMTP protocol client
- `uuid`— UUID objects according to- **RFC 9562**
- `socketserver`— A framework for network servers
- `http.server`— HTTP servers
- `http.cookies`— HTTP state management
- `http.cookiejar`— Cookie handling for HTTP clients
- `xmlrpc`— XMLRPC server and client modules
- `xmlrpc.client`— XML-RPC client access
- `xmlrpc.server`— Basic XML-RPC servers
- `ipaddress`— IPv4/IPv6 manipulation library