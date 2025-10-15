---
description: A comprehensive and fluent way to interact with spreadsheets with BoxLang
icon: file-excel
---

# Spreadsheet +

The BoxLang Spreadsheet module provides a comprehensive and modern API for working with Microsoft Excel files (`.xls` and `.xlsx`) in BoxLang. Built on top of Apache POI, this module offers both traditional BIF-style functions and a powerful **fluent API** for creating, reading, and manipulating spreadsheet files.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://www.boxlang.io/plans) but can be installed to trial purposes.
{% endhint %}

#### ✨ Key Features

* 📊 **Create & Manipulate** - Create new spreadsheets or work with existing files
* 🎨 **Formatting** - Apply cell formatting, styles, and formulas
* 📑 **Multi-Sheet Support** - Work with multiple sheets within a workbook
* 🔐 **Password Protection** - Read and write password-protected files
* ⚡ **Fluent API** - Modern, chainable interface for elegant code
* 🎯 **Type Support** - Handles strings, numbers, dates, and formulas
* 🔄 **Auto-sizing** - Automatically adjust column widths
* ❄️ **Freeze Panes** - Lock rows and columns for better viewing
* 📤 **Export/Import** - Convert to/from JSON and arrays of structs for easy data interchange

#### 📦 Installation

Install the module using CommandBox:

```bash
box install bx-spreadsheet
```

#### 🚀 Quick Start

Here's a taste of what you can do with the fluent API:

```javascript
// Create a new spreadsheet with fluent API (recommended)
SpreadsheetFile()
    .createSheet( "Sales Report" )
    .selectSheet( "Sales Report" )
    .setRowData( 1, [ "Product", "Q1", "Q2", "Q3", "Q4" ] )
    .addRow( [ "Widget A", 1000, 1200, 1100, 1300 ] )
    .addRow( [ "Widget B", 800, 900, 950, 1050 ] )
    .autoSizeColumns()
    .save( "reports/sales.xlsx" );
```

> 💡 **Best Practice**: We recommend using the fluent `SpreadsheetFile()` API directly over the individual BIFs for a more modern, readable, and maintainable codebase.

### 📚 Documentation

#### Table of Contents

* Basic Usage
* Intermediate Usage
* Advanced Usage
* BIF Reference
* Contributing

***

### 🎯 Basic Usage

#### Using the Spreadsheet Component

The `bx:spreadsheet` component provides a **declarative approach** for working with spreadsheets, compatible with CFML's `cfspreadsheet` tag. Unlike the functional BIF approach, the component syntax can be used in both **templating language** and **script** for a more declarative style of programming.

**Creating a New Spreadsheet**

**Template Syntax:**

```xml
<!-- Create a new spreadsheet object -->
<bx:spreadsheet action="create" name="mySpreadsheet" sheetname="Sales" xmlformat="true" />
```

**Script Syntax:**

```javascript
// Declarative component approach in script
bx:spreadsheet action="create" name="mySpreadsheet" sheetname="Sales" xmlformat=true;
```

**Reading a Spreadsheet**

**Template Syntax:**

```xml
<!-- Read from a file -->
<bx:spreadsheet action="read" src="data.xlsx" name="mySpreadsheet" password="optional" />

<!-- Read a specific sheet -->
<bx:spreadsheet action="read" src="data.xlsx" name="mySpreadsheet" sheet="Sheet2" />
```

**Script Syntax:**

```javascript
// Read from a file
bx:spreadsheet action="read" src="data.xlsx" name="mySpreadsheet";

// Read a specific sheet
bx:spreadsheet action="read" src="data.xlsx" name="mySpreadsheet" sheet="Sheet2";
```

**Writing a Spreadsheet**

**Template Syntax:**

```xml
<!-- Write to a file -->
<bx:spreadsheet action="write" name="#mySpreadsheet#" filename="output.xlsx" overwrite="true" />

<!-- Write with password protection -->
<bx:spreadsheet action="write" name="#mySpreadsheet#" filename="protected.xlsx" password="secret123" />
```

**Script Syntax:**

```javascript
// Write to a file
bx:spreadsheet action="write" name=mySpreadsheet filename="output.xlsx" overwrite=true;
```

**Setting Cell Values**

**Template Syntax:**

```xml
<bx:spreadsheet action="create" name="mySpreadsheet" />
<bx:spreadsheet action="setCellValue" name="#mySpreadsheet#" row="1" column="1" value="Name" />
<bx:spreadsheet action="setCellValue" name="#mySpreadsheet#" row="1" column="2" value="Age" />
```

**Script Syntax:**

```javascript
bx:spreadsheet action="create" name="mySpreadsheet";
bx:spreadsheet action="setCellValue" name=mySpreadsheet row=1 column=1 value="Name";
bx:spreadsheet action="setCellValue" name=mySpreadsheet row=1 column=2 value="Age";
```

**Adding Rows**

**Template Syntax:**

```xml
<bx:spreadsheet action="create" name="mySpreadsheet" />
<bx:spreadsheet action="addRow" name="#mySpreadsheet#" data="#['John', 30, 'NYC']#" />
<bx:spreadsheet action="addRow" name="#mySpreadsheet#" data="#['Jane', 25, 'LA']#" />
```

**Script Syntax:**

```javascript
bx:spreadsheet action="create" name="mySpreadsheet";
bx:spreadsheet action="addRow" name=mySpreadsheet data=['John', 30, 'NYC'];
bx:spreadsheet action="addRow" name=mySpreadsheet data=['Jane', 25, 'LA'];
```

**Working with Multiple Sheets**

**Template Syntax:**

```xml
<!-- Create and select a sheet -->
<bx:spreadsheet action="create" name="mySpreadsheet" />
<bx:spreadsheet action="setActiveSheet" name="#mySpreadsheet#" sheetname="Summary" />

<!-- Delete a sheet -->
<bx:spreadsheet action="delete" name="#mySpreadsheet#" sheetname="OldSheet" />
```

**Script Syntax:**

```javascript
// Create and select a sheet
bx:spreadsheet action="create" name="mySpreadsheet";
bx:spreadsheet action="setActiveSheet" name=mySpreadsheet sheetname="Summary";
```

#### Complete Component Example

**Template Syntax:**

```xml
<!-- Create a sales report -->
<bx:spreadsheet action="create" name="report" sheetname="Q1 Sales" />

<!-- Add headers -->
<bx:spreadsheet action="addRow" name="#report#" data="#['Product', 'Units', 'Revenue']#" />

<!-- Add data rows -->
<bx:spreadsheet action="addRow" name="#report#" data="#['Widget A', 100, 5000]#" />
<bx:spreadsheet action="addRow" name="#report#" data="#['Widget B', 75, 3750]#" />

<!-- Add formulas -->
<bx:spreadsheet action="setCellFormula" name="#report#" row="4" column="2" formula="SUM(B2:B3)" />
<bx:spreadsheet action="setCellFormula" name="#report#" row="4" column="3" formula="SUM(C2:C3)" />

<!-- Merge title cells -->
<bx:spreadsheet action="mergeCells" name="#report#" startrow="1" endrow="1" startcolumn="1" endcolumn="3" />

<!-- Write to file -->
<bx:spreadsheet action="write" name="#report#" filename="sales_report.xlsx" overwrite="true" />
```

**Script Syntax:**

```javascript
// Create a sales report using declarative component approach
bx:spreadsheet action="create" name="report" sheetname="Q1 Sales";

// Add headers
bx:spreadsheet action="addRow" name=report data=['Product', 'Units', 'Revenue'];

// Add data rows
bx:spreadsheet action="addRow" name=report data=['Widget A', 100, 5000];
bx:spreadsheet action="addRow" name=report data=['Widget B', 75, 3750];

// Add formulas
bx:spreadsheet action="setCellFormula" name=report row=4 column=2 formula="SUM(B2:B3)";
bx:spreadsheet action="setCellFormula" name=report row=4 column=3 formula="SUM(C2:C3)";

// Merge title cells
bx:spreadsheet action="mergeCells" name=report startrow=1 endrow=1 startcolumn=1 endcolumn=3;

// Write to file
bx:spreadsheet action="write" name=report filename="sales_report.xlsx" overwrite=true;
```

***

### 🎯 Basic Usage (BIFs and Fluent API)

#### Creating a New Spreadsheet

There are two ways to create spreadsheets: using the fluent API (recommended) or traditional BIFs.

**Using Fluent API (Recommended) ✨**

```javascript
// Create a new Excel file
spreadsheet = SpreadsheetFile();

// Create with specific format (.xls vs .xlsx)
spreadsheet = SpreadsheetFile.xlsx(); // Excel 2007+ format (default)
spreadsheet = SpreadsheetFile.xls();  // Excel 97-2003 format
```

**Using Traditional BIFs**

```javascript
// Create a new spreadsheet
spreadsheet = SpreadsheetNew();

// Create with custom sheet name
spreadsheet = SpreadsheetNew( "MySheet" );

// Create with format specification
spreadsheet = SpreadsheetNew( "MySheet", true ); // true = xlsx, false = xls
```

#### Writing Data

**Setting Individual Cell Values**

```javascript
// Fluent API
SpreadsheetFile()
    .setCellValue( 1, 1, "Hello" )
    .setCellValue( 1, 2, "World" )
    .save( "output/greeting.xlsx" );

// Traditional BIF
spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, "Hello", 1, 1 );
SpreadsheetSetCellValue( spreadsheet, "World", 1, 2 );
SpreadsheetWrite( spreadsheet, "output/greeting.xlsx" );
```

**Setting Row Data**

```javascript
// Fluent API - set data for a specific row
SpreadsheetFile()
    .setRowData( 1, [ "Name", "Age", "City" ] )
    .setRowData( 2, [ "John", 30, "New York" ] )
    .save( "output/people.xlsx" );

// Add rows sequentially
SpreadsheetFile()
    .addRow( [ "Name", "Age", "City" ] )
    .addRow( [ "John", 30, "New York" ] )
    .addRow( [ "Jane", 25, "Los Angeles" ] )
    .save( "output/people.xlsx" );

// Traditional BIF
spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Age", "City" ] );
SpreadsheetAddRow( spreadsheet, [ "John", 30, "New York" ] );
SpreadsheetWrite( spreadsheet, "output/people.xlsx", false );
```

#### Reading Data

**Reading Entire File**

```javascript
// Fluent API - load and read all data
spreadsheet = SpreadsheetFile().load( "input/data.xlsx" );
allData = spreadsheet.getAllData();

// Traditional BIF
spreadsheet = SpreadsheetRead( "input/data.xlsx" );
```

**Reading Specific Cells**

```javascript
// Fluent API
value = SpreadsheetFile()
    .load( "input/data.xlsx" )
    .getCellValue( 1, 1 );

// Traditional BIF
spreadsheet = SpreadsheetRead( "input/data.xlsx" );
value = SpreadsheetGetCellValue( spreadsheet, 1, 1 );
```

**Reading with Passwords**

```javascript
// Fluent API
spreadsheet = SpreadsheetFile().load( "protected.xlsx", "myPassword" );

// Traditional BIF
spreadsheet = SpreadsheetRead( "protected.xlsx", password="myPassword" );
```

#### Exporting and Importing Data

The SpreadsheetFile class provides convenient methods for exporting spreadsheet data to various formats and importing data from those formats.

**Exporting to JSON**

```javascript
// Export active sheet to JSON string
import ortus.boxlang.spreadsheet.SpreadsheetFile;

spreadsheet = SpreadsheetFile()
    .addRow( [ "Name", "Age", "City" ] )
    .addRow( [ "John", 30, "New York" ] )
    .addRow( [ "Jane", 25, "Los Angeles" ] );

jsonString = spreadsheet.toJson();
// Returns: [{"Age":30,"City":"New York","Name":"John"},{"Age":25,"City":"Los Angeles","Name":"Jane"}]

// Export specific sheet to JSON
jsonString = spreadsheet.toJson( "Sheet1" );
```

**Exporting to Array of Structs**

```javascript
// Export as query-like data (array of structs)
import ortus.boxlang.spreadsheet.SpreadsheetFile;

spreadsheet = SpreadsheetFile()
    .addRow( [ "Product", "Price", "Qty" ] )
    .addRow( [ "Widget A", 10.99, 5 ] )
    .addRow( [ "Widget B", 15.99, 3 ] );

// toArray() uses first row as headers
arrayData = spreadsheet.toArray();
// Returns: [{"Product":"Widget A","Price":10.99,"Qty":5},{"Product":"Widget B","Price":15.99,"Qty":3}]

// Also available as toQuery() (same functionality)
queryData = spreadsheet.toQuery();
```

**Importing from JSON**

```javascript
// Create spreadsheet from JSON string
import ortus.boxlang.spreadsheet.SpreadsheetFile;

jsonData = '[{"Name":"Alice","Score":95},{"Name":"Bob","Score":87}]';
spreadsheet = SpreadsheetFile.fromJson( jsonData );
// Creates spreadsheet with headers in row 1 and data in subsequent rows
// Headers are sorted alphabetically: "Name", "Score"

spreadsheet.save( "scores.xlsx" );
```

**Importing from Array of Structs**

```javascript
// Create spreadsheet from array of structs
import ortus.boxlang.spreadsheet.SpreadsheetFile;

data = [
    { "Product": "Widget A", "Price": 10.99, "InStock": true },
    { "Product": "Widget B", "Price": 15.99, "InStock": false }
];

spreadsheet = SpreadsheetFile.fromArray( data );
// Creates spreadsheet with headers in row 1 (sorted alphabetically)

// Also available as fromQuery() (same functionality)
spreadsheet = SpreadsheetFile.fromQuery( data );

spreadsheet.save( "products.xlsx" );
```

**Round-trip Export/Import Example**

```javascript
// Export to JSON, modify, and import back
import ortus.boxlang.spreadsheet.SpreadsheetFile;

// Create and export
original = SpreadsheetFile()
    .addRow( [ "Name", "Email" ] )
    .addRow( [ "John", "john@example.com" ] );

json = original.toJson();

// Send JSON to API, save to database, etc.
// ...

// Later, import back
imported = SpreadsheetFile.fromJson( json );
imported.save( "restored.xlsx" );
```

#### Saving Spreadsheets

```javascript
// Fluent API - various save options
SpreadsheetFile()
    .load( "input.xlsx" )
    .setCellValue( 1, 1, "Updated" )
    .save( "output.xlsx" );

// Save with password protection
SpreadsheetFile()
    .addRow( [ "Secret", "Data" ] )
    .save( "protected.xlsx", "myPassword" );

// Save with overwrite
SpreadsheetFile()
    .addRow( [ "Data" ] )
    .overwrite( true )
    .save( "existing.xlsx" );

// Traditional BIF
spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, "Data", 1, 1 );
SpreadsheetWrite( spreadsheet, "output.xlsx", "", true ); // overwrite=true
```

***

### 🎨 Intermediate Usage

#### Working with Multiple Sheets

```javascript
// Fluent API
SpreadsheetFile()
    .createSheet( "Summary" )
    .createSheet( "Details" )
    .selectSheet( "Summary" )
    .addRow( [ "Total Sales", 50000 ] )
    .selectSheet( "Details" )
    .addRow( [ "Item", "Price", "Qty" ] )
    .addRow( [ "Widget", 10.50, 100 ] )
    .save( "report.xlsx" );

// Traditional BIFs
spreadsheet = SpreadsheetNew();
SpreadsheetCreateSheet( spreadsheet, "Summary" );
SpreadsheetCreateSheet( spreadsheet, "Details" );
SpreadsheetSetActiveSheet( spreadsheet, "Summary" );
SpreadsheetAddRow( spreadsheet, [ "Total Sales", 50000 ] );
SpreadsheetSetActiveSheet( spreadsheet, "Details" );
SpreadsheetAddRow( spreadsheet, [ "Item", "Price", "Qty" ] );
```

#### Reading Specific Sheets

```javascript
// Read specific sheet by name
spreadsheet = SpreadsheetRead( "report.xlsx", sheet="Details" );

// Read specific sheet by index (1-based)
spreadsheet = SpreadsheetRead( "report.xlsx", sheet=2 );

// Fluent API
spreadsheet = SpreadsheetFile()
    .load( "report.xlsx" )
    .selectSheet( "Details" );
data = spreadsheet.getAllData();
```

#### Cell Formatting

```javascript
// Format a cell with the traditional BIF
spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1234.56, 1, 1 );

// Apply formatting
format = {
    dataformat: "$#,##0.00",
    bold: true,
    fontsize: 14,
    color: "blue",
    bgcolor: "yellow"
};
SpreadsheetFormatCell( spreadsheet, format, 1, 1 );
```

#### Working with Formulas

```javascript
// Set formulas
spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 10, 1, 1 );
SpreadsheetSetCellValue( spreadsheet, 20, 2, 1 );
SpreadsheetSetCellFormula( spreadsheet, "SUM(A1:A2)", 3, 1 );

// Get formulas
formula = SpreadsheetGetCellFormula( spreadsheet, 3, 1 );
```

#### Auto-sizing Columns

```javascript
// Fluent API - auto-size all columns
SpreadsheetFile()
    .addRow( [ "Short", "A Very Long Column Header", "Medium" ] )
    .autoSizeColumns()
    .save( "sized.xlsx" );

// Auto-size specific column
SpreadsheetFile()
    .addRow( [ "Name", "Description", "Price" ] )
    .autoSizeColumn( 2 ) // Column 2 only
    .save( "sized.xlsx" );
```

#### Column and Row Manipulation

```javascript
// Add a column of data
data = [ "Header", "Row1", "Row2", "Row3" ];
spreadsheet = SpreadsheetNew();
SpreadsheetAddColumn( spreadsheet, data, 1, 1 ); // column 1, starting at row 1

// Add multiple rows
rowData = [
    [ "A1", "B1", "C1" ],
    [ "A2", "B2", "C2" ],
    [ "A3", "B3", "C3" ]
];
SpreadsheetAddRows( spreadsheet, rowData, 1, 1 );

// Delete a row or column
SpreadsheetDeleteRow( spreadsheet, 2 );
SpreadsheetDeleteColumn( spreadsheet, 3 );

// Set column width and row height
SpreadsheetSetColumnWidth( spreadsheet, 1, 25 );
SpreadsheetSetRowHeight( spreadsheet, 1, 30 );
```

#### Merging Cells

```javascript
// Merge cells from row 1-2, column 1-3
spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, "Merged Title", 1, 1 );
SpreadsheetMergeCells( spreadsheet, 1, 2, 1, 3 );
```

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
