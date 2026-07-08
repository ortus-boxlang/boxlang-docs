---
description: Import and export Word documents to and from text, Markdown, and HTML formats
icon: arrows-rotate
---

# 🔄 Import & Export

Convert Word documents to and from text, Markdown, and HTML formats.

---

## Importing Content

### From Plain Text

Split paragraphs on double newlines:

```js
text = "Line one\n\nLine two\n\nLine three"

// Via BIF argument
word( text=text ).save( "from-text.docx" )

// Via instance method (appends to existing document)
word( "template.docx" )
    .fromText( text )
    .save( "appended.docx" )
```

### From Markdown

Uses CommonMark parsing — supports headings, paragraphs, lists, code blocks, blockquotes, links, and thematic breaks:

```js
markdown = "
## Introduction

This is a paragraph with **bold** and *italic* text.

- Item 1
- Item 2
- Item 3

> A blockquote

`inline code`
"

// Via BIF argument
word( markdown=markdown ).save( "from-markdown.docx" )

// Via instance method
word().fromMarkdown( markdown ).save( "from-markdown.docx" )
```

### From HTML

Uses Jsoup parsing — supports headings, paragraphs, lists, tables, images, links, and basic formatting:

```js
html = "<h1>Title</h1><p>Hello <b>World</b></p><ul><li>Item 1</li><li>Item 2</li></ul>"

// Via BIF argument
word( html=html ).save( "from-html.docx" )

// Via instance method
word().fromHTML( html ).save( "from-html.docx" )
```

### Supported HTML Elements

| HTML Element | Word Output |
|-------------|-------------|
| `<h1>`–`<h6>` | Heading (level 1–6) |
| `<p>` | Paragraph |
| `<br>` | New line |
| `<b>`, `<strong>` | Bold text |
| `<i>`, `<em>` | Italic text |
| `<ul>` | Unordered (bulleted) list |
| `<ol>` | Ordered (numbered) list |
| `<li>` | List item (supports nesting) |
| `<table>`, `<tr>`, `<td>`, `<th>` | Table |
| `<a href="...">` | Hyperlink |
| `<img src="...">` | Image (base64 data URIs supported) |
| `<pre>`, `<code>` | Monospace paragraph |
| `<blockquote>` | Indented, italic paragraph |
| `<hr>` | Page break |

---

## Exporting Content

### To Plain Text

Extracts all visible text including tables (tab-separated), headers, and footers:

```js
doc = word( "report.docx" )
plainText = doc.toText()
```

**Output example:**

```
Report Title
Introduction paragraph.
Further details.
Product	Price	Stock
Widget A	$10.00	150
Widget B	$15.00	200
[Header] Company Confidential
[Footer] Page 1
```

{% hint style="info" %}
Table cells are separated by tabs (`\t`). Headers and footers are prefixed with `[Header]` and `[Footer]` markers.
{% endhint %}

### To Markdown

Converts to Markdown with:
- YAML front matter (title, author, subject from document properties)
- `#` headings with proper level
- Pipe-delimited tables
- `**bold**` / `*italic*` formatting
- Base64-embedded images
- Blockquoted headers and footers

```js
doc = word( "report.docx" )
markdown = doc.toMarkdown()
```

**Output example:**

```markdown
---
title: "Q4 Report"
author: "Jane Doe"
---

# Report Title

Introduction paragraph.

| Product | Price | Stock |
| --- | --- | --- |
| Widget A | $10.00 | 150 |
| Widget B | $15.00 | 200 |

> **Header:** Company Confidential
> **Footer:** Page 1
```

### To HTML

Converts to a full HTML document with:
- Semantic heading tags (`<h1>`–`<h6>`)
- Standard `<table>` structure with `<thead>`/`<tbody>`
- Inline styles for bold, italic, color, size, and font family
- Base64-embedded images
- `<footer>` elements for headers and footers

```js
doc = word( "report.docx" )
html = doc.toHTML()
```

**Output example:**

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Q4 Report</title>
</head>
<body>
<h1>Report Title</h1>
<p>Introduction paragraph.</p>
<table border="1" cellpadding="4" cellspacing="0" style="border-collapse:collapse;">
  <thead>
    <tr>
      <th>Product</th><th>Price</th><th>Stock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Widget A</td><td>$10.00</td><td>150</td>
    </tr>
  </tbody>
</table>
<footer style="border-top:1px solid #ccc;">
  <p><em>Header: Company Confidential</em></p>
  <p><em>Footer: Page 1</em></p>
</footer>
</body>
</html>
```

---

## Format Conversion Pipeline

Chain import and export for format conversion:

```js
// HTML → Word → Markdown
html = "<h1>Article</h1><p>Content with <b>bold</b> text.</p>"
markdown = word( html=html ).toMarkdown()
// # Article
//
// Content with **bold** text.

// Markdown → Word → HTML
md = "## Hello\n\nWorld"
html = word( markdown=md ).toHTML()

// Text → Word → Markdown
text = "Title\n\nParagraph one\n\nParagraph two"
md = word( text=text ).toMarkdown()
```

---

## Fidelity Notes

{% hint style="warning" %}
Not all formatting is perfectly preserved in round-trip conversions. Key considerations:
{% endhint %}

| Direction | Preserved | Lost |
|-----------|-----------|------|
| Word → Text | Visible text, table structure | All formatting, images, headers |
| Word → Markdown | Headings, tables, bold/italic, images (base64) | Exact font/size/color, custom styles |
| Word → HTML | Headings, tables, bold/italic, colors, fonts, images (base64) | Custom paragraph spacing, section breaks |
| Markdown → Word | Headings, paragraphs, lists, bold/italic, code, links, blockquotes | Embedded images become links |
| HTML → Word | Headings, paragraphs, lists, tables, bold, links, base64 images | CSS classes, external stylesheets |
| Text → Word | Paragraph structure (double-newline split) | All formatting |

---

## 📚 Related Resources

{% content-ref url="user-guide.md" %}
{% content-ref url="formatting.md" %}
{% content-ref url="reference/fluent-api/README.md" %}
