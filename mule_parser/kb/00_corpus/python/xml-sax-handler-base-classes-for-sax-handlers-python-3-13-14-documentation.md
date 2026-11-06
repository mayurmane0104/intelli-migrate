# xml.sax.handler — Base classes for SAX handlers — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/xml.sax.handler.html](https://docs.python.org/3.13/library/xml.sax.handler.html)

---

`xml.sax.handler` — Base classes for SAX handlers[¶](#module-xml.sax.handler)

**Source code:** [Lib/xml/sax/handler.py](https://github.com/python/cpython/tree/3.13/Lib/xml/sax/handler.py)

The SAX API defines five kinds of handlers: content handlers, DTD handlers,
error handlers, entity resolvers and lexical handlers. Applications normally
only need to implement those interfaces whose events they are interested in;
they can implement the interfaces in a single object or in multiple objects.
Handler implementations should inherit from the base classes provided in the
module `xml.sax.handler`, so that all methods get default implementations.

- 
*class*xml.sax.handler.ContentHandler[¶](#xml.sax.handler.ContentHandler)
- This is the main callback interface in SAX, and the one most important to applications. The order of events in this interface mirrors the order of the information in the document. 

- 
*class*xml.sax.handler.DTDHandler[¶](#xml.sax.handler.DTDHandler)
- Handle DTD events. - This interface specifies only those DTD events required for basic parsing (unparsed entities and attributes). 

- 
*class*xml.sax.handler.EntityResolver[¶](#xml.sax.handler.EntityResolver)
- Basic interface for resolving entities. If you create an object implementing this interface, then register the object with your Parser, the parser will call the method in your object to resolve all external entities. 

- 
*class*xml.sax.handler.ErrorHandler[¶](#xml.sax.handler.ErrorHandler)
- Interface used by the parser to present error and warning messages to the application. The methods of this object control whether errors are immediately converted to exceptions or are handled in some other way. 

- 
*class*xml.sax.handler.LexicalHandler[¶](#xml.sax.handler.LexicalHandler)
- Interface used by the parser to represent low frequency events which may not be of interest to many applications. 

In addition to these classes, `xml.sax.handler` provides symbolic constants
for the feature and property names.

- 
xml.sax.handler.feature_namespaces[¶](#xml.sax.handler.feature_namespaces)
- value:`"http://xml.org/sax/features/namespaces"`true: Perform Namespace processing.false: Optionally do not perform Namespace processing (implies namespace-prefixes; default).access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.feature_namespace_prefixes[¶](#xml.sax.handler.feature_namespace_prefixes)
- value:`"http://xml.org/sax/features/namespace-prefixes"`true: Report the original prefixed names and attributes used for Namespace declarations.false: Do not report attributes used for Namespace declarations, and optionally do not report original prefixed names (default).access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.feature_string_interning[¶](#xml.sax.handler.feature_string_interning)
- value:`"http://xml.org/sax/features/string-interning"`true: All element names, prefixes, attribute names, Namespace URIs, and local names are interned using the built-in intern function.false: Names are not necessarily interned, although they may be (default).access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.feature_validation[¶](#xml.sax.handler.feature_validation)
- value:`"http://xml.org/sax/features/validation"`true: Report all validation errors (implies external-general-entities and external-parameter-entities).false: Do not report validation errors.access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.feature_external_ges[¶](#xml.sax.handler.feature_external_ges)
- Warning - Enabling opens a vulnerability to - [external entity attacks](https://en.wikipedia.org/wiki/XML_external_entity_attack)if the parser is used with user-provided XML content. Please reflect on your- [threat model](https://en.wikipedia.org/wiki/Threat_model)before enabling this feature.value:- `"http://xml.org/sax/features/external-general-entities"`true: Include all external general (text) entities.false: Do not include external general entities.access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.feature_external_pes[¶](#xml.sax.handler.feature_external_pes)
- value:`"http://xml.org/sax/features/external-parameter-entities"`true: Include all external parameter entities, including the external DTD subset.false: Do not include any external parameter entities, even the external DTD subset.access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.all_features[¶](#xml.sax.handler.all_features)
- List of all features. 

- 
xml.sax.handler.property_lexical_handler[¶](#xml.sax.handler.property_lexical_handler)
- value:`"http://xml.org/sax/properties/lexical-handler"`data type: xml.sax.handler.LexicalHandler (not supported in Python 2)description: An optional extension handler for lexical events like comments.access: read/write

- 
xml.sax.handler.property_declaration_handler[¶](#xml.sax.handler.property_declaration_handler)
- value:`"http://xml.org/sax/properties/declaration-handler"`data type: xml.sax.sax2lib.DeclHandler (not supported in Python 2)description: An optional extension handler for DTD-related events other than notations and unparsed entities.access: read/write

- 
xml.sax.handler.property_dom_node[¶](#xml.sax.handler.property_dom_node)
- value:`"http://xml.org/sax/properties/dom-node"`data type: org.w3c.dom.Node (not supported in Python 2)description: When parsing, the current DOM node being visited if this is a DOM iterator; when not parsing, the root DOM node for iteration.access: (parsing) read-only; (not parsing) read/write

- 
xml.sax.handler.property_xml_string[¶](#xml.sax.handler.property_xml_string)
- value:`"http://xml.org/sax/properties/xml-string"`data type: Bytesdescription: The literal string of characters that was the source for the current event.access: read-only

- 
xml.sax.handler.all_properties[¶](#xml.sax.handler.all_properties)
- List of all known property names. 

## ContentHandler Objects[¶](#contenthandler-objects)

Users are expected to subclass [ ContentHandler](#xml.sax.handler.ContentHandler) to support their
application.  The following methods are called by the parser on the appropriate
events in the input document:

- 
ContentHandler.setDocumentLocator(*locator*)[¶](#xml.sax.handler.ContentHandler.setDocumentLocator)
- Called by the parser to give the application a locator for locating the origin of document events. - SAX parsers are strongly encouraged (though not absolutely required) to supply a locator: if it does so, it must supply the locator to the application by invoking this method before invoking any of the other methods in the DocumentHandler interface. - The locator allows the application to determine the end position of any document-related event, even if the parser is not reporting an error. Typically, the application will use this information for reporting its own errors (such as character content that does not match an application’s business rules). The information returned by the locator is probably not sufficient for use with a search engine. - Note that the locator will return correct information only during the invocation of the events in this interface. The application should not attempt to use it at any other time. 

- 
ContentHandler.startDocument()[¶](#xml.sax.handler.ContentHandler.startDocument)
- Receive notification of the beginning of a document. - The SAX parser will invoke this method only once, before any other methods in this interface or in DTDHandler (except for - `setDocumentLocator()`

- 
ContentHandler.endDocument()[¶](#xml.sax.handler.ContentHandler.endDocument)
- Receive notification of the end of a document. - The SAX parser will invoke this method only once, and it will be the last method invoked during the parse. The parser shall not invoke this method until it has either abandoned parsing (because of an unrecoverable error) or reached the end of input. 

- 
ContentHandler.startPrefixMapping(*prefix*,*uri*)[¶](#xml.sax.handler.ContentHandler.startPrefixMapping)
- Begin the scope of a prefix-URI Namespace mapping. - The information from this event is not necessary for normal Namespace processing: the SAX XML reader will automatically replace prefixes for element and attribute names when the - `feature_namespaces`feature is enabled (the default).- There are cases, however, when applications need to use prefixes in character data or in attribute values, where they cannot safely be expanded automatically; the - `startPrefixMapping()`and- `endPrefixMapping()`- Note that - `startPrefixMapping()`and- `endPrefixMapping()`- `startPrefixMapping()`events will occur before the corresponding- `startElement()`- `endPrefixMapping()`events will occur after the corresponding- `endElement()`

- 
ContentHandler.endPrefixMapping(*prefix*)[¶](#xml.sax.handler.ContentHandler.endPrefixMapping)
- End the scope of a prefix-URI mapping. - See - `startPrefixMapping()`- `endElement()`- `endPrefixMapping()`events is not otherwise guaranteed.

- 
ContentHandler.startElement(*name*,*attrs*)[¶](#xml.sax.handler.ContentHandler.startElement)
- Signals the start of an element in non-namespace mode. - The - *name*parameter contains the raw XML 1.0 name of the element type as a string and the- *attrs*parameter holds an object of the- [Attributes](xml.sax.reader.html#attributes-objects)interface containing the attributes of the element. The object passed as- *attrs*may be re-used by the parser; holding on to a reference to it is not a reliable way to keep a copy of the attributes. To keep a copy of the attributes, use the- `copy()`- *attrs*object.

- 
ContentHandler.endElement(*name*)[¶](#xml.sax.handler.ContentHandler.endElement)
- Signals the end of an element in non-namespace mode. - The - *name*parameter contains the name of the element type, just as with the- `startElement()`

- 
ContentHandler.startElementNS(*name*,*qname*,*attrs*)[¶](#xml.sax.handler.ContentHandler.startElementNS)
- Signals the start of an element in namespace mode. - The - *name*parameter contains the name of the element type as a- `(uri, localname)`tuple, the- *qname*parameter contains the raw XML 1.0 name used in the source document, and the- *attrs*parameter holds an instance of the- [AttributesNS](xml.sax.reader.html#attributes-ns-objects)interface containing the attributes of the element. If no namespace is associated with the element, the- *uri*component of- *name*will be- `None`. The object passed as- *attrs*may be re-used by the parser; holding on to a reference to it is not a reliable way to keep a copy of the attributes. To keep a copy of the attributes, use the- `copy()`- *attrs*object.- Parsers may set the - *qname*parameter to- `None`, unless the- `feature_namespace_prefixes`feature is activated.

- 
ContentHandler.endElementNS(*name*,*qname*)[¶](#xml.sax.handler.ContentHandler.endElementNS)
- Signals the end of an element in namespace mode. - The - *name*parameter contains the name of the element type, just as with the- `startElementNS()`- *qname*parameter.

- 
ContentHandler.characters(*content*)[¶](#xml.sax.handler.ContentHandler.characters)
- Receive notification of character data. - The Parser will call this method to report each chunk of character data. SAX parsers may return all contiguous character data in a single chunk, or they may split it into several chunks; however, all of the characters in any single event must come from the same external entity so that the Locator provides useful information. - *content*may be a string or bytes instance; the- `expat`reader module always produces strings.- Note - The earlier SAX 1 interface provided by the Python XML Special Interest Group used a more Java-like interface for this method. Since most parsers used from Python did not take advantage of the older interface, the simpler signature was chosen to replace it. To convert old code to the new interface, use - *content*instead of slicing content with the old- *offset*and- *length*parameters.

- 
ContentHandler.ignorableWhitespace(*whitespace*)[¶](#xml.sax.handler.ContentHandler.ignorableWhitespace)
- Receive notification of ignorable whitespace in element content. - Validating Parsers must use this method to report each chunk of ignorable whitespace (see the W3C XML 1.0 recommendation, section 2.10): non-validating parsers may also use this method if they are capable of parsing and using content models. - SAX parsers may return all contiguous whitespace in a single chunk, or they may split it into several chunks; however, all of the characters in any single event must come from the same external entity, so that the Locator provides useful information. 

- 
ContentHandler.processingInstruction(*target*,*data*)[¶](#xml.sax.handler.ContentHandler.processingInstruction)
- Receive notification of a processing instruction. - The Parser will invoke this method once for each processing instruction found: note that processing instructions may occur before or after the main document element. - A SAX parser should never report an XML declaration (XML 1.0, section 2.8) or a text declaration (XML 1.0, section 4.3.1) using this method. 

- 
ContentHandler.skippedEntity(*name*)[¶](#xml.sax.handler.ContentHandler.skippedEntity)
- Receive notification of a skipped entity. - The Parser will invoke this method once for each entity skipped. Non-validating processors may skip entities if they have not seen the declarations (because, for example, the entity was declared in an external DTD subset). All processors may skip external entities, depending on the values of the - `feature_external_ges`and the- `feature_external_pes`properties.

## DTDHandler Objects[¶](#dtdhandler-objects)

[ DTDHandler](#xml.sax.handler.DTDHandler) instances provide the following methods:

- 
DTDHandler.notationDecl(*name*,*publicId*,*systemId*)[¶](#xml.sax.handler.DTDHandler.notationDecl)
- Handle a notation declaration event. 

- 
DTDHandler.unparsedEntityDecl(*name*,*publicId*,*systemId*,*ndata*)[¶](#xml.sax.handler.DTDHandler.unparsedEntityDecl)
- Handle an unparsed entity declaration event. 

## EntityResolver Objects[¶](#entityresolver-objects)

- 
EntityResolver.resolveEntity(*publicId*,*systemId*)[¶](#xml.sax.handler.EntityResolver.resolveEntity)
- Resolve the system identifier of an entity and return either the system identifier to read from as a string, or an InputSource to read from. The default implementation returns - *systemId*.

## ErrorHandler Objects[¶](#errorhandler-objects)

Objects with this interface are used to receive error and warning information
from the [ XMLReader](xml.sax.reader.html#xml.sax.xmlreader.XMLReader).  If you create an object that
implements this interface, then register the object with your

`XMLReader`, the parser
will call the methods in your object to report all warnings and errors. There
are three levels of errors available: warnings, (possibly) recoverable errors,
and unrecoverable errors.  All methods take a [as the only parameter. Errors and warnings may be converted to an exception by raising the passed-in exception object.](xml.sax.html#xml.sax.SAXParseException)

`SAXParseException`- 
ErrorHandler.error(*exception*)[¶](#xml.sax.handler.ErrorHandler.error)
- Called when the parser encounters a recoverable error. If this method does not raise an exception, parsing may continue, but further document information should not be expected by the application. Allowing the parser to continue may allow additional errors to be discovered in the input document. 

- 
ErrorHandler.fatalError(*exception*)[¶](#xml.sax.handler.ErrorHandler.fatalError)
- Called when the parser encounters an error it cannot recover from; parsing is expected to terminate when this method returns. 

- 
ErrorHandler.warning(*exception*)[¶](#xml.sax.handler.ErrorHandler.warning)
- Called when the parser presents minor warning information to the application. Parsing is expected to continue when this method returns, and document information will continue to be passed to the application. Raising an exception in this method will cause parsing to end. 

## LexicalHandler Objects[¶](#lexicalhandler-objects)

Optional SAX2 handler for lexical events.

This handler is used to obtain lexical information about an XML document. Lexical information includes information describing the document encoding used and XML comments embedded in the document, as well as section boundaries for the DTD and for any CDATA sections. The lexical handlers are used in the same manner as content handlers.

Set the LexicalHandler of an XMLReader by using the setProperty method
with the property identifier
`'http://xml.org/sax/properties/lexical-handler'`.

- 
LexicalHandler.comment(*content*)[¶](#xml.sax.handler.LexicalHandler.comment)
- Reports a comment anywhere in the document (including the DTD and outside the document element). 

- 
LexicalHandler.startDTD(*name*,*public_id*,*system_id*)[¶](#xml.sax.handler.LexicalHandler.startDTD)
- Reports the start of the DTD declarations if the document has an associated DTD. 

- 
LexicalHandler.endDTD()[¶](#xml.sax.handler.LexicalHandler.endDTD)
- Reports the end of DTD declaration. 

- 
LexicalHandler.startCDATA()[¶](#xml.sax.handler.LexicalHandler.startCDATA)
- Reports the start of a CDATA marked section. - The contents of the CDATA marked section will be reported through the characters handler. 

- 
LexicalHandler.endCDATA()[¶](#xml.sax.handler.LexicalHandler.endCDATA)
- Reports the end of a CDATA marked section.