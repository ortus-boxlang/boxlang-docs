---
description: Complete guide to creating, modifying, and exporting Word documents with BoxLang
icon: book
---

# 📖 User Guide

Comprehensive guide to all features of the BoxLang Word Module.

---

## Core Concepts

### The `word()` BIF

The `word()` BIF is the primary entry point. It returns a `WordDocument` instance that supports fluent method chaining:

```js
result = word()                          // new empty document
result = word( "/path/to/file.docx" )    // open existing file
result = word( text="Hello World" )      // create from text
result = word( markdown="## Title" )     // create from Markdown
result = word( html="<h1>Title</h1>" )   // create from HTML
```

### The `WordDocument` Object

All mutating methods return `this`, enabling chaining:

```js
word()
    .margins( 1.5, 1.5, 1.5, 1.5 )
    .addHeading( "Title", 1 )
    .addParagraph( "Content" )
    .save( "output.docx" )
```

### Method Chaining Pattern

Every method that modifies the document returns the `WordDocument` instance. This means you can chain indefinitely:

```js
word()
    .setTitle( "My Doc" )
    .setAuthor( "Jane Doe" )
    .margins( 1.78, 1.78, 1.78, 1.78 )
    .pageSize( "A4" )
    .header( "Confidential" )
    .addHeading( "Report", 1 )
    .addParagraph( "Introduction paragraph." )
    .addTable( myQueryData )
    .addPageBreak()
    .addHeading( "Conclusion", 2 )
    .addParagraph( "Final thoughts." )
    .save( "report.docx" )
```

---

## Creating Documents

### From Scratch

```js
doc = word()
```

### Opening Existing Files

```js
doc = word( "/path/to/existing.docx" )
```

### From Text Content

```js
// Via BIF argument
doc = word( text="Hello World\n\nParagraph two" )

// Via importer method
doc = word().fromText( "Hello World\n\nParagraph two" )

// Via static factory
doc = WordDocument.fromText( context, "Hello World\n\nParagraph two" )
```

### From Markdown

```js
// Via BIF argument
doc = word( markdown="## Title\n\n**bold** text" )

// Via importer method
doc = word().fromMarkdown( "## Title\n\n**bold** text" )
```

### From HTML

```js
// Via BIF argument
doc = word( html="<h1>Title</h1><p>Content</p>" )

// Via importer method
doc = word().fromHTML(

## Adding Content

### Headings

Add headings at levels 1 through 6. Levels 1–2 are automatically bold:

```js
word()
    .addHeading( "Document Title", 1 )
    .addHeading( "Section Heading", 2 )
    .addHeading( "Sub-section", 3 )
    .addHeading( "Minor Heading", 4 )
```

{% hint style="info" %}
Levels are clamped to the range 1–6. Level 0 becomes 1; level 7 becomes 6.
{% endhint %}

### Paragraphs

**Plain paragraphs:**

```js
word().addParagraph( "Simple text paragraph." )
```

**Formatted paragraphs:**

```js
word().addParagraph( "Formatted text", {
    bold: true,
    italic: false,
    size: 14,
    color: "FF0000",
    font: "Times New Roman",
    alignment: "CENTER",
    spacingBefore: 240,       // twips (240 twips ≈ 12pt)
    spacingAfter: 120,
    lineSpacing: 360,         // twips for 1.5 line spacing
    firstLineIndent: 720      // twips for 0.5 inch indent
} )
```

| Option | Type | Description |
|--------|------|-------------|
| `bold` | Boolean | Bold text |
| `italic` | Boolean | Italic text |
| `size` | Integer | Font size in points |
| `color` | String | Hex color (with or without `#`) |
| `font` | String | Font family name |
| `alignment` | String | `LEFT`, `CENTER`, `RIGHT`, `JUSTIFY` |
| `spacingBefore` | Integer | Space before paragraph in twips |
| `spacingAfter` | Integer | Space after paragraph in twips |
| `lineSpacing` | Integer | Line spacing in twips (240 = single, 360 = 1.5) |
| `firstLineIndent` | Integer | First line indent in twips |

### Page Breaks

```js
word()
    .addParagraph( "Page one content." )
    .addPageBreak()
    .addParagraph( "Page two content." )
```

### Empty Lines

```js
word()
    .addParagraph( "Above" )
    .newLine()
    .addParagraph( "Below (one blank line between)" )
```

---

## Tables

### From a 2-D Array

The first row is automatically bolded as the header:

```js
word().addTable( [
    [ "Product", "Price", "Stock" ],
    [ "Widget A", "$10.00", "150" ],
    [ "Widget B", "$15.00", "200" ],
    [ "Widget C", "$20.00", "75" ]
] )
```

### From a Query

Column names become bold headers:

```js
products = queryExecute( "SELECT name, price, stock FROM products" )
word().addTable( products )
```

### From a Struct

With explicit `headers` and `data` keys:

```js
word().addTable( {
    headers: [ "Month", "Revenue", "Expenses" ],
    data: [
        [ "January", "$50,000", "$30,000" ],
        [ "February", "$55,000", "$32,000" ]
    ]
} )
```

---

## Lists

### Unordered (Bulleted)

```js
word().addUnorderedList( [ "Apples", "Bananas", "Cherries" ] )
```

### Ordered (Numbered)

```js
word().addOrderedList( [ "First step", "Second step", "Third step" ] )
```

### Nested Lists

Use a struct with `text` and `items` keys for sub-lists:

```js
word().addUnorderedList( [
    "Fruits",
    { text: "Vegetables", items: [ "Carrots", "Broccoli", "Spinach" ] },
    "Grains"
] )
```

{% hint style="info" %}
Nesting supports any depth — sub-items can themselves contain further sub-lists.
{% endhint %}

---

## Images

### From File Path

```js
// Default size: 10cm × 7.5cm
word().addImage( "/path/to/photo.png" )

// Explicit dimensions in cm
word().addImage( "/path/to/photo.png", 5.0, 3.0 )

// With options struct
word().addImage( "/path/to/photo.png", { width: 5.0, height: 3.0 } )
```

### From Bytes

```js
imageBytes = fileReadBinary( "/path/to/photo.png" )
word().addImage( imageBytes, "photo.png" )
word().addImage( imageBytes, "photo.png", 8.0, 6.0 )
```

### From Base64

```js
word().addImageBase64( base64String, "chart.png" )
```

### From URL

```js
word().addImageFromUrl( "https://example.com/logo.png" )
word().addImageFromUrl( "https://example.com/hero.jpg", 15.0, 5.0 )
```

---

## Hyperlinks

```js
word().addHyperlink( "Visit BoxLang", "https://boxlang.io" )
word().addHyperlink( "Email Support", "mailto:support@ortussolutions.com" )
```

Hyperlinks are rendered as blue, underlined text.

---

## Page Setup

### Margins

```js
// Positional: top, bottom, left, right (cm)
word().margins( 2.0, 2.0, 2.5, 2.5 )

// Struct-based
word().margins( { top: 2.0, bottom: 2.0, left: 2.5, right: 2.5 } )
```

### Page Size

```js
word().pageSize( "A4" )       // 210mm × 297mm (default)
word().pageSize( "LETTER" )   // 8.5in × 11in
word().pageSize( "LEGAL" )    // 8.5in × 14in
```

### Orientation

```js
word().orientation( "portrait" )   // default
word().orientation( "landscape" )
```

### Headers & Footers

```js
word()
    .header( "Company Name — Confidential" )
    .footer( "Generated on " & now() )
```

### Section Breaks

Create a new section to apply different page setup to subsequent pages:

```js
word()
    .pageSize( "A4" )
    .orientation( "portrait" )
    .addParagraph( "Portrait page content..." )
    .addSectionBreak()
    .pageSize( "A4" )
    .orientation( "landscape" )
    .addParagraph( "Landscape page content..." )
```

---

## Template Population

### Placeholder Replacement

Replace `{{variableName}}` patterns with actual values:

```js
word( "template.docx" )
    .populate( {
        clientName: "Acme Corp",
        projectDate: "2024-06-15",
        totalAmount: "$150,000"
    } )
    .save( "filled.docx" )
```

### Literal Find & Replace

```js
word( "template.docx" )
    .replaceText( "[COMPANY_NAME]", "Ortus Solutions" )
    .replaceText( "[DATE]", dateTimeFormat( now(), "yyyy-mm-dd" ) )
    .save( "output.docx" )
```

### Bookmarks

```js
word( "template.docx" )
    .setBookmark( "clientAddress", "123 Main St, Springfield" )
    .save( "output.docx" )
```

---

## Saving & Exporting

### Save to File

```js
// Save to a specific path
word().addParagraph( "Hello" ).save( "/output/hello.docx" )

// Save back to the opened path
word( "/output/hello.docx" )
    .addParagraph( "Appended" )
    .save()
```

### Get as Bytes

```js
bytes = word().addParagraph( "Content" ).toBytes()
// Use for HTTP responses, binary storage, etc.
```

### Get as Base64

```js
b64 = word().addParagraph( "Content" ).toBase64()
```

### Write to Stream

```js
word().addParagraph( "Content" ).writeTo( outputStream )
```

---

## Document Properties

```js
word()
    .setTitle( "Q4 Financial Report" )
    .setAuthor( "Jane Doe" )
    .setSubject( "Quarterly financial summary and projections" )
    .setKeywords( "finance, Q4, report, 2024" )
```

---

## Fluent Helpers

### `tap()` — Side Effects in Chains

Execute an action without breaking the chain. Useful for logging or debugging:

```js
word()
    .addParagraph( "Hello" )
    .tap( ( doc ) => logger.info( "Current text: " & doc.toText() ) )
    .addParagraph( "World" )
    .save( "output.docx" )
```

### `when()` — Conditional Branching

Conditionally execute actions without breaking the fluent chain:

```js
word()
    .addHeading( "Report", 1 )
    .when( includeSummary, ( doc ) => doc
        .addHeading( "Summary", 2 )
        .addParagraph( summaryText )
    )
    .addParagraph( "Main content..." )
    .save( "report.docx" )
```

---

## Document Cleanup

The `WordDocument` implements `AutoCloseable`. When done, release POI resources:

```js
doc = word( "input.docx" )
// ... work with document ...
doc.close()
```

{% hint style="warning" %}
After calling `close()`, the document is no longer usable.
{% endhint %}

---

## 📚 Related Resources

{% content-ref url="formatting.md" %}
{% content-ref url="import-export.md" %}
{% content-ref url="advanced-features.md" %}
{% content-ref url="examples.md" %}
{% content-ref url="reference/fluent-api/README.md" %}
