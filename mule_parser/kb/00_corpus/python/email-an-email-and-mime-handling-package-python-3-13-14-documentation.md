# email — An email and MIME handling package — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/email.html](https://docs.python.org/3.13/library/email.html)

---

`email` — An email and MIME handling package[¶](#module-email)

**Source code:** [Lib/email/__init__.py](https://github.com/python/cpython/tree/3.13/Lib/email/__init__.py)

The `email` package is a library for managing email messages.  It is
specifically *not* designed to do any sending of email messages to SMTP
([ RFC 2821](https://datatracker.ietf.org/doc/html/rfc2821.html)), NNTP, or other servers; those are functions of modules such as

[. The](smtplib.html#module-smtplib)

`smtplib``email` package attempts to be as
RFC-compliant as possible, supporting [and](https://datatracker.ietf.org/doc/html/rfc5322.html)

**RFC 5322**[, as well as such MIME-related RFCs as](https://datatracker.ietf.org/doc/html/rfc6532.html)

**RFC 6532**[,](https://datatracker.ietf.org/doc/html/rfc2045.html)

**RFC 2045**[,](https://datatracker.ietf.org/doc/html/rfc2046.html)

**RFC 2046**[,](https://datatracker.ietf.org/doc/html/rfc2047.html)

**RFC 2047**[, and](https://datatracker.ietf.org/doc/html/rfc2183.html)

**RFC 2183**[.](https://datatracker.ietf.org/doc/html/rfc2231.html)

**RFC 2231**The overall structure of the email package can be divided into three major components, plus a fourth component that controls the behavior of the other components.

The central component of the package is an “object model” that represents email
messages.  An application interacts with the package primarily through the
object model interface defined in the [ message](email.message.html#module-email.message) sub-module.  The
application can use this API to ask questions about an existing email, to
construct a new email, or to add or remove email subcomponents that themselves
use the same object model interface.  That is, following the nature of email
messages and their MIME subcomponents, the email object model is a tree
structure of objects that all provide the 

[API.](email.message.html#email.message.EmailMessage)

`EmailMessage`The other two major components of the package are the [ parser](email.parser.html#module-email.parser) and
the 

[. The parser takes the serialized version of an email message (a stream of bytes) and converts it into a tree of](email.generator.html#module-email.generator)

`generator`[objects. The generator takes an](email.message.html#email.message.EmailMessage)

`EmailMessage``EmailMessage` and turns it back into a serialized byte
stream.  (The parser and generator also handle streams of text characters, but
this usage is discouraged as it is too easy to end up with messages that are
not valid in one way or another.)The control component is the [ policy](email.policy.html#module-email.policy) module.  Every

[, every](email.message.html#email.message.EmailMessage)

`EmailMessage`[, and every](email.generator.html#module-email.generator)

`generator`[has an associated](email.parser.html#module-email.parser)

`parser``policy` object that
controls its behavior.  Usually an application only needs to specify the policy
when an `EmailMessage` is created, either by directly
instantiating an `EmailMessage`  to create a new email,
or by parsing an input stream using a `parser`.  But the policy can
be changed when the message is serialized using a `generator`.
This allows, for example, a generic email message to be parsed from disk, but
to serialize it using standard SMTP settings when sending it to an email
server.The email package does its best to hide the details of the various governing RFCs from the application. Conceptually the application should be able to treat the email message as a structured tree of unicode text and binary attachments, without having to worry about how these are represented when serialized. In practice, however, it is often necessary to be aware of at least some of the rules governing MIME messages and their structure, specifically the names and nature of the MIME “content types” and how they identify multipart documents. For the most part this knowledge should only be required for more complex applications, and even then it should only be the high level structure in question, and not the details of how those structures are represented. Since MIME content types are used widely in modern internet software (not just email), this will be a familiar concept to many programmers.

The following sections describe the functionality of the `email` package.
We start with the [ message](email.message.html#module-email.message) object model, which is the primary
interface an application will use, and follow that with the

[and](email.parser.html#module-email.parser)

`parser`[components. Then we cover the](email.generator.html#module-email.generator)

`generator`[controls, which completes the treatment of the main components of the library.](email.policy.html#module-email.policy)

`policy`The next three sections cover the exceptions the package may raise and the
defects (non-compliance with the RFCs) that the [ parser](email.parser.html#module-email.parser) may
detect.  Then we cover the 

[and the](email.headerregistry.html#module-email.headerregistry)

`headerregistry`[sub-components, which provide tools for doing more detailed manipulation of headers and payloads, respectively. Both of these components contain features relevant to consuming and producing non-trivial messages, but also document their extensibility APIs, which will be of interest to advanced applications.](email.contentmanager.html#module-email.contentmanager)

`contentmanager`Following those is a set of examples of using the fundamental parts of the APIs covered in the preceding sections.

The foregoing represent the modern (unicode friendly) API of the email package.
The remaining sections, starting with the [ Message](email.compat32-message.html#email.message.Message)
class, cover the legacy 

[API that deals much more directly with the details of how email messages are represented. The](email.policy.html#email.policy.compat32)

`compat32``compat32` API does *not*hide the details of the RFCs from the application, but for applications that need to operate at that level, they can be useful tools. This documentation is also relevant for applications that are still using the

[API for backward compatibility reasons.](email.policy.html#email.policy.compat32)

`compat32`Changed in version 3.6: Docs reorganized and rewritten to promote the new
[ EmailMessage](email.message.html#email.message.EmailMessage)/

[API.](email.policy.html#email.policy.EmailPolicy)

`EmailPolicy`Contents of the `email` package documentation:

- `email.message`: Representing an email message
- `email.parser`: Parsing email messages
- `email.generator`: Generating MIME documents
- `email.policy`: Policy Objects
- `email.errors`: Exception and Defect classes
- `email.headerregistry`: Custom Header Objects
- `email.contentmanager`: Managing MIME Content
- `email`: Examples

Legacy API:

- `email.message.Message`: Representing an email message using the- `compat32`API
- `email.mime`: Creating email and MIME objects from scratch
- `email.header`: Internationalized headers
- `email.charset`: Representing character sets
- `email.encoders`: Encoders
- `email.utils`: Miscellaneous utilities
- `email.iterators`: Iterators