# email.generator: Generating MIME documents — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/email.generator.html](https://docs.python.org/3.13/library/email.generator.html)

---

`email.generator`: Generating MIME documents[¶](#module-email.generator)

**Source code:** [Lib/email/generator.py](https://github.com/python/cpython/tree/3.13/Lib/email/generator.py)

One of the most common tasks is to generate the flat (serialized) version of
the email message represented by a message object structure.  You will need to
do this if you want to send your message via [ smtplib.SMTP.sendmail()](smtplib.html#smtplib.SMTP.sendmail),
or print the message on the console.  Taking a
message object structure and producing a serialized representation is the job
of the generator classes.

As with the [ email.parser](email.parser.html#module-email.parser) module, you aren’t limited to the functionality
of the bundled generator; you could write one from scratch yourself.  However
the bundled generator knows how to generate most email in a standards-compliant
way, should handle MIME and non-MIME email messages just fine, and is designed
so that the bytes-oriented parsing and generation operations are inverses,
assuming the same non-transforming 

[is used for both. That is, parsing the serialized byte stream via the](email.policy.html#module-email.policy)

`policy`[class and then regenerating the serialized byte stream using](email.parser.html#email.parser.BytesParser)

`BytesParser`[should produce output identical to the input](#email.generator.BytesGenerator)

`BytesGenerator`[[1]](#id3). (On the other hand, using the generator on an

[constructed by program may result in changes to the](email.message.html#email.message.EmailMessage)

`EmailMessage``EmailMessage` object as defaults are
filled in.)The [ Generator](#email.generator.Generator) class can be used to flatten a message into a text (as
opposed to binary) serialized representation, but since Unicode cannot
represent binary data directly, the message is of necessity transformed into
something that contains only ASCII characters, using the standard email RFC
Content Transfer Encoding techniques for encoding email messages for transport
over channels that are not “8 bit clean”.

To accommodate reproducible processing of SMIME-signed messages
[ Generator](#email.generator.Generator) disables header folding for message parts of type

`multipart/signed` and all subparts.- 
*class*email.generator.BytesGenerator(*outfp*,*mangle_from_=None*,*maxheaderlen=None*,***,*policy=None*)[¶](#email.generator.BytesGenerator)
- Return a - `BytesGenerator`object that will write any message provided to the- `flatten()`- `write()`- [file-like object](../glossary.html#term-file-like-object)- *outfp*.- *outfp*must support a- `write`method that accepts binary data.- If optional - *mangle_from_*is- `True`, put a- `>`character in front of any line in the body that starts with the exact string- `"From "`, that is- `From`followed by a space at the beginning of a line.- *mangle_from_*defaults to the value of the- `mangle_from_`- *policy*(which is- `True`for the- `compat32`- `False`for all others).- *mangle_from_*is intended for use when messages are stored in Unix mbox format (see- `mailbox`- [WHY THE CONTENT-LENGTH FORMAT IS BAD](https://www.jwz.org/doc/content-length.html)).- If - *maxheaderlen*is not- `None`, refold any header lines that are longer than- *maxheaderlen*, or if- `0`, do not rewrap any headers. If- *manheaderlen*is- `None`(the default), wrap headers and other message lines according to the- *policy*settings.- If - *policy*is specified, use that policy to control message generation. If- *policy*is- `None`(the default), use the policy associated with the- `Message`- `EmailMessage`- `flatten`to control the message generation. See- `email.policy`- *policy*controls.- Added in version 3.2. - Changed in version 3.3: Added the - *policy*keyword.- Changed in version 3.6: The default behavior of the - *mangle_from_*and- *maxheaderlen*parameters is to follow the policy.- 
flatten(*msg*,*unixfrom=False*,*linesep=None*)[¶](#email.generator.BytesGenerator.flatten)
- Print the textual representation of the message object structure rooted at - *msg*to the output file specified when the- `BytesGenerator`instance was created.- If the - `policy`- `cte_type`- `8bit`(the default), copy any headers in the original parsed message that have not been modified to the output with any bytes with the high bit set reproduced as in the original, and preserve the non-ASCII- *Content-Transfer-Encoding*of any body parts that have them. If- `cte_type`is- `7bit`, convert the bytes with the high bit set as needed using an ASCII-compatible- *Content-Transfer-Encoding*. That is, transform parts with non-ASCII- *Content-Transfer-Encoding*(- *Content-Transfer-Encoding: 8bit*) to an ASCII compatible- *Content-Transfer-Encoding*, and encode RFC-invalid non-ASCII bytes in headers using the MIME- `unknown-8bit`character set, thus rendering them RFC-compliant.- If - *unixfrom*is- `True`, print the envelope header delimiter used by the Unix mailbox format (see- `mailbox`- **RFC 5322**- `False`. Note that for subparts, no envelope header is ever printed.- If - *linesep*is not- `None`, use it as the separator character between all the lines of the flattened message. If- *linesep*is- `None`(the default), use the value specified in the- *policy*.
 - 
clone(*fp*)[¶](#email.generator.BytesGenerator.clone)
- Return an independent clone of this - `BytesGenerator`instance with the exact same option settings, and- *fp*as the new- *outfp*.
 - 
write(*s*)[¶](#email.generator.BytesGenerator.write)
- Encode - *s*using the- `ASCII`codec and the- `surrogateescape`error handler, and pass it to the- *write*method of the- *outfp*passed to the- `BytesGenerator`’s constructor.
 
- 
flatten(

As a convenience, [ EmailMessage](email.message.html#email.message.EmailMessage) provides the methods

[and](email.message.html#email.message.EmailMessage.as_bytes)

`as_bytes()``bytes(aMessage)` (a.k.a.
[), which simplify the generation of a serialized binary representation of a message object. For more detail, see](email.message.html#email.message.EmailMessage.__bytes__)

`__bytes__()`[.](email.message.html#module-email.message)

`email.message`Because strings cannot represent binary data, the [ Generator](#email.generator.Generator) class must
convert any binary data in any message it flattens to an ASCII compatible
format, by converting them to an ASCII compatible

*Content-Transfer_Encoding*. Using the terminology of the email RFCs, you can think of this as

`Generator` serializing to an I/O stream
that is not “8 bit clean”.  In other words, most applications will want
to be using [, and not](#email.generator.BytesGenerator)

`BytesGenerator``Generator`.- 
*class*email.generator.Generator(*outfp*,*mangle_from_=None*,*maxheaderlen=None*,***,*policy=None*)[¶](#email.generator.Generator)
- Return a - `Generator`object that will write any message provided to the- `flatten()`- `write()`- [file-like object](../glossary.html#term-file-like-object)- *outfp*.- *outfp*must support a- `write`method that accepts string data.- If optional - *mangle_from_*is- `True`, put a- `>`character in front of any line in the body that starts with the exact string- `"From "`, that is- `From`followed by a space at the beginning of a line.- *mangle_from_*defaults to the value of the- `mangle_from_`- *policy*(which is- `True`for the- `compat32`- `False`for all others).- *mangle_from_*is intended for use when messages are stored in Unix mbox format (see- `mailbox`- [WHY THE CONTENT-LENGTH FORMAT IS BAD](https://www.jwz.org/doc/content-length.html)).- If - *maxheaderlen*is not- `None`, refold any header lines that are longer than- *maxheaderlen*, or if- `0`, do not rewrap any headers. If- *manheaderlen*is- `None`(the default), wrap headers and other message lines according to the- *policy*settings.- If - *policy*is specified, use that policy to control message generation. If- *policy*is- `None`(the default), use the policy associated with the- `Message`- `EmailMessage`- `flatten`to control the message generation. See- `email.policy`- *policy*controls.- Changed in version 3.3: Added the - *policy*keyword.- Changed in version 3.6: The default behavior of the - *mangle_from_*and- *maxheaderlen*parameters is to follow the policy.- 
flatten(*msg*,*unixfrom=False*,*linesep=None*)[¶](#email.generator.Generator.flatten)
- Print the textual representation of the message object structure rooted at - *msg*to the output file specified when the- `Generator`instance was created.- If the - `policy`- `cte_type`- `8bit`, generate the message as if the option were set to- `7bit`. (This is required because strings cannot represent non-ASCII bytes.) Convert any bytes with the high bit set as needed using an ASCII-compatible- *Content-Transfer-Encoding*. That is, transform parts with non-ASCII- *Content-Transfer-Encoding*(- *Content-Transfer-Encoding: 8bit*) to an ASCII compatible- *Content-Transfer-Encoding*, and encode RFC-invalid non-ASCII bytes in headers using the MIME- `unknown-8bit`character set, thus rendering them RFC-compliant.- If - *unixfrom*is- `True`, print the envelope header delimiter used by the Unix mailbox format (see- `mailbox`- **RFC 5322**- `False`. Note that for subparts, no envelope header is ever printed.- If - *linesep*is not- `None`, use it as the separator character between all the lines of the flattened message. If- *linesep*is- `None`(the default), use the value specified in the- *policy*.- Changed in version 3.2: Added support for re-encoding - `8bit`message bodies, and the- *linesep*argument.
 - 
clone(*fp*)[¶](#email.generator.Generator.clone)
- Return an independent clone of this - `Generator`instance with the exact same options, and- *fp*as the new- *outfp*.
 
- 
flatten(

As a convenience, [ EmailMessage](email.message.html#email.message.EmailMessage) provides the methods

[and](email.message.html#email.message.EmailMessage.as_string)

`as_string()``str(aMessage)` (a.k.a.
[), which simplify the generation of a formatted string representation of a message object. For more detail, see](email.message.html#email.message.EmailMessage.__str__)

`__str__()`[.](email.message.html#module-email.message)

`email.message`The `email.generator` module also provides a derived class,
[ DecodedGenerator](#email.generator.DecodedGenerator), which is like the 

[base class, except that non-](#email.generator.Generator)

`Generator`*text*parts are not serialized, but are instead represented in the output stream by a string derived from a template filled in with information about the part.

- 
*class*email.generator.DecodedGenerator(*outfp*,*mangle_from_=None*,*maxheaderlen=None*,*fmt=None*,***,*policy=None*)[¶](#email.generator.DecodedGenerator)
- Act like - `Generator`- `Generator.flatten()`- *text*, print the decoded payload of the subpart, and if the main type is not- *text*, instead of printing it fill in the string- *fmt*using information from the part and print the resulting filled-in string.- To fill in - *fmt*, execute- `fmt % part_info`, where- `part_info`is a dictionary composed of the following keys and values:- `type`– Full MIME type of the non-- *text*part
- `maintype`– Main MIME type of the non-- *text*part
- `subtype`– Sub-MIME type of the non-- *text*part
- `filename`– Filename of the non-- *text*part
- `description`– Description associated with the non-- *text*part
- `encoding`– Content transfer encoding of the non-- *text*part
 - If - *fmt*is- `None`, use the following default- *fmt*:- “[Non-text (%(type)s) part of message omitted, filename %(filename)s]” - Optional - *_mangle_from_*and- *maxheaderlen*are as with the- `Generator`

Footnotes