# email.errors: Exception and Defect classes — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/email.errors.html](https://docs.python.org/library/email.errors.html)

---

`email.errors`: Exception and Defect classes[¶](#module-email.errors)

**Source code:** [Lib/email/errors.py](https://github.com/python/cpython/tree/3.14/Lib/email/errors.py)

The following exception classes are defined in the `email.errors` module:

- 
*exception*email.errors.MessageError[¶](#email.errors.MessageError)
- This is the base class for all exceptions that the - `email`- `Exception`

- 
*exception*email.errors.MessageParseError[¶](#email.errors.MessageParseError)
- This is the base class for exceptions raised by the - `Parser`- `MessageError`- `headerregistry`

- 
*exception*email.errors.HeaderParseError[¶](#email.errors.HeaderParseError)
- Raised under some error conditions when parsing the - **RFC 5322**- `MessageParseError`- `set_boundary()`- `Header`

- 
*exception*email.errors.BoundaryError[¶](#email.errors.BoundaryError)
- Deprecated and no longer used. 

- 
*exception*email.errors.MultipartConversionError[¶](#email.errors.MultipartConversionError)
- Raised if the - `attach()`- `MIMENonMultipart`- `MIMEImage`- `MultipartConversionError`multiply inherits from- `MessageError`- `TypeError`

- 
*exception*email.errors.HeaderWriteError[¶](#email.errors.HeaderWriteError)
- Raised when an error occurs when the - `generator`

- 
*exception*email.errors.MessageDefect[¶](#email.errors.MessageDefect)
- This is the base class for all defects found when parsing email messages. It is derived from - `ValueError`

- 
*exception*email.errors.HeaderDefect[¶](#email.errors.HeaderDefect)
- This is the base class for all defects found when parsing email headers. It is derived from - `MessageDefect`

Here is the list of the defects that the [ FeedParser](email.parser.html#email.parser.FeedParser)
can find while parsing messages.  Note that the defects are added to the message
where the problem was found, so for example, if a message nested inside a

*multipart/alternative*had a malformed header, that nested message object would have a defect, but the containing messages would not.

All defect classes are subclassed from [ email.errors.MessageDefect](#email.errors.MessageDefect).

- 
*exception*email.errors.NoBoundaryInMultipartDefect[¶](#email.errors.NoBoundaryInMultipartDefect)
- A message claimed to be a multipart, but had no - *boundary*parameter.

- 
*exception*email.errors.StartBoundaryNotFoundDefect[¶](#email.errors.StartBoundaryNotFoundDefect)
- The start boundary claimed in the - *Content-Type*header was never found.

- 
*exception*email.errors.CloseBoundaryNotFoundDefect[¶](#email.errors.CloseBoundaryNotFoundDefect)
- A start boundary was found, but no corresponding close boundary was ever found. - Added in version 3.3. 

- 
*exception*email.errors.FirstHeaderLineIsContinuationDefect[¶](#email.errors.FirstHeaderLineIsContinuationDefect)
- The message had a continuation line as its first header line. 

- 
*exception*email.errors.MisplacedEnvelopeHeaderDefect[¶](#email.errors.MisplacedEnvelopeHeaderDefect)
- A “Unix From” header was found in the middle of a header block. 

- 
*exception*email.errors.MissingHeaderBodySeparatorDefect[¶](#email.errors.MissingHeaderBodySeparatorDefect)
- A line was found while parsing headers that had no leading white space but contained no ‘:’. Parsing continues assuming that the line represents the first line of the body. - Added in version 3.3. 

- 
*exception*email.errors.MalformedHeaderDefect[¶](#email.errors.MalformedHeaderDefect)
- A header was found that was missing a colon, or was otherwise malformed. - Deprecated since version 3.3: This defect has not been used for several Python versions. 

- 
*exception*email.errors.MultipartInvariantViolationDefect[¶](#email.errors.MultipartInvariantViolationDefect)
- A message claimed to be a - *multipart*, but no subparts were found. Note that when a message has this defect, its- `is_multipart()`- `False`even though its content type claims to be- *multipart*.

- 
*exception*email.errors.InvalidBase64PaddingDefect[¶](#email.errors.InvalidBase64PaddingDefect)
- When decoding a block of base64 encoded bytes, the padding was not correct. Enough padding is added to perform the decode, but the resulting decoded bytes may be invalid. 

- 
*exception*email.errors.InvalidBase64CharactersDefect[¶](#email.errors.InvalidBase64CharactersDefect)
- When decoding a block of base64 encoded bytes, characters outside the base64 alphabet were encountered. The characters are ignored, but the resulting decoded bytes may be invalid. 

- 
*exception*email.errors.InvalidBase64LengthDefect[¶](#email.errors.InvalidBase64LengthDefect)
- When decoding a block of base64 encoded bytes, the number of non-padding base64 characters was invalid (1 more than a multiple of 4). The encoded block was kept as-is. 

- 
*exception*email.errors.InvalidDateDefect[¶](#email.errors.InvalidDateDefect)
- When decoding an invalid or unparsable date field. The original value is kept as-is.