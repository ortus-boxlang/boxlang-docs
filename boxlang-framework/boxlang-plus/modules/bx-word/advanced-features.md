---
description: Advanced Word document features including watermarks, protection, table of contents, section breaks, and document properties
icon: star
---

# ⭐ Advanced Features

Advanced capabilities for production-grade Word documents.

---

## Watermarks

Add semi-transparent text watermarks like "DRAFT", "CONFIDENTIAL", or custom text to every page:

```js
word()
    .addHeading( "Confidential Report", 1 )
    .addParagraph( "Sensitive financial data." )
    .addWatermark( "CONFIDENTIAL" )
    .save( "confidential-report.docx" )
```

{% hint style="info" %}
The watermark is rendered as large, light gray, centered text in the document header, appearing on every page.
{% endhint %}

Multiple watermarks can be added with different text:

```js
word()
    .addWatermark( "DRAFT" )
    .addParagraph( "Work in progress..." )
    .save( "draft.docx" )
```

---

## Document Protection

Password-protect your document so users must enter a password to view it:

```js
word()
    .addHeading( "Sensitive Document", 1 )
    .addParagraph( "This content is protected." )
    .protect( "mySecretPassword123" )
    .save( "protected.docx" )
```

{% hint style="warning" %}
Protection is applied at the document level. When opened in Word, the user will be prompted for the password. This uses SHA-512 hashing for the protection.
{% endhint %}

---

## Table of Contents

Insert a Table of Contents field that Word auto-generates when the document is opened:

```js
word()
    .setTitle( "Employee Handbook" )
    .addTableOfContents()
    .addPageBreak()
    .addHeading( "Introduction", 1 )
    .addParagraph( "Welcome to the company..." )
    .addHeading( "Policies", 1 )
    .addParagraph( "Company policies..." )
    .addHeading( "Code of Conduct", 2 )
    .addParagraph( "Expected behavior..." )
    .addHeading( "Benefits", 1 )
    .addParagraph( "Health insurance, 401k..." )
    .save( "handbook.docx" )
```

{% hint style="info" %}
The TOC field captures headings 1–3 by default. When opened in Word, the user will be prompted to update the table of contents to populate the entries and page numbers.
{% endhint %}

---

## Section Breaks

Use section breaks to apply different page setups within the same document:

```js
word()
    // First section: portrait
    .pageSize( "A4" )
    .orientation( "portrait" )
    .margins( 2.0, 2.0, 2.5, 2.5 )
    .addHeading( "Portrait Section", 1 )
    .addParagraph( "This page is in portrait orientation." )

    // Section break
    .addSectionBreak()

    // Second section: landscape
    .pageSize( "A4" )
    .orientation( "landscape" )
    .margins( 1.5, 1.5, 2.0, 2.0 )
    .addHeading( "Landscape Section", 1 )
    .addParagraph( "This page is in landscape — great for wide tables." )
    .addTable( wideTableData )

    // Another section break
    .addSectionBreak()

    // Third section: back to portrait
    .orientation( "portrait" )
    .addHeading( "Back to Portrait", 1 )
    .addParagraph( "Normal orientation resumes." )
    .save( "mixed-orientation.docx" )
```

{% hint style="success" %}
Each section break creates a new Word section. Page size, orientation, and margins set after a section break apply only to that new section.
{% endhint %}

---

## Page Setup

### Margins

Set all four margins in centimeters:

```js
// Positional: top, bottom, left, right
word().margins( 2.54, 2.54, 2.54, 2.54 )  // 1 inch all around

// Struct-based with partial overrides
word().margins( { top: 2.0, left: 3.0 } )  // bottom and right default to 2.54cm
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

{% hint style="warning" %}
Setting `landscape` orientation automatically swaps width and height dimensions to ensure width > height.
{% endhint %}

### Headers & Footers

```js
word()
    .header( "ACME Corp — Q4 2024 Report" )
    .footer( "Confidential — Do Not Distribute" )
```

---

## Document Properties

Set metadata that appears in Word's document properties panel:

```js
word()
    .setTitle( "Q4 Financial Report" )
    .setAuthor( "Jane Doe" )
    .setSubject( "Quarterly financial summary and projections for FY2024" )
    .setKeywords( "finance, quarterly, report, 2024, projections" )
    .addHeading( "Executive Summary", 1 )
    .addParagraph( "This quarter exceeded expectations..." )
    .save( "financial-report.docx" )
```

{% hint style="info" %}
These properties are visible in Word via **File → Info → Properties** and are included in the YAML front matter when exporting to Markdown via `toMarkdown()`.
{% endhint %}

---

## Default Font

Apply a consistent font family and size to all existing text runs:

```js
word( "template.docx" )
    .setDefaultFont( "Calibri", 11 )
    .save( "formatted.docx" )
```

{% hint style="warning" %}
`setDefaultFont()` only applies to existing runs at the time of the call. Content added afterward is not affected.
{% endhint %}

---

## Fluent Helpers

### `tap()` — Side Effects

Execute an action mid-chain without breaking the flow:

```js
word()
    .addParagraph( "Step 1" )
    .tap( ( doc ) => logger.info( "After step 1" ) )
    .addParagraph( "Step 2" )
    .tap( ( doc ) => writeLog( "Current state: " & doc.toText() ) )
    .save( "output.docx" )
```

### `when()` — Conditional Branching

Conditionally execute a block in the fluent chain:

```js
isAdmin = user.hasRole( "admin" )

word()
    .addHeading( "Report", 1 )
    .addParagraph( "Standard content for all users." )
    .when( isAdmin, ( doc ) => doc
        .addHeading( "Admin Section", 2 )
        .addParagraph( "Sensitive data visible only to admins." )
        .addTable( sensitiveData )
    )
    .addParagraph( "Footer content for all users." )
    .save( "report.docx" )
```

---

## Document Cleanup

`WordDocument` implements `AutoCloseable`. Release POI resources when done:

```js
doc = word( "input.docx" )
try {
    // ... work with document ...
} finally {
    doc.close()
}
```

Or use try-with-resources in Java interop scenarios.

---

## 📚 Related Resources

{% content-ref url="user-guide.md" %}
{% content-ref url="formatting.md" %}
{% content-ref url="examples.md" %}
{% content-ref url="reference/fluent-api/README.md" %}
