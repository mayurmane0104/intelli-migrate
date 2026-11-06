# urllib.robotparser — Parser for robots.txt — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/urllib.robotparser.html](https://docs.python.org/3.13/library/urllib.robotparser.html)

---

`urllib.robotparser` —  Parser for robots.txt[¶](#module-urllib.robotparser)

**Source code:** [Lib/urllib/robotparser.py](https://github.com/python/cpython/tree/3.13/Lib/urllib/robotparser.py)

This module provides a single class, [ RobotFileParser](#urllib.robotparser.RobotFileParser), which answers
questions about whether or not a particular user agent can fetch a URL on the
website that published the 

`robots.txt` file.  For more details on the
structure of `robots.txt` files, see [.](https://datatracker.ietf.org/doc/html/rfc9309.html)

**RFC 9309**- 
*class*urllib.robotparser.RobotFileParser(*url=''*)[¶](#urllib.robotparser.RobotFileParser)
- This class provides methods to read, parse and answer questions about the - `robots.txt`file at- *url*.- 
set_url(*url*)[¶](#urllib.robotparser.RobotFileParser.set_url)
- Sets the URL referring to a - `robots.txt`file.
 - 
read()[¶](#urllib.robotparser.RobotFileParser.read)
- Reads the - `robots.txt`URL and feeds it to the parser.
 - 
parse(*lines*)[¶](#urllib.robotparser.RobotFileParser.parse)
- Parses the lines argument. 
 - 
can_fetch(*useragent*,*url*)[¶](#urllib.robotparser.RobotFileParser.can_fetch)
- Returns - `True`if the- *useragent*is allowed to fetch the- *url*according to the rules contained in the parsed- `robots.txt`file.
 - 
mtime()[¶](#urllib.robotparser.RobotFileParser.mtime)
- Returns the time the - `robots.txt`file was last fetched. This is useful for long-running web spiders that need to check for new- `robots.txt`files periodically.
 - 
modified()[¶](#urllib.robotparser.RobotFileParser.modified)
- Sets the time the - `robots.txt`file was last fetched to the current time.
 - 
crawl_delay(*useragent*)[¶](#urllib.robotparser.RobotFileParser.crawl_delay)
- Returns the value of the - `Crawl-delay`parameter from- `robots.txt`for the- *useragent*in question. If there is no such parameter or it doesn’t apply to the- *useragent*specified or the- `robots.txt`entry for this parameter has invalid syntax, return- `None`.- Added in version 3.6. 
 - 
request_rate(*useragent*)[¶](#urllib.robotparser.RobotFileParser.request_rate)
- Returns the contents of the - `Request-rate`parameter from- `robots.txt`as a- [named tuple](../glossary.html#term-named-tuple)- `RequestRate(requests, seconds)`. If there is no such parameter or it doesn’t apply to the- *useragent*specified or the- `robots.txt`entry for this parameter has invalid syntax, return- `None`.- Added in version 3.6. 
 
- 
set_url(

The following example demonstrates basic use of the [ RobotFileParser](#urllib.robotparser.RobotFileParser)
class:

```
>>> import urllib.robotparser
>>> rp = urllib.robotparser.RobotFileParser()
>>> rp.set_url("http://www.pythontest.net/robots.txt")
>>> rp.read()
>>> rrate = rp.request_rate("*")
>>> rrate.requests
1
>>> rrate.seconds
1
>>> rp.crawl_delay("*")
6
>>> rp.can_fetch("*", "http://www.pythontest.net/")
True
>>> rp.can_fetch("*", "http://www.pythontest.net/no-robots-here/")
False
```