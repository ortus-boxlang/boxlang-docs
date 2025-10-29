---
description: A comprehensive and fluent way to interact with spreadsheets with BoxLang
icon: file-excel
---

# 📊 BoxLang Spreadsheet Module

A powerful BoxLang module for creating, reading, and manipulating Excel spreadsheet files.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://www.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](../bx-plus/README.md) with a limited trial.
{% endhint %}

---

## 🎯 Three Ways to Work with Spreadsheets

The **BoxLang Spreadsheet Module** (`bx-spreadsheet`) offers three distinct APIs to suit different coding styles and migration scenarios:

| API Type | Entry Point | Status | Use Case | Documentation |
|----------|-------------|--------|----------|---------------|
| **Fluent API** ✨ | `Spreadsheet()` | **✅ Recommended** | Modern chainable interface for new code | [Fluent API Reference](reference/fluent-api/) |
| **BIF Functions** 📚 | `SpreadsheetNew()`, etc. | 🔄 CFML Compatibility | Migration from Adobe ColdFusion/Lucee | [BIF Reference](reference/built-in-functions/) |
| **Component Tag** 🏷️ | `<bx:spreadsheet>` | 🔄 CFML Compatibility | Legacy tag-based code migration | [Component Reference](reference/components/) |

> 💡 **For new code, we strongly recommend using the Fluent API** which provides better readability, maintainability, and modern method chaining.

---

## ✨ Features

- ✨ **Fluent Method Chaining** - Intuitive, readable code with chainable methods
- 📊 **Multiple Formats** - Support for `.xls` (binary) and `.xlsx` (XML) formats
- 🎨 **Rich Formatting** - Fonts, colors, borders, alignments, and cell styles
- 🔢 **Formula Support** - Set, evaluate, and recalculate Excel formulas
- 📈 **Data Import/Export** - Convert to/from JSON, CSV, Query, and Array formats
- 🖼️ **Image Embedding** - Add images to spreadsheets with positioning control
- 🔐 **Password Protection** - Secure spreadsheet files with passwords
- 📄 **Multi-Sheet Support** - Create, manage, copy, and manipulate multiple worksheets
- 🚀 **High Performance** - Built on Apache POI for reliable, efficient processing
- 🔧 **Comprehensive API** - 85+ BIF functions and full component support
- 🤖 **Automatic Resource Management** - No need to manually close workbooks
- ❄️ **Freeze Panes** - Lock rows/columns for better viewing
- 📐 **Auto-sizing** - Automatically adjust column widths
- 🔗 **Hyperlinks** - Add and manage cell hyperlinks
- 💬 **Comments** - Add cell comments with rich formatting
- 📎 **Merge Cells** - Combine cells for better layout
- 🚀 **Large File Streaming** - Memory-efficient processing of large spreadsheets using Consumer callbacks

---

## 📋 Requirements

- **BoxLang Runtime** 1.0.0 or higher
- **BoxLang+ License** - This module requires a BoxLang+ license

---

## 📦 Installation

Using CommandBox:

```bash
box install bx-spreadsheet@ortus
```

---

## 🚀 Quick Start

### Create Your First Spreadsheet (Fluent API)

```js
// Create a sales report
Spreadsheet( "sales-report.xlsx" )
    .createAndSelectSheet( "Q1 Sales" )
    .setRowData( 1, [ "Product", "Revenue", "Profit" ] )
    .addRow( [ "Widget A", 50000, 20000 ] )
    .addRow( [ "Widget B", 45000, 18000 ] )
    .setCellFormula( 2, 3, "B2-20000" )
    .formatRow( 1, { bold: true, fgcolor: "blue", fontColor: "white" } )
    .autoSizeColumns()
    .save();

// Read and export data
data = Spreadsheet( "sales-report.xlsx" ).toArray();
json = Spreadsheet( "sales-report.xlsx" ).toJson();
```

### Quick Examples

```js
// Load existing file
sheet = Spreadsheet( "data.xlsx" );

// Chain multiple operations
Spreadsheet()
    .setCellValue( 1, 1, "Name" )
    .setCellValue( 1, 2, "Age" )
    .addRow( [ "John Doe", 30 ] )
    .addRow( [ "Jane Smith", 25 ] )
    .formatRow( 1, { bold: true } )
    .save( "employees.xlsx" );

// Export to different formats
csvData = Spreadsheet( "report.xlsx" ).toCSV();
queryData = Spreadsheet( "report.xlsx" ).toQuery();
arrayData = Spreadsheet( "report.xlsx" ).toArray();
```

---

## 📚 Documentation

### Getting Started

{% content-ref url="quick-start.md" %}
[quick-start.md](quick-start.md)
{% endcontent-ref %}

{% content-ref url="user-guide.md" %}
[user-guide.md](user-guide.md)
{% endcontent-ref %}

### Guides

{% content-ref url="formatting.md" %}
[formatting.md](formatting.md)
{% endcontent-ref %}

{% content-ref url="formulas.md" %}
[formulas.md](formulas.md)
{% endcontent-ref %}

{% content-ref url="data-export.md" %}
[data-export.md](data-export.md)
{% endcontent-ref %}

{% content-ref url="advanced-features.md" %}
[advanced-features.md](advanced-features.md)
{% endcontent-ref %}

{% content-ref url="examples.md" %}
[examples.md](examples.md)
{% endcontent-ref %}

### API Reference

{% content-ref url="reference/" %}
[reference](reference/)
{% endcontent-ref %}

---

## 🔍 Quick Reference

### ✨ Fluent API (Recommended)

The modern, chainable interface for working with spreadsheets:

```js
Spreadsheet( "file.xlsx" )
    .setCellValue( 1, 1, "Hello" )
    .addRow( [ "Data", "Here" ] )
    .save();
```

**Complete Documentation:** [Fluent API Reference](reference/fluent-api/)

### 📚 Built-in Functions (CFML Migration)

Traditional function-based approach for migrating from Adobe ColdFusion or Lucee:

```js
sheet = SpreadsheetNew( "Report" );
SpreadsheetSetCellValue( sheet, "Hello", 1, 1 );
SpreadsheetWrite( sheet, "file.xlsx", true );
```

**Complete Documentation:** [BIF Reference](reference/built-in-functions/)

### 🏷️ Component Tag (Legacy Migration)

Tag-based approach for migrating legacy CFML code:

```xml
<bx:spreadsheet action="create" name="sheet" />
<bx:spreadsheet action="setCellValue" name="#sheet#" row="1" column="1" value="Hello" />
<bx:spreadsheet action="write" name="#sheet#" filename="file.xlsx" />
```

**Complete Documentation:** [Component Reference](reference/components/)

---

## 📖 API Documentation

Complete JavaDoc API documentation with detailed method signatures, parameters, and return types:

**📚 [BoxLang Spreadsheet Module API Docs](https://apidocs.ortussolutions.com/boxlang-modules/bx-spreadsheet/1.0.0/index.html)**

---

## 🎯 Key Concepts

### Fluent API Benefits

The Fluent API provides several advantages over traditional approaches:

- **Method Chaining** - Chain operations for readable, maintainable code
- **Automatic Resource Management** - No need to manually close workbooks
- **Modern Syntax** - Clean, intuitive interface
- **Better IDE Support** - Enhanced autocomplete and type hints

### File Formats

- **`.xlsx`** (XML Format) - Modern Excel format, default
- **`.xls`** (Binary Format) - Legacy Excel format for compatibility

### Common Operations

| Operation | Fluent API | BIF Equivalent |
|-----------|------------|----------------|
| Create new | `Spreadsheet()` | `SpreadsheetNew()` |
| Load file | `Spreadsheet("file.xlsx")` | `SpreadsheetRead()` |
| Set cell | `.setCellValue(1, 1, "Value")` | `SpreadsheetSetCellValue()` |
| Add row | `.addRow(["A", "B"])` | `SpreadsheetAddRow()` |
| Save | `.save("file.xlsx")` | `SpreadsheetWrite()` |
| Export | `.toArray()` | N/A |

---

## 💡 Migration Guide

### From Adobe ColdFusion / Lucee

If you're migrating from ACF or Lucee:

1. **Start with BIFs** - Use the [BIF Reference](reference/built-in-functions/) for drop-in compatibility
2. **Gradually adopt Fluent API** - Each BIF page shows the Fluent API equivalent
3. **Update incrementally** - No need to refactor everything at once

**Example Migration:**

```js
// Old CFML approach
sheet = SpreadsheetNew("Report");
SpreadsheetAddRow(sheet, "Name,Age");
SpreadsheetAddRow(sheet, "John,30");
SpreadsheetWrite(sheet, "output.xlsx", true);

// Modern Fluent API (Recommended)
Spreadsheet("output.xlsx")
    .addRow(["Name", "Age"])
    .addRow(["John", 30])
    .save();
```

---

## 🤝 Contributing

We welcome contributions! Please see the [Contributing Guide](https://github.com/ortus-boxlang/bx-spreadsheet) for details.

---

## 📄 License

Apache License 2.0 - See [LICENSE](https://github.com/ortus-boxlang/bx-spreadsheet/blob/main/LICENSE) file for details.
