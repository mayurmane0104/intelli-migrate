# quopri — Encode and decode MIME quoted-printable data — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/quopri.html](https://docs.python.org/3.13/library/quopri.html)

---

`quopri` — Encode and decode MIME quoted-printable data[¶](#module-quopri)

**Source code:** [Lib/quopri.py](https://github.com/python/cpython/tree/3.13/Lib/quopri.py)

This module performs quoted-printable transport encoding and decoding, as
defined in [ RFC 1521](https://datatracker.ietf.org/doc/html/rfc1521.html): “MIME (Multipurpose Internet Mail Extensions) Part One:
Mechanisms for Specifying and Describing the Format of Internet Message Bodies”.
The quoted-printable encoding is designed for data where there are relatively
few nonprintable characters; the base64 encoding scheme available via the

[module is more compact if there are many such characters, as when sending a graphics file.](base64.html#module-base64)

`base64`- 
quopri.decode(*input*,*output*,*header=False*)[¶](#quopri.decode)
- Decode the contents of the - *input*file and write the resulting decoded binary data to the- *output*file.- *input*and- *output*must be- [binary file objects](../glossary.html#term-file-object). If the optional argument- *header*is present and true, underscore will be decoded as space. This is used to decode “Q”-encoded headers as described in- **RFC 1522**

- 
quopri.encode(*input*,*output*,*quotetabs*,*header=False*)[¶](#quopri.encode)
- Encode the contents of the - *input*file and write the resulting quoted-printable data to the- *output*file.- *input*and- *output*must be- [binary file objects](../glossary.html#term-file-object).- *quotetabs*, a non-optional flag which controls whether to encode embedded spaces and tabs; when true it encodes such embedded whitespace, and when false it leaves them unencoded. Note that spaces and tabs appearing at the end of lines are always encoded, as per- **RFC 1521**- *header*is a flag which controls if spaces are encoded as underscores as per- **RFC 1522**

- 
quopri.decodestring(*s*,*header=False*)[¶](#quopri.decodestring)
- Like - `decode()`- `bytes`- `bytes`.

- 
quopri.encodestring(*s*,*quotetabs=False*,*header=False*)[¶](#quopri.encodestring)
- Like - `encode()`- `bytes`- `bytes`. By default, it sends a- `False`value to- *quotetabs*parameter of the- `encode()`function.

See also

- Module `base64`
- Encode and decode MIME base64 data