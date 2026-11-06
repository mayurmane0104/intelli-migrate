# html — HyperText Markup Language support — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/html.html](https://docs.python.org/3.13/library/html.html)

---

`html` — HyperText Markup Language support[¶](#module-html)

**Source code:** [Lib/html/__init__.py](https://github.com/python/cpython/tree/3.13/Lib/html/__init__.py)

This module defines utilities to manipulate HTML.

- 
html.escape(*s*,*quote=True*)[¶](#html.escape)
- Convert the characters - `&`,- `<`and- `>`in string- *s*to HTML-safe sequences. Use this if you need to display text that might contain such characters in HTML. If the optional flag- *quote*is true (the default), the characters (- `"`) and (- `'`) are also translated; this helps for inclusion in an HTML attribute value delimited by quotes, as in- `<a href="...">`. If- *quote*is set to false, the characters (- `"`) and (- `'`) are not translated.- Added in version 3.2. 

- 
html.unescape(*s*)[¶](#html.unescape)
- Convert all named and numeric character references (e.g. - `>`,- `>`,- `>`) in the string- *s*to the corresponding Unicode characters. This function uses the rules defined by the HTML 5 standard for both valid and invalid character references, and the- `list of HTML 5 named character references`- Added in version 3.4. 

Submodules in the `html` package are:

- `html.parser`
- `html.entities`