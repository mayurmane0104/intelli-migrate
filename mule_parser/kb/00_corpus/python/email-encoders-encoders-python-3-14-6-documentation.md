# email.encoders: Encoders — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/email.encoders.html](https://docs.python.org/library/email.encoders.html)

---

`email.encoders`: Encoders[¶](#module-email.encoders)

**Source code:** [Lib/email/encoders.py](https://github.com/python/cpython/tree/3.14/Lib/email/encoders.py)

This module is part of the legacy (`Compat32`) email API.  In the
new API the functionality is provided by the *cte* parameter of
the [ set_content()](email.message.html#email.message.EmailMessage.set_content) method.

This module is deprecated in Python 3.  The functions provided here
should not be called explicitly since the [ MIMEText](email.mime.html#email.mime.text.MIMEText)
class sets the content type and CTE header using the 

*_subtype*and

*_charset*values passed during the instantiation of that class.

The remaining text in this section is the original documentation of the module.

When creating [ Message](email.compat32-message.html#email.message.Message) objects from scratch, you often
need to encode the payloads for transport through compliant mail servers. This
is especially true for 

*image/**and

*text/**type messages containing binary data.

The [ email](email.html#module-email) package provides some convenient encoders in its

`encoders` module.  These encoders are actually used by the
[and](email.mime.html#email.mime.audio.MIMEAudio)

`MIMEAudio`[class constructors to provide default encodings. All encoder functions take exactly one argument, the message object to encode. They usually extract the payload, encode it, and reset the payload to this newly encoded value. They should also set the](email.mime.html#email.mime.image.MIMEImage)

`MIMEImage`*Content-Transfer-Encoding*header as appropriate.

Note that these functions are not meaningful for a multipart message.  They
must be applied to individual subparts instead, and will raise a
[ TypeError](exceptions.html#TypeError) if passed a message whose type is multipart.

Here are the encoding functions provided:

- 
email.encoders.encode_quopri(*msg*)[¶](#email.encoders.encode_quopri)
- Encodes the payload into quoted-printable form and sets the - *Content-Transfer-Encoding*header to- `quoted-printable`- [[1]](#id2). This is a good encoding to use when most of your payload is normal printable data, but contains a few unprintable characters.

- 
email.encoders.encode_base64(*msg*)[¶](#email.encoders.encode_base64)
- Encodes the payload into base64 form and sets the - *Content-Transfer-Encoding*header to- `base64`. This is a good encoding to use when most of your payload is unprintable data since it is a more compact form than quoted-printable. The drawback of base64 encoding is that it renders the text non-human readable.

- 
email.encoders.encode_7or8bit(*msg*)[¶](#email.encoders.encode_7or8bit)
- This doesn’t actually modify the message’s payload, but it does set the - *Content-Transfer-Encoding*header to either- `7bit`or- `8bit`as appropriate, based on the payload data.

- 
email.encoders.encode_noop(*msg*)[¶](#email.encoders.encode_noop)
- This does nothing; it doesn’t even set the - *Content-Transfer-Encoding*header.

Footnotes