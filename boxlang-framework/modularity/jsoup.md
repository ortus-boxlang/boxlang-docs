---
description: >-
  A powerful BoxLang module that provides HTML parsing and cleaning capabilities
  using Jsoup.
icon: html5
---

# Jsoup

A powerful BoxLang module that provides HTML parsing and cleaning capabilities using [Jsoup](https://jsoup.org/). This module enables developers to safely parse, manipulate, and clean HTML content with ease.

### Features

* **HTML Parsing**: Parse HTML strings into manipulable document objects
* **HTML Cleaning**: Sanitize HTML content with customizable safety levels
* **XSS Protection**: Built-in protection against Cross-Site Scripting attacks
* **Flexible Safelists**: Multiple predefined safety levels from strict to relaxed
* **CSS Selectors**: Extract elements using familiar CSS selector syntax
* **Relative Link Handling**: Control how relative links are processed during cleaning

### Installation

This module can be installed using CommandBox or the BoxLang Installer Scripts

```bash
# BoxLang Installer Script
install-bx-module bx-jsoup
# commandbox
box install bx-jsoup
```

### Available BIFs (Built-in Functions)

#### htmlParse( html )

Parses an HTML string and returns a BoxDocument object for manipulation. BoxDocument extends Jsoup's Document class with additional BoxLang-specific methods.

**Parameters:**

* `html` (string, required): The HTML string to parse

**Returns:** A BoxDocument object with methods for HTML manipulation

**Example:**

```javascript
// Parse HTML content
htmlContent = "<html><head><title>My Page</title></head><body><h1>Hello World</h1></body></html>";
doc = htmlParse( htmlContent );

// Access document properties
title = doc.title(); // Returns "My Page"
bodyText = doc.body().text(); // Returns "Hello World"

// Use CSS selectors
htmlContent = "<ul><li class='item'>Item 1</li><li class='item'>Item 2</li></ul>";
doc = htmlParse( htmlContent );
items = doc.select( ".item" ); // Returns elements with class 'item'

// Extract text content
textContent = doc.text(); // Returns plain text without HTML tags

// Enhanced BoxDocument methods
htmlContent = "<div class='container'><h1>Title</h1><p>Content</p></div>";
doc = htmlParse( htmlContent );

// Convert to JSON
jsonString = doc.toJSON(); // Compact JSON
prettyJson = doc.toJSON( true ); // Pretty-printed JSON

// Convert to XML
xmlString = doc.toXML(); // Compact XML
prettyXml = doc.toXML( true, 2 ); // Pretty-printed XML with 2-space indentation
```

**Standard Jsoup Document Methods:**

* `title()` – Get the contents of the `<title>` tag
* `select(selector)` – Find elements using CSS selectors
* `text()` – Get the combined text of the entire document
* `outerHtml()` – Get the HTML of the entire document
* `body()` – Get the `<body>` element
* `head()` – Get the `<head>` element
* `getElementById(id)` – Find an element by its ID attribute
* `getElementsByTag(tagName)` – Get all elements with the given tag
* `getElementsByClass(className)` – Get all elements with the given class
* `getElementsByAttribute(attrName)` – Get elements that have the specified attribute
* `html()` – Get the inner HTML of the document body
* `createElement(tagName)` – Create a new element with the given tag

**Enhanced BoxDocument Methods:**

* `toJSON()` – Convert the document to a compact JSON representation
* `toJSON(prettyPrint)` – Convert to JSON with optional pretty-printing
* `toXML()` – Convert the document to a compact XML representation
* `toXML(prettyPrint, indentFactor)` – Convert to XML with optional pretty-printing and custom indentation

**Enhanced Methods Examples:**

```javascript
// Sample HTML for examples
htmlContent = `
<div class="product" id="item-1">
    <h2>Product Name</h2>
    <p class="description">Product description here</p>
    <span class="price">$19.99</span>
</div>
`;
doc = htmlParse( htmlContent );

// Convert to JSON (compact)
jsonCompact = doc.toJSON();
// Result: {"tag":"html","children":[{"tag":"head"},{"tag":"body","children":[{"tag":"div","attributes":{"class":"product","id":"item-1"},"children":[{"tag":"h2","children":[{"text":"Product Name"}]},{"tag":"p","attributes":{"class":"description"},"children":[{"text":"Product description here"}]},{"tag":"span","attributes":{"class":"price"},"children":[{"text":"$19.99"}]}]}]}]}

// Convert to JSON (pretty-printed)
jsonPretty = doc.toJSON( true );
// Result: Formatted JSON with proper indentation

// Convert to XML (compact)
xmlCompact = doc.toXML();
// Result: <html><head></head><body><div class="product" id="item-1"><h2>Product Name</h2>...</div></body></html>

// Convert to XML (pretty-printed with 4-space indentation)
xmlPretty = doc.toXML( true, 4 );
// Result:
// <html>
//     <head></head>
//     <body>
//         <div class="product" id="item-1">
//             <h2>Product Name</h2>
//             <p class="description">Product description here</p>
//             <span class="price">$19.99</span>
//         </div>
//     </body>
// </html>
```

#### htmlClean( html, safeList, preserveRelativeLinks, baseUri )

Cleans and sanitizes HTML content to prevent XSS attacks and ensure safe rendering.

**Parameters:**

* `html` (string, required): The HTML string to clean
* `safeList` (string, optional): The safety level to apply (default: "relaxed")
* `preserveRelativeLinks` (boolean, optional): Whether to preserve relative links (default: false)
* `baseUri` (string, optional): Base URI for resolving relative links (default: "")

**Returns:** A cleaned HTML string

**Safelist Options:**

* `none`: Maximum cleaning, removes all tags and returns plain text only
* `simpletext`: Allows very limited inline formatting tags like `<b>`, `<i>`, `<br>`
* `basic`: Basic cleaning, removes all tags except for a few safe ones
* `basicwithimages`: Basic cleaning but allows images
* `relaxed`: More lenient cleaning, allows more tags (default)

**Examples:**

```javascript
// Basic cleaning with default "relaxed" safelist
dirtyHtml = "<script>alert('XSS')</script><p>Hello World!</p>";
cleanHtml = htmlClean( dirtyHtml );
// Result: "<p>Hello World!</p>"

// Strict cleaning with "basic" safelist
cleanHtml = htmlClean(
    html: "<img src='image.jpg' /><script>alert('XSS')</script><p>Hello World!</p>",
    safeList: "basic"
);
// Result: "<p>Hello World!</p>"

// Allow images with "basicwithimages" safelist
cleanHtml = htmlClean(
    html: "<img src='image.jpg' /><script>alert('XSS')</script><p>Hello World!</p>",
    safeList: "basicwithimages"
);
// Result: "<img src='image.jpg' /><p>Hello World!</p>"

// Plain text only with "none" safelist
cleanHtml = htmlClean(
    html: "<p><strong>Bold text</strong> and <em>italic text</em></p>",
    safeList: "none"
);
// Result: "Bold text and italic text"

// Preserve relative links
cleanHtml = htmlClean(
    html: "<a href='page.html'>Link</a>",
    preserveRelativeLinks: true
);
// Result: "<a href='page.html'>Link</a>"

// Convert relative links to absolute
cleanHtml = htmlClean(
    html: "<a href='page.html'>Link</a>",
    baseUri: "https://example.com/",
    preserveRelativeLinks: false
);
// Result: "<a href='https://example.com/page.html'>Link</a>"
```

### Use Cases

#### Content Management Systems

Clean user-generated content before storing or displaying:

```javascript
userContent = "<p>Great article! <script>alert('hack')</script></p>";
safeContent = htmlClean( userContent );
// Store or display safeContent safely
```

#### Web Scraping

Parse and extract data from HTML content:

```javascript
scrapedHtml = "<div class='product'><h2>Product Name</h2><span class='price'>$19.99</span></div>";
doc = htmlParse( scrapedHtml );
productName = doc.select( ".product h2" ).text();
price = doc.select( ".price" ).text();
```

#### Data Transformation

Convert HTML to different formats using BoxDocument's enhanced methods:

```javascript
// Parse HTML content
htmlContent = `
<article>
    <header>
        <h1>Article Title</h1>
        <meta name="author" content="John Doe">
    </header>
    <section class="content">
        <p>First paragraph of the article.</p>
        <p>Second paragraph with <em>emphasis</em>.</p>
    </section>
</article>
`;
doc = htmlParse( htmlContent );

// Convert to structured JSON for API responses
jsonData = doc.toJSON( true );
// Use jsonData in REST APIs or data processing

// Convert to XML for legacy systems
xmlData = doc.toXML( true, 2 );
// Use xmlData for XML-based integrations

// Extract plain text for search indexing
textContent = doc.text();
// Use textContent for full-text search
```

#### Email Template Processing

Clean HTML emails before sending:

```javascript
emailTemplate = "<p>Hello {{name}}, <script>malicious()</script></p>";
cleanTemplate = htmlClean( emailTemplate, "basic" );
// Process cleanTemplate safely
```

### GitHub Repository and Reporting Issues

Visit the GitHub repository: [https://github.com/ortus-boxlang/bx-jsoup](https://github.com/ortus-boxlang/bx-jsoup) for release notes. You can also file a bug report or improvement suggestion via [Jira](https://ortussolutions.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=13359\&issuetype=1)
