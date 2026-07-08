---
description: Entry point for Word document operations — returns a fluent WordDocument builder
icon: code
---

# `word()` BIF

The `word()` BIF is the primary entry point for all Word document operations. It returns a `WordDocument` instance that supports fluent method chaining.

## Method Signature

```js
word( [file], [text], [html], [markdown] )
```

## Arguments

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `file` | String | No | — | Path to an existing `.docx` file to open and modify |
| `text` | String | No | — | Plain text content to populate the document with |
| `html` | String | No | — | HTML string to parse and populate the document with |
| `markdown` | String | No | — | Markdown string to parse and populate the document with |

{% hint style="info" %}
When no arguments are provided, a new empty document is created. When multiple content arguments are provided (e.g., `text` and `html`), the content is appended in argument order.
{% endhint %}

## Returns

A `WordDocument` instance — a fluent builder that supports method chaining.

---

## Examples

### Create a New Empty Document

```js
doc = word()
doc.addHeading( "My Report", 1 )
doc.addParagraph( "Hello world!" )
doc.save( "report.docx" )
```

### Open an Existing Document

```js
doc = word( "/path/to/template.docx" )
doc.replaceText( "[DATE]", "2024-06-15" )
doc.save( "/path/to/filled.docx" )
```

### Create from Plain Text

```js
word( text="Hello World\n\nParagraph two" )
    .save( "from-text.docx" )
```

### Create from Markdown

```js
word( markdown="## Introduction\n\n**Bold** and *italic* text." )
    .save( "from-markdown.docx" )
```

### Create from HTML

```js
word( html="<h1>Title</h1><p>Paragraph with <b>bold</b> text.</p>" )
    .save( "from-html.docx" )
```

### Combined Arguments

```js
word( file="/templates/base.docx", markdown="## Appended Section\n\nExtra content." )
    .save( "combined.docx" )
```

### Full Fluent Chain

```js
word( "/path/to/report.docx" )
    .margins( 1.78, 1.78, 1.78, 1.78 )
    .pageSize( "A4" )
    .header( "Confidential" )
    .addHeading( "Q4 Report", 1 )
    .addParagraph( "Executive summary..." )
    .addTable( salesDataQuery )
    .addPageBreak()
    .addHeading( "Details", 2 )
    .addParagraph( "Detailed breakdown..." )
    .save()
```

---

## Related

{% content-ref url="../fluent-api/README.md" %}
{% content-ref url="../../../../user-guide.md" %}
