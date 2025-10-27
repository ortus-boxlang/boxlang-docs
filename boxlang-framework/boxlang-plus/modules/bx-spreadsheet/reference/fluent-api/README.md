---
description: Complete reference for the SpreadsheetFile Fluent API - the recommended approach for working with spreadsheets in BoxLang
icon: sparkles
---

# ✨ Fluent API Reference

The **Fluent API** is the modern, recommended way to work with spreadsheets in BoxLang. It provides a chainable, intuitive interface centered around the `SpreadsheetFile` object.

{% hint style="success" %}
**Recommended Approach**: The Fluent API is the preferred method for all spreadsheet operations. It's more intuitive, easier to read, and provides better code organization than traditional BIFs or component methods.
{% endhint %}

---

## 🎯 Quick Start

```js
// Create new spreadsheet with fluent chaining
Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Name", "Value" ] )
    .addRow( [ "Item 1", 100 ] )
    .formatRow( 1, { bold: true } )
    .autoSizeColumns()
    .save();
```

---

## 📋 API Categories

The Fluent API is organized into functional categories:

### Core Operations

{% content-ref url="creating-and-loading.md" %}
[creating-and-loading.md](creating-and-loading.md)
{% endcontent-ref %}

{% content-ref url="reading-data.md" %}
[reading-data.md](reading-data.md)
{% endcontent-ref %}

{% content-ref url="writing-data.md" %}
[writing-data.md](writing-data.md)
{% endcontent-ref %}

{% content-ref url="saving-and-exporting.md" %}
[saving-and-exporting.md](saving-and-exporting.md)
{% endcontent-ref %}

### Formatting & Style

{% content-ref url="formatting.md" %}
[formatting.md](formatting.md)
{% endcontent-ref %}

{% content-ref url="sizing.md" %}
[sizing.md](sizing.md)
{% endcontent-ref %}

### Calculations

{% content-ref url="formulas.md" %}
[formulas.md](formulas.md)
{% endcontent-ref %}

### Sheet Management

{% content-ref url="sheet-operations.md" %}
[sheet-operations.md](sheet-operations.md)
{% endcontent-ref %}

### Advanced Features

{% content-ref url="data-validation.md" %}
[data-validation.md](data-validation.md)
{% endcontent-ref %}

{% content-ref url="protection.md" %}
[protection.md](protection.md)
{% endcontent-ref %}

{% content-ref url="advanced-features.md" %}
[advanced-features.md](advanced-features.md)
{% endcontent-ref %}

### Utility Operations

{% content-ref url="utility-methods.md" %}
[utility-methods.md](utility-methods.md)
{% endcontent-ref %}

{% content-ref url="merging-and-comments.md" %}
[merging-and-comments.md](merging-and-comments.md)
{% endcontent-ref %}

---

## 🔗 Method Chaining

Most Fluent API methods return the `SpreadsheetFile` object, enabling method chaining:

```js
Spreadsheet( "chained.xlsx" )
    .setRowData( 1, [ "Header" ] )
    .formatRow( 1, { bold: true } )
    .addRow( [ "Data" ] )
    .autoSizeColumns()
    .save();
```

---

## 📖 SpreadsheetFile Object

### Creating SpreadsheetFile

```js
// New empty spreadsheet
sheet = Spreadsheet();

// New spreadsheet with filename
sheet = Spreadsheet( "output.xlsx" );

// Load existing file
sheet = Spreadsheet( "existing.xlsx", load = true );

// Explicit load method
sheet = Spreadsheet().load( "existing.xlsx" );
```

### Method Return Values

- **Chainable methods**: Return `SpreadsheetFile` object for chaining
- **Read methods**: Return data (string, number, array, struct, etc.)
- **Query methods**: Return information about the spreadsheet

---

## 🎨 Common Patterns

### Pattern: Create and Save

```js
Spreadsheet( "output.xlsx" )
    .setRowData( 1, [ "Data" ] )
    .save();
```

### Pattern: Load, Modify, Save

```js
Spreadsheet( "existing.xlsx", load = true )
    .addRow( [ "New data" ] )
    .save();
```

### Pattern: Create, Work With, Then Save

```js
sheet = Spreadsheet();
sheet.setRowData( 1, [ "Header" ] );
sheet.addRow( [ "Data" ] );
sheet.save( "output.xlsx" );
```

### Pattern: Export to Multiple Formats

```js
sheet = Spreadsheet( "data.xlsx", load = true );

csv = sheet.toCSV();
json = sheet.toJson();
qry = sheet.toQuery();
```

---

## 🔍 Finding Methods

### By Task

- **Creating**: See [Creating and Loading](creating-and-loading.md)
- **Reading**: See [Reading Data](reading-data.md)
- **Writing**: See [Writing Data](writing-data.md)
- **Formatting**: See [Formatting](formatting.md)
- **Formulas**: See [Formulas](formulas.md)
- **Sheets**: See [Sheet Operations](sheet-operations.md)

### By Name

All methods are documented in their respective category pages with:
- Method signature
- Parameter descriptions
- Return values
- Code examples

---

## 💡 Migration from BIFs

If you're migrating from traditional CFML BIFs:

```js
// Old BIF approach
spreadsheetObj = spreadsheetNew();
spreadsheetSetCellValue( spreadsheetObj, "Hello", 1, 1 );
spreadsheetWrite( spreadsheetObj, "output.xlsx" );

// New Fluent API approach ✨
Spreadsheet( "output.xlsx" )
    .setCellValue( 1, 1, "Hello" )
    .save();
```

See the [Built-In Functions Reference](../built-in-functions/) for BIF-to-Fluent API conversion guides.

---

## 📚 See Also

- [Quick Start Guide](../../quick-start.md) - Get started in 5 minutes
- [User Guide](../../user-guide.md) - Comprehensive usage guide
- [Examples](../../examples.md) - Real-world code samples
- [Built-In Functions](../built-in-functions/) - Traditional BIF reference
- [Components](../components/) - Component-based API

---

## 🔗 External Resources

- [Full API Documentation](https://apidocs.ortussolutions.com/boxlang-modules/bx-spreadsheet/1.0.0/)
- [Apache POI Documentation](https://poi.apache.org/) - Underlying library
