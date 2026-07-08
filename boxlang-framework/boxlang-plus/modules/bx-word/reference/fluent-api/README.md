---
description: Complete fluent API reference for WordDocument — all methods organized by category
icon: code
---

# Fluent API Reference

Complete reference for all `WordDocument` methods, organized by category.

---

## Lifecycle

### `word()`

Entry point. Creates a new document or opens an existing one.

```js
word()                                // new empty document
word( "/path/to/file.docx" )          // open existing file
word( text="Hello" )                  // create from text
word( markdown="## Title" )           // create from Markdown
word( html="<h1>Title</h1>" )         // create from HTML
```

### `.open( path )`

Open an existing `.docx` file. Already called when using `word( path )`.

| Argument | Type | Description |
|----------|------|-------------|
| `path` | String | Absolute or relative file path |

```js
word().open( "/path/to/file.docx" )
```

### `.save( [path] )`

Save the document. If no path is specified, saves back to the originally opened path.

| Argument | Type | Description |
|----------|------|-------------|
| `path` | String | Destination file path (optional) |

```js
word().addParagraph( "Hello" ).save( "/output/hello.docx" )
word( "/input.docx" ).addParagraph( "Appended" ).save()  // saves back to /input.docx
```

{% hint style="info" %}
Parent directories are automatically created if they don't exist.
{% endhint %}

### `.toBytes()`

Get the document as a byte array.

```js
bytes = word().addParagraph( "Content" ).toBytes()
```

### `.toBase64()`

Get the document as a Base64-encoded string.

```js
b64 = word().addParagraph( "Content" ).toBase64()
```

### `.writeTo( stream )`

Write the document to an `OutputStream`.

| Argument | Type | Description |
|----------|------|-------------|
| `stream` | OutputStream | Target stream (caller is responsible for closing) |

```js
word().addParagraph( "Content" ).writeTo( response.getOutputStream() )
```

### `.getDocument()`

Expose the underlying Apache POI `XWPFDocument` for advanced use cases.

```js
poiDoc = word().getDocument()
```

### `.close()`

Release the underlying POI document resources. Implements `AutoCloseable`.

```js
doc = word( "input.docx" )
// ... work with document ...
doc.close()
```

---

## Importers

### `.fromText( text )`

Populate the document from plain text. Paragraphs are split on double newlines.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Plain text content |

```js
word().fromText( "Hello World\n\nParagraph two" )
```

### `.fromMarkdown( markdown )`

Populate the document from Markdown using CommonMark parsing.

| Argument | Type | Description |
|----------|------|-------------|
| `markdown` | String | Markdown content |

```js
word().fromMarkdown( "## Title\n\n**Bold** and *italic* text." )
```

### `.fromHTML( html )`

Populate the document from HTML using Jsoup parsing.

| Argument | Type | Description |
|----------|------|-------------|
| `html` | String | HTML content |

```js
word().fromHTML( "<h1>Title</h1><p>Content</p>" )
```

---

## Exporters

### `.toText()`

Extract all visible text as a plain string. Includes paragraphs, table cell content, headers, and footers.

```js
text = word( "report.docx" ).toText()
```

### `.toMarkdown()`

Convert the document to Markdown with YAML front matter, pipe tables, and base64 images.

```js
markdown = word( "report.docx" ).toMarkdown()
```

### `.toHTML()`

Convert the document to HTML with inline styles and base64 images.

```js
html = word( "report.docx" ).toHTML()
```

---

## Content

### `.addHeading( text, level )`

Add a heading at the given level (1–6). Levels 1–2 are automatically bold.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Heading text |
| `level` | Integer | Heading level (1–6, clamped) |

```js
word()
    .addHeading( "Main Title", 1 )
    .addHeading( "Section", 2 )
    .addHeading( "Sub-section", 3 )
```

### `.addParagraph( text, [options] )`

Add a paragraph with optional formatting.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Paragraph content |
| `options` | Struct | Formatting options (bold, italic, size, color, font, alignment, spacingBefore, spacingAfter, lineSpacing, firstLineIndent) |

```js
// Plain paragraph
word().addParagraph( "Simple text." )

// Formatted paragraph
word().addParagraph( "Formatted text", {
    bold: true,
    size: 14,
    color: "FF0000",
    alignment: "CENTER",
    spacingAfter: 240
} )
```

### `.addPageBreak()`

Insert a page break.

```js
word()
    .addParagraph( "Page 1 content" )
    .addPageBreak()
    .addParagraph( "Page 2 content" )
```

### `.addSectionBreak()`

Insert a section break (next page). Subsequent page setup changes apply to the new section only.

```js
word()
    .orientation( "portrait" )
    .addParagraph( "Portrait page" )
    .addSectionBreak()
    .orientation( "landscape" )
    .addParagraph( "Landscape page" )
```

### `.newLine()`

Add an empty paragraph (blank line).

```js
word()
    .addParagraph( "Above" )
    .newLine()
    .addParagraph( "Below (one blank line between)" )
```

---

## Tables

### `.addTable( data )`

Add a table from an Array (2-D), Query, or Struct.

| Argument | Type | Description |
|----------|------|-------------|
| `data` | Array / Query / Struct | Table data |

**From Array:** First row is auto-bolded as header.

```js
word().addTable( [
    [ "Name", "Role" ],
    [ "Alice", "Engineer" ],
    [ "Bob", "Designer" ]
] )
```

**From Query:** Column names become bold headers.

```js
word().addTable( queryExecute( "SELECT name, role FROM employees" ) )
```

**From Struct:** With `headers` and `data` keys.

```js
word().addTable( {
    headers: [ "Product", "Price" ],
    data: [ [ "Widget A", "$10" ], [ "Widget B", "$15" ] ]
} )
```

---

## Images

### `.addImage( path, [widthCm], [heightCm] )`

Add an image from a file path. Default size: 10cm × 7.5cm.

| Argument | Type | Description |
|----------|------|-------------|
| `path` | String | Absolute path to the image file |
| `widthCm` | Double | Width in cm (optional, default 10.0) |
| `heightCm` | Double | Height in cm (optional, default 7.5) |

### `.addImage( path, options )`

Add an image with options struct.

| Option | Type | Description |
|--------|------|-------------|
| `width` | Double | Width in cm |
| `height` | Double | Height in cm |

```js
word()
    .addImage( "/path/to/photo.png" )
    .addImage( "/path/to/logo.png", 5.0, 3.0 )
    .addImage( "/path/to/chart.png", { width: 12.0, height: 8.0 } )
```

### `.addImage( bytes, fileName, [widthCm], [heightCm] )`

Add an image from raw byte data.

| Argument | Type | Description |
|----------|------|-------------|
| `bytes` | byte[] | Image data |
| `fileName` | String | File name (used to infer format) |
| `widthCm` | Double | Width in cm (optional, default 10.0) |
| `heightCm` | Double | Height in cm (optional, default 7.5) |

```js
bytes = fileReadBinary( "/path/to/photo.png" )
word().addImage( bytes, "photo.png" )
word().addImage( bytes, "photo.png", 8.0, 6.0 )
```

### `.addImageBase64( base64Str, fileName )`

Add an image from a Base64-encoded string.

| Argument | Type | Description |
|----------|------|-------------|
| `base64Str` | String | Base64-encoded image data |
| `fileName` | String | File name (used to infer format) |

```js
word().addImageBase64( base64Data, "chart.png" )
```

### `.addImageFromUrl( url, [widthCm], [heightCm] )`

Download and embed an image from a URL.

| Argument | Type | Description |
|----------|------|-------------|
| `url` | String | URL of the image |
| `widthCm` | Double | Width in cm (optional, default 10.0) |
| `heightCm` | Double | Height in cm (optional, default 7.5) |

```js
word()
    .addImageFromUrl( "https://example.com/logo.png" )
    .addImageFromUrl( "https://example.com/hero.jpg", 15.0, 5.0 )
```

---

## Lists

### `.addUnorderedList( items )`

Add a bulleted list. Supports nesting via structs with `text` and `items` keys.

| Argument | Type | Description |
|----------|------|-------------|
| `items` | Array | Array of strings or structs |

```js
word().addUnorderedList( [ "Apples", "Bananas", "Cherries" ] )

// With nesting
word().addUnorderedList( [
    "Fruits",
    { text: "Vegetables", items: [ "Carrots", "Broccoli" ] }
] )
```

### `.addOrderedList( items )`

Add a numbered list. Supports nesting via structs with `text` and `items` keys.

| Argument | Type | Description |
|----------|------|-------------|
| `items` | Array | Array of strings or structs |

```js
word().addOrderedList( [ "First", "Second", "Third" ] )
```

---

## Hyperlinks

### `.addHyperlink( text, url )`

Add a clickable hyperlink as a new paragraph. Rendered as blue, underlined text.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Display text |
| `url` | String | Hyperlink URL |

```js
word().addHyperlink( "Visit BoxLang", "https://boxlang.io" )
word().addHyperlink( "Email Support", "mailto:support@ortussolutions.com" )
```

---

## Page Setup

### `.margins( top, bottom, left, right )`

Set all four page margins in centimeters.

| Argument | Type | Description |
|----------|------|-------------|
| `top` | Double | Top margin (cm) |
| `bottom` | Double | Bottom margin (cm) |
| `left` | Double | Left margin (cm) |
| `right` | Double | Right margin (cm) |

```js
word().margins( 2.0, 2.0, 2.5, 2.5 )
```

### `.margins( options )`

Set margins via a struct.

| Option | Type | Description |
|--------|------|-------------|
| `top` | Double | Top margin (cm, default 2.54) |
| `bottom` | Double | Bottom margin (cm, default 2.54) |
| `left` | Double | Left margin (cm, default 2.54) |
| `right` | Double | Right margin (cm, default 2.54) |

```js
word().margins( { top: 2.0, left: 3.0 } )
```

### `.pageSize( size )`

Set the page size.

| Argument | Type | Description |
|----------|------|-------------|
| `size` | String | `"A4"`, `"LETTER"`, or `"LEGAL"` |

```js
word().pageSize( "A4" )
word().pageSize( "LETTER" )
word().pageSize( "LEGAL" )
```

### `.orientation( orientation )`

Set page orientation.

| Argument | Type | Description |
|----------|------|-------------|
| `orientation` | String | `"portrait"` or `"landscape"` |

```js
word().orientation( "portrait" )
word().orientation( "landscape" )
```

### `.header( text )`

Set the document header text.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Header content |

```js
word().header( "Company Confidential" )
```

### `.footer( text )`

Set the document footer text.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Footer content |

```js
word().footer( "Page 1" )
```

---

## Template Population

### `.populate( data )`

Replace `{{variableName}}` placeholders throughout the document.

| Argument | Type | Description |
|----------|------|-------------|
| `data` | Struct | Key-value pairs mapping placeholder names to replacement values |

```js
word( "template.docx" )
    .populate( { name: "John", date: "2024-01-01", amount: "$500" } )
    .save()
```

### `.replaceText( find, replace )`

Literal find-and-replace across all paragraphs (including table cells).

| Argument | Type | Description |
|----------|------|-------------|
| `find` | String | Literal text to find |
| `replace` | String | Replacement text |

```js
word( "template.docx" )
    .replaceText( "[COMPANY]", "ACME Corp" )
    .replaceText( "[DATE]", "2024-06-15" )
    .save()
```

### `.setBookmark( name, value )`

Set a named bookmark to the given text.

| Argument | Type | Description |
|----------|------|-------------|
| `name` | String | Bookmark name |
| `value` | String | Replacement text |

```js
word( "template.docx" )
    .setBookmark( "clientName", "Acme Corp" )
    .save()
```

### `.setContentControl( tag, value )`

Set a content control (SDT) by its tag name.

| Argument | Type | Description |
|----------|------|-------------|
| `tag` | String | SDT tag value |
| `value` | String | Replacement text |

```js
word( "template.docx" )
    .setContentControl( "signatureDate", "2024-06-15" )
    .save()
```

---

## Document Properties

### `.setTitle( title )`

Set the document title (appears in Word properties and Markdown YAML front matter).

| Argument | Type | Description |
|----------|------|-------------|
| `title` | String | Document title |

### `.setAuthor( author )`

Set the document author/creator.

| Argument | Type | Description |
|----------|------|-------------|
| `author` | String | Author name |

### `.setSubject( subject )`

Set the document subject/description.

| Argument | Type | Description |
|----------|------|-------------|
| `subject` | String | Document subject |

### `.setKeywords( keywords )`

Set comma-separated keywords.

| Argument | Type | Description |
|----------|------|-------------|
| `keywords` | String | Comma-separated keywords |

```js
word()
    .setTitle( "Q4 Report" )
    .setAuthor( "Jane Doe" )
    .setSubject( "Quarterly financial summary" )
    .setKeywords( "finance, Q4, report" )
    .save( "report.docx" )
```

### `.setDefaultFont( family, size )`

Apply a font family and size to all existing runs.

| Argument | Type | Description |
|----------|------|-------------|
| `family` | String | Font family name |
| `size` | Integer | Font size in points |

```js
word( "template.docx" )
    .setDefaultFont( "Calibri", 11 )
    .save()
```

---

## Security & Advanced

### `.addWatermark( text )`

Add a text watermark ("DRAFT", "CONFIDENTIAL", etc.) to every page.

| Argument | Type | Description |
|----------|------|-------------|
| `text` | String | Watermark text |

```js
word()
    .addWatermark( "CONFIDENTIAL" )
    .save( "confidential.docx" )
```

### `.protect( password )`

Password-protect the document. User must enter the password to view it.

| Argument | Type | Description |
|----------|------|-------------|
| `password` | String | Protection password |

```js
word()
    .addParagraph( "Sensitive content" )
    .protect( "secret123" )
    .save( "protected.docx" )
```

### `.addTableOfContents()`

Insert a TOC field that Word auto-generates when the document is opened.

```js
word()
    .addTableOfContents()
    .addPageBreak()
    .addHeading( "Introduction", 1 )
    .addParagraph( "..." )
    .save( "handbook.docx" )
```

---

## Fluent Helpers

### `.tap( action )`

Execute a side-effect action without breaking the chain. Useful for logging or debugging.

| Argument | Type | Description |
|----------|------|-------------|
| `action` | Consumer\<WordDocument\> | Action to perform on this document |

```js
word()
    .addParagraph( "Hello" )
    .tap( ( doc ) => logger.info( doc.toText() ) )
    .addParagraph( "World" )
    .save()
```

### `.when( condition, action )`

Conditionally execute an action in the fluent chain.

| Argument | Type | Description |
|----------|------|-------------|
| `condition` | Boolean | Whether to execute the action |
| `action` | Consumer\<WordDocument\> | Action to perform if condition is true |

```js
word()
    .addHeading( "Report", 1 )
    .when( isAdmin, ( doc ) => doc.addParagraph( "Admin-only content" ) )
    .save()
```

---

## 📚 Related Resources

{% content-ref url="../../user-guide.md" %}
{% content-ref url="../../advanced-features.md" %}
{% content-ref url="../../formatting.md" %}
{% content-ref url="../built-in-functions/Word.md" %}
