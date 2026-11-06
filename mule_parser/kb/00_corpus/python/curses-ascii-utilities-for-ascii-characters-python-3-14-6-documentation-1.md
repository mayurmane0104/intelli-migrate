# curses.ascii — Utilities for ASCII characters — Python 3.14.6 documentation

**Source:** [https://docs.python.org/3.14/library/curses.ascii.html](https://docs.python.org/3.14/library/curses.ascii.html)

---

`curses.ascii` — Utilities for ASCII characters[¶](#module-curses.ascii)

**Source code:** [Lib/curses/ascii.py](https://github.com/python/cpython/tree/3.14/Lib/curses/ascii.py)

The `curses.ascii` module supplies name constants for ASCII characters and
functions to test membership in various ASCII character classes.  The constants
supplied are names for control characters as follows:

| Name | Meaning | 
|---|---|
| 
 | |
| 
 | Start of heading, console interrupt | 
| 
 | Start of text | 
| 
 | End of text | 
| 
 | End of transmission | 
| 
 | Enquiry, goes with  | 
| 
 | Acknowledgement | 
| 
 | Bell | 
| 
 | Backspace | 
| 
 | Tab | 
| 
 | Alias for  | 
| 
 | Line feed | 
| 
 | Alias for  | 
| 
 | Vertical tab | 
| 
 | Form feed | 
| 
 | Carriage return | 
| 
 | Shift-out, begin alternate character set | 
| 
 | Shift-in, resume default character set | 
| 
 | Data-link escape | 
| 
 | XON, for flow control | 
| 
 | Device control 2, block-mode flow control | 
| 
 | XOFF, for flow control | 
| 
 | Device control 4 | 
| 
 | Negative acknowledgement | 
| 
 | Synchronous idle | 
| 
 | End transmission block | 
| 
 | Cancel | 
| 
 | End of medium | 
| 
 | Substitute | 
| 
 | Escape | 
| 
 | File separator | 
| 
 | Group separator | 
| 
 | Record separator, block-mode terminator | 
| 
 | Unit separator | 
| 
 | Space | 
| 
 | Delete | 

Note that many of these have little practical significance in modern usage. The mnemonics derive from teleprinter conventions that predate digital computers.

The module supplies the following functions, patterned on those in the standard C library:

- 
curses.ascii.isalnum(*c*)[¶](#curses.ascii.isalnum)
- Checks for an ASCII alphanumeric character; it is equivalent to - `isalpha(c) or isdigit(c)`.

- 
curses.ascii.isalpha(*c*)[¶](#curses.ascii.isalpha)
- Checks for an ASCII alphabetic character; it is equivalent to - `isupper(c) or islower(c)`.

- 
curses.ascii.isascii(*c*)[¶](#curses.ascii.isascii)
- Checks for a character value that fits in the 7-bit ASCII set. 

- 
curses.ascii.isblank(*c*)[¶](#curses.ascii.isblank)
- Checks for an ASCII whitespace character; space or horizontal tab. 

- 
curses.ascii.iscntrl(*c*)[¶](#curses.ascii.iscntrl)
- Checks for an ASCII control character (in the range 0x00 to 0x1f or 0x7f). 

- 
curses.ascii.isdigit(*c*)[¶](#curses.ascii.isdigit)
- Checks for an ASCII decimal digit, - `'0'`through- `'9'`. This is equivalent to- `c in string.digits`.

- 
curses.ascii.isgraph(*c*)[¶](#curses.ascii.isgraph)
- Checks for any ASCII printable character except space. 

- 
curses.ascii.islower(*c*)[¶](#curses.ascii.islower)
- Checks for an ASCII lower-case character. 

- 
curses.ascii.isprint(*c*)[¶](#curses.ascii.isprint)
- Checks for any ASCII printable character including space. 

- 
curses.ascii.ispunct(*c*)[¶](#curses.ascii.ispunct)
- Checks for any ASCII printable character which is not a space or an alphanumeric character. 

- 
curses.ascii.isspace(*c*)[¶](#curses.ascii.isspace)
- Checks for ASCII white-space characters; space, line feed, carriage return, form feed, horizontal tab, vertical tab. 

- 
curses.ascii.isupper(*c*)[¶](#curses.ascii.isupper)
- Checks for an ASCII uppercase letter. 

- 
curses.ascii.isxdigit(*c*)[¶](#curses.ascii.isxdigit)
- Checks for an ASCII hexadecimal digit. This is equivalent to - `c in string.hexdigits`.

- 
curses.ascii.isctrl(*c*)[¶](#curses.ascii.isctrl)
- Checks for an ASCII control character (ordinal values 0 to 31). 

- 
curses.ascii.ismeta(*c*)[¶](#curses.ascii.ismeta)
- Checks for a non-ASCII character (ordinal values 0x80 and above). 

These functions accept either integers or single-character strings; when the argument is a
string, it is first converted using the built-in function [ ord()](functions.html#ord).

Note that all these functions check ordinal bit values derived from the character of the string you pass in; they do not actually know anything about the host machine’s character encoding.

The following two functions take either a single-character string or integer byte value; they return a value of the same type.

- 
curses.ascii.ascii(*c*)[¶](#curses.ascii.ascii)
- Return the ASCII value corresponding to the low 7 bits of - *c*.

- 
curses.ascii.ctrl(*c*)[¶](#curses.ascii.ctrl)
- Return the control character corresponding to the given character (the character bit value is bitwise-anded with 0x1f). 

- 
curses.ascii.alt(*c*)[¶](#curses.ascii.alt)
- Return the 8-bit character corresponding to the given ASCII character (the character bit value is bitwise-ored with 0x80). 

The following function takes either a single-character string or integer value; it returns a string.

- 
curses.ascii.unctrl(*c*)[¶](#curses.ascii.unctrl)
- Return a string representation of the ASCII character - *c*. If- *c*is printable, this string is the character itself. If the character is a control character (0x00–0x1f) the string consists of a caret (- `'^'`) followed by the corresponding uppercase letter. If the character is an ASCII delete (0x7f) the string is- `'^?'`. If the character has its meta bit (0x80) set, the meta bit is stripped, the preceding rules applied, and- `'!'`prepended to the result.

- 
curses.ascii.controlnames[¶](#curses.ascii.controlnames)
- A 33-element string array that contains the ASCII mnemonics for the thirty-two ASCII control characters from 0 (NUL) to 0x1f (US), in order, plus the mnemonic - `SP`for the space character.