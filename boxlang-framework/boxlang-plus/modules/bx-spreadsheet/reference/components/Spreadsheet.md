---
description: Spreadsheet component for Excel file operations
icon: file-code
---

# Spreadsheet

The `Spreadsheet` component provides functionality to work with Excel spreadsheet files (.xlsx, .xls). It supports multiple actions for reading, writing, and manipulating spreadsheet data including cell formatting, formulas, multiple sheets, and advanced features like merging cells and data validation.

The component can be used in template syntax with the `<bx:Spreadsheet>` tag or programmatically in script using the traditional object-oriented approach. For new development, the [Fluent API](../fluent-api/) is recommended as it provides a more modern, chainable interface.

## Syntax

**Template:**

```xml

<bx:Spreadsheet action="read" src="data.xlsx" name="mySheet" />

```

**Script:**

```js

bx:spreadsheet action="read" src="data.xlsx" name="mySheet";

```

## Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `action` | string | Yes | read | The action to perform. One of: read, write, update, create, delete, addColumn, addRow, addRows, deleteColumn, deleteRow, formatCell, formatColumn, formatRow, formatCells, mergeCells, setActiveSheet, setCellValue, setCellFormula, info. |
| `name` | any | Yes* | | The variable name containing the spreadsheet object (required for most actions). |
| `src` | string | No | | The source file path for the read action. |
| `filename` | string | No | | The destination file path for write/update actions. |
| `sheetname` | string | No | | The name of the sheet to work with or create. |
| `sheetindex` | numeric | No | | The index of the sheet to work with (1-based). |
| `format` | string | No | | The format for the spreadsheet (xlsx, xls). |
| `overwrite` | boolean | No | false | Whether to overwrite an existing file. |
| `password` | string | No | | Password for reading or writing password-protected files. |
| `xmlformat` | boolean | No | true | Use XML format (xlsx) when creating new spreadsheets. |
| `sheet` | any | No | | Sheet name or number to select when reading. |
| `headerrow` | numeric | No | | The row number containing headers when reading. |
| `rows` | string | No | | Row range to read (e.g., "1-10"). |
| `columns` | string | No | | Column range to read (e.g., "1-5" or "A-E"). |
| `columnnames` | string | No | | Comma-separated list of column names. |
| `data` | any | No | | Data to add (array for rows/columns). |
| `row` | numeric | No | | Row number for cell/row operations. |
| `column` | numeric | No | | Column number for cell/column operations. |
| `startrow` | numeric | No | | Starting row for range operations. |
| `endrow` | numeric | No | | Ending row for range operations. |
| `startcolumn` | numeric | No | | Starting column for range operations. |
| `endcolumn` | numeric | No | | Ending column for range operations. |
| `formatstruct` | struct | No | | Struct containing format options (bold, fontsize, fgcolor, etc.). |
| `value` | any | No | | Value to set in a cell. |
| `formula` | string | No | | Formula to set in a cell (without leading =). |
| `query` | query | No | | Query object to add as rows. |

## Actions

### read

Reads a spreadsheet file into a variable.

**Required Attributes:** `src`, `name`

**Optional Attributes:** `sheet`, `password`, `headerrow`, `rows`, `columns`, `columnnames`

**Example:**

```xml

<bx:Spreadsheet action="read" src="data.xlsx" name="mySheet" />
<bx:Spreadsheet action="read" src="data.xlsx" name="mySheet" sheet="Sheet2" />
<bx:Spreadsheet action="read" src="protected.xlsx" name="mySheet" password="secret" />

```

### write

Writes a spreadsheet object to a file.

**Required Attributes:** `name`, `filename`

**Optional Attributes:** `overwrite`, `password`

**Example:**

```xml

<bx:Spreadsheet action="write" name="#mySheet#" filename="output.xlsx" overwrite="true" />
<bx:Spreadsheet action="write" name="#mySheet#" filename="protected.xlsx" password="secret" />

```

### update

Updates an existing spreadsheet file (same as write).

**Required Attributes:** `name`, `filename`

**Optional Attributes:** `overwrite`

**Example:**

```xml

<bx:Spreadsheet action="update" name="#mySheet#" filename="existing.xlsx" overwrite="true" />

```

### create

Creates a new spreadsheet object.

**Required Attributes:** `name`

**Optional Attributes:** `sheetname`, `xmlformat`

**Example:**

```xml

<bx:Spreadsheet action="create" name="mySheet" />
<bx:Spreadsheet action="create" name="mySheet" sheetname="Data" xmlformat="true" />

```

### delete

Deletes a sheet from a spreadsheet.

**Required Attributes:** `name`, `sheetname`

**Example:**

```xml

<bx:Spreadsheet action="delete" name="#mySheet#" sheetname="Sheet2" />

```

### addColumn

Adds a column of data to the spreadsheet.

**Required Attributes:** `name`, `data`, `column`

**Optional Attributes:** `row` (starting row, default: 1)

**Example:**

```xml

<bx:Spreadsheet action="addColumn" name="#mySheet#" data="#columnData#" column="3" row="2" />

```

### addRow

Adds a single row of data to the spreadsheet.

**Required Attributes:** `name`, `data`

**Example:**

```xml

<bx:Spreadsheet action="addRow" name="#mySheet#" data="#rowArray#" />

```

### addRows

Adds multiple rows of data to the spreadsheet.

**Required Attributes:** `name`, `data`

**Optional Attributes:** `row` (starting row number)

**Example:**

```xml

<bx:Spreadsheet action="addRows" name="#mySheet#" data="#arrayOfRows#" />
<bx:Spreadsheet action="addRows" name="#mySheet#" data="#arrayOfRows#" row="5" />

```

### deleteColumn

Deletes a column from the spreadsheet.

**Required Attributes:** `name`, `column`

**Example:**

```xml

<bx:Spreadsheet action="deleteColumn" name="#mySheet#" column="3" />

```

### deleteRow

Deletes a row from the spreadsheet.

**Required Attributes:** `name`, `row`

**Example:**

```xml

<bx:Spreadsheet action="deleteRow" name="#mySheet#" row="5" />

```

### formatCell

Formats a specific cell.

**Required Attributes:** `name`, `formatstruct`, `row`, `column`

**Example:**

```xml

<bx:Spreadsheet
    action="formatCell"
    name="#mySheet#"
    row="1"
    column="1"
    formatstruct="#{ bold: true, fontsize: 14, fgcolor: 'blue' }#"
/>

```

### formatColumn

Formats an entire column (not yet implemented).

### formatRow

Formats an entire row (not yet implemented).

### formatCells

Formats a range of cells (not yet implemented).

### mergeCells

Merges a range of cells.

**Required Attributes:** `name`, `startrow`, `endrow`, `startcolumn`, `endcolumn`

**Example:**

```xml

<bx:Spreadsheet
    action="mergeCells"
    name="#mySheet#"
    startrow="1"
    endrow="1"
    startcolumn="1"
    endcolumn="5"
/>

```

### setActiveSheet

Selects a sheet to work with.

**Required Attributes:** `name`, and either `sheetname` or `sheetindex`

**Example:**

```xml

<bx:Spreadsheet action="setActiveSheet" name="#mySheet#" sheetname="Data" />
<bx:Spreadsheet action="setActiveSheet" name="#mySheet#" sheetindex="2" />

```

### setCellValue

Sets the value of a cell.

**Required Attributes:** `name`, `value`, `row`, `column`

**Example:**

```xml

<bx:Spreadsheet action="setCellValue" name="#mySheet#" value="Hello World" row="1" column="1" />
<bx:Spreadsheet action="setCellValue" name="#mySheet#" value="#myValue#" row="2" column="3" />

```

### setCellFormula

Sets a formula in a cell.

**Required Attributes:** `name`, `formula`, `row`, `column`

**Example:**

```xml

<bx:Spreadsheet action="setCellFormula" name="#mySheet#" formula="SUM(A1:A10)" row="11" column="1" />
<bx:Spreadsheet action="setCellFormula" name="#mySheet#" formula="B2*C2" row="2" column="4" />

```

### info

Gets information about the spreadsheet.

**Required Attributes:** `name`

**Optional Attributes:** `result` (variable name for the info struct)

**Example:**

```xml

<bx:Spreadsheet action="info" name="#mySheet#" />
<!-- Info stored in variables.info -->

<bx:Spreadsheet action="info" name="#mySheet#" result="sheetInfo" />
<!-- Info stored in variables.sheetInfo -->

```

## Complete Examples

### Reading and Processing a Spreadsheet


**Template:**

```xml

<!-- Read spreadsheet -->
<bx:Spreadsheet action="read" src="sales-data.xlsx" name="salesSheet" sheet="Q1" />

<!-- Get info -->
<bx:Spreadsheet action="info" name="#salesSheet#" result="sheetInfo" />

<!-- Process each sheet -->
<bx:loop array="#sheetInfo.SHEETNAMES#" index="sheetName">
    <bx:Spreadsheet action="setActiveSheet" name="#salesSheet#" sheetname="#sheetName#" />
    <!-- Process data... -->
</bx:loop>

```

**Script:**

```js

// Read spreadsheet
bx:spreadsheet action="read" src="sales-data.xlsx" name="salesSheet" sheet="Q1";

// Get info
bx:spreadsheet action="info" name=salesSheet result="sheetInfo";

// Process each sheet
sheetInfo.SHEETNAMES.each( ( sheetName ) => {
    bx:spreadsheet action="setActiveSheet" name=salesSheet sheetname=sheetName;
    // Process data...
} );

```

### Creating and Formatting a Report


**Template:**

```xml

<!-- Create new spreadsheet -->
<bx:Spreadsheet action="create" name="report" sheetname="Sales Report" />

<!-- Add title -->
<bx:Spreadsheet action="setCellValue" name="#report#" value="Q4 Sales Report" row="1" column="1" />
<bx:Spreadsheet
    action="formatCell"
    name="#report#"
    row="1"
    column="1"
    formatstruct="#{ bold: true, fontsize: 16, fgcolor: 'darkblue', fontColor: 'white' }#"
/>

<!-- Merge title cells -->
<bx:Spreadsheet
    action="mergeCells"
    name="#report#"
    startrow="1"
    endrow="1"
    startcolumn="1"
    endcolumn="5"
/>

<!-- Add data -->
<bx:Spreadsheet action="addRow" name="#report#" data="#[ 'Name', 'Region', 'Sales', 'Commission', 'Total' ]#" />
<bx:Spreadsheet action="addRows" name="#report#" data="#salesData#" />

<!-- Add formula for totals -->
<bx:Spreadsheet action="setCellFormula" name="#report#" formula="SUM(C3:C100)" row="101" column="3" />

<!-- Write to file -->
<bx:Spreadsheet action="write" name="#report#" filename="sales-report.xlsx" overwrite="true" />

```

**Script:**

```js

// Create new spreadsheet
bx:spreadsheet action="create" name="report" sheetname="Sales Report";

// Add title
bx:spreadsheet action="setCellValue" name=report value="Q4 Sales Report" row=1 column=1;
bx:spreadsheet action="formatCell" name=report row=1 column=1
    formatstruct={ bold: true, fontsize: 16, fgcolor: "darkblue", fontColor: "white" };

// Merge title cells
bx:spreadsheet action="mergeCells" name=report startrow=1 endrow=1 startcolumn=1 endcolumn=5;

// Add data
bx:spreadsheet action="addRow" name=report data=[ "Name", "Region", "Sales", "Commission", "Total" ];
bx:spreadsheet action="addRows" name=report data=salesData;

// Add formula for totals
bx:spreadsheet action="setCellFormula" name=report formula="SUM(C3:C100)" row=101 column=3;

// Write to file
bx:spreadsheet action="write" name=report filename="sales-report.xlsx" overwrite=true;

```

### Multi-Sheet Workbook


**Template:**

```xml

<!-- Create workbook -->
<bx:Spreadsheet action="create" name="workbook" sheetname="Summary" />

<!-- Add summary data -->
<bx:Spreadsheet action="addRow" name="#workbook#" data="#[ 'Quarter', 'Revenue' ]#" />

<!-- Create detail sheets -->
<bx:loop from="1" to="4" index="quarter">
    <bx:Spreadsheet action="create" name="workbook" sheetname="Q#quarter#" />
    <bx:Spreadsheet action="setActiveSheet" name="#workbook#" sheetname="Q#quarter#" />
    <bx:Spreadsheet action="addRows" name="#workbook#" data="#quarterData[ quarter ]#" />
</bx:loop>

<!-- Save -->
<bx:Spreadsheet action="write" name="#workbook#" filename="annual-report.xlsx" overwrite="true" />

```

## Format Struct Options

The `formatStruct` attribute accepts a struct with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `bold` | boolean | Bold text |
| `italic` | boolean | Italic text |
| `underline` | boolean | Underline text |
| `strikeout` | boolean | Strikethrough text |
| `font` | string | Font name (e.g., "Arial") |
| `fontsize` | numeric | Font size in points |
| `fontColor` | string | Font color (named or hex #RRGGBB) |
| `fgcolor` | string | Background color |
| `bgcolor` | string | Alias for fgcolor |
| `alignment` | string | "left", "center", "right", "justify" |
| `verticalalignment` | string | "top", "center", "bottom" |
| `dataformat` | string | Excel format code (e.g., "$#,##0.00") |
| `wraptext` | boolean | Wrap text in cell |
| `leftborder` | string | "thin", "medium", "thick", "none" |
| `rightborder` | string | Border style |
| `topborder` | string | Border style |
| `bottomborder` | string | Border style |
| `leftbordercolor` | string | Border color |
| `rightbordercolor` | string | Border color |
| `topbordercolor` | string | Border color |
| `bottombordercolor` | string | Border color |

## Migration to Fluent API

**Component Approach:**

```js

bx:spreadsheet action="create" name="sheet";
bx:spreadsheet action="setCellValue" name=sheet value="Title" row=1 column=1;
bx:spreadsheet action="formatCell" name=sheet row=1 column=1 formatstruct={ bold: true };
bx:spreadsheet action="addRow" name=sheet data=[ "Data" ];
bx:spreadsheet action="write" name=sheet filename="output.xlsx" overwrite=true;

```

**Fluent API (Recommended):**

```js

Spreadsheet( "output.xlsx" )
    .setCellValue( 1, 1, "Title" )
    .formatCell( 1, 1, { bold: true } )
    .addRow( [ "Data" ] )
    .save();

```

## Notes

* The component does not allow a body; all configuration is via attributes.
* The `name` attribute typically refers to the variable containing the spreadsheet object.
* For the `create` action, `name` is the variable to assign the new spreadsheet to.
* Row and column numbers are 1-based.
* Formulas should not include the leading `=` sign.
* The `xmlformat` attribute controls whether to use .xlsx (true) or .xls (false) format.
* Password protection works with both reading and writing operations.
* Some format actions (formatColumn, formatRow, formatCells) are not yet fully implemented.

## See Also

* [Fluent API Reference](../fluent-api/) - ✨ **Recommended** modern API
* [Built-In Functions](../built-in-functions/) - BIF reference
* [Components Overview](README.md)
* [User Guide](../../user-guide.md)
