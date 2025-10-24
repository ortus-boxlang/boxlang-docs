---
description: A comprehensive and fluent way to interact with spreadsheets with BoxLang
icon: file-excel
---

# 📊 BoxLang Spreadsheet Module

A powerful BoxLang module for creating, reading, and manipulating Excel spreadsheet files.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](./bx-plus.md) with a limited tria.
{% endhint %}


<blockquote>
	Copyright Since 2023 by Ortus Solutions, Corp<br>
	<a href="https://www.boxlang.io">www.boxlang.io</a> |
	<a href="https://www.ortussolutions.com">www.ortussolutions.com</a>
</blockquote>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Fluent API Guide](#fluent-api-guide)
- [BIF Reference](#bif-reference)
- [Component Reference](#component-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **BoxLang Spreadsheet Module** (`bx-spreadsheet`) is a comprehensive library for Excel file manipulation in BoxLang. It offers three distinct APIs to suit different coding styles:

### 🎯 Three Ways to Work with Spreadsheets

| API Type | Entry Point | Use Case | Example |
|----------|-------------|----------|---------|
| **Fluent API** ✨ | `Spreadsheet()` | Modern chainable interface (recommended) | `Spreadsheet("data.xlsx").toArray()` |
| **BIF Functions** 📚 | `SpreadsheetNew()`, etc. | Traditional function-based approach | `SpreadsheetRead("data.xlsx")` |
| **Component Tag** 🏷️ | `<bx:spreadsheet>` | Declarative CFML-compatible syntax | `<bx:spreadsheet action="read" src="data.xlsx">` |

> 💡 **Recommended**: Use the **Fluent API** (`Spreadsheet()`) for the most modern, readable, and maintainable code.

## Features

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

## Requirements

- **BoxLang Runtime** 1.0.0 or higher
- **BoxLang+ License** - This module requires a BoxLang+ license

---

## Installation

Using CommandBox just run:

```bash
box install bx-spreadsheet@ortus
```

---

## Quick Start

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

## Fluent API Guide

The fluent API starts off by calling the `Spreadsheet()` BIF, which returns a `SpreadsheetFile` object. You can then chain methods to perform various operations.

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

## BIF Reference

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

## Component Reference

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

## Examples

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

***

### 🚀 Advanced Usage

#### Freeze Panes

```javascript
// Freeze first row and first column
spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Q1", "Q2", "Q3", "Q4" ] );
SpreadsheetAddFreezePane( spreadsheet, 1, 1 );

// Freeze first 2 rows
SpreadsheetAddFreezePane( spreadsheet, 0, 2 );
```

#### Auto Filters

```javascript
// Add auto filter to header row
spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Product", "Region", "Sales" ] );
SpreadsheetAddRow( spreadsheet, [ "Widget A", "North", 1000 ] );
SpreadsheetAddRow( spreadsheet, [ "Widget B", "South", 800 ] );
SpreadsheetAddAutofilter( spreadsheet, 1 ); // Filter on row 1
```

#### Shifting Rows

```javascript
// Shift rows down to insert space
spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Row 1" ] );
SpreadsheetAddRow( spreadsheet, [ "Row 2" ] );
SpreadsheetAddRow( spreadsheet, [ "Row 3" ] );

// Shift rows 2-3 down by 2 positions
SpreadsheetShiftRows( spreadsheet, 2, 3, 2 );
```

#### Complex Fluent API Examples

**Creating a Report with Multiple Sheets**

```javascript
// Build a complete financial report
SpreadsheetFile()
    // Summary Sheet
    .createSheet( "Summary" )
    .selectSheet( "Summary" )
    .setRowData( 1, [ "Metric", "Value" ] )
    .addRow( [ "Total Revenue", 150000 ] )
    .addRow( [ "Total Expenses", 95000 ] )
    .addRow( [ "Net Profit", 55000 ] )

    // Revenue Details Sheet
    .createSheet( "Revenue Details" )
    .selectSheet( "Revenue Details" )
    .setRowData( 1, [ "Product", "Q1", "Q2", "Q3", "Q4", "Total" ] )
    .addRow( [ "Product A", 25000, 30000, 28000, 32000, 115000 ] )
    .addRow( [ "Product B", 15000, 18000, 20000, 22000, 75000 ] )

    // Format and save
    .autoSizeColumns()
    .save( "reports/financial-report.xlsx" );
```

**Loading, Modifying, and Saving**

```javascript
// Load existing file, make changes, save to new location
SpreadsheetFile()
    .load( "templates/report-template.xlsx" )
    .selectSheet( "Data" )
    .setCellValue( 1, 1, "Updated: " & now() )
    .addRow( [ "New Entry", 12345 ] )
    .selectSheet( "Summary" )
    .setCellValue( 2, 2, "Status: Complete" )
    .overwrite( true )
    .save( "output/completed-report.xlsx" );
```

**Working with Query Results**

```javascript
// Convert query results to spreadsheet
qData = queryExecute( "SELECT name, email, status FROM users" );

spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Email", "Status" ] );
SpreadsheetAddRows( spreadsheet, qData, 2, 1 );
SpreadsheetWrite( spreadsheet, "users-export.xlsx" );
```

#### Reading Spreadsheet Information

```javascript
// Get spreadsheet metadata
spreadsheet = SpreadsheetRead( "report.xlsx" );
info = SpreadsheetInfo( spreadsheet );

// info structure contains:
// - SHEETCOUNT: number of sheets
// - CURRENTSHEET: name of active sheet
// - SHEETNAMES: array of all sheet names

// Get column count
columnCount = SpreadsheetGetColumnCount( spreadsheet );
```

#### Binary Operations

```javascript
// Read spreadsheet as binary
binaryData = SpreadsheetReadBinary( "document.xlsx" );

// This is useful for:
// - Sending files as HTTP responses
// - Storing in databases
// - Processing in memory
```

#### Chaining Multiple Operations

The fluent API really shines when chaining operations:

```javascript
// Build an invoice in one fluid expression
invoice = SpreadsheetFile()
    .createSheet( "Invoice" )
    .selectSheet( "Invoice" )
    // Header
    .setRowData( 1, [ "INVOICE", "", "", "" ] )
    .setRowData( 2, [ "Invoice #: INV-001", "", "Date: " & dateFormat( now(), "mm/dd/yyyy" ), "" ] )
    // Line items
    .setRowData( 4, [ "Item", "Description", "Quantity", "Price", "Total" ] )
    .addRow( [ "001", "Professional Services", 10, 150.00, 1500.00 ] )
    .addRow( [ "002", "Software License", 1, 500.00, 500.00 ] )
    .addRow( [ "003", "Support Contract", 12, 100.00, 1200.00 ] )
    // Total
    .setRowData( 8, [ "", "", "", "Subtotal:", 3200.00 ] )
    .setRowData( 9, [ "", "", "", "Tax (10%):", 320.00 ] )
    .setRowData( 10, [ "", "", "", "Total:", 3520.00 ] )
    // Format
    .autoSizeColumns()
    .save( "invoices/INV-001.xlsx" );
```

***

### 📖 BIF Reference

#### BX:Spreadsheet Component

The `bx:spreadsheet` component provides a **declarative approach** for spreadsheet operations, compatible with CFML's `cfspreadsheet` tag. This component can be used in both **templating language** (XML-style tags) and **script** (declarative component syntax), offering a more expressive alternative to functional BIF calls.

> 💡 **Note**: The component approach is declarative rather than functional. Use it when you prefer a configuration-style syntax over chained method calls.

**Common Attributes**

* **action** (required, string) - The operation to perform
* **name** (string) - Variable name for the spreadsheet object
* **src** (string) - Source file path (for read action)
* **filename** (string) - Destination file path (for write action)
* **sheetname** (string) - Name of the sheet to work with
* **sheetindex** (numeric) - Index of the sheet (1-based)
* **format** (string) - File format (xlsx, xls)
* **overwrite** (boolean) - Whether to overwrite existing files
* **password** (string) - Password for encrypted files
* **xmlformat** (boolean) - True for .xlsx format, false for .xls (default: true)

**Supported Actions**

**create**

Creates a new spreadsheet object.

**Attributes:**

* `name` (required) - Variable name for the new spreadsheet
* `sheetname` (optional) - Name of the initial sheet
* `xmlformat` (optional) - File format (default: true for .xlsx)

**Template Example:**

```xml
<bx:spreadsheet action="create" name="mySpreadsheet" sheetname="Data" />
```

**Script Example:**

```javascript
bx:spreadsheet action="create" name="mySpreadsheet" sheetname="Data";
```

**read**

Reads a spreadsheet file into a variable.

**Attributes:**

* `src` (required) - Path to the spreadsheet file
* `name` (required) - Variable name to store the spreadsheet
* `sheet` (optional) - Sheet name or index to read
* `password` (optional) - Password for encrypted files

**Template Example:**

```xml
<bx:spreadsheet action="read" src="data.xlsx" name="mySpreadsheet" sheet="Sales" />
```

**Script Example:**

```javascript
bx:spreadsheet action="read" src="data.xlsx" name="mySpreadsheet" sheet="Sales";
```

**write**

Writes a spreadsheet object to a file.

**Attributes:**

* `name` (required) - Spreadsheet object to write
* `filename` (required) - Output file path
* `overwrite` (optional) - Whether to overwrite existing files
* `password` (optional) - Password to protect the file

**Template Example:**

```xml
<bx:spreadsheet action="write" name="#mySpreadsheet#" filename="output.xlsx" overwrite="true" />
```

**Script Example:**

```javascript
bx:spreadsheet action="write" name=mySpreadsheet filename="output.xlsx" overwrite=true;
```

**update**

Updates an existing spreadsheet file (same as write).

**Attributes:** Same as write action.

**delete**

Deletes a sheet from a spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object
* `sheetname` (required) - Name of the sheet to delete

**Template Example:**

```xml
<bx:spreadsheet action="delete" name="#mySpreadsheet#" sheetname="OldSheet" />
```

**Script Example:**

```javascript
bx:spreadsheet action="delete" name=mySpreadsheet sheetname="OldSheet";
```

**addRow**

Adds a row of data to the spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object
* `data` (required) - Array of values for the row
* `row` (optional) - Row number where to insert
* `column` (optional) - Starting column number

**Template Example:**

```xml
<bx:spreadsheet action="addRow" name="#mySpreadsheet#" data="#['John', 30, 'NYC']#" />
```

**Script Example:**

```javascript
bx:spreadsheet action="addRow" name=mySpreadsheet data=['John', 30, 'NYC'];
```

**addRows**

Adds multiple rows to the spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object
* `data` (required) - Array of arrays or query object
* `row` (optional) - Starting row number
* `column` (optional) - Starting column number

**Template Example:**

```xml
<bx:spreadsheet action="addRows" name="#mySpreadsheet#" data="#dataArray#" row="2" />
```

**addColumn**

Adds a column of data to the spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object
* `data` (required) - Array of values for the column
* `column` (optional) - Column number
* `row` (optional) - Starting row number

**Template Example:**

```xml
<bx:spreadsheet action="addColumn" name="#mySpreadsheet#" data="#['Q1', 1000, 1200]#" column="2" />
```

**deleteRow**

Deletes a row from the spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object
* `row` (required) - Row number to delete

**Template Example:**

```xml
<bx:spreadsheet action="deleteRow" name="#mySpreadsheet#" row="5" />
```

**deleteColumn**

Deletes a column from the spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object
* `column` (required) - Column number to delete

**Template Example:**

```xml
<bx:spreadsheet action="deleteColumn" name="#mySpreadsheet#" column="3" />
```

**setCellValue**

Sets the value of a specific cell.

**Attributes:**

* `name` (required) - Spreadsheet object
* `row` (required) - Row number
* `column` (required) - Column number
* `value` (required) - Value to set

**Template Example:**

```xml
<bx:spreadsheet action="setCellValue" name="#mySpreadsheet#" row="1" column="1" value="Hello" />
```

**setCellFormula**

Sets a formula in a specific cell.

**Attributes:**

* `name` (required) - Spreadsheet object
* `row` (required) - Row number
* `column` (required) - Column number
* `formula` (required) - Excel formula

**Template Example:**

```xml
<bx:spreadsheet action="setCellFormula" name="#mySpreadsheet#" row="10" column="1" formula="SUM(A1:A9)" />
```

**formatCell**

Formats a specific cell.

**Attributes:**

* `name` (required) - Spreadsheet object
* `row` (required) - Row number
* `column` (required) - Column number
* `formatStruct` (required) - Struct with formatting options

**Template Example:**

```xml
<bx:set formatOptions = { bold: true, fontsize: 14, color: "blue" } />
<bx:spreadsheet action="formatCell" name="#mySpreadsheet#" row="1" column="1" formatStruct="#formatOptions#" />
```

**mergeCells**

Merges a range of cells.

**Attributes:**

* `name` (required) - Spreadsheet object
* `startrow` (required) - Starting row number
* `endrow` (required) - Ending row number
* `startcolumn` (required) - Starting column number
* `endcolumn` (required) - Ending column number

**Template Example:**

```xml
<bx:spreadsheet action="mergeCells" name="#mySpreadsheet#" startrow="1" endrow="1" startcolumn="1" endcolumn="3" />
```

**setActiveSheet**

Sets the active sheet by name or index.

**Attributes:**

* `name` (required) - Spreadsheet object
* `sheetname` or `sheetindex` (required) - Sheet identifier

**Template Example:**

```xml
<bx:spreadsheet action="setActiveSheet" name="#mySpreadsheet#" sheetname="Summary" />
```

**info**

Gets information about the spreadsheet.

**Attributes:**

* `name` (required) - Spreadsheet object

**Template Example:**

```xml
<bx:spreadsheet action="info" name="#mySpreadsheet#" />
<!-- Info stored in 'info' variable -->
```

***

### 📖 BIF Reference (Functions)

#### Core Functions

**SpreadsheetFile( \[path] )**

Returns a fluent SpreadsheetFile object for creating or manipulating spreadsheet files.

**Parameters:**

* `path` (optional, string) - Path to load an existing file or where the file will be saved

**Returns:** SpreadsheetFile object

**Example:**

```javascript
// Create new
spreadsheet = SpreadsheetFile();

// Load existing
spreadsheet = SpreadsheetFile( "data.xlsx" );
```

**SpreadsheetNew( \[sheetname], \[xmlformat] )**

Creates a new BoxLang spreadsheet object.

**Parameters:**

* `sheetname` (optional, string) - Name of the initial sheet (default: "Sheet1")
* `xmlformat` (optional, boolean) - True for .xlsx, false for .xls (default: true)

**Returns:** Spreadsheet object

**Example:**

```javascript
spreadsheet = SpreadsheetNew( "MySheet", true );
```

**SpreadsheetRead( src, \[sheet], \[format], \[headerrow], \[password] )**

Reads a spreadsheet file into a BoxLang spreadsheet object.

**Parameters:**

* `src` (required, string) - Path to the spreadsheet file
* `sheet` (optional, string|number) - Sheet name or index to read
* `format` (optional, string) - Format (auto-detected, included for compatibility)
* `headerrow` (optional, number) - Row number to start reading from (default: 1)
* `password` (optional, string) - Password for encrypted files

**Returns:** Spreadsheet object

**Example:**

```javascript
spreadsheet = SpreadsheetRead( "data.xlsx", sheet="Sales", password="secret" );
```

**SpreadsheetWrite( spreadsheetObj, filename, \[password], \[overwrite] )**

Writes a spreadsheet object to a file.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `filename` (required, string) - Output file path
* `password` (optional, string) - Password to protect the file
* `overwrite` (optional, boolean) - Whether to overwrite existing files (default: false)

**Returns:** void

**Example:**

```javascript
SpreadsheetWrite( spreadsheet, "output.xlsx", "", true );
```

#### Sheet Management

**SpreadsheetCreateSheet( spreadsheetObj, sheetName )**

Creates a new sheet in the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `sheetName` (required, string) - Name of the new sheet

**Example:**

```javascript
SpreadsheetCreateSheet( spreadsheet, "NewSheet" );
```

**SpreadsheetSetActiveSheet( spreadsheetObj, sheetName )**

Sets a sheet as the active sheet by name.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `sheetName` (required, string) - Name of the sheet

**Example:**

```javascript
SpreadsheetSetActiveSheet( spreadsheet, "Sales" );
```

**SpreadsheetSetActiveSheetNumber( spreadsheetObj, sheetNumber )**

Sets a sheet as the active sheet by index.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `sheetNumber` (required, number) - Sheet index (1-based)

**Example:**

```javascript
SpreadsheetSetActiveSheetNumber( spreadsheet, 2 );
```

**SpreadsheetRemoveSheet( spreadsheetObj, sheetName )**

Removes a sheet from the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `sheetName` (required, string) - Name of the sheet to remove

**Example:**

```javascript
SpreadsheetRemoveSheet( spreadsheet, "OldSheet" );
```

#### Cell Operations

**SpreadsheetSetCellValue( spreadsheetObj, value, row, column )**

Sets the value of a specific cell.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `value` (required) - Value to set (string, number, date, etc.)
* `row` (required, number) - Row number (1-based)
* `column` (required, number) - Column number (1-based)

**Example:**

```javascript
SpreadsheetSetCellValue( spreadsheet, "Hello", 1, 1 );
SpreadsheetSetCellValue( spreadsheet, 42, 1, 2 );
```

**SpreadsheetGetCellValue( spreadsheetObj, row, column )**

Gets the value from a specific cell.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `row` (required, number) - Row number (1-based)
* `column` (required, number) - Column number (1-based)

**Returns:** Cell value

**Example:**

```javascript
value = SpreadsheetGetCellValue( spreadsheet, 1, 1 );
```

**SpreadsheetSetCellFormula( spreadsheetObj, formula, row, column )**

Sets a formula for a cell.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `formula` (required, string) - Excel formula (e.g., "=SUM(A1:A10)")
* `row` (required, number) - Row number (1-based)
* `column` (required, number) - Column number (1-based)

**Example:**

```javascript
SpreadsheetSetCellFormula( spreadsheet, "=SUM(A1:A10)", 11, 1 );
```

**SpreadsheetGetCellFormula( spreadsheetObj, \[row], \[column] )**

Gets the formula from a cell, or all formulas if row/column not specified.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `row` (optional, number) - Row number (1-based)
* `column` (optional, number) - Column number (1-based)

**Returns:** Formula string or struct of all formulas

**Example:**

```javascript
formula = SpreadsheetGetCellFormula( spreadsheet, 11, 1 );
```

**SpreadsheetFormatCell( spreadsheetObj, format, row, column )**

Applies formatting to a cell.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `format` (required, struct) - Format specification
* `row` (required, number) - Row number (1-based)
* `column` (required, number) - Column number (1-based)

**Format Structure Keys:**

* `dataformat` - Number/date format pattern
* `bold` - Bold text (boolean)
* `italic` - Italic text (boolean)
* `underline` - Underline text (boolean)
* `fontsize` - Font size
* `color` - Font color
* `bgcolor` - Background color
* `alignment` - Text alignment (left, center, right)

**Example:**

```javascript
format = {
    dataformat: "$#,##0.00",
    bold: true,
    fontsize: 12,
    color: "blue"
};
SpreadsheetFormatCell( spreadsheet, format, 1, 1 );
```

#### Row and Column Operations

**SpreadsheetAddRow( spreadsheetObj, data, \[row], \[column] )**

Adds a row of data to the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `data` (required, array) - Array of values for the row
* `row` (optional, number) - Starting row number (default: next empty row)
* `column` (optional, number) - Starting column number (default: 1)

**Example:**

```javascript
SpreadsheetAddRow( spreadsheet, [ "Name", "Age", "City" ] );
```

**SpreadsheetAddRows( spreadsheetObj, data, \[row], \[column] )**

Adds multiple rows from an array or query.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `data` (required, array|query) - Array of arrays or query object
* `row` (optional, number) - Starting row number (default: 1)
* `column` (optional, number) - Starting column number (default: 1)

**Example:**

```javascript
data = [
    [ "John", 30, "NY" ],
    [ "Jane", 25, "LA" ]
];
SpreadsheetAddRows( spreadsheet, data, 2, 1 );
```

**SpreadsheetAddColumn( spreadsheetObj, data, \[column], \[row] )**

Adds a column of data to the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `data` (required, array) - Array of values for the column
* `column` (optional, number) - Column number (default: 1)
* `row` (optional, number) - Starting row number (default: 1)

**Example:**

```javascript
SpreadsheetAddColumn( spreadsheet, [ "Q1", 1000, 1200, 1100 ], 2, 1 );
```

**SpreadsheetDeleteRow( spreadsheetObj, row )**

Deletes data in a row (does not remove the row itself).

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `row` (required, number) - Row number to delete

**Example:**

```javascript
SpreadsheetDeleteRow( spreadsheet, 5 );
```

**SpreadsheetDeleteColumn( spreadsheetObj, column )**

Deletes a column from the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `column` (required, number) - Column number to delete

**Example:**

```javascript
SpreadsheetDeleteColumn( spreadsheet, 3 );
```

**SpreadsheetShiftRows( spreadsheetObj, start, end, offset )**

Shifts rows up or down in the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `start` (required, number) - Starting row number
* `end` (required, number) - Ending row number
* `offset` (required, number) - Number of rows to shift (positive=down, negative=up)

**Example:**

```javascript
SpreadsheetShiftRows( spreadsheet, 5, 10, 2 ); // Shift rows 5-10 down by 2
```

#### Formatting Operations

**SpreadsheetSetColumnWidth( spreadsheetObj, column, width )**

Sets the width of a column.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `column` (required, number) - Column number
* `width` (required, number) - Width in characters

**Example:**

```javascript
SpreadsheetSetColumnWidth( spreadsheet, 1, 25 );
```

**SpreadsheetSetRowHeight( spreadsheetObj, row, height )**

Sets the height of a row.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `row` (required, number) - Row number
* `height` (required, number) - Height in points

**Example:**

```javascript
SpreadsheetSetRowHeight( spreadsheet, 1, 30 );
```

**SpreadsheetMergeCells( spreadsheetObj, startRow, endRow, startColumn, endColumn )**

Merges a range of cells.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `startRow` (required, number) - Starting row
* `endRow` (required, number) - Ending row
* `startColumn` (required, number) - Starting column
* `endColumn` (required, number) - Ending column

**Example:**

```javascript
SpreadsheetMergeCells( spreadsheet, 1, 1, 1, 3 ); // Merge A1:C1
```

#### Advanced Features

**SpreadsheetAddFreezePane( spreadsheetObj, column, row )**

Adds a freeze pane to lock rows and/or columns.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `column` (required, number) - Number of columns to freeze
* `row` (required, number) - Number of rows to freeze

**Example:**

```javascript
SpreadsheetAddFreezePane( spreadsheet, 1, 1 ); // Freeze first row and column
```

**SpreadsheetAddAutofilter( spreadsheetObj, \[row] )**

Adds auto-filter functionality to a row.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object
* `row` (optional, number) - Row to apply filter to (default: 1)

**Example:**

```javascript
SpreadsheetAddAutofilter( spreadsheet, 1 );
```

#### Information Functions

**SpreadsheetInfo( spreadsheetObj )**

Gets information about the spreadsheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object

**Returns:** Struct containing:

* `SHEETCOUNT` - Number of sheets
* `CURRENTSHEET` - Name of active sheet
* `SHEETNAMES` - Array of all sheet names

**Example:**

```javascript
info = SpreadsheetInfo( spreadsheet );
writeOutput( "Sheet count: " & info.SHEETCOUNT );
```

**SpreadsheetGetColumnCount( spreadsheetObj )**

Gets the number of columns in the active sheet.

**Parameters:**

* `spreadsheetObj` (required) - The spreadsheet object

**Returns:** Number of columns

**Example:**

```javascript
columnCount = SpreadsheetGetColumnCount( spreadsheet );
```

**SpreadsheetReadBinary( src )**

Reads a spreadsheet file as binary data.

**Parameters:**

* `src` (required, string) - Path to the spreadsheet file

**Returns:** Binary data

**Example:**

```javascript
binaryData = SpreadsheetReadBinary( "report.xlsx" );
```

***

### 🤝 Contributing

We ❤️ contributions! The BoxLang Spreadsheet module is open source and we welcome your involvement.

#### How to Contribute

1. **Fork the Repository** 📝
   * Visit [github.com/ortus-boxlang/bx-spreadsheet](https://github.com/ortus-boxlang/bx-spreadsheet)
   * Click the "Fork" button
2.  **Clone Your Fork** 💻

    ```bash
    git clone https://github.com/YOUR-USERNAME/bx-spreadsheet.git
    cd bx-spreadsheet
    ```
3.  **Create a Feature Branch** 🌿

    ```bash
    git checkout -b feature/my-awesome-feature development
    ```
4. **Make Your Changes** ✏️
   * Write clean, well-documented code
   * Follow the [Ortus Coding Standards](https://github.com/Ortus-Solutions/coding-standards)
   * Add tests for new functionality
5.  **Test Your Changes** 🧪

    ```bash
    ./gradlew downloadBoxLang  # First time only
    ./gradlew test
    ```
6.  **Format Your Code** 🎨

    ```bash
    ./gradlew spotlessApply
    ```
7.  **Commit Your Changes** 💾

    ```bash
    git add .
    git commit -m "feat: Add awesome new feature"
    ```
8.  **Push and Create a Pull Request** 🚀

    ```bash
    git push origin feature/my-awesome-feature
    ```

    * Go to GitHub and create a Pull Request against the `development` branch
    * Link any related issues in your PR description

#### Development Setup

**Prerequisites**

* JDK 21 or higher
* Gradle (included via wrapper)

**Building the Module**

```bash
# Download BoxLang binary (first time only)
./gradlew downloadBoxLang

# Build the module
./gradlew build

# Run tests
./gradlew test

# Format code
./gradlew spotlessApply

# Check code formatting
./gradlew spotlessCheck
```

**Project Structure**

```
bx-spreadsheet/
├── src/
│   ├── main/
│   │   ├── java/           # Java source code
│   │   │   └── ortus/boxlang/spreadsheet/
│   │   │       ├── SpreadsheetFile.java    # Main fluent API class
│   │   │       └── bifs/                    # BIF implementations
│   │   └── resources/
│   └── test/
│       ├── java/           # Java tests
│       └── resources/
├── build.gradle            # Build configuration
├── readme.md              # This file
└── CONTRIBUTING.md        # Detailed contribution guidelines
```

#### Types of Contributions

**🐛 Bug Reports**

Found a bug? Please [open an issue](https://github.com/ortus-boxlang/bx-spreadsheet/issues) with:

* A clear description of the problem
* Steps to reproduce
* Expected vs actual behavior
* BoxLang version and environment details

**✨ Feature Requests**

Have an idea? We'd love to hear it! [Open an issue](https://github.com/ortus-boxlang/bx-spreadsheet/issues) describing:

* The feature you'd like to see
* Why it would be useful
* Any implementation ideas

**📝 Documentation**

Documentation improvements are always welcome:

* Fix typos or clarify existing docs
* Add examples
* Improve code comments
* Write tutorials or blog posts

**💻 Code Contributions**

When contributing code:

* Keep changes focused and atomic
* Write or update tests
* Update documentation
* Follow existing code style
* Include meaningful commit messages

#### Code Style

We use:

* **Java Code**: Ortus Java Style (`.ortus-java-style.xml`)
* **BoxLang Code**: CFFormat (`.cfformat.json`)

The `spotlessApply` Gradle task will automatically format your code.

#### Testing

All new features and bug fixes should include tests:

* Write JUnit tests for Java code
* Place tests in `src/test/java`
* Ensure all tests pass before submitting a PR

#### Getting Help

Need help contributing?

* 💬 [Ortus Community Discourse](https://community.ortussolutions.com)
* 💼 [Box Slack Team](http://boxteam.ortussolutions.com/)
* 📧 Email: [info@ortussolutions.com](mailto:info@ortussolutions.com)

#### Code of Conduct

We follow the **Golden Rule**: Do to others as you want them to do to you.

* Be respectful and considerate
* Welcome newcomers warmly
* Assume good intentions
* Focus on constructive feedback

See our full Code of Conduct for details.

#### Recognition

All contributors will be recognized in our:

* Contributors graph
* Release notes
* Project documentation

Thank you for making BoxLang Spreadsheet better! 🎉

***

### 📄 License

Apache License, Version 2.0

***

### Directory Structure

Here is a brief overview of the directory structure:

* `.github/workflows` - These are the github actions to test and build the module via CI
* `gradle` - The gradle wrapper and configuration
* `src` - Where your module source code lives
* `build.gradle` - The gradle build file for the module
* `changelog.md` - A nice changelog tracking file
* `CONTRIBUTING.md` - Detailed contribution guidelines
* `readme.md` - This file

Here is a brief overview of the source directory structure:

* `src/main/java` - Java source code
  * `ortus/boxlang/spreadsheet/` - Main package
    * `SpreadsheetFile.java` - The fluent API implementation
    * `bifs/` - BoxLang built-in function implementations
    * `util/` - Utility classes
* `src/test/java` - Java test code

### Gradle Tasks

Before you get started, you need to run the `downloadBoxLang` task in order to download the latest BoxLang binary until we publish to Maven.

```bash
gradle downloadBoxLang
```

This will store the binary under `/src/test/resources/libs` for you to use in your tests and compiler. Here are some basic tasks:

| Task                | Description                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `build`             | The default lifecycle task that triggers the build process, including tasks like `clean`, `assemble`, and others. |
| `clean`             | Deletes the `build` folders. It helps ensure a clean build by removing any previously generated artifacts.        |
| `compileJava`       | Compiles Java source code files located in the `src/main/java` directory                                          |
| `compileTestJava`   | Compiles Java test source code files located in the `src/test/java` directory                                     |
| `dependencyUpdates` | Checks for updated versions of all dependencies                                                                   |
| `downloadBoxLang`   | Downloads the latest BoxLang binary for testing                                                                   |
| `jar`               | Packages your project's compiled classes and resources into a JAR file `build/libs` folder                        |
| `javadoc`           | Generates the Javadocs for your project and places them in the `build/docs/javadoc` folder                        |
| `spotlessApply`     | Runs the Spotless plugin to format the code                                                                       |
| `spotlessCheck`     | Runs the Spotless plugin to check the formatting of the code                                                      |
| `test`              | Executes the unit tests in your project and produces the reports in the `build/reports/tests` folder              |

### 💰 Support & Sponsorship

BoxLang is a professional open-source project and it is completely funded by the [community](https://patreon.com/ortussolutions) and [Ortus Solutions, Corp](https://www.ortussolutions.com).
