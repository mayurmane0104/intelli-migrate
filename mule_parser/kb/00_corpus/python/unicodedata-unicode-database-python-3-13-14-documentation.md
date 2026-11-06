# unicodedata — Unicode Database — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/unicodedata.html](https://docs.python.org/3.13/library/unicodedata.html)

---

`unicodedata` — Unicode Database[¶](#module-unicodedata)

This module provides access to the Unicode Character Database (UCD) which
defines character properties for all Unicode characters. The data contained in
this database is compiled from the [UCD version 15.1.0](https://www.unicode.org/Public/15.1.0/ucd).

The module uses the same names and symbols as defined by Unicode
Standard Annex #44, [“Unicode Character Database”](https://www.unicode.org/reports/tr44/).  It defines the
following functions:

See also

The [Unicode HOWTO](../howto/unicode.html#unicode-howto) for more information about Unicode and how to use
this module.

- 
unicodedata.lookup(*name*)[¶](#unicodedata.lookup)
- Look up character by name. If a character with the given name is found, return the corresponding character. If not found, - `KeyError`- >>> unicodedata.lookup('LEFT CURLY BRACKET') '{' - The characters returned by this function are the same as those produced by - `\N`escape sequence in string literals. For example:- >>> unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}' True 

- 
unicodedata.name(*chr*,*default=None*,*/*)[¶](#unicodedata.name)
- Returns the name assigned to the character - *chr*as a string. If no name is defined,- *default*is returned, or, if not given,- `ValueError`- >>> unicodedata.name('½') 'VULGAR FRACTION ONE HALF' >>> unicodedata.name('\uFFFF', 'fallback') 'fallback' 

- 
unicodedata.decimal(*chr*,*default=None*,*/*)[¶](#unicodedata.decimal)
- Returns the decimal value assigned to the character - *chr*as integer. If no such value is defined,- *default*is returned, or, if not given,- `ValueError`- >>> unicodedata.decimal('\N{ARABIC-INDIC DIGIT NINE}') 9 >>> unicodedata.decimal('\N{SUPERSCRIPT NINE}', -1) -1 

- 
unicodedata.digit(*chr*,*default=None*,*/*)[¶](#unicodedata.digit)
- Returns the digit value assigned to the character - *chr*as integer. If no such value is defined,- *default*is returned, or, if not given,- `ValueError`- >>> unicodedata.digit('\N{SUPERSCRIPT NINE}') 9 

- 
unicodedata.numeric(*chr*,*default=None*,*/*)[¶](#unicodedata.numeric)
- Returns the numeric value assigned to the character - *chr*as float. If no such value is defined,- *default*is returned, or, if not given,- `ValueError`- >>> unicodedata.numeric('½') 0.5 

- 
unicodedata.category(*chr*)[¶](#unicodedata.category)
- Returns the general category assigned to the character - *chr*as string. General category names consist of two letters. See the- [General Category Values section of the Unicode Character Database documentation](https://www.unicode.org/reports/tr44/tr44-30.html#General_Category_Values)for a list of category codes. For example:- >>> unicodedata.category('A') # 'L'etter, 'u'ppercase 'Lu' 

- 
unicodedata.bidirectional(*chr*)[¶](#unicodedata.bidirectional)
- Returns the bidirectional class assigned to the character - *chr*as string. If no such value is defined, an empty string is returned. See the- [Bidirectional Class Values section of the Unicode Character Database](https://www.unicode.org/reports/tr44/tr44-30.html#Bidi_Class_Values)documentation for a list of bidirectional codes. For example:- >>> unicodedata.bidirectional('\N{ARABIC-INDIC DIGIT SEVEN}') # 'A'rabic, 'N'umber 'AN' 

- 
unicodedata.combining(*chr*)[¶](#unicodedata.combining)
- Returns the canonical combining class assigned to the character - *chr*as integer. Returns- `0`if no combining class is defined. See the- [Canonical Combining Class Values section of the Unicode Character Database](https://www.unicode.org/reports/tr44/tr44-30.html#Canonical_Combining_Class_Values)for more information.

- 
unicodedata.east_asian_width(*chr*)[¶](#unicodedata.east_asian_width)
- Returns the east asian width assigned to the character - *chr*as string. For a list of widths and or more information, see the- [Unicode Standard Annex #11](https://www.unicode.org/reports/tr11/tr11-41.html).

- 
unicodedata.mirrored(*chr*)[¶](#unicodedata.mirrored)
- Returns the mirrored property assigned to the character - *chr*as integer. Returns- `1`if the character has been identified as a “mirrored” character in bidirectional text,- `0`otherwise. For example:- >>> unicodedata.mirrored('>') 1 

- 
unicodedata.decomposition(*chr*)[¶](#unicodedata.decomposition)
- Returns the character decomposition mapping assigned to the character - *chr*as string. An empty string is returned in case no such mapping is defined. For example:- >>> unicodedata.decomposition('Ã') '0041 0303' 

- 
unicodedata.normalize(*form*,*unistr*)[¶](#unicodedata.normalize)
- Return the normal form - *form*for the Unicode string- *unistr*. Valid values for- *form*are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.- The Unicode standard defines various normalization forms of a Unicode string, based on the definition of canonical equivalence and compatibility equivalence. In Unicode, several characters can be expressed in various way. For example, the character U+00C7 (LATIN CAPITAL LETTER C WITH CEDILLA) can also be expressed as the sequence U+0043 (LATIN CAPITAL LETTER C) U+0327 (COMBINING CEDILLA). - For each character, there are two normal forms: normal form C and normal form D. Normal form D (NFD) is also known as canonical decomposition, and translates each character into its decomposed form. Normal form C (NFC) first applies a canonical decomposition, then composes pre-combined characters again. - In addition to these two forms, there are two additional normal forms based on compatibility equivalence. In Unicode, certain characters are supported which normally would be unified with other characters. For example, U+2160 (ROMAN NUMERAL ONE) is really the same thing as U+0049 (LATIN CAPITAL LETTER I). However, it is supported in Unicode for compatibility with existing character sets (for example, gb2312). - The normal form KD (NFKD) will apply the compatibility decomposition, that is, replace all compatibility characters with their equivalents. The normal form KC (NFKC) first applies the compatibility decomposition, followed by the canonical composition. - Even if two unicode strings are normalized and look the same to a human reader, if one has combining characters and the other doesn’t, they may not compare equal. 

- 
unicodedata.is_normalized(*form*,*unistr*)[¶](#unicodedata.is_normalized)
- Return whether the Unicode string - *unistr*is in the normal form- *form*. Valid values for- *form*are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.- Added in version 3.8. 

In addition, the module exposes the following constant:

- 
unicodedata.unidata_version[¶](#unicodedata.unidata_version)
- The version of the Unicode database used in this module. 

- 
unicodedata.ucd_3_2_0[¶](#unicodedata.ucd_3_2_0)
- This is an object that has the same methods as the entire module, but uses the Unicode database version 3.2 instead, for applications that require this specific version of the Unicode database (such as IDNA). 

Footnotes