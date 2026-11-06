# html.parser — Simple HTML and XHTML parser — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/html.parser.html](https://docs.python.org/3.13/library/html.parser.html)

---

`html.parser` — Simple HTML and XHTML parser[¶](#module-html.parser)

**Source code:** [Lib/html/parser.py](https://github.com/python/cpython/tree/3.13/Lib/html/parser.py)

This module defines a class [ HTMLParser](#html.parser.HTMLParser) which serves as the basis for
parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML.

- 
*class*html.parser.HTMLParser(***,*convert_charrefs=True*,*scripting=False*)[¶](#html.parser.HTMLParser)
- Create a parser instance able to parse invalid markup. - If - *convert_charrefs*is true (the default), all character references (except the ones in elements like- `script`and- `style`) are automatically converted to the corresponding Unicode characters.- If - *scripting*is false (the default), the content of the- `noscript`element is parsed normally; if it’s true, it’s returned as is without being parsed.- An - `HTMLParser`instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. The user should subclass- `HTMLParser`and override its methods to implement the desired behavior.- This parser does not check that end tags match start tags or call the end-tag handler for elements which are closed implicitly by closing an outer element. - Changed in version 3.4: - *convert_charrefs*keyword argument added.- Changed in version 3.5: The default value for argument - *convert_charrefs*is now- `True`.- Changed in version 3.13.10: Added the - *scripting*parameter.

## Example HTML Parser Application[¶](#example-html-parser-application)

As a basic example, below is a simple HTML parser that uses the
[ HTMLParser](#html.parser.HTMLParser) class to print out start tags, end tags, and data
as they are encountered:

```
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
```
The output will then be:

```
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html
```
`HTMLParser`[¶](#htmlparser-methods)

`HTMLParser`[ HTMLParser](#html.parser.HTMLParser) instances have the following methods:

- 
HTMLParser.feed(*data*)[¶](#html.parser.HTMLParser.feed)
- Feed some text to the parser. It is processed insofar as it consists of complete elements; incomplete data is buffered until more data is fed or - `close()`- *data*must be- `str`

- 
HTMLParser.close()[¶](#html.parser.HTMLParser.close)
- Force processing of all buffered data as if it were followed by an end-of-file mark. This method may be redefined by a derived class to define additional processing at the end of the input, but the redefined version should always call the - `HTMLParser`- `close()`.

- 
HTMLParser.reset()[¶](#html.parser.HTMLParser.reset)
- Reset the instance. Loses all unprocessed data. This is called implicitly at instantiation time. 

- 
HTMLParser.getpos()[¶](#html.parser.HTMLParser.getpos)
- Return current line number and offset. 

- 
HTMLParser.get_starttag_text()[¶](#html.parser.HTMLParser.get_starttag_text)
- Return the text of the most recently opened start tag. This should not normally be needed for structured processing, but may be useful in dealing with HTML “as deployed” or for re-generating input with minimal changes (whitespace between attributes can be preserved, etc.). 

The following methods are called when data or markup elements are encountered
and they are meant to be overridden in a subclass.  The base class
implementations do nothing (except for [ handle_startendtag()](#html.parser.HTMLParser.handle_startendtag)):

- 
HTMLParser.handle_starttag(*tag*,*attrs*)[¶](#html.parser.HTMLParser.handle_starttag)
- This method is called to handle the start tag of an element (e.g. - `<div id="main">`).- The - *tag*argument is the name of the tag converted to lower case. The- *attrs*argument is a list of- `(name, value)`pairs containing the attributes found inside the tag’s- `<>`brackets. The- *name*will be translated to lower case, and quotes in the- *value*have been removed, and character and entity references have been replaced. For empty attributes,- *value*is- `None`.- For instance, for the tag - `<A HREF="https://www.cwi.nl/">`, this method would be called as- `handle_starttag('a', [('href', 'https://www.cwi.nl/')])`.- All entity references from - `html.entities`

- 
HTMLParser.handle_endtag(*tag*)[¶](#html.parser.HTMLParser.handle_endtag)
- This method is called to handle the end tag of an element (e.g. - `</div>`).- The - *tag*argument is the name of the tag converted to lower case.

- 
HTMLParser.handle_startendtag(*tag*,*attrs*)[¶](#html.parser.HTMLParser.handle_startendtag)
- Similar to - `handle_starttag()`- `<img ... />`). This method may be overridden by subclasses which require this particular lexical information; the default implementation simply calls- `handle_starttag()`and- `handle_endtag()`

- 
HTMLParser.handle_data(*data*)[¶](#html.parser.HTMLParser.handle_data)
- This method is called to process arbitrary data (e.g. text nodes and the content of elements like - `script`and- `style`).

- 
HTMLParser.handle_entityref(*name*)[¶](#html.parser.HTMLParser.handle_entityref)
- This method is called to process a named character reference of the form - `&name;`(e.g.- `>`), where- *name*is a general entity reference (e.g.- `'gt'`). This method is only called if- *convert_charrefs*is false.

- 
HTMLParser.handle_charref(*name*)[¶](#html.parser.HTMLParser.handle_charref)
- This method is called to process decimal and hexadecimal numeric character references of the form - `&#`and- *NNN*;- `&#x`. For example, the decimal equivalent for- *NNN*;- `>`is- `>`, whereas the hexadecimal is- `>`; in this case the method will receive- `'62'`or- `'x3E'`. This method is only called if- *convert_charrefs*is false.

- 
HTMLParser.handle_comment(*data*)[¶](#html.parser.HTMLParser.handle_comment)
- This method is called when a comment is encountered (e.g. - `<!--comment-->`).- For example, the comment - `<!-- comment -->`will cause this method to be called with the argument- `' comment '`.- The content of Internet Explorer conditional comments (condcoms) will also be sent to this method, so, for - `<!--[if IE 9]>IE9-specific content<![endif]-->`, this method will receive- `'[if IE 9]>IE9-specific content<![endif]'`.

- 
HTMLParser.handle_decl(*decl*)[¶](#html.parser.HTMLParser.handle_decl)
- This method is called to handle an HTML doctype declaration (e.g. - `<!DOCTYPE html>`).- The - *decl*parameter will be the entire contents of the declaration inside the- `<!...>`markup (e.g.- `'DOCTYPE html'`).

- 
HTMLParser.handle_pi(*data*)[¶](#html.parser.HTMLParser.handle_pi)
- Method called when a processing instruction is encountered. The - *data*parameter will contain the entire processing instruction. For example, for the processing instruction- `<?proc color='red'>`, this method would be called as- `handle_pi("proc color='red'")`. It is intended to be overridden by a derived class; the base class implementation does nothing.- Note - The - `HTMLParser`- `'?'`will cause the- `'?'`to be included in- *data*.

- 
HTMLParser.unknown_decl(*data*)[¶](#html.parser.HTMLParser.unknown_decl)
- This method is called when an unrecognized declaration is read by the parser. - The - *data*parameter will be the entire contents of the declaration inside the- `<![...]>`markup. It is sometimes useful to be overridden by a derived class. The base class implementation does nothing.

## Examples[¶](#examples)

The following class implements a parser that will be used to illustrate more examples:

```
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
    def handle_endtag(self, tag):
        print("End tag  :", tag)
    def handle_data(self, data):
        print("Data     :", data)
    def handle_comment(self, data):
        print("Comment  :", data)
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    def handle_decl(self, data):
        print("Decl     :", data)
parser = MyHTMLParser()
```
Parsing a doctype:

```
>>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
...             '"http://www.w3.org/TR/html4/strict.dtd">')
Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"
```
Parsing an element with a few attributes and a title:

```
>>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
Start tag: img
     attr: ('src', 'python-logo.png')
     attr: ('alt', 'The Python logo')
>>>
>>> parser.feed('<h1>Python</h1>')
Start tag: h1
Data     : Python
End tag  : h1
```
The content of elements like `script` and `style` is returned as is,
without further parsing:

```
>>> parser.feed('<style type="text/css">#python { color: green }</style>')
Start tag: style
     attr: ('type', 'text/css')
Data     : #python { color: green }
End tag  : style
>>> parser.feed('<script type="text/javascript">'
...             'alert("<strong>hello! ☺</strong>");</script>')
Start tag: script
     attr: ('type', 'text/javascript')
Data     : alert("<strong>hello! ☺</strong>");
End tag  : script
```
Attribute names are converted to lowercase, quotes from attribute values removed,
and `None` is returned as *value* for empty attributes (such as `checked`):

```
>>> parser.feed("<input TYPE='checkbox' checked required='' disabled=disabled>")
Start tag: input
     attr: ('type', 'checkbox')
     attr: ('checked', None)
     attr: ('required', '')
     attr: ('disabled', 'disabled')
```
Parsing comments:

```
>>> parser.feed('<!--a comment-->'
...             '<!--[if IE 9]>IE-specific content<![endif]-->')
Comment  : a comment
Comment  : [if IE 9]>IE-specific content<![endif]
```
Parsing named and numeric character references and converting them to the
correct char (note: these 3 references are all equivalent to `'>'`):

```
>>> parser = MyHTMLParser()
>>> parser.feed('>>>')
Data     : >>>
>>> parser = MyHTMLParser(convert_charrefs=False)
>>> parser.feed('>>>')
Named ent: >
Num ent  : >
Num ent  : >
```
Feeding incomplete chunks to [ feed()](#html.parser.HTMLParser.feed) works, but

[might be called more than once if](#html.parser.HTMLParser.handle_data)

`handle_data()`*convert_charrefs*is false:

```
>>> for chunk in ['<sp', 'an>buff', 'ered', ' text</s', 'pan>']:
...     parser.feed(chunk)
...
Start tag: span
Data     : buff
Data     : ered
Data     :  text
End tag  : span
```
Parsing invalid HTML (e.g. unquoted attributes) also works:

```
>>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
Start tag: p
Start tag: a
     attr: ('class', 'link')
     attr: ('href', '#main')
Data     : tag soup
End tag  : p
End tag  : a
```