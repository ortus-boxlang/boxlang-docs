---
description: A comprehensive and fluent way to interact with spreadsheets with BoxLang
icon: file-excel
---

# 📊 BoxLang Spreadsheet Module

A powerful BoxLang module for creating, reading, and manipulating Excel spreadsheet files.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](./bx-plus.md) with a limited trial.
{% endhint %}

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Fluent API Guide](#fluent-api-guide)
- [BIF Reference](#bif-reference)
- [Component Reference](#component-reference)
- [Examples](#examples)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **BoxLang Spreadsheet Module** (`bx-spreadsheet`) is a comprehensive library for Excel file manipulation in BoxLang. It offers three distinct APIs to suit different coding styles:

### 🎯 Three Ways to Work with Spreadsheets

| API Type | Entry Point | Use Case | Example |
|----------|-------------|----------|---------|
| **Fluent API** ✨ | `Spreadsheet()` | Modern chainable interface (recommended) | `Spreadsheet("data.xlsx").toArray()` |
| **BIF Functions** 📚 | `SpreadsheetNew()`, etc. | Traditional function-based approach | `SpreadsheetRead("data.xlsx")` |
| **Component Tag** 🏷️ | `<bx:spreadsheet>` | Declarative CFML-compatible syntax | `<bx:spreadsheet action="read" src="data.xlsx">` |

> 💡 **Recommended**: Use the **Fluent API** (`Spreadsheet()`) for the most modern, readable, and maintainable code.

## ✨ Features

- ✨ **Fluent Method Chaining** - Intuitive, readable code with chainable methods
- 📊 **Multiple Formats** - Support for `.xls` (binary) and `.xlsx` (XML) formatss
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

## 📋 Requirements

- **BoxLang Runtime** 1.0.0 or higher
- **BoxLang+ License** - This module requires a BoxLang+ license

---

## 📦 Installation

Using CommandBox just run:

```bash
box install bx-spreadsheet@ortus
```

---

## 🚀 Quick Start

### Fluent API (Recommended)

The fluent API provides a modern, chainable interface for elegant spreadsheet manipulation:

```javascript
// Create a new spreadsheet and populate it
Spreadsheet( "sales-report.xlsx" )
    .createAndSelectSheet( "Sales Report" )
    .setRowData( 1, [ "Product", "Q1", "Q2", "Q3", "Q4", "Total" ] )
    .addRow( [ "Widget A", 1000, 1200, 1100, 1300, 4600 ] )
    .addRow( [ "Widget B", 800, 900, 950, 1050, 3700 ] )
    .setCellFormula( 2, 6, "SUM(B2:E2)" )
    .setCellFormula( 3, 6, "SUM(B3:E3)" )
    .formatRow( 1, { bold: true, fgcolor: "blue", fontColor: "white" } )
    .autoSizeColumns()
    .save();

// Read an existing spreadsheet
data = Spreadsheet( "sales-data.xlsx" )
    .selectSheet( "Sheet1" )
    .toArray();

// Export to different formats
csvData = Spreadsheet( "report.xlsx" ).toCSV();
jsonData = Spreadsheet( "report.xlsx" ).toJson();
queryData = Spreadsheet( "report.xlsx" ).toQuery();
```

### Traditional BIF Functions

For those familiar with CFML-style functions:

```javascript
// Create a new spreadsheet
spreadsheet = SpreadsheetNew( "My Report", true ); // true = .xlsx format

// Add data
SpreadsheetSetCellValue( spreadsheet, "Product", 1, 1 );
SpreadsheetSetCellValue( spreadsheet, "Price", 1, 2 );
SpreadsheetAddRow( spreadsheet, "Widget A,29.99" );
SpreadsheetAddRow( spreadsheet, "Widget B,39.99" );

// Format and save
SpreadsheetFormatRow( spreadsheet, { bold: true }, 1 );
SpreadsheetWrite( spreadsheet, "products.xlsx", true );

// Read a spreadsheet
data = SpreadsheetRead( "products.xlsx" );
info = SpreadsheetInfo( data );
```

### Components

You can also use the `Spreadsheet` component for a declarative approach in either the templating language or scripting language:

#### Templating

```xml
<!-- Create and populate a spreadsheet -->
<bx:spreadsheet action="create" name="mySheet" sheetname="Report" />
<bx:spreadsheet action="setCellValue" name="#mySheet#" row="1" column="1" value="Name" />
<bx:spreadsheet action="addRow" name="#mySheet#" data="#['John Doe', 'Engineer']#" />
<bx:spreadsheet action="write" name="#mySheet#" filename="output.xlsx" overwrite="true" />

<!-- Read a spreadsheet -->
<bx:spreadsheet action="read" src="data.xlsx" name="importedData" sheet="Sheet1" />
```

#### Scripting

```javascript
// Create and manipulate with component in script
bx:spreadsheet action="create" name="mySheet" sheetname="Report";
bx:spreadsheet action="setCellValue" name="#mySheet#" row="1" column="1" value="Name";
bx:spreadsheet action="addRow" name="#mySheet#" data="#['John Doe', 'Engineer']#";
bx:spreadsheet action="write" name="#mySheet#" filename="output.xlsx" overwrite="true";

// Read a spreadsheet
bx:spreadsheet action="read" src="data.xlsx" name="importedData" sheet="Sheet1";
```

---

## 💎 Fluent API Guide

The fluent API starts off by calling the `Spreadsheet()` BIF, which returns a `SpreadsheetFile` object. You can then chain methods to perform various operations.

You can also find the API documentation here: https://apidocs.ortussolutions.com/boxlang-modules/bx-spreadsheet/1.0.0/index.html

### BIF Arguments

| Argument | Type | Description | Default |
|----------|------|-------------|---------|
| `path` | String | Path to an existing or new spreadsheet file | N/A |
| `sheetName` | String | Name of the initial sheet to create | "Sheet1" |
| `xmlFormat` | Boolean | Use XML (.xlsx) format if true, binary (.xls) if false | true |
| `password` | String | Password for encrypted files | N/A |

### Method Reference by Category

| Category | Methods | Description |
|----------|---------|-------------|
| **📁 File Operations** | `load()`, `save()`, `saveAndClose()`, `overwrite()`, `setPath()`, `getPath()`, `autoCloseOnSave()`, `isAutoCloseOnSave()` | Load/save files, manage paths, auto-cleanup |
| **📄 Sheet Management** | `createSheet()`, `createAndSelectSheet()`, `selectSheet()`, `removeSheet()`, `renameSheet()`, `copySheet()`, `hideSheet()`, `unhideSheet()`, `moveSheet()` | Create, select, and manipulate worksheets |
| **📝 Cell Operations** | `setCellValue()`, `getCellValue()`, `clearCell()`, `getCellType()`, `getCellFormat()`, `getCellAddress()`, `getActiveCell()`, `setActiveCell()` | Read/write individual cell values |
| **📊 Row Operations** | `setRowData()`, `getRowData()`, `addRow()`, `addRows()`, `removeRow()`, `setRowHeight()`, `hideRow()`, `showRow()`, `isRowHidden()`, `shiftRows()`, `getRowCount()`, `getLastRowNumber()` | Manipulate entire rows |
| **📋 Column Operations** | `deleteColumn()`, `deleteColumns()`, `setColumnWidth()`, `hideColumn()`, `showColumn()`, `isColumnHidden()`, `shiftColumns()`, `getColumnCount()`, `getColumnNames()`, `getColumnTypes()`, `autoSizeColumn()`, `autoSizeColumns()` | Manipulate entire columns |
| **🎨 Formatting** | `formatCell()`, `formatRow()`, `formatRows()`, `formatColumn()`, `formatColumns()`, `formatCellRange()` | Apply visual styling to cells/ranges |
| **🔢 Formulas** | `setCellFormula()`, `getCellFormula()`, `getAllFormulas()`, `recalculateAllFormulas()`, `getAutoCalculate()`, `setAutoCalculate()`, `getRecalculateFormulasOnNextOpen()`, `setRecalculateFormulasOnNextOpen()` | Work with Excel formulas |
| **📤 Data Export** | `toArray()`, `toQuery()`, `toJson()`, `toCSV()`, `toMatrix()`, `getAllData()`, `getDataAsQuery()` | Export data to various formats |
| **🔗 Hyperlinks & Comments** | `setCellHyperlink()`, `getCellHyperlink()`, `setCellComment()`, `getCellComment()`, `getAllCellComments()` | Add links and annotations |
| **🖼️ Images & Media** | `addImage()`, `setHeader()`, `setFooter()`, `setHeaderImage()`, `setFooterImage()` | Embed images and headers/footers |
| **🎯 Advanced Features** | `mergeCells()`, `addAutofilter()`, `addFreezePane()`, `addSplitPane()`, `setRepeatingRows()`, `setRepeatingColumns()`, `groupRows()`, `groupColumns()`, `ungroupRows()`, `ungroupColumns()` | Cell merging, filters, panes, grouping |
| **🖨️ Print Settings** | `setSheetPrintOrientation()`, `getPrintOrientation()`, `setFitToPage()`, `addPrintGridlines()`, `removePrintGridlines()`, `setRowBreak()`, `removeRowBreak()`, `setColumnBreak()`, `removeColumnBreak()` | Configure printing options |
| **🔍 Inspection** | `info()`, `getActiveSheetName()`, `getSheetCount()`, `getSheetNames()`, `getSheetsVisibility()`, `hasSheet()`, `isXmlFormat()`, `isBinaryFormat()`, `isOverwriteEnabled()` | Query workbook information |
| **🗑️ Data Clearing** | `clearCell()`, `clearSheet()`, `clearCellRange()`, `setCellRangeValue()` | Remove or bulk-set cell content |
| **ℹ️ Metadata** | `setInfo()` | Set document properties |



### Creating Spreadsheets

```javascript
// Create a new blank .xlsx file
sheet = Spreadsheet();

// Create with a specific sheet name
sheet = Spreadsheet( sheetName = "MySheet" );

// Create with .xls format (binary)
sheet = Spreadsheet( xmlFormat = false );

// Create with a file path - loads if exists, sets path if not
sheet = Spreadsheet( "reports/monthly.xlsx" );

// Path to existing file - automatically loads it
sheet = Spreadsheet( "data/existing.xlsx" );

// Path to new file - sets the path for later save()
sheet = Spreadsheet( "output/new-report.xlsx" );
```

**💡 Pro Tips:**

- When you pass a path to `Spreadsheet()`:
  - If the file exists, it's automatically loaded
  - If the file doesn't exist, the path is set for when you call `save()`
  - No need to call `load()` or `setPath()` separately!
- **No manual cleanup needed** - Resources are automatically managed for you, no need to call `close()`

### Loading & Saving

```javascript
// RECOMMENDED: Pass path directly to Spreadsheet()
sheet = Spreadsheet( "data.xlsx" ); // Auto-loads if exists, sets path if not

// Alternative: Load explicitly with load()
sheet = Spreadsheet().load( "data.xlsx" );

// Load with password
sheet = Spreadsheet().load( "protected.xlsx", "password123" );

// Save to a file
sheet.save( "output.xlsx" );

// Save with password protection
sheet.save( "protected.xlsx", "secret123" );

// When path is already set, just call save()
sheet = Spreadsheet( "output.xlsx" )
    .addRow( [ "Name", "Age" ] )
    .addRow( [ "John", 30 ] )
    .save(); // Saves to "output.xlsx"

// Enable overwrite mode (won't throw error if file exists)
sheet.overwrite( true ).save( "output.xlsx" );

// Set path and save later
sheet.setPath( "reports/monthly.xlsx" );
// ... do work ...
sheet.save(); // Saves to previously set path

// Save and close in one operation
sheet.saveAndClose(); // Uses current path
sheet.saveAndClose( "output.xlsx" );
sheet.saveAndClose( "protected.xlsx", "password123" );

// Auto-close on save - workbook closes automatically after save()
sheet.autoCloseOnSave( true )
    .addRow( [ "Data" ] )
    .save( "output.xlsx" ); // Workbook is automatically closed after save
```

**💡 Pro Tips:**

- **autoCloseOnSave()** is useful for long-lived objects that should cleanup after saving
- Use `saveAndClose()` when you want to explicitly save and close in one call
- No need to manually call `close()` in these patterns

### Working with Sheets

```javascript
// Create a new sheet
sheet.createSheet( "Q1 Data" );

// Create and immediately select a sheet
sheet.createAndSelectSheet( "Q2 Data" );

// Select an existing sheet by name
sheet.selectSheet( "Summary" );

// Select a sheet by index (1-based)
sheet.selectSheet( 1 );

// Rename a sheet
sheet.renameSheet( "Old Name", "New Name" );

// Copy a sheet
sheet.copySheet( "Template", "January" );

// Remove a sheet
sheet.removeSheet( "Temporary" );
sheet.removeSheet( 2 ); // By index

// Hide/unhide sheets
sheet.hideSheet( "Internal Data" );
sheet.unhideSheet( "Public Report" );

// Move a sheet
sheet.moveSheet( "Summary", 1 ); // Move to first position
sheet.moveSheet( 3, 1 ); // Move sheet at index 3 to index 1

// Get sheet information
sheetNames = sheet.getSheetNames(); // Returns array of sheet names
activeSheet = sheet.getActiveSheetName();
visibility = sheet.getSheetsVisibility(); // Returns struct with sheet visibility
hasSheet = sheet.hasSheet( "Data" ); // Boolean check
```

### Cell Operations

```javascript
// Set cell values
sheet.setCellValue( row = 1, col = 1, value = "Name" );
sheet.setCellValue( 1, 2, "Age" );

// Set cell value on a specific sheet
sheet.setCellValue( "Sheet2", 5, 3, "Value" );

// Get cell value
value = sheet.getCellValue( 1, 1 );

// Set cell formulas
sheet.setCellFormula( 2, 5, "SUM(B2:D2)" );
sheet.setCellFormula( 3, 5, "AVERAGE(B3:D3)" );

// Get cell formula
formula = sheet.getCellFormula( 2, 5 );

// Get all formulas in the sheet
formulas = sheet.getAllFormulas();

// Clear cells
sheet.clearCell( 1, 1 );
sheet.clearCellRange( startRow = 1, startCol = 1, endRow = 10, endCol = 5 );

// Set the same value to a range of cells
sheet.setCellRangeValue( value = "N/A", startRow = 5, startCol = 1, endRow = 10, endCol = 3 );

// Get cell type (returns "blank", "numeric", "string", "formula", "boolean", "error")
type = sheet.getCellType( 2, 3 );

// Get cell address (e.g., "A1", "B5")
address = sheet.getCellAddress( 1, 1 ); // Returns "A1"

// Active cell operations
sheet.setActiveCell( 5, 3 );
activeInfo = sheet.getActiveCell(); // Returns struct with row and column
```

### Row Operations

```javascript
// Set row data
sheet.setRowData( row = 1, values = [ "Name", "Age", "City" ] );

// Get row data
rowData = sheet.getRowData( 2 );

// Add rows
sheet.addRow( [ "John Doe", 30, "NYC" ] );
sheet.addRow( "Value1,Value2,Value3" ); // Comma-delimited string

// Add row at specific position
sheet.addRow( values = [ "Data" ], row = 5, column = 1, insert = true );

// Add multiple rows from an array of arrays
data = [
    [ "John", 30 ],
    [ "Jane", 25 ],
    [ "Bob", 35 ]
];
sheet.addRows( data );

// Add rows with column names
sheet.addRows( data, includeColumnNames = true );

// Remove a row
sheet.removeRow( 5 );

// Shift rows up or down
sheet.shiftRows( start = 5, end = 10, n = 2 ); // Shift rows 5-10 down by 2

// Hide/show rows
sheet.hideRow( 5 );
sheet.showRow( 5 );
sheet.setRowHidden( 5, true );
isHidden = sheet.isRowHidden( 5 );

// Set row height
sheet.setRowHeight( row = 1, height = 30 );

// Group rows (for collapsible outlines)
sheet.groupRows( startRow = 5, endRow = 10 );
sheet.groupRows( 5, 10, true ); // Collapsed by default
sheet.ungroupRows( 5, 10 );

// Set repeating rows (for printing)
sheet.setRepeatingRows( startRow = 1, endRow = 2 );

// Set row break (for printing)
sheet.setRowBreak( 10 );
sheet.removeRowBreak( 10 );
```

### Column Operations

```javascript
// Delete columns
sheet.deleteColumn( 3 );
sheet.deleteColumns( startColumn = 2, endColumn = 4 );

// Add columns
SpreadsheetAddColumn( sheet.workbook, data = "Value1,Value2,Value3" );

// Shift columns left or right
sheet.shiftColumns( start = 3, end = 5, n = 2 );

// Hide/show columns
sheet.hideColumn( 3 );
sheet.showColumn( 3 );
sheet.setColumnHidden( 3, true );
isHidden = sheet.isColumnHidden( 3 );

// Set column width
sheet.setColumnWidth( column = 1, width = 20 );

// Auto-size columns
sheet.autoSizeColumn( 1 );
sheet.autoSizeColumns(); // All columns in active sheet

// Get column information
columnNames = sheet.getColumnNames();
columnTypes = sheet.getColumnTypes();
columnCount = sheet.getColumnCount();

// Group columns (for collapsible outlines)
sheet.groupColumns( startColumn = 3, endColumn = 6 );
sheet.groupColumns( 3, 6, true ); // Collapsed by default
sheet.ungroupColumns( 3, 6 );

// Set repeating columns (for printing)
sheet.setRepeatingColumns( startCol = 1, endCol = 2 );

// Set column break (for printing)
sheet.setColumnBreak( 5 );
sheet.removeColumnBreak( 5 );
```

### Formatting

```javascript
// Format a single cell
formatStruct = {
    bold: true,
    italic: false,
    underline: false,
    fontsize: 12,
    font: "Arial",
    fgcolor: "yellow",
    fontColor: "black",
    alignment: "center",
    verticalalignment: "top",
    textwrap: true,
    dataformat: "0.00"
};
sheet.formatCell( row = 1, col = 1, format = formatStruct );

// Format a row
sheet.formatRow( 1, { bold: true, fgcolor: "blue", fontColor: "white" } );

// Format multiple rows (comma-delimited)
sheet.formatRows( "1,3,5", { italic: true } );

// Format a column
sheet.formatColumn( 1, { alignment: "right", dataformat: "0.00" } );

// Format multiple columns
sheet.formatColumns( "1,2,3", { bold: true } );

// Format a cell range
sheet.formatCellRange(
    format = { bold: true, fgcolor: "lightgray" },
    startRow = 1,
    startCol = 1,
    endRow = 1,
    endCol = 10
);

// Get cell format
cellFormat = sheet.getCellFormat( 1, 1 );

// Available format options:
// - bold, italic, underline, strikeout
// - font, fontsize, fontColor
// - alignment (left, center, right, justify)
// - verticalalignment (top, center, bottom, justify)
// - fgcolor (background color)
// - textwrap
// - dataformat (Excel format string like "0.00", "mm/dd/yyyy")
// - leftborder, rightborder, topborder, bottomborder
// - leftbordercolor, rightbordercolor, topbordercolor, bottombordercolor
```

### Formulas

```javascript
// Set formulas
sheet.setCellFormula( 5, 5, "SUM(A1:A4)" );
sheet.setCellFormula( 2, 10, "IF(A2>100,'High','Low')" );

// Get a specific formula
formula = sheet.getCellFormula( 5, 5 );

// Get all formulas in the active sheet
allFormulas = sheet.getAllFormulas();

// Recalculate all formulas
sheet.recalculateAllFormulas();

// Control formula calculation
sheet.setAutoCalculate( true ); // Auto-calculate on edit
isAutoCalc = sheet.getAutoCalculate();

// Force recalculation on next open
sheet.setRecalculateFormulasOnNextOpen( true );
willRecalc = sheet.getRecalculateFormulasOnNextOpen();
```

### Data Export

```javascript
// Export to array of arrays (matrix)
matrix = sheet.toMatrix();
matrix = sheet.toMatrix( "Sheet2" );

// Export to array of structs (column names as keys)
arrayData = sheet.toArray();
arrayData = sheet.toArray( "Sheet2" );

// Export to Query object
queryData = sheet.toQuery();
queryData = sheet.toQuery( "Sheet2" );

// Export to JSON
json = sheet.toJson();
json = sheet.toJson( pretty = true );
json = sheet.toJson( sheetName = "Data", pretty = true );

// Export to CSV
csv = sheet.toCSV();
csv = sheet.toCSV( { delimiter: "|", includeHeaderRow: true } );
csv = sheet.toCSV( "Sheet2", { delimiter: "\t" } );

// Get all data as array
allData = sheet.getAllData();
allData = sheet.getAllData( "Sheet2" );

// Get specific row data
rowData = sheet.getRowData( 5 );
```

### Advanced Features

#### Merge Cells

```javascript
sheet.mergeCells( startRow = 1, startColumn = 1, endRow = 1, endColumn = 5 );
```

#### Add Images

```javascript
// Add image at specific cell
sheet.addImage( filepath = "logo.png", row = 1, column = 1 );

// Add image spanning multiple cells
sheet.addImage(
    filepath = "chart.png",
    startRow = 5,
    startCol = 1,
    endRow = 15,
    endCol = 5
);
```

#### Hyperlinks

```javascript
// Set hyperlink
sheet.setCellHyperlink( row = 1, column = 1, hyperlink = "https://boxlang.io", label = "BoxLang" );
sheet.setCellHyperlink( 2, 1, "mailto:info@boxlang.io" );

// Get hyperlink
linkInfo = sheet.getCellHyperlink( 1, 1 );
```

#### Comments

```javascript
// Simple comment
sheet.setCellComment( row = 1, col = 1, comment = "This is a note" );

// Comment with author
sheet.setCellComment( 1, 2, "Review this value", "John Doe" );

// Rich comment with formatting
commentStruct = {
    comment: "Important!",
    author: "Manager",
    bold: true,
    fontsize: 12,
    fontcolor: "red"
};
sheet.setCellComment( 1, 3, commentStruct );

// Get comment
comment = sheet.getCellComment( 1, 1 );

// Get all comments
allComments = sheet.getAllCellComments();
```

#### Freeze & Split Panes

```javascript
// Freeze panes (lock rows/columns in place)
sheet.addFreezePane( column = 1, row = 2 ); // Freeze first column and first row

// Split panes
sheet.addSplitPane(
    xSplitPos = 2000,
    ySplitPos = 1000,
    leftmostColumn = 0,
    topRow = 0,
    activePane = 0
);
```

#### Autofilter

```javascript
// Add autofilter to a range
sheet.addAutofilter(
    startRow = 1,
    startColumn = 1,
    endRow = 100,
    endColumn = 5
);
```

#### Print Settings

```javascript
// Set print orientation
sheet.setSheetPrintOrientation( "landscape" ); // or "portrait"
orientation = sheet.getPrintOrientation();

// Fit to page
sheet.setFitToPage( fitToPage = true, pagesWide = 1, pagesHigh = 1 );

// Print gridlines
sheet.addPrintGridlines();
sheet.removePrintGridlines();

// Headers and footers
sheet.setHeader( { left: "Confidential", center: "&A", right: "&D" } );
sheet.setFooter( { left: "&F", center: "Page &P of &N", right: "&T" } );

// Header/footer images
sheet.setHeaderImage( alignment = "center", imagePath = "logo.png" );
sheet.setFooterImage( alignment = "right", imagePath = "watermark.png" );
```

#### Workbook Metadata

```javascript
// Set workbook properties
sheet.setInfo( {
    author: "John Doe",
    title: "Sales Report 2024",
    subject: "Q1 Sales Data",
    keywords: "sales, quarterly, report",
    comments: "Generated automatically"
} );

// Get workbook info
info = sheet.info();
```

#### Utilities

```javascript
// Check file format
isXml = sheet.isXmlFormat(); // .xlsx
isBinary = sheet.isBinaryFormat(); // .xls

// Get row/column counts
rowCount = sheet.getRowCount();
colCount = sheet.getColumnCount();

// Close workbook (release resources)
sheet.close();

// Get file path
path = sheet.getPath();

// Clear entire sheet
sheet.clearSheet( "Sheet1" );
```

---

## 📚 BIF Reference

The module provides **85+ BIF functions** for traditional function-based programming. All functions are prefixed with `Spreadsheet` except for utility functions like `IsSpreadsheetFile` and `IsSpreadsheetObject`.

### 📋 Complete BIF List

| Category | Functions |
|----------|-----------|
| **Creation & Loading** | `SpreadsheetNew`, `SpreadsheetRead`, `SpreadsheetReadBinary`, `SpreadsheetFile` |
| **Saving & Writing** | `SpreadsheetWrite` |
| **Sheet Management** | `SpreadsheetCreateSheet`, `SpreadsheetSetActiveSheet`, `SpreadsheetSetActiveSheetNumber`, `SpreadsheetRemoveSheet`, `SpreadsheetRemoveSheetNumber`, `SpreadsheetRenameSheet` |
| **Cell Operations** | `SpreadsheetSetCellValue`, `SpreadsheetGetCellValue`, `SpreadsheetSetCellFormula`, `SpreadsheetGetCellFormula`, `SpreadsheetGetCellType`, `SpreadsheetClearCell`, `SpreadsheetSetCellRangeValue`, `SpreadsheetClearCellRange`, `SpreadsheetSetCellComment`, `SpreadsheetGetCellComment`, `SpreadsheetSetCellHyperlink`, `SpreadsheetGetCellHyperlink`, `SpreadsheetSetActiveCell`, `SpreadsheetGetActiveCell` |
| **Row Operations** | `SpreadsheetAddRow`, `SpreadsheetAddRows`, `SpreadsheetDeleteRow`, `SpreadsheetDeleteRows`, `SpreadsheetShiftRows`, `SpreadsheetSetRowHeight`, `SpreadsheetSetRowHidden`, `SpreadsheetSetRowBreak`, `SpreadsheetRemoveRowBreak`, `SpreadsheetGroupRows`, `SpreadsheetUngroupRows`, `SpreadsheetisRowHidden` |
| **Column Operations** | `SpreadsheetAddColumn`, `SpreadsheetDeleteColumn`, `SpreadsheetDeleteColumns`, `SpreadsheetShiftColumns`, `SpreadsheetSetColumnWidth`, `SpreadsheetGetColumnWidth`, `SpreadsheetSetColumnHidden`, `SpreadsheetSetColumnBreak`, `SpreadsheetRemoveColumnBreak`, `SpreadsheetGroupColumns`, `SpreadsheetUngroupColumns`, `SpreadsheetisColumnHidden`, `SpreadsheetGetColumnCount` |
| **Formatting** | `SpreadsheetFormatCell`, `SpreadsheetFormatRow`, `SpreadsheetFormatRows`, `SpreadsheetFormatColumn`, `SpreadsheetFormatColumns`, `SpreadsheetFormatCellRange`, `SpreadsheetGetCellFormat` |
| **Advanced Features** | `SpreadsheetMergeCells`, `SpreadsheetAddImage`, `SpreadsheetAddAutofilter`, `SpreadsheetAddFreezePane`, `SpreadsheetAddSplitPane`, `SpreadsheetAddPageBreaks`, `SpreadsheetAddInfo` |
| **Print Settings** | `SpreadsheetSetPrintOrientation`, `SpreadsheetGetPrintOrientation`, `SpreadsheetSetFitToPage`, `SpreadsheetAddPrintGridlines`, `SpreadsheetRemovePrintGridlines`, `SpreadsheetSetHeader`, `SpreadsheetSetFooter`, `SpreadsheetSetHeaderImage`, `SpreadsheetSetFooterImage`, `SpreadsheetSetRepeatingRows`, `SpreadsheetSetRepeatingColumns` |
| **Formulas** | `SpreadsheetSetAutoCalculate`, `SpreadsheetGetAutoCalculate`, `SpreadsheetSetForceFormulaRecalculation`, `SpreadsheetGetForceFormulaRecalculation` |
| **Information** | `SpreadsheetInfo`, `SpreadsheetGetLastRowNumber`, `IsSpreadsheetFile`, `IsSpreadsheetObject`, `SpreadsheetIsBinaryFormat`, `SpreadsheetIsXMLFormat` |

### Usage Examples

```javascript
// Create and manipulate with BIFs
sheet = SpreadsheetNew( "Report", true );
SpreadsheetAddRow( sheet, "Name,Age,City" );
SpreadsheetAddRow( sheet, "John,30,NYC" );
SpreadsheetFormatRow( sheet, { bold: true }, 1 );
SpreadsheetWrite( sheet, "output.xlsx", true );

// Read and inspect
data = SpreadsheetRead( "input.xlsx" );
info = SpreadsheetInfo( data );
colCount = SpreadsheetGetColumnCount( data );

// Check file types
if ( IsSpreadsheetFile( "data.xlsx" ) ) {
    isXlsx = SpreadsheetIsXMLFormat( "data.xlsx" );
}

// Formula operations
SpreadsheetSetCellFormula( sheet, "SUM(A1:A10)", 11, 1 );
SpreadsheetSetAutoCalculate( sheet, true );
```

---

## 🏷️ Component Reference

The `Spreadsheet` component provides a declarative, or a tag-based approach to spreadsheet manipulation. It can be used in both templating and scripting contexts.

### 📋 Supported Actions

| Action | Description | Required Attributes | Optional Attributes |
|--------|-------------|---------------------|---------------------|
| `read` | Read a spreadsheet file | `src`, `name` | `sheet`, `sheetindex`, `headerrow`, `rows`, `columns`, `columnnames`, `password` |
| `write` | Write spreadsheet to file | `name`, `filename` | `overwrite`, `password` |
| `create` | Create new spreadsheet object | `name` | `sheetname`, `xmlformat` |
| `delete` | Delete a sheet | `name` | `sheetname`, `sheetindex` |
| `addColumn` | Add column data | `name`, `data` | `column`, `startrow` |
| `addRow` | Add row data | `name`, `data` | `row`, `column` |
| `addRows` | Add multiple rows | `name`, `data` | `startrow`, `startcolumn` |
| `deleteColumn` | Delete a column | `name`, `column` |  |
| `deleteRow` | Delete a row | `name`, `row` |  |
| `formatCell` | Format a cell | `name`, `formatstruct`, `row`, `column` |  |
| `formatColumn` | Format a column | `name`, `formatstruct`, `column` |  |
| `formatRow` | Format a row | `name`, `formatstruct`, `row` |  |
| `formatCells` | Format cell range | `name`, `formatstruct`, `startrow`, `startcolumn`, `endrow`, `endcolumn` |  |
| `mergeCells` | Merge cells | `name`, `startrow`, `startcolumn`, `endrow`, `endcolumn` |  |
| `setActiveSheet` | Set active sheet | `name` | `sheetname`, `sheetindex` |
| `setCellValue` | Set cell value | `name`, `value`, `row`, `column` |  |
| `setCellFormula` | Set cell formula | `name`, `formula`, `row`, `column` |  |
| `info` | Get spreadsheet info | `name` |  |

### Usage Examples

```xml
<!-- Read a spreadsheet -->
<bx:spreadsheet action="read" src="data.xlsx" name="myData" sheet="Sheet1" />

<!-- Create and populate -->
<bx:spreadsheet action="create" name="report" sheetname="Sales" xmlformat="true" />
<bx:spreadsheet action="setCellValue" name="#report#" row="1" column="1" value="Product" />
<bx:spreadsheet action="addRow" name="#report#" data="#['Widget A', 100, 29.99]#" />

<!-- Format and save -->
<bx:spreadsheet action="formatRow" name="#report#" row="1" formatstruct="{ bold: true }" />
<bx:spreadsheet action="write" name="#report#" filename="sales.xlsx" overwrite="true" />

<!-- Script syntax -->
<bx:script>
    bx:spreadsheet action="read" src="data.xlsx" name="data";
    bx:spreadsheet action="formatCell" name=data row=1 column=1 formatstruct={ bold: true };
</bx:script>
```

---

## 💡 Examples

### Example 1: Sales Report Generator

```javascript
// Create a comprehensive sales report
Spreadsheet()
    .createSheet( "Q1 Sales" )
    .selectSheet( "Q1 Sales" )
    .setRowData( 1, [ "Month", "Revenue", "Expenses", "Profit", "Margin %" ] )
    .addRow( [ "January", 50000, 30000, 20000, "=D2/B2" ] )
    .addRow( [ "February", 55000, 32000, 23000, "=D3/B3" ] )
    .addRow( [ "March", 60000, 35000, 25000, "=D4/B4" ] )
    .addRow( [ "Total", "=SUM(B2:B4)", "=SUM(C2:C4)", "=SUM(D2:D4)", "=D5/B5" ] )
    .formatRow( 1, { bold: true, fgcolor: "blue", fontColor: "white" } )
    .formatRow( 5, { bold: true, fgcolor: "lightgray" } )
    .formatColumn( 2, { dataformat: "$#,##0.00" } )
    .formatColumn( 3, { dataformat: "$#,##0.00" } )
    .formatColumn( 4, { dataformat: "$#,##0.00" } )
    .formatColumn( 5, { dataformat: "0.0%" } )
    .autoSizeColumns()
    .recalculateAllFormulas()
    .save( "q1-sales-report.xlsx" );
```

### Example 2: Data Import and Analysis

```javascript
// Read CSV-like data and create Excel report
importData = [
    [ "Name", "Department", "Salary" ],
    [ "John Doe", "Engineering", 95000 ],
    [ "Jane Smith", "Marketing", 85000 ],
    [ "Bob Johnson", "Sales", 75000 ]
];

Spreadsheet( sheetName = "Employees" )
    .addRows( importData, includeColumnNames = true )
    .formatRow( 1, { bold: true } )
    .addRow( [ "AVERAGE", "", "=AVERAGE(C2:C4)" ] )
    .formatCell( 5, 3, { bold: true, dataformat: "$#,##0" } )
    .autoSizeColumns()
    .save( "employee-report.xlsx" );
```

### Example 3: Multi-Sheet Workbook

```javascript
// Create workbook with multiple sheets
workbook = Spreadsheet()
    .createSheet( "Summary" )
    .createSheet( "Details" )
    .createSheet( "Charts" )

    // Populate Summary
    .selectSheet( "Summary" )
    .setRowData( 1, [ "Report Summary" ] )
    .mergeCells( 1, 1, 1, 5 )
    .formatCell( 1, 1, { bold: true, fontsize: 16, alignment: "center" } )

    // Populate Details
    .selectSheet( "Details" )
    .addRows( detailData, includeColumnNames = true )
    .autoSizeColumns()

    // Copy sheet
    .copySheet( "Details", "Details Backup" )

    .save( "multi-sheet-report.xlsx" );
```

### Example 4: Export to Multiple Formats

```javascript
// Load and export to different formats
sheet = Spreadsheet( "source-data.xlsx" );

// Export to JSON file
fileWrite( "data.json", sheet.toJson( pretty = true ) );

// Export to CSV file
fileWrite( "data.csv", sheet.toCSV() );

// Get as Query object for database operations
queryData = sheet.toQuery();

// Get as array for manipulation
arrayData = sheet.toArray();
```

### Example 5: Template-Based Report

```javascript
// Load template and fill with data
report = Spreadsheet( "report-template.xlsx" )
    .selectSheet( "Data" )
    .setCellValue( 2, 1, "Acme Corp" )
    .setCellValue( 2, 2, dateFormat( now(), "yyyy-mm-dd" ) )
    .addRows( getData(), startRow = 5, startColumn = 1 )
    .recalculateAllFormulas()
    .save( "filled-report-#dateFormat(now(),'yyyymmdd')#.xlsx" );
```

---

## 📖 API Documentation

Complete API documentation with detailed method signatures, parameters, and return types is available online:

**📚 [BoxLang Spreadsheet Module API Docs](https://apidocs.ortussolutions.com/boxlang-modules/bx-spreadsheet/1.0.0/index.html)**

The API documentation includes:

- Full JavaDoc for all classes and methods
- Detailed parameter descriptions
- Return type information
- Code examples and usage patterns

---