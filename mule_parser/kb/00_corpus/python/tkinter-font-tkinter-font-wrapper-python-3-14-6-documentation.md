# tkinter.font — Tkinter font wrapper — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/tkinter.font.html](https://docs.python.org/library/tkinter.font.html)

---

`tkinter.font` — Tkinter font wrapper[¶](#module-tkinter.font)

**Source code:** [Lib/tkinter/font.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/font.py)

The `tkinter.font` module provides the [ Font](#tkinter.font.Font) class for creating
and using named fonts.

The different font weights and slants are:

- 
*class*tkinter.font.Font(*root=None*,*font=None*,*name=None*,*exists=False*,***options*)[¶](#tkinter.font.Font)
- The - `Font`class represents a named font.- *Font*instances are given unique names and can be specified by their family, size, and style configuration. Named fonts are Tk’s method of creating and identifying fonts as a single object, rather than specifying a font by its attributes with each occurrence.- arguments: - *font*- font specifier tuple (family, size, options)- *name*- unique font name- *exists*- self points to existing named font if true- additional keyword options (ignored if - *font*is specified):- *family*- font family i.e. Courier, Times- *size*- font sizeIf- *size*is positive it is interpreted as size in points.If- *size*is a negative number its absolute value is treatedas size in pixels.- *weight*- font emphasis (NORMAL, BOLD)- *slant*- ROMAN, ITALIC- *underline*- font underlining (0 - none, 1 - underline)- *overstrike*- font strikeout (0 - none, 1 - strikeout)- 
actual(*option=None*,*displayof=None*)[¶](#tkinter.font.Font.actual)
- Return the attributes of the font. 
 - 
cget(*option*)[¶](#tkinter.font.Font.cget)
- Retrieve an attribute of the font. 
 - 
config(***options*)[¶](#tkinter.font.Font.config)
- Modify attributes of the font. 
 - 
copy()[¶](#tkinter.font.Font.copy)
- Return new instance of the current font. 
 - 
measure(*text*,*displayof=None*)[¶](#tkinter.font.Font.measure)
- Return amount of space the text would occupy on the specified display when formatted in the current font. If no display is specified then the main application window is assumed. 
 - 
metrics(**options*,***kw*)[¶](#tkinter.font.Font.metrics)
- Return font-specific data. Options include: - *ascent*- distance between baseline and highest point that a
- character of the font can occupy 
- *descent*- distance between baseline and lowest point that a
- character of the font can occupy 
- *linespace*- minimum vertical separation necessary between any two
- characters of the font that ensures no vertical overlap between lines. 
 - *fixed*- 1 if font is fixed-width else 0
 
- 
actual(

- 
tkinter.font.families(*root=None*,*displayof=None*)[¶](#tkinter.font.families)
- Return the different font families. 

- 
tkinter.font.names(*root=None*)[¶](#tkinter.font.names)
- Return the names of defined fonts.