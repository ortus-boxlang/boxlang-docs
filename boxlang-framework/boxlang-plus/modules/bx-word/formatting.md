---
description: Formatting and styling Word documents with BoxLang — fonts, alignment, spacing, page setup
icon: paintbrush
---

# 🎨 Formatting

Control the visual appearance of your Word documents with rich formatting options.

---

## Paragraph Formatting

### Alignment

Control text alignment within paragraphs:

```js
word()
    .addParagraph( "Left-aligned (default)", { alignment: "LEFT" } )
    .addParagraph( "Centered text", { alignment: "CENTER" } )
    .addParagraph( "Right-aligned text", { alignment: "RIGHT" } )
    .addParagraph( "Justified text fills the line width evenly on both sides.", { alignment: "JUSTIFY" } )
    .save( "alignment.docx" )
```

### Spacing

Control space before/after paragraphs and line height:

```js
word()
    .addParagraph( "Paragraph with extra space below.", {
        spacingAfter: 240    // 240 twips ≈ 12pt
    } )
    .addParagraph( "Double-spaced paragraph.", {
        lineSpacing: 480     // 480 twips = double spacing
    } )
    .addParagraph( "1.5 line spacing with indent.", {
        lineSpacing: 360,    // 360 twips = 1.5 spacing
        spacingBefore: 120,
        firstLineIndent: 720 // 0.5 inch indent
    } )
```

| Option | Unit | Description |
|--------|------|-------------|
| `spacingBefore` | twips | Space before paragraph (240 twips ≈ 12pt) |
| `spacingAfter` | twips | Space after paragraph |
| `lineSpacing` | twips | Line spacing (240 = single, 360 = 1.5, 480 = double) |
| `firstLineIndent` | twips | First line indentation (720 twips ≈ 0.5in) |

{% hint style="info" %}
**Twips** (twentieth of a point) is a standard unit in Word. Common values:
- 240 twips = 12pt = single line spacing
- 360 twips = 18pt = 1.5 line spacing
- 480 twips = 24pt = double line spacing
- 720 twips = 36pt = 0.5 inch indent
{% endhint %}

---

## Run Formatting

### Font Properties

Control per-character formatting within paragraphs:

```js
word()
    .addParagraph( "Bold text", { bold: true } )
    .addParagraph( "Italic text", { italic: true } )
    .addParagraph( "Bold and Italic", { bold: true, italic: true } )
    .addParagraph( "Large text", { size: 18 } )
    .addParagraph( "Small text", { size: 8 } )
    .addParagraph( "Custom font", { font: "Times New Roman", size: 12 } )
```

### Colors

Specify colors as hex values (with or without `#`):

```js
word()
    .addParagraph( "Red text", { color: "FF0000" } )
    .addParagraph( "Blue text", { color: "#0000FF" } )
    .addParagraph( "Green text", { color: "008000" } )
    .addParagraph( "Gray text", { color: "808080" } )
```

### Combined Formatting

```js
word()
    .addParagraph( "Professional Header", {
        bold: true,
        size: 16,
        color: "2C3E50",
        font: "Calibri",
        alignment: "CENTER",
        spacingAfter: 240
    } )
    .addParagraph( "Body text with standard formatting.", {
        font: "Calibri",
        size: 11,
        alignment: "JUSTIFY",
        lineSpacing: 360
    } )
```

---

## Page Setup

### Margins

```js
// Positional: top, bottom, left, right in cm
word().margins( 1.78, 1.78, 1.78, 1.78 )  // all equal

// Struct-based with selective overrides
word().margins( { top: 2.0, bottom: 2.0, left: 3.0, right: 2.0 } )
word().margins( { left: 3.0 } )  // only change left, others default to 2.54cm
```

{% hint style="warning" %}
All margin values are in **centimeters**. To convert from inches, multiply by 2.54 (1 inch = 2.54 cm).
{% endhint %}

### Page Size

```js
word().pageSize( "A4" )       // 210 × 297 mm — European standard
word().pageSize( "LETTER" )   // 8.5 × 11 in — US standard
word().pageSize( "LEGAL" )    // 8.5 × 14 in — US legal
```

### Orientation

```js
word().orientation( "portrait" )   // vertical (default)
word().orientation( "landscape" )  // horizontal
```

{% hint style="success" %}
Use section breaks to mix portrait and landscape pages in the same document. See [Advanced Features](advanced-features.md#section-breaks).
{% endhint %}

### Headers & Footers

```js
word()
    .header( "Document Title — Page Header" )
    .footer( "Confidential | Generated " & dateTimeFormat( now(), "yyyy-mm-dd" ) )
```

---

## Tables

Table headers (first row) are automatically bold:

```js
word().addTable( [
    [ "Product", "Price", "Stock" ],
    [ "Widget A", "$10.00", "150" ],
    [ "Widget B", "$15.00", "200" ]
] )
```

{% hint style="info" %}
For more advanced table formatting (cell borders, background colors, merging), use the underlying `XWPFDocument` via `.getDocument()`. Future versions will add native table styling.
{% endhint %}

---

## Headings

Headings 1–2 are bold by default; headings 3–6 use the Word style's built-in formatting:

```js
word()
    .addHeading( "Document Title", 1 )     // Bold, Heading1 style
    .addHeading( "Section", 2 )            // Bold, Heading2 style
    .addHeading( "Sub-section", 3 )        // Regular weight, Heading3 style
    .addHeading( "Minor Heading", 4 )      // Regular weight, Heading4 style
```

{% hint style="info" %}
Heading levels are clamped to 1–6. Level 0 → 1; level 7+ → 6.
{% endhint %}

---

## Hyperlinks

Hyperlinks are rendered as blue, underlined text:

```js
word()
    .addHyperlink( "Visit BoxLang", "https://boxlang.io" )
    .addHyperlink( "Email Support", "mailto:support@ortussolutions.com" )
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

### With Nested Sub-lists

```js
word().addUnorderedList( [
    "Fruits",
    { text: "Vegetables", items: [ "Carrots", "Broccoli" ] },
    "Grains"
] )
```

---

## Default Font

Apply a consistent font to all existing text runs:

```js
word( "template.docx" )
    .setDefaultFont( "Calibri", 11 )
    .save( "output.docx" )
```

{% hint style="warning" %}
Only affects runs present at call time. Content added afterward uses Word defaults.
{% endhint %}

---

## Document Properties

```js
word()
    .setTitle( "My Document" )
    .setAuthor( "Jane Doe" )
    .setSubject( "A detailed subject description" )
    .setKeywords( "boxlang, word, document, example" )
```

---

## 📚 Related Resources

{% content-ref url="user-guide.md" %}
{% content-ref url="advanced-features.md" %}
{% content-ref url="examples.md" %}
