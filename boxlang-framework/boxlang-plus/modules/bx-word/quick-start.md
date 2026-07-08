---
description: Create your first Word document with BoxLang in under 5 minutes
icon: rocket
---

# 🚀 Quick Start

Get up and running with the BoxLang Word Module in minutes.

---

## 📦 Installation

Install the module via CommandBox:

```bash
box install bx-word
```

> {% hint style="info" %}
> This module requires a **BoxLang+ license**. Make sure `bx-plus` is installed and licensed.
> {% endhint %}

---

## 1. Your First Document

Create a new document, add content, and save it — all in a single fluent chain:

```js
word( "my-first-document.docx" )
    .addHeading( "Hello, BoxLang!", 1 )
    .addParagraph( "This is my first Word document created with BoxLang." )
    .save()
```

That's it! You now have a `.docx` file on disk.

---

## 2. Adding Content

### Headings

Add headings at levels 1 through 6:

```js
word()
    .addHeading( "Main Title", 1 )
    .addHeading( "Section", 2 )
    .addHeading( "Sub-section", 3 )
    .save( "headings.docx" )
```

### Paragraphs

Plain and formatted paragraphs:

```js
word()
    .addParagraph( "A simple paragraph." )
    .addParagraph( "Bold and colored text.", { bold: true, color: "FF0000", size: 14 } )
    .save( "paragraphs.docx" )
```

### Tables

Tables from arrays, queries, or structs:

```js
word()
    .addHeading( "Team Roster", 2 )
    .addTable( [
        [ "Name", "Role", "Location" ],
        [ "Alice", "Engineer", "New York" ],
        [ "Bob", "Designer", "London" ]
    ] )
    .save( "table.docx" )
```

{% hint style="success" %}
The first row is automatically bolded as the header row.
{% endhint %}

### Lists

Ordered and unordered lists:

```js
word()
    .addHeading( "Agenda", 2 )
    .addOrderedList( [ "Introductions", "Quarterly Review", "Q&A" ] )
    .addUnorderedList( [ "Apples", "Bananas", "Cherries" ] )
    .save( "lists.docx" )
```

### Images

Images from files, bytes, base64, or URLs:

```js
word()
    .addHeading( "Photo", 2 )
    .addImage( "/path/to/photo.png" )           // from file (10cm × 7.5cm default)
    .addImage( "/path/to/logo.png", 5.0, 3.0 )  // with explicit dimensions
    .addImageFromUrl( "https://example.com/pic.jpg" )
    .save( "images.docx" )
```

### Hyperlinks

Clickable links:

```js
word()
    .addHyperlink( "Visit BoxLang", "https://boxlang.io" )
    .save( "links.docx" )
```

---

## 3. Opening Existing Documents

Load an existing `.docx` file to modify it:

```js
word( "/path/to/existing.docx" )
    .addParagraph( "Appended content!" )
    .save( "/path/to/modified.docx" )
```

---

## 4. Template Population

Replace `{{placeholders}}` in a template with real data:

```js
word( "/templates/contract.docx" )
    .populate( {
        clientName: "Acme Corp",
        signDate: "2024-06-15",
        contractValue: "$50,000"
    } )
    .save( "/output/contract_acme.docx" )
```

---

## 5. Exporting to Other Formats

Convert your document to text, Markdown, or HTML:

```js
doc = word()
    .addHeading( "Report", 1 )
    .addParagraph( "Q4 results are in." )
    .addTable( [ [ "Metric", "Value" ], [ "Revenue", "$1.2M" ] ] )

// Export to different formats
plainText = doc.toText()
markdown  = doc.toMarkdown()
html      = doc.toHTML()

// Or save as .docx
doc.save( "report.docx" )
```

| Method | Output |
|--------|--------|
| `.toText()` | Plain text with tab-separated tables |
| `.toMarkdown()` | Markdown with YAML front matter, pipe tables, base64 images |
| `.toHTML()` | HTML with inline styles and base64 images |

---

## 6. Page Setup

Control margins, size, orientation, headers, and footers:

```js
word()
    .margins( 1.5, 1.5, 2.0, 2.0 )   // top, bottom, left, right in cm
    .pageSize( "A4" )                   // A4, LETTER, LEGAL
    .orientation( "landscape" )         // portrait or landscape
    .header( "Company Confidential" )
    .footer( "Page 1" )
    .addParagraph( "Content goes here..." )
    .save( "formatted.docx" )
```

---

## 7. Document Properties

- Dive into the [User Guide](user-guide.md) for comprehensive coverage
- Explore [Formatting](formatting.md) options for paragraphs and runs
- Learn about [Import & Export](import-export.md) conversion pipelines
- Check out [Advanced Features](advanced-features.md) for watermarks, TOC, and protection
- Browse [Examples](examples.md) for real-world patterns
