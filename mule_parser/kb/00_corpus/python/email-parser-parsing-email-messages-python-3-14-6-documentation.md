# email.parser: Parsing email messages — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/email.parser.html](https://docs.python.org/library/email.parser.html)

---

`email.parser`: Parsing email messages[¶](#module-email.parser)

**Source code:** [Lib/email/parser.py](https://github.com/python/cpython/tree/3.14/Lib/email/parser.py)

Message object structures can be created in one of two ways: they can be
created from whole cloth by creating an [ EmailMessage](email.message.html#email.message.EmailMessage)
object, adding headers using the dictionary interface, and adding payload(s)
using 

[and related methods, or they can be created by parsing a serialized representation of the email message.](email.message.html#email.message.EmailMessage.set_content)

`set_content()`The [ email](email.html#module-email) package provides a standard parser that understands most email
document structures, including MIME documents.  You can pass the parser a
bytes, string or file object, and the parser will return to you the root

[instance of the object structure. For simple, non-MIME messages the payload of this root object will likely be a string containing the text of the message. For MIME messages, the root object will return](email.message.html#email.message.EmailMessage)

`EmailMessage``True` from its [method, and the subparts can be accessed via the payload manipulation methods, such as](email.message.html#email.message.EmailMessage.is_multipart)

`is_multipart()`[,](email.message.html#email.message.EmailMessage.get_body)

`get_body()`[, and](email.message.html#email.message.EmailMessage.iter_parts)

`iter_parts()`[.](email.message.html#email.message.EmailMessage.walk)

`walk()`There are actually two parser interfaces available for use, the [ Parser](#email.parser.Parser)
API and the incremental 

[API. The](#email.parser.FeedParser)

`FeedParser``Parser` API is
most useful if you have the entire text of the message in memory, or if the
entire message lives in a file on the file system.  `FeedParser` is more
appropriate when you are reading the message from a stream which might block
waiting for more input (such as reading an email message from a socket).  The
`FeedParser` can consume and parse the message incrementally, and only
returns the root object when you close the parser.Note that the parser can be extended in limited ways, and of course you can
implement your own parser completely from scratch.  All of the logic that
connects the [ email](email.html#module-email) package’s bundled parser and the

[class is embodied in the](email.message.html#email.message.EmailMessage)

`EmailMessage`[class, so a custom parser can create message object trees any way it finds necessary by implementing custom versions of the appropriate](email.policy.html#email.policy.Policy)

`Policy``Policy`
methods.## FeedParser API[¶](#feedparser-api)

The [ BytesFeedParser](#email.parser.BytesFeedParser), imported from the 

`email.feedparser` module,
provides an API that is conducive to incremental parsing of email messages,
such as would be necessary when reading the text of an email message from a
source that can block (such as a socket).  The `BytesFeedParser` can of
course be used to parse an email message fully contained in a [bytes-like object](../glossary.html#term-bytes-like-object), string, or file, but the

[API may be more convenient for such use cases. The semantics and results of the two parser APIs are identical.](#email.parser.BytesParser)

`BytesParser`The [ BytesFeedParser](#email.parser.BytesFeedParser)’s API is simple; you create an instance, feed it a
bunch of bytes until there’s no more to feed it, then close the parser to
retrieve the root message object.  The 

`BytesFeedParser` is extremely
accurate when parsing standards-compliant messages, and it does a very good job
of parsing non-compliant messages, providing information about how a message
was deemed broken.  It will populate a message object’s
[attribute with a list of any problems it found in a message. See the](email.message.html#email.message.EmailMessage.defects)

`defects`[module for the list of defects that it can find.](email.errors.html#module-email.errors)

`email.errors`Here is the API for the [ BytesFeedParser](#email.parser.BytesFeedParser):

- 
*class*email.parser.BytesFeedParser(*_factory=None*,***,*policy=policy.compat32*)[¶](#email.parser.BytesFeedParser)
- Create a - `BytesFeedParser`instance. Optional- *_factory*is a no-argument callable; if not specified use the- `message_factory`- *policy*. Call- *_factory*whenever a new message object is needed.- If - *policy*is specified use the rules it specifies to update the representation of the message. If- *policy*is not set, use the- `compat32`- `Message`- `EmailMessage`- *_factory*. For more information on what else- *policy*controls, see the- `policy`- Note: - **The policy keyword should always be specified**; The default will change to- `email.policy.default`- Added in version 3.2. - Changed in version 3.3: Added the - *policy*keyword.- Changed in version 3.6: - *_factory*defaults to the policy- `message_factory`.- 
feed(*data*)[¶](#email.parser.BytesFeedParser.feed)
- Feed the parser some more data. - *data*should be a- [bytes-like object](../glossary.html#term-bytes-like-object)containing one or more lines. The lines can be partial and the parser will stitch such partial lines together properly. The lines can have any of the three common line endings: carriage return, newline, or carriage return and newline (they can even be mixed).
 
- 
feed(

- 
*class*email.parser.FeedParser(*_factory=None*,***,*policy=policy.compat32*)[¶](#email.parser.FeedParser)
- Works like - `BytesFeedParser`- `feed()`- `utf8`- `True`, no binary attachments.- Changed in version 3.3: Added the - *policy*keyword.

## Parser API[¶](#parser-api)

The [ BytesParser](#email.parser.BytesParser) class, imported from the 

`email.parser` module,
provides an API that can be used to parse a message when the complete contents
of the message are available in a [bytes-like object](../glossary.html#term-bytes-like-object)or file. The

`email.parser` module also provides [for parsing strings, and header-only parsers,](#email.parser.Parser)

`Parser`[and](#email.parser.BytesHeaderParser)

`BytesHeaderParser`[, which can be used if you’re only interested in the headers of the message.](#email.parser.HeaderParser)

`HeaderParser``BytesHeaderParser` and `HeaderParser`
can be much faster in these situations, since they do not attempt to parse the
message body, instead setting the payload to the raw body.- 
*class*email.parser.BytesParser(*_class=None*,***,*policy=policy.compat32*)[¶](#email.parser.BytesParser)
- Create a - `BytesParser`instance. The- *_class*and- *policy*arguments have the same meaning and semantics as the- *_factory*and- *policy*arguments of- `BytesFeedParser`- Note: - **The policy keyword should always be specified**; The default will change to- `email.policy.default`- Changed in version 3.3: Removed the - *strict*argument that was deprecated in 2.4. Added the- *policy*keyword.- Changed in version 3.6: - *_class*defaults to the policy- `message_factory`.- 
parse(*fp*,*headersonly=False*)[¶](#email.parser.BytesParser.parse)
- Read all the data from the binary file-like object - *fp*, parse the resulting bytes, and return the message object.- *fp*must support both the- `readline()`- `read()`- The bytes contained in - *fp*must be formatted as a block of- **RFC 5322**- `utf8`- `True`,- **RFC 6532**- *Content-Transfer-Encoding*of- `8bit`).- Optional - *headersonly*is a flag specifying whether to stop parsing after reading the headers or not. The default is- `False`, meaning it parses the entire contents of the file.
 - 
parsebytes(*bytes*,*headersonly=False*)[¶](#email.parser.BytesParser.parsebytes)
- Similar to the - `parse()`- [bytes-like object](../glossary.html#term-bytes-like-object)instead of a file-like object. Calling this method on a bytes-like object is equivalent to wrapping- *bytes*in a- `BytesIO`- `parse()`.- Optional - *headersonly*is as with the- `parse()`
 - Added in version 3.2. 
- 
parse(

- 
*class*email.parser.BytesHeaderParser(*_class=None*,***,*policy=policy.compat32*)[¶](#email.parser.BytesHeaderParser)
- Exactly like - `BytesParser`- *headersonly*defaults to- `True`.- Added in version 3.3. 

- 
*class*email.parser.Parser(*_class=None*,***,*policy=policy.compat32*)[¶](#email.parser.Parser)
- This class is parallel to - `BytesParser`- Changed in version 3.3: Removed the - *strict*argument. Added the- *policy*keyword.- Changed in version 3.6: - *_class*defaults to the policy- `message_factory`.- 
parse(*fp*,*headersonly=False*)[¶](#email.parser.Parser.parse)
- Read all the data from the text-mode file-like object - *fp*, parse the resulting text, and return the root message object.- *fp*must support both the- `readline()`- `read()`- Other than the text mode requirement, this method operates like - `BytesParser.parse()`
 
- 
parse(

- 
*class*email.parser.HeaderParser(*_class=None*,***,*policy=policy.compat32*)[¶](#email.parser.HeaderParser)
- Exactly like - `Parser`- *headersonly*defaults to- `True`.

Since creating a message object structure from a string or a file object is such
a common task, four functions are provided as a convenience.  They are available
in the top-level [ email](email.html#module-email) package namespace.

- 
email.message_from_bytes(*s*,*_class=None*,***,*policy=policy.compat32*)[¶](#email.message_from_bytes)
- Return a message object structure from a - [bytes-like object](../glossary.html#term-bytes-like-object). This is equivalent to- `BytesParser().parsebytes(s)`. Optional- *_class*and- *policy*are interpreted as with the- `BytesParser`- Added in version 3.2. - Changed in version 3.3: Removed the - *strict*argument. Added the- *policy*keyword.

- 
email.message_from_binary_file(*fp*,*_class=None*,***,*policy=policy.compat32*)[¶](#email.message_from_binary_file)
- Return a message object structure tree from an open binary - [file object](../glossary.html#term-file-object). This is equivalent to- `BytesParser().parse(fp)`.- *_class*and- *policy*are interpreted as with the- `BytesParser`- Added in version 3.2. - Changed in version 3.3: Removed the - *strict*argument. Added the- *policy*keyword.

- 
email.message_from_string(*s*,*_class=None*,***,*policy=policy.compat32*)[¶](#email.message_from_string)
- Return a message object structure from a string. This is equivalent to - `Parser().parsestr(s)`.- *_class*and- *policy*are interpreted as with the- `Parser`- Changed in version 3.3: Removed the - *strict*argument. Added the- *policy*keyword.

- 
email.message_from_file(*fp*,*_class=None*,***,*policy=policy.compat32*)[¶](#email.message_from_file)
- Return a message object structure tree from an open - [file object](../glossary.html#term-file-object). This is equivalent to- `Parser().parse(fp)`.- *_class*and- *policy*are interpreted as with the- `Parser`- Changed in version 3.3: Removed the - *strict*argument. Added the- *policy*keyword.- Changed in version 3.6: - *_class*defaults to the policy- `message_factory`.

Here’s an example of how you might use [ message_from_bytes()](#email.message_from_bytes) at an
interactive Python prompt:

```
>>> import email
>>> msg = email.message_from_bytes(myBytes)
```
## Additional notes[¶](#additional-notes)

Here are some notes on the parsing semantics:

- Most non- - *multipart*type messages are parsed as a single message object with a string payload. These objects will return- `False`for- `is_multipart()`- `iter_parts()`
- All - *multipart*type messages will be parsed as a container message object with a list of sub-message objects for their payload. The outer container message will return- `True`for- `is_multipart()`- `iter_parts()`
- Most messages with a content type of - *message/**(such as- *message/delivery-status*and- *message/rfc822*) will also be parsed as container object containing a list payload of length 1. Their- `is_multipart()`- `True`. The single element yielded by- `iter_parts()`
- Some non-standards-compliant messages may not be internally consistent about their - *multipart*-edness. Such messages may have a- *Content-Type*header of type- *multipart*, but their- `is_multipart()`- `False`. If such messages were parsed with the- `FeedParser`- `MultipartInvariantViolationDefect`- *defects*attribute list. See- `email.errors`