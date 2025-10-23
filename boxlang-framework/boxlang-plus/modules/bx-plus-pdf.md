---
description: Premium PDF generation and manipulation module for BoxLang+ applications: build, merge, stamp, secure, and extract content programmatically.
icon: file-pdf
---

# 📑 `bx-plus-pdf` Module ( **Coming Soon!** )

The `bx-plus-pdf` module equips your BoxLang+ applications with robust PDF creation and processing capabilities—ideal for invoices, reports, forms, certificates, and archival workflows.

## 🚀 Features

* Generate PDFs from dynamic data (tables, paragraphs, headings)
* Merge, split, and reorder pages
* Apply watermarks and stamps
* Embed fonts & manage text styling
* Add images, shapes, and vector elements
* Secure documents (passwords, permissions)
* Extract text and metadata
* Form field population (conceptual placeholder)

## 📦 Installation

### Via CommandBox

```bash
box install bx-plus-pdf
```

### Via BoxLang

```bash
install-bx-module bx-plus-pdf
```

## ⚙ Basic PDF Creation

```js
pdf = pdfNew( title = "Monthly Report" );

pdfAddHeading( pdf, text = "Revenue Summary", level = 1 );
pdfAddParagraph( pdf, text = "This report provides an overview of monthly revenue performance." );

pdfAddTable( pdf, data = [
    ["Region","Total"],
    ["NA","$123,000"],
    ["EU","$98,500"],
    ["APAC","$67,250"]
] );

binary = pdfWriteBinary( pdf );
fileWrite( expandPath( "monthly-report.pdf" ), binary );
```

## 🖼 Adding Images

```js
pdfAddImage( pdf, path = expandPath( "assets/logo.png" ), x = 50, y = 750, width = 120 );
```

## 🧩 Merging PDFs

```js
merged = pdfMerge( [ fileReadBinary( expandPath( "intro.pdf" ) ), fileReadBinary( expandPath( "monthly-report.pdf" ) ) ] );
fileWrite( expandPath( "bundle.pdf" ), merged );
```

## 🔐 Securing a PDF

```js
pdfSecure( pdf,
  userPassword = "viewer123",
  ownerPassword = "control456",
  allowPrinting = true,
  allowCopy = false
);
```

## 🧪 Extracting Text

```js
binaryInput = fileReadBinary( expandPath( "monthly-report.pdf" ) );
textOut     = pdfExtractText( binaryInput );
writeOutput( left( textOut, 200 ) );
```

## 🛡 Error Handling

```js
try {
    pdfAddTable( pdf, data = hugeDataSet );
} catch ( e ) {
    writeLog( text = "PDF generation failed: " & e.message, type = "error" );
}
```

## 🔐 Entitlement

Requires active BoxLang+ subscription. Attempts to use premium PDF features without entitlement produce clear exceptions.

## 📏 Performance Tips

* Stream large tables incrementally
* Reuse fonts where possible to reduce file size
* Avoid excessive raster image scaling at runtime

## 📎 Related Modules

{% content-ref url="bx-spreadsheet.md" %}
Spreadsheet Module
{% endcontent-ref %}

{% content-ref url="bx-plus.md" %}
Subscription Bootstrap
{% endcontent-ref %}

---
Return to the [Modules Overview](README.md).
