# telnetlib — Telnet client — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/telnetlib.html](https://docs.python.org/3.12/library/telnetlib.html)

---

`telnetlib`[¶](#module-telnetlib)

`telnetlib`**Source code:** [Lib/telnetlib.py](https://github.com/python/cpython/tree/3.12/Lib/telnetlib.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ telnetlib](#module-telnetlib) module is deprecated
(see 

[for details and alternatives).](https://peps.python.org/pep-0594/#telnetlib)

**PEP 594**The [ telnetlib](#module-telnetlib) module provides a 

[class that implements the Telnet protocol. See](#telnetlib.Telnet)

`Telnet`[for details about the protocol. In addition, it provides symbolic constants for the protocol characters (see below), and for the telnet options. The symbolic names of the telnet options follow the definitions in](https://datatracker.ietf.org/doc/html/rfc854.html)

**RFC 854**`arpa/telnet.h`, with the leading `TELOPT_` removed. For symbolic names
of options which are traditionally not included in `arpa/telnet.h`, see the
module source itself.The symbolic constants for the telnet commands are: IAC, DONT, DO, WONT, WILL, SE (Subnegotiation End), NOP (No Operation), DM (Data Mark), BRK (Break), IP (Interrupt process), AO (Abort output), AYT (Are You There), EC (Erase Character), EL (Erase Line), GA (Go Ahead), SB (Subnegotiation Begin).

[Availability](intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

- 
*class*telnetlib.Telnet(*host=None*,*port=0*[,*timeout*])[¶](#telnetlib.Telnet)
- `Telnet`- `open()`- *timeout*parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used).- Do not reopen an already connected instance. - This class has many - `read_*()`methods. Note that some of them raise- `EOFError`- A - `Telnet`- `with`- `with`block ends, the- `close()`- >>> from telnetlib import Telnet >>> with Telnet('localhost', 23) as tn: ... tn.interact() ... - Changed in version 3.6: Context manager support added 

See also

- **RFC 854**
- Definition of the Telnet protocol. 

## Telnet Objects[¶](#telnet-objects)

[ Telnet](#telnetlib.Telnet) instances have the following methods:

- 
Telnet.read_until(*expected*,*timeout=None*)[¶](#telnetlib.Telnet.read_until)
- Read until a given byte string, - *expected*, is encountered or until- *timeout*seconds have passed.- When no match is found, return whatever is available instead, possibly empty bytes. Raise - `EOFError`

- 
Telnet.read_all()[¶](#telnetlib.Telnet.read_all)
- Read all data until EOF as bytes; block until connection closed. 

- 
Telnet.read_some()[¶](#telnetlib.Telnet.read_some)
- Read at least one byte of cooked data unless EOF is hit. Return - `b''`if EOF is hit. Block if no data is immediately available.

- 
Telnet.read_very_eager()[¶](#telnetlib.Telnet.read_very_eager)
- Read everything that can be without blocking in I/O (eager). - Raise - `EOFError`- `b''`if no cooked data available otherwise. Do not block unless in the midst of an IAC sequence.

- 
Telnet.read_eager()[¶](#telnetlib.Telnet.read_eager)
- Read readily available data. - Raise - `EOFError`- `b''`if no cooked data available otherwise. Do not block unless in the midst of an IAC sequence.

- 
Telnet.read_lazy()[¶](#telnetlib.Telnet.read_lazy)
- Process and return data already in the queues (lazy). - Raise - `EOFError`- `b''`if no cooked data available otherwise. Do not block unless in the midst of an IAC sequence.

- 
Telnet.read_very_lazy()[¶](#telnetlib.Telnet.read_very_lazy)
- Return any data available in the cooked queue (very lazy). - Raise - `EOFError`- `b''`if no cooked data available otherwise. This method never blocks.

- 
Telnet.read_sb_data()[¶](#telnetlib.Telnet.read_sb_data)
- Return the data collected between a SB/SE pair (suboption begin/end). The callback should access these data when it was invoked with a - `SE`command. This method never blocks.

- 
Telnet.open(*host*,*port=0*[,*timeout*])[¶](#telnetlib.Telnet.open)
- Connect to a host. The optional second argument is the port number, which defaults to the standard Telnet port (23). The optional - *timeout*parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used).- Do not try to reopen an already connected instance. - Raises an - [auditing event](sys.html#auditing)- `telnetlib.Telnet.open`with arguments- `self`,- `host`,- `port`.

- 
Telnet.msg(*msg*,**args*)[¶](#telnetlib.Telnet.msg)
- Print a debug message when the debug level is - `>`0. If extra arguments are present, they are substituted in the message using the standard string formatting operator.

- 
Telnet.set_debuglevel(*debuglevel*)[¶](#telnetlib.Telnet.set_debuglevel)
- Set the debug level. The higher the value of - *debuglevel*, the more debug output you get (on- `sys.stdout`).

- 
Telnet.close()[¶](#telnetlib.Telnet.close)
- Close the connection. 

- 
Telnet.get_socket()[¶](#telnetlib.Telnet.get_socket)
- Return the socket object used internally. 

- 
Telnet.fileno()[¶](#telnetlib.Telnet.fileno)
- Return the file descriptor of the socket object used internally. 

- 
Telnet.write(*buffer*)[¶](#telnetlib.Telnet.write)
- Write a byte string to the socket, doubling any IAC characters. This can block if the connection is blocked. May raise - `OSError`- Raises an - [auditing event](sys.html#auditing)- `telnetlib.Telnet.write`with arguments- `self`,- `buffer`.- Changed in version 3.3: This method used to raise - `socket.error`- `OSError`

- 
Telnet.interact()[¶](#telnetlib.Telnet.interact)
- Interaction function, emulates a very dumb Telnet client. 

- 
Telnet.mt_interact()[¶](#telnetlib.Telnet.mt_interact)
- Multithreaded version of - `interact()`

- 
Telnet.expect(*list*,*timeout=None*)[¶](#telnetlib.Telnet.expect)
- Read until one from a list of a regular expressions matches. - The first argument is a list of regular expressions, either compiled ( - [regex objects](re.html#re-objects)) or uncompiled (byte strings). The optional second argument is a timeout, in seconds; the default is to block indefinitely.- Return a tuple of three items: the index in the list of the first regular expression that matches; the match object returned; and the bytes read up till and including the match. - If end of file is found and no bytes were read, raise - `EOFError`- `(-1, None, data)`where- *data*is the bytes received so far (may be empty bytes if a timeout happened).- If a regular expression ends with a greedy match (such as - `.*`) or if more than one expression can match the same input, the results are non-deterministic, and may depend on the I/O timing.

- 
Telnet.set_option_negotiation_callback(*callback*)[¶](#telnetlib.Telnet.set_option_negotiation_callback)
- Each time a telnet option is read on the input flow, this - *callback*(if set) is called with the following parameters: callback(telnet socket, command (DO/DONT/WILL/WONT), option). No other action is done afterwards by telnetlib.

## Telnet Example[¶](#telnet-example)

A simple example illustrating typical use:

```
import getpass
import telnetlib
HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"ls\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))
```