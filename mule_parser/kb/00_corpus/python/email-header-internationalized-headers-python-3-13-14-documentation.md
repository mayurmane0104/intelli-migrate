# email.header: Internationalized headers — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/email.header.html](https://docs.python.org/3.13/library/email.header.html)

---

`email.header`: Internationalized headers[¶](#module-email.header)

**Source code:** [Lib/email/header.py](https://github.com/python/cpython/tree/3.13/Lib/email/header.py)

This module is part of the legacy (`Compat32`) email API.  In the current API
encoding and decoding of headers is handled transparently by the
dictionary-like API of the [ EmailMessage](email.message.html#email.message.EmailMessage) class.  In
addition to uses in legacy code, this module can be useful in applications that
need to completely control the character sets used when encoding headers.

The remaining text in this section is the original documentation of the module.

[ RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822.html) is the base standard that describes the format of email messages.
It derives from the older 

[standard which came into widespread use at a time when most email was composed of ASCII characters only.](https://datatracker.ietf.org/doc/html/rfc822.html)

**RFC 822**[is a specification written assuming email contains only 7-bit ASCII characters.](https://datatracker.ietf.org/doc/html/rfc2822.html)

**RFC 2822**Of course, as email has been deployed worldwide, it has become
internationalized, such that language specific character sets can now be used in
email messages.  The base standard still requires email messages to be
transferred using only 7-bit ASCII characters, so a slew of RFCs have been
written describing how to encode email containing non-ASCII characters into
[ RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822.html)-compliant format. These RFCs include 

[,](https://datatracker.ietf.org/doc/html/rfc2045.html)

**RFC 2045**[,](https://datatracker.ietf.org/doc/html/rfc2046.html)

**RFC 2046**[, and](https://datatracker.ietf.org/doc/html/rfc2047.html)

**RFC 2047**[. The](https://datatracker.ietf.org/doc/html/rfc2231.html)

**RFC 2231**[package supports these standards in its](email.html#module-email)

`email``email.header` and [modules.](email.charset.html#module-email.charset)

`email.charset`If you want to include non-ASCII characters in your email headers, say in the
*Subject* or *To* fields, you should use the
[ Header](#email.header.Header) class and assign the field in the 

[object to an instance of](email.compat32-message.html#email.message.Message)

`Message``Header` instead of using a string for the header
value.  Import the `Header` class from the `email.header` module.
For example:```
>>> from email.message import Message
>>> from email.header import Header
>>> msg = Message()
>>> h = Header('p\xf6stal', 'iso-8859-1')
>>> msg['Subject'] = h
>>> msg.as_string()
'Subject: =?iso-8859-1?q?p=F6stal?=\n\n'
```
Notice here how we wanted the *Subject* field to contain a non-ASCII
character?  We did this by creating a [ Header](#email.header.Header) instance and passing in
the character set that the byte string was encoded in.  When the subsequent

[instance was flattened, the](email.compat32-message.html#email.message.Message)

`Message`*Subject*field was properly

[encoded. MIME-aware mail readers would show this header using the embedded ISO-8859-1 character.](https://datatracker.ietf.org/doc/html/rfc2047.html)

**RFC 2047**Here is the [ Header](#email.header.Header) class description:

- 
*class*email.header.Header(*s=None*,*charset=None*,*maxlinelen=None*,*header_name=None*,*continuation_ws=' '*,*errors='strict'*)[¶](#email.header.Header)
- Create a MIME-compliant header that can contain strings in different character sets. - Optional - *s*is the initial header value. If- `None`(the default), the initial header value is not set. You can later append to the header with- `append()`- *s*may be an instance of- `bytes`- `str`- `append()`documentation for semantics.- Optional - *charset*serves two purposes: it has the same meaning as the- *charset*argument to the- `append()`- `append()`calls that omit the- *charset*argument. If- *charset*is not provided in the constructor (the default), the- `us-ascii`character set is used both as- *s*’s initial charset and as the default for subsequent- `append()`calls.- The maximum line length can be specified explicitly via - *maxlinelen*. For splitting the first line to a shorter value (to account for the field header which isn’t included in- *s*, e.g.- *Subject*) pass in the name of the field in- *header_name*. The default- *maxlinelen*is 78, and the default value for- *header_name*is- `None`, meaning it is not taken into account for the first line of a long, split header.- Optional - *continuation_ws*must be- **RFC 2822**- *continuation_ws*defaults to a single space character.- Optional - *errors*is passed straight through to the- `append()`- 
append(*s*,*charset=None*,*errors='strict'*)[¶](#email.header.Header.append)
- Append the string - *s*to the MIME header.- Optional - *charset*, if given, should be a- `Charset`- `email.charset`- `Charset`instance. A value of- `None`(the default) means that the- *charset*given in the constructor is used.- *s*may be an instance of- `bytes`- `str`- `bytes`, then- *charset*is the encoding of that byte string, and a- `UnicodeError`- If - *s*is an instance of- `str`- *charset*is a hint specifying the character set of the characters in the string.- In either case, when producing an - **RFC 2822**- **RFC 2047**- Optional - *errors*is passed as the errors argument to the decode call if- *s*is a byte string.
 - 
encode(*splitchars=';, \t'*,*maxlinelen=None*,*linesep='\n'*)[¶](#email.header.Header.encode)
- Encode a message header into an RFC-compliant format, possibly wrapping long lines and encapsulating non-ASCII parts in base64 or quoted-printable encodings. - Optional - *splitchars*is a string containing characters which should be given extra weight by the splitting algorithm during normal header wrapping. This is in very rough support of- **RFC 2822**- **RFC 2047**- *maxlinelen*, if given, overrides the instance’s value for the maximum line length.- *linesep*specifies the characters used to separate the lines of the folded header. It defaults to the most useful value for Python application code (- `\n`), but- `\r\n`can be specified in order to produce headers with RFC-compliant line separators.- Changed in version 3.2: Added the - *linesep*argument.
 - The - `Header`class also provides a number of methods to support standard operators and built-in functions.- 
__str__()[¶](#email.header.Header.__str__)
- Returns an approximation of the - `Header`as a string, using an unlimited line length. All pieces are converted to unicode using the specified encoding and joined together appropriately. Any pieces with a charset of- `'unknown-8bit'`are decoded as ASCII using the- `'replace'`error handler.- Changed in version 3.2: Added handling for the - `'unknown-8bit'`charset.
 - 
__eq__(*other*)[¶](#email.header.Header.__eq__)
- This method allows you to compare two - `Header`instances for equality.
 - 
__ne__(*other*)[¶](#email.header.Header.__ne__)
- This method allows you to compare two - `Header`instances for inequality.
 
- 
append(

The `email.header` module also provides the following convenient functions.

- 
email.header.decode_header(*header*)[¶](#email.header.decode_header)
- Decode a message header value without converting the character set. The header value is in - *header*.- For historical reasons, this function may return either: - A list of pairs containing each of the decoded parts of the header, - `(decoded_bytes, charset)`, where- *decoded_bytes*is always an instance of- `bytes`- *charset*is either:- A lower case string containing the name of the character set specified. 
- `None`for non-encoded parts of the header.
 
- A list of length 1 containing a pair - `(string, None)`, where- *string*is always an instance of- `str`
 - An - `email.errors.HeaderParseError`- Here are examples: - >>> from email.header import decode_header >>> decode_header('=?iso-8859-1?q?p=F6stal?=') [(b'p\xf6stal', 'iso-8859-1')] >>> decode_header('unencoded_string') [('unencoded_string', None)] >>> decode_header('bar =?utf-8?B?ZsOzbw==?=') [(b'bar ', None), (b'f\xc3\xb3o', 'utf-8')] - Note - This function exists for backwards compatibility only. For new code, we recommend using - `email.headerregistry.HeaderRegistry`

- 
email.header.make_header(*decoded_seq*,*maxlinelen=None*,*header_name=None*,*continuation_ws=' '*)[¶](#email.header.make_header)
- Create a - `Header`- `decode_header()`- `decode_header()`- `(decoded_string, charset)`where- *charset*is the name of the character set.- This function takes one of those sequence of pairs and returns a - `Header`- *maxlinelen*,- *header_name*, and- *continuation_ws*are as in the- `Header`constructor.- Note - This function exists for backwards compatibility only, and is not recommended for use in new code.