# poplib — POP3 protocol client — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/poplib.html](https://docs.python.org/3.13/library/poplib.html)

---

`poplib` — POP3 protocol client[¶](#module-poplib)

**Source code:** [Lib/poplib.py](https://github.com/python/cpython/tree/3.13/Lib/poplib.py)

This module defines a class, [ POP3](#poplib.POP3), which encapsulates a connection to a
POP3 server and implements the protocol as defined in 

[. The](https://datatracker.ietf.org/doc/html/rfc1939.html)

**RFC 1939**`POP3` class supports both the minimal and optional command sets from
[. The](https://datatracker.ietf.org/doc/html/rfc1939.html)

**RFC 1939**`POP3` class also supports the `STLS` command introduced
in [to enable encrypted communication on an already established connection.](https://datatracker.ietf.org/doc/html/rfc2595.html)

**RFC 2595**Additionally, this module provides a class [ POP3_SSL](#poplib.POP3_SSL), which provides
support for connecting to POP3 servers that use SSL as an underlying protocol
layer.

Note that POP3, though widely supported, is obsolescent.  The implementation
quality of POP3 servers varies widely, and too many are quite poor. If your
mailserver supports IMAP, you would be better off using the
[ imaplib.IMAP4](imaplib.html#imaplib.IMAP4) class, as IMAP servers tend to be better implemented.

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

The `poplib` module provides two classes:

- 
*class*poplib.POP3(*host*,*port=POP3_PORT*[,*timeout*])[¶](#poplib.POP3)
- This class implements the actual POP3 protocol. The connection is created when the instance is initialized. If - *port*is omitted, the standard POP3 port (110) is used. The optional- *timeout*parameter specifies a timeout in seconds for the connection attempt (if not specified, the global default timeout setting will be used).- Raises an - [auditing event](sys.html#auditing)- `poplib.connect`with arguments- `self`,- `host`,- `port`.- All commands will raise an - [auditing event](sys.html#auditing)- `poplib.putline`with arguments- `self`and- `line`, where- `line`is the bytes about to be sent to the remote host.- Changed in version 3.9: If the - *timeout*parameter is set to be zero, it will raise a- `ValueError`

- 
*class*poplib.POP3_SSL(*host*,*port=POP3_SSL_PORT*,***,*timeout=None*,*context=None*)[¶](#poplib.POP3_SSL)
- This is a subclass of - `POP3`- *port*is not specified, 995, the standard POP3-over-SSL port is used.- *timeout*works as in the- `POP3`constructor.- *context*is an optional- `ssl.SSLContext`- [Security considerations](ssl.html#ssl-security)for best practices.- Raises an - [auditing event](sys.html#auditing)- `poplib.connect`with arguments- `self`,- `host`,- `port`.- All commands will raise an - [auditing event](sys.html#auditing)- `poplib.putline`with arguments- `self`and- `line`, where- `line`is the bytes about to be sent to the remote host.- Changed in version 3.2: - *context*parameter added.- Changed in version 3.4: The class now supports hostname check with - `ssl.SSLContext.check_hostname`- *Server Name Indication*(see- `ssl.HAS_SNI`- Changed in version 3.9: If the - *timeout*parameter is set to be zero, it will raise a- `ValueError`- Changed in version 3.12: The deprecated - *keyfile*and- *certfile*parameters have been removed.

One exception is defined as an attribute of the `poplib` module:

- 
*exception*poplib.error_proto[¶](#poplib.error_proto)
- Exception raised on any errors from this module (errors from - `socket`

See also

- Module `imaplib`
- The standard Python IMAP module. 
- [Frequently Asked Questions About Fetchmail](http://www.catb.org/~esr/fetchmail/fetchmail-FAQ.html)
- The FAQ for the - **fetchmail**POP/IMAP client collects information on POP3 server variations and RFC noncompliance that may be useful if you need to write an application based on the POP protocol.

## POP3 Objects[¶](#pop3-objects)

All POP3 commands are represented by methods of the same name, in lowercase; most return the response text sent by the server.

A [ POP3](#poplib.POP3) instance has the following methods:

- 
POP3.set_debuglevel(*level*)[¶](#poplib.POP3.set_debuglevel)
- Set the instance’s debugging level. This controls the amount of debugging output printed. The default, - `0`, produces no debugging output. A value of- `1`produces a moderate amount of debugging output, generally a single line per request. A value of- `2`or higher produces the maximum amount of debugging output, logging each line sent and received on the control connection.

- 
POP3.getwelcome()[¶](#poplib.POP3.getwelcome)
- Returns the greeting string sent by the POP3 server. 

- 
POP3.capa()[¶](#poplib.POP3.capa)
- Query the server’s capabilities as specified in - **RFC 2449**- `{'name': ['param'...]}`.- Added in version 3.4. 

- 
POP3.user(*username*)[¶](#poplib.POP3.user)
- Send user command, response should indicate that a password is required. 

- 
POP3.pass_(*password*)[¶](#poplib.POP3.pass_)
- Send password, response includes message count and mailbox size. Note: the mailbox on the server is locked until - `quit()`

- 
POP3.apop(*user*,*secret*)[¶](#poplib.POP3.apop)
- Use the more secure APOP authentication to log into the POP3 server. 

- 
POP3.rpop(*user*)[¶](#poplib.POP3.rpop)
- Use RPOP authentication (similar to UNIX r-commands) to log into POP3 server. 

- 
POP3.stat()[¶](#poplib.POP3.stat)
- Get mailbox status. The result is a tuple of 2 integers: - `(message count, mailbox size)`.

- 
POP3.list([*which*])[¶](#poplib.POP3.list)
- Request message list, result is in the form - `(response, ['mesg_num octets', ...], octets)`. If- *which*is set, it is the message to list.

- 
POP3.retr(*which*)[¶](#poplib.POP3.retr)
- Retrieve whole message number - *which*, and set its seen flag. Result is in form- `(response, ['line', ...], octets)`.

- 
POP3.dele(*which*)[¶](#poplib.POP3.dele)
- Flag message number - *which*for deletion. On most servers deletions are not actually performed until QUIT (the major exception is Eudora QPOP, which deliberately violates the RFCs by doing pending deletes on any disconnect).

- 
POP3.rset()[¶](#poplib.POP3.rset)
- Remove any deletion marks for the mailbox. 

- 
POP3.noop()[¶](#poplib.POP3.noop)
- Do nothing. Might be used as a keep-alive. 

- 
POP3.quit()[¶](#poplib.POP3.quit)
- Signoff: commit changes, unlock mailbox, drop connection. 

- 
POP3.top(*which*,*howmuch*)[¶](#poplib.POP3.top)
- Retrieves the message header plus - *howmuch*lines of the message after the header of message number- *which*. Result is in form- `(response, ['line', ...], octets)`.- The POP3 TOP command this method uses, unlike the RETR command, doesn’t set the message’s seen flag; unfortunately, TOP is poorly specified in the RFCs and is frequently broken in off-brand servers. Test this method by hand against the POP3 servers you will use before trusting it. 

- 
POP3.uidl(*which=None*)[¶](#poplib.POP3.uidl)
- Return message digest (unique id) list. If - *which*is specified, result contains the unique id for that message in the form- `'response mesgnum uid`, otherwise result is list- `(response, ['mesgnum uid', ...], octets)`.

- 
POP3.utf8()[¶](#poplib.POP3.utf8)
- Try to switch to UTF-8 mode. Returns the server response if successful, raises - `error_proto`- **RFC 6856**- Added in version 3.5. 

- 
POP3.stls(*context=None*)[¶](#poplib.POP3.stls)
- Start a TLS session on the active connection as specified in - **RFC 2595**- *context*parameter is a- `ssl.SSLContext`- [Security considerations](ssl.html#ssl-security)for best practices.- This method supports hostname checking via - `ssl.SSLContext.check_hostname`- *Server Name Indication*(see- `ssl.HAS_SNI`- Added in version 3.4. 

Instances of [ POP3_SSL](#poplib.POP3_SSL) have no additional methods. The interface of this
subclass is identical to its parent.

## POP3 Example[¶](#pop3-example)

Here is a minimal example (without error checking) that opens a mailbox and retrieves and prints all messages:

```
import getpass, poplib
M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)
```
At the end of the module, there is a test section that contains a more extensive example of usage.