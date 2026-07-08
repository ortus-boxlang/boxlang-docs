---
description: A powerful BoxLang module for creating, reading, populating, and converting Word documents with a fluent, chainable API
icon: file-word
---

# BoxLang Word Module 📝

The **BoxLang Word Module** (`bx-word`) is a fluent document builder for `.docx` files in BoxLang. Built on Apache POI, it lets you create, populate, style, and export Word documents with a clean, chainable API. Import content from text, Markdown, and HTML on the fly.

| API Type | Entry Point | Use Case |
|----------|-------------|----------|
| **Fluent API** ✨ | `word()` | Modern chainable interface (recommended) |
| **Importers** 📥 | `.fromText()` / `.fromMarkdown()` / `.fromHTML()` | Ingest content from multiple formats |
| **Exporters** 📤 | `.toText()` / `.toMarkdown()` / `.toHTML()` | Convert documents to text or markup |

> 💡 The fluent API is the recommended approach. Chain methods to build, style, and save documents in a single expression.

## ✨ Key Features

- ✨ **Fluent Method Chaining** — Intuitive, readable code
- 📝 **Template Population** — `{{placeholder}}` substitution with struct data
- 📊 **Table Support** — Arrays, Queries, and Struct-based tables with auto-header bolding
- 🎨 **Rich Formatting** — Bold, italic, colors, fonts, alignment, spacing
- 📥 **Multi-Format Import** — Plain text, Markdown (CommonMark), HTML (Jsoup)
- 📤 **Multi-Format Export** — Plain text, Markdown, HTML (inline styles + base64 images)
- 🖼️ **Image Embedding** — From file path, byte array, base64 string, or URL
- 📄 **Page Setup** — Margins, page size, orientation, headers, footers, section breaks
- 🔗 **Hyperlinks** — Clickable links with underline styling
- 📋 **Lists** — Ordered and unordered lists with nested/indented support
- 📖 **Document Properties** — Title, author, subject, keywords
- 🔒 **Document Protection** — Password-protect documents
- 🏷️ **Watermarks** — "DRAFT", "CONFIDENTIAL", or custom text
- 📑 **Table of Contents** — Insert TOC field for Word to generate
- 🔀 **Static Factories** — `WordDocument.fromText()`, `.fromMarkdown()`, `.fromHTML()`
- ⚡ **Fluent Helpers** — `.tap()` for side effects, `.when()` for conditional chaining

## 📋 Requirements

- **BoxLang Runtime** 1.14.0 or higher
- **BoxLang+ License** — This module requires a BoxLang+ license

---

## 📦 Installation

Using CommandBox:

```bash
box install bx-word
```

---

## 🚀 Quick Start

### Create Your First Document

```js
// Build a document from scratch
word( "/path/to/report.docx" )
    .margins( 1.78, 1.78, 1.78, 1.78 )
    .addHeading( "My Report", 1 )
    .addParagraph( "Hello World" )
    .addTable( [ [ "Name", "Role" ], [ "John Doe", "Engineer" ] ] )
    .save()
```

### Populate a Template

```js
// Open an existing template and fill placeholders
word( "/templates/contract.docx" )
    .populate( { name: "John Doe", date: "2024-01-01" } )
    .save( "/output/contract.docx" )
```

### Create from Text, Markdown, or HTML

```js
// The word() BIF accepts text, markdown, and html arguments directly
word( text="Hello World\n\nParagraph two" )
    .save( "from-text.docx" )

word( markdown="## Title\n\nParagraph with **bold** text." )
    .save( "from-markdown.docx" )

word( html="<h1>Title</h1><p>Hello <b>World</b></p>" )
    .save( "from-html.docx" )
```

### Export to Text, Markdown, or HTML

```js
// Build and convert in one chain
doc = word().addHeading( "Report", 1 ).addParagraph( "Content" )

plainText = doc.toText()       // plain text
markdown  = doc.toMarkdown()   // markdown with YAML front matter
html      = doc.toHTML()       // HTML with inline styles + base64 images
```

---

## 📖 Documentation

| Guide | Description |
|-------|-------------|
| [Quick Start](quick-start.md) | Create your first Word document in 5 minutes |
| [User Guide](user-guide.md) | Comprehensive usage guide for all features |
| [Formatting](formatting.md) | Fonts, alignment, spacing, and page setup |
| [Import & Export](import-export.md) | Convert between text, Markdown, HTML, and Word |
| [Advanced Features](advanced-features.md) | Watermarks, TOC, protection, section breaks |
| [Examples](examples.md) | Real-world scenarios and patterns |
| [BIF Reference](reference/built-in-functions/Word.md) | The `word()` BIF |
| [Fluent API Reference](reference/fluent-api/README.md) | Complete `WordDocument` API |

---

## 💬 Support & Community

- 📧 **Email**: [support@ortussolutions.com](mailto:support@ortussolutions.com)
- 💬 **Slack**: [Join BoxLang Community](https://boxlang.io/community)
- 🐛 **Issues**: [GitHub Issues](https://github.com/ortus-boxlang/bx-word/issues)
- 📖 **Forums**: [BoxLang Forums](https://community.boxlang.io)
- 📚 **Docs**: [BoxLang Documentation](https://boxlang.ortusbooks.com)

---

## Built with ❤️ by Ortus Solutions

**Professional Services Available** — Need help with BoxLang implementation, training, or consulting? [Contact Ortus Solutions](https://www.ortussolutions.com/services)
