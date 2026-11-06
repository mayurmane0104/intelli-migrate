# imghdr — Determine the type of an image — Python 3.12.13 documentation

**Source:** [https://docs.python.org/3.12/library/imghdr.html](https://docs.python.org/3.12/library/imghdr.html)

---

`imghdr`[¶](#module-imghdr)

`imghdr`**Source code:** [Lib/imghdr.py](https://github.com/python/cpython/tree/3.12/Lib/imghdr.py)

Deprecated since version 3.11, will be removed in version 3.13: The [ imghdr](#module-imghdr) module is deprecated
(see 

[for details and alternatives).](https://peps.python.org/pep-0594/#imghdr)

**PEP 594**The [ imghdr](#module-imghdr) module determines the type of image contained in a file or
byte stream.

The [ imghdr](#module-imghdr) module defines the following function:

- 
imghdr.what(*file*,*h=None*)[¶](#imghdr.what)
- Test the image data contained in the file named - *file*and return a string describing the image type. If- *h*is provided, the- *file*argument is ignored and- *h*is assumed to contain the byte stream to test.- Changed in version 3.6: Accepts a - [path-like object](../glossary.html#term-path-like-object).

The following image types are recognized, as listed below with the return value
from [ what()](#imghdr.what):

| Value | Image format | 
|---|---|
| 
 | SGI ImgLib Files | 
| 
 | GIF 87a and 89a Files | 
| 
 | Portable Bitmap Files | 
| 
 | Portable Graymap Files | 
| 
 | Portable Pixmap Files | 
| 
 | TIFF Files | 
| 
 | Sun Raster Files | 
| 
 | X Bitmap Files | 
| 
 | JPEG data in JFIF or Exif formats | 
| 
 | BMP files | 
| 
 | Portable Network Graphics | 
| 
 | WebP files | 
| 
 | OpenEXR Files | 

Added in version 3.5: The *exr* and *webp* formats were added.

You can extend the list of file types [ imghdr](#module-imghdr) can recognize by appending
to this variable:

- 
imghdr.tests[¶](#imghdr.tests)
- A list of functions performing the individual tests. Each function takes two arguments: the byte-stream and an open file-like object. When - `what()`- `None`.- The test function should return a string describing the image type if the test succeeded, or - `None`if it failed.

Example:

```
>>> import imghdr
>>> imghdr.what('bass.gif')
'gif'
```