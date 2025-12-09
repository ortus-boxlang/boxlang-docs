---
description: Work with XML documents using BoxLang's powerful XML type and functions
icon: code
---

# 🔖 XML

## 📋 Table of Contents

- [What is XML in BoxLang?](#what-is-xml-in-boxlang)
- [Creating XML Objects](#creating-xml-objects)
- [Accessing XML Data](#accessing-xml-data)
- [Modifying XML](#modifying-xml)
- [XML Attributes](#xml-attributes)
- [XML Namespaces](#xml-namespaces)
- [XPath Queries](#xpath-queries)
- [XML Validation](#xml-validation)
- [XSLT Transformations](#xslt-transformations)
- [Best Practices](#best-practices)

## 🙋 What is XML in BoxLang?

XML (eXtensible Markup Language) is a markup language that defines rules for encoding documents in a format that is both human-readable and machine-readable. BoxLang provides a comprehensive XML type that implements the `IStruct` interface, allowing you to work with XML documents using familiar struct-like syntax while maintaining full DOM (Document Object Model) functionality.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<books>
    <book id="1">
        <title>BoxLang Programming</title>
        <author>BoxLang Developer</author>
        <price>29.99</price>
    </book>
</books>
```

### **🎯 Why Use BoxLang's XML Type?**

* **Struct-like Interface:** Access XML elements using familiar dot notation and struct methods
* **DOM Integration:** Full W3C DOM support for advanced XML manipulation
* **XPath Support:** Query XML documents using powerful XPath expressions
* **Validation:** Built-in DTD and XSD schema validation
* **Transformation:** XSLT support for XML transformations
* **Case Sensitivity:** Configurable case sensitivity for element and attribute names
* **Namespace Aware:** Full XML namespace support

## 🚀 Creating XML Objects

### 📄 Parsing XML from Strings

```javascript
// Parse XML from a string
xmlString = '<?xml version="1.0"?><root><item>value</item></root>';
xmlDoc = xmlParse( xmlString );

// Parse XML from a file
xmlDoc = xmlParse( "./data/books.xml" );

// Parse XML from a URL
xmlDoc = xmlParse( "https://example.com/api/data.xml" );
```

### 🆕 Creating New XML Documents

```javascript
// Create a new empty XML document
xmlDoc = xmlNew();

// Create with case sensitivity (default is false)
xmlDoc = xmlNew( true );

// Create new XML elements
rootElement = xmlElemNew( xmlDoc, "books" );
bookElement = xmlElemNew( xmlDoc, "book" );

// Create elements with namespaces
nsElement = xmlElemNew( xmlDoc, "item", "http://example.com/namespace" );
```

### 🏗️ Using the XML Component

```xml
<bx:xml variable="myXML">
    <books>
        <book id="1">
            <title>Learning BoxLang</title>
            <author>BoxLang Expert</author>
        </book>
    </books>
</bx:xml>
```

The content within the `<bx:xml>` tags is parsed as XML and stored in the specified variable.

### 🎨 XML String Interpolation (The Easy Way!)

BoxLang makes XML creation incredibly simple with string interpolation. You don't need complex builders or verbose DOM manipulation - just use variables directly in your XML strings!

```javascript
// Define your data
bookId = 42;
bookTitle = "BoxLang Mastery";
bookAuthor = "Expert Developer";
bookPrice = 39.99;
category = "programming";
publishDate = dateFormat( now(), "yyyy-mm-dd" );

// Create XML with string interpolation - clean and readable!
xmlString = '
<?xml version="1.0" encoding="UTF-8"?>
<books>
    <book id="#bookId#" category="#category#">
        <title>#bookTitle#</title>
        <author>#bookAuthor#</author>
        <price currency="USD">#numberFormat(bookPrice, "0.00")#</price>
        <publishDate>#publishDate#</publishDate>
        <description>Learn #bookTitle# from #bookAuthor# - the complete guide!</description>
    </book>
</books>';

// Parse the interpolated string into an XML object
xmlDoc = xmlParse( xmlString );
```

#### 🔥 Dynamic XML Generation

```javascript
// Generate XML from arrays and loops
books = [
    { id: 1, title: "BoxLang Basics", author: "Jane Doe", price: 29.99 },
    { id: 2, title: "Advanced BoxLang", author: "John Smith", price: 39.99 },
    { id: 3, title: "BoxLang Best Practices", author: "Sarah Wilson", price: 34.99 }
];

// Build the books section dynamically
booksXML = "";
for ( book in books ) {
    booksXML &= '
        <book id="#book.id#">
            <title>#book.title#</title>
            <author>#book.author#</author>
            <price>#numberFormat(book.price, "0.00")#</price>
        </book>';
}

// Create the complete XML document
catalogXML = '
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
    <metadata>
        <generated>#dateTimeFormat(now(), "yyyy-mm-dd HH:nn:ss")#</generated>
        <totalBooks>#arrayLen(books)#</totalBooks>
    </metadata>
    <books>#booksXML#</books>
</catalog>';

// Parse into XML object
xmlDoc = xmlParse( catalogXML );
```

#### 🛡️ Safe Interpolation with User Data

```javascript
// Always escape user input when building XML
userName = "O'Reilly & Associates";
userComment = 'This book has <script>alert("xss")</script> content';

// Escape dangerous content
safeUserName = xmlFormat( userName );
safeComment = xmlFormat( userComment );

// Safe interpolation
reviewXML = '
<review>
    <reviewer>#safeUserName#</reviewer>
    <comment>#safeComment#</comment>
    <rating>5</rating>
    <date>#dateFormat(now(), "yyyy-mm-dd")#</date>
</review>';

xmlDoc = xmlParse( reviewXML );
```

#### 🎯 Conditional XML Content

```javascript
// Include sections conditionally
includeExtendedInfo = true;
includeAuthorBio = false;
book = {
    title: "BoxLang Guide",
    author: "Tech Writer",
    authorBio: "Experienced developer with 10+ years...",
    isbn: "978-1234567890",
    pages: 350
};

xmlContent = '
<book>
    <title>#book.title#</title>
    <author>#book.author#</author>
    #includeExtendedInfo ? '<isbn>#book.isbn#</isbn><pages>#book.pages#</pages>' : ''#
    #includeAuthorBio ? '<authorBio>#xmlFormat(book.authorBio)#</authorBio>' : ''#
</book>';

xmlDoc = xmlParse( xmlContent );
```

**🌟 Why String Interpolation is Awesome:**

* **Readable:** XML structure is immediately visible
* **Concise:** No verbose DOM manipulation code
* **Flexible:** Easy to include conditional content
* **Familiar:** Uses standard BoxLang string interpolation
* **Efficient:** Single parse operation vs. multiple DOM calls

## 📖 Reading XML Data

### 🔍 Accessing Elements and Attributes

```javascript
// Load XML document
xmlDoc = xmlParse( fileRead( "./books.xml" ) );

// Access root element
rootElement = xmlDoc.XMLRoot;

// Access child elements using dot notation
firstBook = xmlDoc.XMLRoot.book[1];

// Access element text content
title = xmlDoc.XMLRoot.book[1].title.XMLText;

// Access attributes
bookId = xmlDoc.XMLRoot.book[1].XMLAttributes.id;

// Check if element exists
if ( structKeyExists( xmlDoc.XMLRoot, "book" ) ) {
    writeOutput( "Books found!" );
}
```

### 📊 Working with XML Collections

```javascript
// Get all child elements
allBooks = xmlDoc.XMLRoot.XMLChildren;

// Loop through child elements
for ( book in xmlDoc.XMLRoot.book ) {
    writeOutput( "Title: " & book.title.XMLText );
    writeOutput( "Author: " & book.author.XMLText );
}

// Get element count
bookCount = arrayLen( xmlDoc.XMLRoot.book );
```

### 🔎 XPath Queries

```javascript
// Search using XPath
books = xmlSearch( xmlDoc, "//book[@id > 5]" );

// XPath with parameters
results = xmlSearch(
    xmlDoc,
    "//book[price > $minPrice]",
    { "minPrice": 20.00 }
);

// Get specific node information
nodeType = xmlGetNodeType( xmlDoc.XMLRoot );
```

## ✏️ Modifying XML Documents

### 🔧 Adding Elements and Attributes

```javascript
// Create a new book element
newBook = xmlElemNew( xmlDoc, "book" );

// Set attributes
newBook.XMLAttributes.id = "999";
newBook.XMLAttributes.category = "programming";

// Add child elements
titleElement = xmlElemNew( xmlDoc, "title" );
titleElement.XMLText = "Advanced BoxLang";

authorElement = xmlElemNew( xmlDoc, "author" );
authorElement.XMLText = "BoxLang Master";

// Append to parent
arrayAppend( newBook.XMLChildren, titleElement );
arrayAppend( newBook.XMLChildren, authorElement );
arrayAppend( xmlDoc.XMLRoot.XMLChildren, newBook );
```

### 📝 Setting Text Content and CDATA

```javascript
// Set element text
bookElement.title.XMLText = "New Title";

// Add CDATA section
description = xmlElemNew( xmlDoc, "description" );
description.XMLCData = "This is <b>HTML</b> content that should not be parsed";
```

### 🗑️ Removing Elements

```javascript
// Remove an element by index
arrayDeleteAt( xmlDoc.XMLRoot.XMLChildren, 1 );

// Remove all child elements of a specific type
xmlDoc.XMLRoot.book = [];

// Find and remove specific elements
booksToRemove = xmlSearch( xmlDoc, "//book[@id='999']" );
for ( book in booksToRemove ) {
    // Remove from parent's children
    parentNode = book.XMLParent;
    arrayDelete( parentNode.XMLChildren, book );
}
```

## 🔍 Advanced XML Operations

### 🔄 XML Transformations (XSLT)

```javascript
// Define XSLT stylesheet
xslContent = '
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Books</h2>
                <xsl:for-each select="books/book">
                    <p><xsl:value-of select="title"/> by <xsl:value-of select="author"/></p>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>';

// Transform XML to HTML
htmlOutput = xmlTransform( xmlDoc, xslContent );

// Transform with parameters
htmlOutput = xmlTransform(
    xmlDoc,
    xslContent,
    { "showPrices": true, "currency": "USD" }
);
```

### 🛡️ XML Validation

```javascript
// Validate against DTD (embedded in XML)
validationResult = xmlValidate( xmlDoc );

// Validate against external DTD
validationResult = xmlValidate( xmlDoc, "./schemas/books.dtd" );

// Validate against XSD schema
validationResult = xmlValidate( xmlDoc, "./schemas/books.xsd" );

// Check validation results
if ( validationResult.status ) {
    writeOutput( "XML is valid!" );
} else {
    writeOutput( "Validation errors:" );
    for ( error in validationResult.errors ) {
        writeOutput( error );
    }
}
```

### 🏷️ Working with Namespaces

```javascript
// Create elements with namespaces
nsElement = xmlElemNew( xmlDoc, "ns:item", "http://example.com/namespace" );

// Access namespace information
elementPrefix = someElement.XMLNsPrefix;
elementNamespace = someElement.XMLNsURI;

// Search with namespaces in XPath
namespacedResults = xmlSearch(
    xmlDoc,
    "//ns:item[@type='special']"
);
```

## 🔧 Utility Functions

### 📍 Element Position and Navigation

```javascript
// Find position of a child element
position = xmlChildPos( parentElement, "book", 2 ); // Find 2nd book element

// Navigate parent-child relationships
parentElement = childElement.XMLParent;
childElements = parentElement.XMLChildren;

// Get all nodes (including text nodes, comments, etc.)
allNodes = element.XMLNodes;
```

### 🎨 Formatting and Output

```javascript
// Format strings for XML content
safeXMLString = xmlFormat( userInput );

// Format with character escaping
safeXMLString = xmlFormat( userInput, true );

// Convert XML to string
xmlString = toString( xmlDoc );

// Pretty print XML (using Java DOM methods)
xmlString = xmlDoc.toString();
```

## 📚 Common Usage Patterns

### 🗂️ Configuration Files

```javascript
// Load application configuration from XML
configXML = xmlParse( expandPath( "./config/app.xml" ) );

// Read database settings
dbHost = configXML.XMLRoot.database.host.XMLText;
dbPort = configXML.XMLRoot.database.port.XMLText;
dbName = configXML.XMLRoot.database.name.XMLText;

// Read array of allowed IPs
allowedIPs = [];
for ( ip in configXML.XMLRoot.security.allowedIPs.ip ) {
    arrayAppend( allowedIPs, ip.XMLText );
}
```

### 🌐 Web Service Responses

```javascript
// Parse SOAP response
soapResponse = xmlParse( httpResponse.fileContent );

// Extract data from response
resultData = xmlSearch( soapResponse, "//soap:Body//*[local-name()='result']" );

// Process each result
for ( result in resultData ) {
    resultValue = result.XMLText;
    writeOutput( "Result: " & resultValue );
}
```

### 📊 Data Import/Export

```javascript
// Create XML from database query
query = queryExecute( "SELECT * FROM books" );
booksXML = xmlNew();
rootElement = xmlElemNew( booksXML, "books" );

for ( row in query ) {
    bookElement = xmlElemNew( booksXML, "book" );
    bookElement.XMLAttributes.id = row.id;

    titleElement = xmlElemNew( booksXML, "title" );
    titleElement.XMLText = row.title;
    arrayAppend( bookElement.XMLChildren, titleElement );

    authorElement = xmlElemNew( booksXML, "author" );
    authorElement.XMLText = row.author;
    arrayAppend( bookElement.XMLChildren, authorElement );

    arrayAppend( rootElement.XMLChildren, bookElement );
}

// Save to file
fileWrite( "./export/books.xml", toString( booksXML ) );
```

### 🔄 XML-to-JSON Conversion

```javascript
// Convert XML structure to struct
function xmlToStruct( xmlNode ) {
    var result = {};

    // Handle attributes
    if ( structKeyExists( xmlNode, "XMLAttributes" ) ) {
        for ( var attr in xmlNode.XMLAttributes ) {
            result["@" & attr] = xmlNode.XMLAttributes[attr];
        }
    }

    // Handle text content
    if ( structKeyExists( xmlNode, "XMLText" ) && len( trim( xmlNode.XMLText ) ) ) {
        result["#text"] = xmlNode.XMLText;
    }

    // Handle child elements
    if ( structKeyExists( xmlNode, "XMLChildren" ) ) {
        for ( var child in xmlNode.XMLChildren ) {
            var childName = child.XMLName;
            var childData = xmlToStruct( child );

            if ( structKeyExists( result, childName ) ) {
                if ( !isArray( result[childName] ) ) {
                    result[childName] = [ result[childName] ];
                }
                arrayAppend( result[childName], childData );
            } else {
                result[childName] = childData;
            }
        }
    }

    return result;
}

// Convert and serialize to JSON
xmlStruct = xmlToStruct( xmlDoc.XMLRoot );
jsonString = serializeJSON( xmlStruct );
```

## 🔍 RSS/Atom Feed Processing

```javascript
// Parse RSS feed
rssFeed = xmlParse( "https://example.com/rss.xml" );

// Extract feed information
feedTitle = rssFeed.XMLRoot.channel.title.XMLText;
feedDescription = rssFeed.XMLRoot.channel.description.XMLText;

// Process feed items
for ( item in rssFeed.XMLRoot.channel.item ) {
    itemTitle = item.title.XMLText;
    itemLink = item.link.XMLText;
    itemDescription = item.description.XMLText;

    // Parse publication date
    if ( structKeyExists( item, "pubDate" ) ) {
        pubDate = parseDateTime( item.pubDate.XMLText );
    }

    writeOutput( "<h3>#itemTitle#</h3>" );
    writeOutput( "<p>#itemDescription#</p>" );
    writeOutput( "<a href='#itemLink#'>Read more</a>" );
}
```

## 🛡️ Error Handling and Best Practices

### 🚨 Exception Management

```javascript
try {
    // Parse potentially malformed XML
    xmlDoc = xmlParse( userProvidedXML );

    // Validate structure
    if ( !structKeyExists( xmlDoc.XMLRoot, "requiredElement" ) ) {
        throw( type="XMLStructureException", message="Required element not found" );
    }

} catch ( any e ) {
    if ( findNoCase( "parser", e.message ) ) {
        writeOutput( "Invalid XML format: " & e.message );
    } else {
        writeOutput( "XML processing error: " & e.message );
    }
}
```

### ✅ Safe XML Access

```javascript
// Safe element access with null checks
function getXMLText( xmlNode, elementPath, defaultValue = "" ) {
    try {
        var pathParts = listToArray( elementPath, "." );
        var currentNode = xmlNode;

        for ( var part in pathParts ) {
            if ( structKeyExists( currentNode, part ) ) {
                currentNode = currentNode[part];
            } else {
                return defaultValue;
            }
        }

        return structKeyExists( currentNode, "XMLText" ) ? currentNode.XMLText : defaultValue;

    } catch ( any e ) {
        return defaultValue;
    }
}

// Usage
bookTitle = getXMLText( xmlDoc.XMLRoot, "book.title", "Unknown Title" );
```

### 🔒 XML Security

```javascript
// Sanitize user input before including in XML
function sanitizeXMLInput( userInput ) {
    // Remove potentially dangerous content
    var cleaned = reReplace( userInput, "<!(?:--.*?--|[^>]*>)", "", "all" );

    // Escape XML special characters
    return xmlFormat( cleaned );
}

// Safe XML construction
userTitle = sanitizeXMLInput( form.bookTitle );
titleElement.XMLText = userTitle;
```

## 🎯 Best Practices

### ✅ Do's

* **Use XPath for complex queries** instead of nested loops
* **Validate XML** against schemas when data integrity is critical
* **Handle namespaces properly** when working with complex XML documents
* **Cache parsed XML** for frequently accessed documents
* **Use appropriate escaping** for user-generated content
* **Leverage struct methods** for familiar data manipulation

### ❌ Don'ts

* **Don't ignore validation errors** - they indicate data quality issues
* **Don't modify XML during iteration** - it can cause unexpected behavior
* **Don't trust external XML** without validation
* **Don't forget namespace prefixes** in XPath queries
* **Don't mix text content and child elements** unnecessarily
* **Don't create overly deep XML structures** - they're hard to maintain

## 🚦 Performance Tips

### 🎯 Optimization Guidelines

* **Use XPath wisely** - complex expressions can be slow on large documents
* **Cache compiled XPath expressions** for repeated queries
* **Process XML in streams** for very large documents
* **Minimize DOM manipulation** - batch changes when possible
* **Use appropriate validation** - only validate when necessary

### 📊 Memory Management

```javascript
// Process large XML efficiently
function processLargeXML( xmlFile ) {
    var xmlDoc = xmlParse( xmlFile );
    var results = [];

    // Use XPath to get only needed nodes
    var targetNodes = xmlSearch( xmlDoc, "//item[@status='active']" );

    for ( var node in targetNodes ) {
        // Process each node
        results.append( {
            "id": node.XMLAttributes.id,
            "name": node.name.XMLText
        });
    }

    // Clear reference to help GC
    xmlDoc = null;

    return results;
}
```

## 🔗 Integration Examples

### 🌐 Web Services

```javascript
// SOAP web service call
soapEnvelope = '
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetBookInfo xmlns="http://example.com/bookservice">
            <BookId>#bookId#</BookId>
        </GetBookInfo>
    </soap:Body>
</soap:Envelope>';

// Make SOAP request
cfhttp( url="http://example.com/bookservice.asmx", method="POST" ) {
    cfhttpparam( type="header", name="Content-Type", value="text/xml; charset=utf-8" );
    cfhttpparam( type="header", name="SOAPAction", value="http://example.com/GetBookInfo" );
    cfhttpparam( type="body", value=soapEnvelope );
}

// Parse response
responseXML = xmlParse( cfhttp.fileContent );
bookTitle = xmlSearch( responseXML, "//BookTitle" )[1].XMLText;
```

### 📱 Mobile API Responses

```javascript
// Parse mobile app configuration
configResponse = xmlParse( httpResponse.fileContent );

// Extract app settings
appSettings = {
    "version": configResponse.XMLRoot.app.version.XMLText,
    "updateRequired": configResponse.XMLRoot.app.updateRequired.XMLText.toBoolean(),
    "features": []
};

// Extract enabled features
for ( feature in configResponse.XMLRoot.features.feature ) {
    if ( feature.XMLAttributes.enabled == "true" ) {
        arrayAppend( appSettings.features, feature.XMLAttributes.name );
    }
}
```

### 🗄️ Database Integration

```javascript
// Export database to XML
products = queryExecute( "SELECT * FROM products WHERE active = 1" );
catalogXML = xmlNew();
rootElement = xmlElemNew( catalogXML, "catalog" );

for ( product in products ) {
    productElement = xmlElemNew( catalogXML, "product" );
    productElement.XMLAttributes.id = product.id;
    productElement.XMLAttributes.sku = product.sku;

    // Add product details
    nameElement = xmlElemNew( catalogXML, "name" );
    nameElement.XMLText = product.name;
    arrayAppend( productElement.XMLChildren, nameElement );

    priceElement = xmlElemNew( catalogXML, "price" );
    priceElement.XMLText = numberFormat( product.price, "0.00" );
    priceElement.XMLAttributes.currency = "USD";
    arrayAppend( productElement.XMLChildren, priceElement );

    arrayAppend( rootElement.XMLChildren, productElement );
}

// Save catalog
fileWrite( "./exports/catalog.xml", toString( catalogXML ) );
```

BoxLang's XML type provides a powerful, flexible way to work with XML documents that combines the familiarity of struct syntax with the full capabilities of XML DOM manipulation. Whether you're processing configuration files, web service responses, or complex data transformations, BoxLang's XML support offers the tools you need for robust XML handling.
