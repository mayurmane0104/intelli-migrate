# html.entities — Definitions of HTML general entities — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/html.entities.html](https://docs.python.org/3.13/library/html.entities.html)

---

`html.entities` — Definitions of HTML general entities[¶](#module-html.entities)

**Source code:** [Lib/html/entities.py](https://github.com/python/cpython/tree/3.13/Lib/html/entities.py)

This module defines four dictionaries, [ html5](#html.entities.html5),

[,](#html.entities.name2codepoint)

`name2codepoint`[, and](#html.entities.codepoint2name)

`codepoint2name`[.](#html.entities.entitydefs)

`entitydefs`- 
html.entities.html5[¶](#html.entities.html5)
- A dictionary that maps HTML5 named character references - [[1]](#id2)to the equivalent Unicode character(s), e.g.- `html5['gt;'] == '>'`. Note that the trailing semicolon is included in the name (e.g.- `'gt;'`), however some of the names are accepted by the standard even without the semicolon: in this case the name is present with and without the- `';'`. See also- `html.unescape()`- Added in version 3.3. 

- 
html.entities.entitydefs[¶](#html.entities.entitydefs)
- A dictionary mapping XHTML 1.0 entity definitions to their replacement text in ISO Latin-1. 

- 
html.entities.name2codepoint[¶](#html.entities.name2codepoint)
- A dictionary that maps HTML4 entity names to the Unicode code points. 

- 
html.entities.codepoint2name[¶](#html.entities.codepoint2name)
- A dictionary that maps Unicode code points to HTML4 entity names. 

Footnotes