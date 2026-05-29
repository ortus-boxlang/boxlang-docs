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

## 📋 Quick Navigation

- [Creating & Loading](#creating--loading)
- [Saving](#saving)
- [Sheet Management](#sheet-management)
- [Cell Operations](#cell-operations)
- [Row Operations](#row-operations)
- [Column Operations](#column-operations)
- [Data Conversion](#data-conversion)
- [Formatting](#formatting)
- [Advanced Features](#advanced-features)
- [Large File Streaming](#large-file-streaming)
- [Information & Accessors](#information--accessors)

---

## Creating & Loading

<details>
<summary>Creating & Loading</summary>

### `Spreadsheet()`

Creates a new empty spreadsheet in XLSX format with a default sheet named "Sheet1".

```js
sheet = Spreadsheet();
```

#### Arguments

None

#### Example

```js
// Create new spreadsheet and add data
Spreadsheet()
    .setCellValue( 1, 1, "Hello World" )
    .save( "output.xlsx" );
```

---

### `Spreadsheet( path )`

Creates or loads a spreadsheet from the specified path.

```js
sheet = Spreadsheet( path );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Path to the spreadsheet file |

#### Example

```js
// Create new file reference
sheet = Spreadsheet( "myfile.xlsx" )
    .setCellValue( 1, 1, "Data" )
    .save();
```

---

### `Spreadsheet( path, load )`

Loads an existing spreadsheet file or creates a new one.

```js
sheet = Spreadsheet( path, load );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Path to the spreadsheet file |
| load | Boolean | Yes | If true, loads existing file; if false, creates new file reference |

#### Example

```js
// Load existing file
sheet = Spreadsheet( "existing.xlsx", true );
data = sheet.toArray();
```

---

### `load( path )`

Loads a spreadsheet file from the specified path.

```js
sheet.load( path );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Fully qualified path to spreadsheet file |

#### Example

```js
sheet = Spreadsheet().load( "data.xlsx" );
```

---

### `load( path, password )`

Loads a password-protected spreadsheet file.

```js
sheet.load( path, password );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Fully qualified path to spreadsheet file |
| password | String | Yes | Password to decrypt the file |

#### Example

```js
sheet = Spreadsheet().load( "protected.xlsx", "secret123" );
```

---

### `fromJson( json )`

Creates a spreadsheet from JSON string data (array of objects).

```js
sheet = SpreadsheetFile.fromJson( json );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| json | String | Yes | JSON string containing array of objects |

#### Example

```js
json = '[{"name":"John","age":30},{"name":"Jane","age":25}]';
sheet = SpreadsheetFile.fromJson( json ).save( "people.xlsx" );
```

---

### `fromArray( data )`

Creates a spreadsheet from an array of structs.

```js
sheet = SpreadsheetFile.fromArray( data );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | Array | Yes | Array of structs where each struct is a row |

#### Example

```js
data = [
    { name: "John", age: 30 },
    { name: "Jane", age: 25 }
];
sheet = SpreadsheetFile.fromArray( data ).save( "people.xlsx" );
```

---

### `fromQuery( query )`

Creates a spreadsheet from a BoxLang query.

```js
sheet = SpreadsheetFile.fromQuery( query );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| query | Query | Yes | A BoxLang query object |

#### Example

```js
qry = queryExecute( "SELECT name, email FROM users" );
sheet = SpreadsheetFile.fromQuery( qry ).save( "users.xlsx" );
```

</details>

---

## Saving

### `save()`

Saves the spreadsheet to the currently loaded path.

```js
sheet.save();
```

#### Arguments

None

#### Example

```js
Spreadsheet( "output.xlsx" )
    .setCellValue( 1, 1, "Data" )
    .save();
```

---

### `save( path )`

Saves the spreadsheet to the specified path.

```js
sheet.save( path );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Path where file should be saved |

#### Example

```js
sheet.save( "reports/monthly.xlsx" );
```

---

### `save( path, password )`

Saves the spreadsheet with password protection.

```js
sheet.save( path, password );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Path where file should be saved |
| password | String | Yes | Password to protect the file |

#### Example

```js
sheet.save( "secure.xlsx", "secret123" );
```

---

### `saveAndClose()`

Saves the spreadsheet and closes the workbook.

```js
sheet.saveAndClose();
```

#### Arguments

None

#### Example

```js
sheet.setCellValue( 1, 1, "Final" ).saveAndClose();
```

---

## Sheet Management

<details>
<summary>Sheet Management</summary>

### `createSheet( sheetName )`

Creates a new sheet with the specified name.

```js
sheet.createSheet( sheetName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of the new sheet |

#### Example

```js
sheet.createSheet( "Q1 Data" );
```

---

### `createSheet( sheetName, overwrite )`

Creates a new sheet with optional overwrite.

```js
sheet.createSheet( sheetName, overwrite );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of the new sheet |
| overwrite | Boolean | Yes | Whether to overwrite existing sheet |

#### Example

```js
sheet.createSheet( "Sales", true );
```

---

### `selectSheet( sheetName )`

Selects (activates) a sheet by name for subsequent operations.

```js
sheet.selectSheet( sheetName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of sheet to activate |

#### Example

```js
sheet.selectSheet( "Q2 Data" )
    .setCellValue( 1, 1, "Quarter 2" );
```

---

### `selectSheet( sheetIndex )`

Selects (activates) a sheet by index (1-based).

```js
sheet.selectSheet( sheetIndex );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetIndex | Integer | Yes | Index of sheet to activate (1-based) |

#### Example

```js
sheet.selectSheet( 2 );  // Select second sheet
```

---

### `removeSheet( sheetName )`

Removes a sheet by name.

```js
sheet.removeSheet( sheetName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of sheet to remove |

#### Example

```js
sheet.removeSheet( "Obsolete Data" );
```

---

### `renameSheet( oldName, newName )`

Renames an existing sheet.

```js
sheet.renameSheet( oldName, newName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| oldName | String | Yes | Current name of the sheet |
| newName | String | Yes | New name for the sheet |

#### Example

```js
sheet.renameSheet( "Sheet1", "Sales Data" );
```

---

### `copySheet( fromName, toName )`

Copies a sheet with a new name.

```js
sheet.copySheet( fromName, toName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| fromName | String | Yes | Name of sheet to copy from |
| toName | String | Yes | Name of new sheet |

#### Example

```js
sheet.copySheet( "Template", "January" );
```

---

### `hideSheet( sheetName )`

Hides a sheet from view.

```js
sheet.hideSheet( sheetName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of sheet to hide |

#### Example

```js
sheet.hideSheet( "Raw Data" );
```

---

### `unhideSheet( sheetName )`

Unhides a sheet to make it visible.

```js
sheet.unhideSheet( sheetName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of sheet to unhide |

#### Example

```js
sheet.unhideSheet( "Hidden Calculations" );
```

---

### `moveSheet( sheetName, toIndex )`

Moves a sheet to a new position.

```js
sheet.moveSheet( sheetName, toIndex );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of sheet to move |
| toIndex | Integer | Yes | Target position (0-based) |

#### Example

```js
sheet.moveSheet( "Summary", 0 );  // Move to first position
```

</details>

---

## Cell Operations

### `setCellValue( row, col, value )`

Sets a cell value at the specified row and column.

```js
sheet.setCellValue( row, col, value );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |
| col | Integer | Yes | Column number (1-based) |
| value | Any | Yes | Value to set (String, Number, Date, Boolean) |

#### Example

```js
sheet.setCellValue( 1, 1, "Product Name" )
    .setCellValue( 1, 2, "Price" )
    .setCellValue( 2, 1, "Widget" )
    .setCellValue( 2, 2, 29.99 );
```

---

### `getCellValue( row, col )`

Gets a cell value at the specified row and column.

```js
value = sheet.getCellValue( row, col );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |
| col | Integer | Yes | Column number (1-based) |

#### Example

```js
productName = sheet.getCellValue( 2, 1 );
price = sheet.getCellValue( 2, 2 );
```

---

### `formatCell( row, col, format )`

Formats a single cell.

```js
sheet.formatCell( row, col, format );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |
| col | Integer | Yes | Column number (1-based) |
| format | Struct | Yes | Formatting options (bold, italic, fontsize, fgcolor, etc.) |

#### Example

```js
sheet.formatCell( 1, 1, {
    bold: true,
    fontsize: 14,
    fgcolor: "blue",
    fontColor: "white"
});
```

---

## Row Operations

<details>
<summary>Row Operations</summary>

### `addRow( values )`

Adds a new row at the end of the sheet.

```js
sheet.addRow( values );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| values | Array | Yes | Array of cell values for the row |

#### Example

```js
sheet.addRow( [ "John", "Doe", 30, "Engineering" ] );
```

---

### `setRowData( row, values )`

Sets multiple cell values in a row.

```js
sheet.setRowData( row, values );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |
| values | Array | Yes | Array of values starting from column 1 |

#### Example

```js
sheet.setRowData( 1, [ "Name", "Age", "Department" ] );
```

---

### `getRowData( row )`

Gets all cell values from a row.

```js
rowData = sheet.getRowData( row );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |

#### Example

```js
headers = sheet.getRowData( 1 );
```

---

### `formatRow( row, format )`

Formats all cells in a single row.

```js
sheet.formatRow( row, format );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |
| format | Struct | Yes | Formatting options |

#### Example

```js
sheet.formatRow( 1, {
    bold: true,
    fgcolor: "gray",
    alignment: "center"
});
```

---

### `formatRows( rows, format )`

Formats multiple rows specified by range or list.

```js
sheet.formatRows( rows, format );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| rows | String | Yes | Row specification: "1,3,5" or "1-5" or combinations |
| format | Struct | Yes | Formatting options |

#### Example

```js
sheet.formatRows( "1-5,10", { bold: true } );
```

---

### `removeRow( rowIndex )`

Removes a row from the sheet.

```js
sheet.removeRow( rowIndex );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| rowIndex | Integer | Yes | Row number to remove (1-based) |

#### Example

```js
sheet.removeRow( 5 );  // Remove row 5
```

---

### `addRows( data )`

Adds multiple rows from a 2D array.

```js
sheet.addRows( data );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | Array | Yes | Array of arrays representing rows |

#### Example

```js
data = [
    [ "John", 30 ],
    [ "Jane", 25 ],
    [ "Bob", 35 ]
];
sheet.addRows( data );
```

</details>

---

## Column Operations

<details>
<summary>Column Operations</summary>

### `formatColumn( column, format )`

Formats all cells in a single column.

```js
sheet.formatColumn( column, format );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| column | Integer | Yes | Column number (1-based) |
| format | Struct | Yes | Formatting options |

#### Example

```js
sheet.formatColumn( 2, { dataformat: "$#,##0.00" } );
```

---

### `formatColumns( columns, format )`

Formats multiple columns specified by range or list.

```js
sheet.formatColumns( columns, format );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| columns | String | Yes | Column specification: "1,3,5" or "1-5" |
| format | Struct | Yes | Formatting options |

#### Example

```js
sheet.formatColumns( "1-3", { alignment: "center" } );
```

---

### `deleteColumn( column )`

Deletes a column by clearing all cells.

```js
sheet.deleteColumn( column );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| column | Integer | Yes | Column number (1-based) |

#### Example

```js
sheet.deleteColumn( 3 );
```

---

### `autoSizeColumn( column )`

Auto-sizes a specific column to fit content.

```js
sheet.autoSizeColumn( column );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| column | Integer | Yes | Column number (1-based) |

#### Example

```js
sheet.autoSizeColumn( 1 );
```

---

### `autoSizeColumns()`

Auto-sizes all columns in the active sheet.

```js
sheet.autoSizeColumns();
```

#### Arguments

None

#### Example

```js
sheet.addRows( data )
    .autoSizeColumns()
    .save();
```

</details>

---

## Data Conversion

<details>
<summary>Data Conversion</summary>

### `toArray()`

Converts sheet data to array of structs (first row as headers).

```js
data = sheet.toArray();
```

#### Arguments

None

#### Example

```js
employees = Spreadsheet( "employees.xlsx", true ).toArray();
// [ { Name: "John", Age: 30 }, { Name: "Jane", Age: 25 } ]
```

---

### `toQuery()`

Converts sheet data to query format (array of structs).

```js
data = sheet.toQuery();
```

#### Arguments

None

#### Example

```js
customers = sheet.toQuery();
```

---

### `toJson()`

Converts sheet data to JSON string.

```js
json = sheet.toJson();
```

#### Arguments

None

#### Example

```js
json = sheet.toJson();
writeFile( "data.json", json );
```

---

### `toJson( pretty )`

Converts sheet data to JSON string with optional formatting.

```js
json = sheet.toJson( pretty );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| pretty | Boolean | Yes | Whether to pretty-print the JSON |

#### Example

```js
json = sheet.toJson( true );  // Pretty-printed JSON
```

---

### `toMatrix()`

Converts sheet to 2D array matrix (including headers).

```js
matrix = sheet.toMatrix();
```

#### Arguments

None

#### Example

```js
matrix = sheet.toMatrix();
// [ ["Name","Age"], ["John",30], ["Jane",25] ]
```

---

### `toCSV()`

Converts sheet data to CSV format.

```js
csv = sheet.toCSV();
```

#### Arguments

None

#### Example

```js
csv = sheet.toCSV();
writeFile( "export.csv", csv );
```

---

### `toCSV( options )`

Converts sheet data to CSV with custom options.

```js
csv = sheet.toCSV( options );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| options | Struct | Yes | CSV options: delimiter, includeHeaders, lineSeparator |

#### Example

```js
csv = sheet.toCSV({
    delimiter: ";",
    includeHeaders: false,
    lineSeparator: "\n"
});
```

</details>

---

## Formatting

### `formatCell( row, col, format )`

Formats a cell with multiple style options.

```js
sheet.formatCell( row, col, format );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |
| col | Integer | Yes | Column number (1-based) |
| format | Struct | Yes | Style options |

**Format Options:**

- `bold` (Boolean) - Bold text
- `italic` (Boolean) - Italic text
- `underline` (Boolean) - Underline text
- `fontsize` (Integer) - Font size in points
- `font` (String) - Font name
- `fontColor` (String) - Font color
- `fgcolor` (String) - Background color
- `alignment` (String) - Horizontal alignment
- `verticalalignment` (String) - Vertical alignment
- `dataformat` (String) - Number/date format

#### Example

```js
sheet.formatCell( 1, 1, {
    bold: true,
    fontsize: 14,
    fgcolor: "blue",
    fontColor: "white",
    alignment: "center",
    dataformat: "$#,##0.00"
});
```

---

## Advanced Features

<details>
<summary>Advanced Features</summary>

### `addFreezePane( column, row )`

Freezes columns and rows for scrolling.

```js
sheet.addFreezePane( column, row );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| column | Integer | Yes | Columns to left are frozen |
| row | Integer | Yes | Rows above are frozen |

#### Example

```js
sheet.addFreezePane( 1, 1 );  // Freeze first row and column
```

---

### `addSplitPane( xSplitPos, ySplitPos, leftmostColumn, topRow )`

Adds a split pane to the sheet.

```js
sheet.addSplitPane( xSplitPos, ySplitPos, leftmostColumn, topRow );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| xSplitPos | Integer | Yes | Horizontal split position (1/20th pixel) |
| ySplitPos | Integer | Yes | Vertical split position (1/20th pixel) |
| leftmostColumn | Integer | Yes | Leftmost visible column in right pane |
| topRow | Integer | Yes | Top visible row in bottom pane |

#### Example

```js
sheet.addSplitPane( 2000, 2000, 2, 2 );
```

---

### `setRowBreak( row )`

Sets a page break at the specified row.

```js
sheet.setRowBreak( row );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| row | Integer | Yes | Row number (1-based) |

#### Example

```js
sheet.setRowBreak( 25 );  // Page break after row 25
```

---

### `setFitToPage( fitToPage, pagesWide, pagesHigh )`

Sets fit-to-page print options.

```js
sheet.setFitToPage( fitToPage, pagesWide, pagesHigh );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| fitToPage | Boolean | Yes | Enable fit-to-page |
| pagesWide | Integer | Yes | Pages wide (0 = no constraint) |
| pagesHigh | Integer | Yes | Pages high (0 = no constraint) |

#### Example

```js
sheet.setFitToPage( true, 1, 0 );  // Fit to 1 page wide
```

---

### `recalculateAllFormulas()`

Recalculates all formulas in the workbook.

```js
sheet.recalculateAllFormulas();
```

#### Arguments

None

#### Example

```js
sheet.setCellValue( 1, 3, "=A1+B1" )
    .recalculateAllFormulas();
```

</details>

---

## Large File Streaming

<details>
<summary>Large File Streaming</summary>

### `process( path, consumer )`

Streams rows from a file using memory-efficient processing.

```js
sheet.process( path, consumer );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Path to spreadsheet file |
| consumer | Consumer<Array> | Yes | Callback receiving each row as Array |

#### Example

```js
Spreadsheet().process( "large-file.xlsx", ( row ) => {
    println( "Name: #row[1]#, Value: #row[2]#" );
    saveToDatabase( row );
});
```

---

### `process( path, sheetName, consumer )`

Streams rows from a specific sheet.

```js
sheet.process( path, sheetName, consumer );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | String | Yes | Path to spreadsheet file |
| sheetName | String | Yes | Name of sheet to process |
| consumer | Consumer<Array> | Yes | Callback receiving each row as Array |

#### Example

```js
Spreadsheet().process( "report.xlsx", "Sales", ( row ) => {
    if ( row[3] > 10000 ) {
        processHighValueOrder( row );
    }
});
```

---

### `process( consumer )`

Streams rows from currently loaded workbook.

```js
sheet.process( consumer );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| consumer | Consumer<Array> | Yes | Callback receiving each row as Array |

#### Example

```js
sheet = Spreadsheet( "data.xlsx", true );
sheet.process( ( row ) => {
    println( row );
});
```

{% hint style="info" %}
**Memory Efficient**: Streaming keeps only ~100 rows in memory at a time. See the [Large File Streaming Guide](../../streaming.md) for complete details.
{% endhint %}

</details>

---

## Information & Accessors

<details>
<summary>Information & Accessors</summary>

### `getSheetNames()`

Gets all sheet names in the workbook.

```js
names = sheet.getSheetNames();
```

#### Arguments

None

#### Example

```js
sheets = sheet.getSheetNames();
// [ "Sheet1", "Data", "Summary" ]
```

---

### `getRowCount()`

Gets the number of rows in the active sheet.

```js
count = sheet.getRowCount();
```

#### Arguments

None

#### Example

```js
totalRows = sheet.getRowCount();
```

---

### `getColumnCount()`

Gets the number of columns in the active sheet.

```js
count = sheet.getColumnCount();
```

#### Arguments

None

#### Example

```js
totalColumns = sheet.getColumnCount();
```

---

### `getColumnNames()`

Gets column names from the first row.

```js
names = sheet.getColumnNames();
```

#### Arguments

None

#### Example

```js
headers = sheet.getColumnNames();
// [ "Name", "Age", "Department" ]
```

---

### `info()`

Returns properties of the spreadsheet as a struct.

```js
properties = sheet.info();
```

#### Arguments

None

#### Example

```js
info = sheet.info();
println( "Sheet count: #info.sheetCount#" );
```

---

### `hasSheet( sheetName )`

Checks if a sheet exists.

```js
exists = sheet.hasSheet( sheetName );
```

#### Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| sheetName | String | Yes | Name of sheet to check |

#### Example

```js
if ( sheet.hasSheet( "Summary" ) ) {
    sheet.selectSheet( "Summary" );
}
```

</details>

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

## 📚 See Also

- [Large File Streaming Guide](../../streaming.md) - Memory-efficient processing
- [Quick Start Guide](../../quick-start.md) - Get started in 5 minutes
- [User Guide](../../user-guide.md) - Comprehensive usage guide
- [Examples](../../examples.md) - Real-world code samples
- [Built-In Functions](../built-in-functions/) - Traditional BIF reference

---

## 🔗 External Resources

- [Full API Documentation](https://apidocs.ortussolutions.com/boxlang-modules/bx-spreadsheet/1.0.0/)
- [Apache POI Documentation](https://poi.apache.org/) - Underlying library
