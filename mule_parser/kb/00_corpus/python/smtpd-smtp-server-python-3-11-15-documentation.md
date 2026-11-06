# smtpd — SMTP Server — Python 3.11.15 documentation

**Source:** [https://docs.python.org/3.11/library/smtpd.html](https://docs.python.org/3.11/library/smtpd.html)

---

`smtpd`[¶](#module-smtpd)

`smtpd`**Source code:** [Lib/smtpd.py](https://github.com/python/cpython/tree/3.11/Lib/smtpd.py)

This module offers several classes to implement SMTP (email) servers.

Deprecated since version 3.6, will be removed in version 3.12: The [ smtpd](#module-smtpd) module is deprecated
(see 

[for details). The](https://peps.python.org/pep-0594/#smtpd)

**PEP 594**[aiosmtpd](https://aiosmtpd.readthedocs.io/)package is a recommended replacement for this module. It is based on

[and provides a more straightforward API.](asyncio.html#module-asyncio)

`asyncio`Several server implementations are present; one is a generic do-nothing implementation, which can be overridden, while the other two offer specific mail-sending strategies.

Additionally the SMTPChannel may be extended to implement very specific interaction behaviour with SMTP clients.

The code supports [ RFC 5321](https://datatracker.ietf.org/doc/html/rfc5321.html), plus the 

[SIZE and](https://datatracker.ietf.org/doc/html/rfc1870.html)

**RFC 1870**[SMTPUTF8 extensions.](https://datatracker.ietf.org/doc/html/rfc6531.html)

**RFC 6531**[Availability](intro.html#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

## SMTPServer Objects[¶](#smtpserver-objects)

- 
*class*smtpd.SMTPServer(*localaddr*,*remoteaddr*,*data_size_limit=33554432*,*map=None*,*enable_SMTPUTF8=False*,*decode_data=False*)[¶](#smtpd.SMTPServer)
- Create a new - `SMTPServer`- *localaddr*. It will treat- *remoteaddr*as an upstream SMTP relayer. Both- *localaddr*and- *remoteaddr*should be a- [(host, port)](socket.html#host-port)tuple. The object inherits from- `asyncore.dispatcher`- `asyncore`- *data_size_limit*specifies the maximum number of bytes that will be accepted in a- `DATA`command. A value of- `None`or- `0`means no limit.- *map*is the socket map to use for connections (an initially empty dictionary is a suitable value). If not specified the- `asyncore`- *enable_SMTPUTF8*determines whether the- `SMTPUTF8`extension (as defined in- **RFC 6531**- `False`. When- `True`,- `SMTPUTF8`is accepted as a parameter to the- `MAIL`command and when present is passed to- `process_message()`- `kwargs['mail_options']`list.- *decode_data*and- *enable_SMTPUTF8*cannot be set to- `True`at the same time.- *decode_data*specifies whether the data portion of the SMTP transaction should be decoded using UTF-8. When- *decode_data*is- `False`(the default), the server advertises the- `8BITMIME`extension (- **RFC 6152**- `BODY=8BITMIME`parameter to the- `MAIL`command, and when present passes it to- `process_message()`- `kwargs['mail_options']`list.- *decode_data*and- *enable_SMTPUTF8*cannot be set to- `True`at the same time.- 
process_message(*peer*,*mailfrom*,*rcpttos*,*data*,***kwargs*)[¶](#smtpd.SMTPServer.process_message)
- Raise a - `NotImplementedError`- *remoteaddr*will be available as the- `_remoteaddr`attribute.- *peer*is the remote host’s address,- *mailfrom*is the envelope originator,- *rcpttos*are the envelope recipients and- *data*is a string containing the contents of the e-mail (which should be in- **RFC 5321**- If the - *decode_data*constructor keyword is set to- `True`, the- *data*argument will be a unicode string. If it is set to- `False`, it will be a bytes object.- *kwargs*is a dictionary containing additional information. It is empty if- `decode_data=True`was given as an init argument, otherwise it contains the following keys:- *mail_options*:
- a list of all received parameters to the - `MAIL`command (the elements are uppercase strings; example:- `['BODY=8BITMIME', 'SMTPUTF8']`).
- *rcpt_options*:
- same as - *mail_options*but for the- `RCPT`command. Currently no- `RCPT TO`options are supported, so for now this will always be an empty list.
 - Implementations of - `process_message`should use the- `**kwargs`signature to accept arbitrary keyword arguments, since future feature enhancements may add keys to the kwargs dictionary.- Return - `None`to request a normal- `250 Ok`response; otherwise return the desired response string in- **RFC 5321**
 - 
channel_class[¶](#smtpd.SMTPServer.channel_class)
- Override this in subclasses to use a custom - `SMTPChannel`
 - New in version 3.4: The - *map*constructor argument.- Changed in version 3.5: - *localaddr*and- *remoteaddr*may now contain IPv6 addresses.- New in version 3.5: The - *decode_data*and- *enable_SMTPUTF8*constructor parameters, and the- *kwargs*parameter to- `process_message()`- *decode_data*is- `False`.- Changed in version 3.6: - *decode_data*is now- `False`by default.
- 
process_message(

## DebuggingServer Objects[¶](#debuggingserver-objects)

- 
*class*smtpd.DebuggingServer(*localaddr*,*remoteaddr*)[¶](#smtpd.DebuggingServer)
- Create a new debugging server. Arguments are as per - `SMTPServer`

## PureProxy Objects[¶](#pureproxy-objects)

- 
*class*smtpd.PureProxy(*localaddr*,*remoteaddr*)[¶](#smtpd.PureProxy)
- Create a new pure proxy server. Arguments are as per - `SMTPServer`- *remoteaddr*. Note that running this has a good chance to make you into an open relay, so please be careful.

## SMTPChannel Objects[¶](#smtpchannel-objects)

- 
*class*smtpd.SMTPChannel(*server*,*conn*,*addr*,*data_size_limit=33554432*,*map=None*,*enable_SMTPUTF8=False*,*decode_data=False*)[¶](#smtpd.SMTPChannel)
- Create a new - `SMTPChannel`- *conn*and- *addr*are as per the instance variables described below.- *data_size_limit*specifies the maximum number of bytes that will be accepted in a- `DATA`command. A value of- `None`or- `0`means no limit.- *enable_SMTPUTF8*determines whether the- `SMTPUTF8`extension (as defined in- **RFC 6531**- `False`.- *decode_data*and- *enable_SMTPUTF8*cannot be set to- `True`at the same time.- A dictionary can be specified in - *map*to avoid using a global socket map.- *decode_data*specifies whether the data portion of the SMTP transaction should be decoded using UTF-8. The default is- `False`.- *decode_data*and- *enable_SMTPUTF8*cannot be set to- `True`at the same time.- To use a custom SMTPChannel implementation you need to override the - `SMTPServer.channel_class`- `SMTPServer`- Changed in version 3.5: The - *decode_data*and- *enable_SMTPUTF8*parameters were added.- Changed in version 3.6: - *decode_data*is now- `False`by default.- The - `SMTPChannel`- 
smtp_server[¶](#smtpd.SMTPChannel.smtp_server)
- Holds the - `SMTPServer`
 - 
conn[¶](#smtpd.SMTPChannel.conn)
- Holds the socket object connecting to the client. 
 - 
addr[¶](#smtpd.SMTPChannel.addr)
- Holds the address of the client, the second value returned by - `socket.accept`
 - 
received_lines[¶](#smtpd.SMTPChannel.received_lines)
- Holds a list of the line strings (decoded using UTF-8) received from the client. The lines have their - `"\r\n"`line ending translated to- `"\n"`.
 - 
smtp_state[¶](#smtpd.SMTPChannel.smtp_state)
- Holds the current state of the channel. This will be either - `COMMAND`initially and then- `DATA`after the client sends a “DATA” line.
 - 
seen_greeting[¶](#smtpd.SMTPChannel.seen_greeting)
- Holds a string containing the greeting sent by the client in its “HELO”. 
 - 
mailfrom[¶](#smtpd.SMTPChannel.mailfrom)
- Holds a string containing the address identified in the “MAIL FROM:” line from the client. 
 - 
rcpttos[¶](#smtpd.SMTPChannel.rcpttos)
- Holds a list of strings containing the addresses identified in the “RCPT TO:” lines from the client. 
 - 
received_data[¶](#smtpd.SMTPChannel.received_data)
- Holds a string containing all of the data sent by the client during the DATA state, up to but not including the terminating - `"\r\n.\r\n"`.
 - 
fqdn[¶](#smtpd.SMTPChannel.fqdn)
- Holds the fully qualified domain name of the server as returned by - `socket.getfqdn()`
 - The - `SMTPChannel`- `smtp_<command>`upon reception of a command line from the client. Built into the base- `SMTPChannel`- Command - Action taken - HELO - Accepts the greeting from the client and stores it in - `seen_greeting`- EHLO - Accepts the greeting from the client and stores it in - `seen_greeting`- NOOP - Takes no action. - QUIT - Closes the connection cleanly. - MAIL - Accepts the “MAIL FROM:” syntax and stores the supplied address as - `mailfrom`- **RFC 1870**- *data_size_limit*.- RCPT - Accepts the “RCPT TO:” syntax and stores the supplied addresses in the - `rcpttos`- RSET - Resets the - `mailfrom`- `rcpttos`- `received_data`- DATA - Sets the internal state to - `DATA`and stores remaining lines from the client in- `received_data`- `"\r\n.\r\n"`is received.- HELP - Returns minimal information on command syntax - VRFY - Returns code 252 (the server doesn’t know if the address is valid) - EXPN - Reports that the command is not implemented. 
- 
smtp_server