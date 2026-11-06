# email.utils: Miscellaneous utilities — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/email.utils.html](https://docs.python.org/3.13/library/email.utils.html)

---

`email.utils`: Miscellaneous utilities[¶](#module-email.utils)

**Source code:** [Lib/email/utils.py](https://github.com/python/cpython/tree/3.13/Lib/email/utils.py)

There are a couple of useful utilities provided in the `email.utils`
module:

- 
email.utils.localtime(*dt=None*)[¶](#email.utils.localtime)
- Return local time as an aware datetime object. If called without arguments, return current time. Otherwise - *dt*argument should be a- `datetime`- *dt*is naive (that is,- `dt.tzinfo`is- `None`), it is assumed to be in local time. The- *isdst*parameter is ignored.- Added in version 3.3. - Deprecated since version 3.12, will be removed in version 3.14: The - *isdst*parameter.

- 
email.utils.make_msgid(*idstring=None*,*domain=None*)[¶](#email.utils.make_msgid)
- Returns a string suitable for an - **RFC 2822**- *Message-ID*header. Optional- *idstring*if given, is a string used to strengthen the uniqueness of the message id. Optional- *domain*if given provides the portion of the msgid after the ‘@’. The default is the local hostname. It is not normally necessary to override this default, but may be useful certain cases, such as a constructing distributed system that uses a consistent domain name across multiple hosts.- Changed in version 3.2: Added the - *domain*keyword.

The remaining functions are part of the legacy (`Compat32`) email API.  There
is no need to directly use these with the new API, since the parsing and
formatting they provide is done automatically by the header parsing machinery
of the new API.

- 
email.utils.quote(*str*)[¶](#email.utils.quote)
- Return a new string with backslashes in - *str*replaced by two backslashes, and double quotes replaced by backslash-double quote.

- 
email.utils.unquote(*str*)[¶](#email.utils.unquote)
- Return a new string which is an - *unquoted*version of- *str*. If- *str*ends and begins with double quotes, they are stripped off. Likewise if- *str*ends and begins with angle brackets, they are stripped off.

- 
email.utils.parseaddr(*address*,***,*strict=True*)[¶](#email.utils.parseaddr)
- Parse address – which should be the value of some address-containing field such as - *To*or- *Cc*– into its constituent- *realname*and- *email address*parts. Returns a tuple of that information, unless the parse fails, in which case a 2-tuple of- `('', '')`is returned.- If - *strict*is true, use a strict parser which rejects malformed inputs.- Changed in version 3.13: Add - *strict*optional parameter and reject malformed inputs by default.

- 
email.utils.formataddr(*pair*,*charset='utf-8'*)[¶](#email.utils.formataddr)
- The inverse of - `parseaddr()`- `(realname, email_address)`and returns the string value suitable for a- *To*or- *Cc*header. If the first element of- *pair*is false, then the second element is returned unmodified.- Optional - *charset*is the character set that will be used in the- **RFC 2047**- `realname`if the- `realname`contains non-ASCII characters. Can be an instance of- `str`- `Charset`- `utf-8`.- Changed in version 3.3: Added the - *charset*option.

- 
email.utils.getaddresses(*fieldvalues*,***,*strict=True*)[¶](#email.utils.getaddresses)
- This method returns a list of 2-tuples of the form returned by - `parseaddr()`.- *fieldvalues*is a sequence of header field values as might be returned by- `Message.get_all`- If - *strict*is true, use a strict parser which rejects malformed inputs.- Here’s a simple example that gets all the recipients of a message: - from email.utils import getaddresses tos = msg.get_all('to', []) ccs = msg.get_all('cc', []) resent_tos = msg.get_all('resent-to', []) resent_ccs = msg.get_all('resent-cc', []) all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs) - Changed in version 3.13: Add - *strict*optional parameter and reject malformed inputs by default.

- 
email.utils.parsedate(*date*)[¶](#email.utils.parsedate)
- Attempts to parse a date according to the rules in - **RFC 2822**- `parsedate()`tries to guess correctly in such cases.- *date*is a string containing an- **RFC 2822**- `"Mon, 20 Nov 1995 19:12:08 -0500"`. If it succeeds in parsing the date,- `parsedate()`returns a 9-tuple that can be passed directly to- `time.mktime()`- `None`will be returned. Note that indexes 6, 7, and 8 of the result tuple are not usable.

- 
email.utils.parsedate_tz(*date*)[¶](#email.utils.parsedate_tz)
- Performs the same function as - `parsedate()`- `None`or a 10-tuple; the first 9 elements make up a tuple that can be passed directly to- `time.mktime()`- [[1]](#id2). If the input string has no timezone, the last element of the tuple returned is- `0`, which represents UTC. Note that indexes 6, 7, and 8 of the result tuple are not usable.

- 
email.utils.parsedate_to_datetime(*date*)[¶](#email.utils.parsedate_to_datetime)
- The inverse of - `format_datetime()`- `parsedate()`- `datetime`- `ValueError`is raised if- *date*contains an invalid value such as an hour greater than 23 or a timezone offset not between -24 and 24 hours. If the input date has a timezone of- `-0000`, the- `datetime`will be a naive- `datetime`, and if the date is conforming to the RFCs it will represent a time in UTC but with no indication of the actual source timezone of the message the date comes from. If the input date has any other valid timezone offset, the- `datetime`will be an aware- `datetime`with the corresponding a- `timezone`- `tzinfo`- Added in version 3.3. 

- 
email.utils.mktime_tz(*tuple*)[¶](#email.utils.mktime_tz)
- Turn a 10-tuple as returned by - `parsedate_tz()`- `None`, assume local time.

- 
email.utils.formatdate(*timeval=None*,*localtime=False*,*usegmt=False*)[¶](#email.utils.formatdate)
- Returns a date string as per - **RFC 2822**- Fri, 09 Nov 2001 01:08:47 -0000 - Optional - *timeval*if given is a floating-point time value as accepted by- `time.gmtime()`- `time.localtime()`- Optional - *localtime*is a flag that when- `True`, interprets- *timeval*, and returns a date relative to the local timezone instead of UTC, properly taking daylight savings time into account. The default is- `False`meaning UTC is used.- Optional - *usegmt*is a flag that when- `True`, outputs a date string with the timezone as an ascii string- `GMT`, rather than a numeric- `-0000`. This is needed for some protocols (such as HTTP). This only applies when- *localtime*is- `False`. The default is- `False`.

- 
email.utils.format_datetime(*dt*,*usegmt=False*)[¶](#email.utils.format_datetime)
- Like - `formatdate`, but the input is a- `datetime`- `-0000`is used for the timezone. If it is an aware- `datetime`, then the numeric timezone offset is used. If it is an aware timezone with offset zero, then- *usegmt*may be set to- `True`, in which case the string- `GMT`is used instead of the numeric timezone offset. This provides a way to generate standards conformant HTTP date headers.- Added in version 3.3. 

- 
email.utils.encode_rfc2231(*s*,*charset=None*,*language=None*)[¶](#email.utils.encode_rfc2231)
- Encode the string - *s*according to- **RFC 2231**- *charset*and- *language*, if given is the character set name and language name to use. If neither is given,- *s*is returned as-is. If- *charset*is given but- *language*is not, the string is encoded using the empty string for- *language*.

- 
email.utils.collapse_rfc2231_value(*value*,*errors='replace'*,*fallback_charset='us-ascii'*)[¶](#email.utils.collapse_rfc2231_value)
- When a header parameter is encoded in - **RFC 2231**- `Message.get_param`- `collapse_rfc2231_value()`turns this into a unicode string. Optional- *errors*is passed to the- *errors*argument of- `str`- `encode()`- `'replace'`. Optional- *fallback_charset*specifies the character set to use if the one in the- **RFC 2231**- `'us-ascii'`.- For convenience, if the - *value*passed to- `collapse_rfc2231_value()`is not a tuple, it should be a string and it is returned unquoted.

- 
email.utils.decode_params(*params*)[¶](#email.utils.decode_params)
- Decode parameters list according to - **RFC 2231**- *params*is a sequence of 2-tuples containing elements of the form- `(content-type, string-value)`.

Footnotes