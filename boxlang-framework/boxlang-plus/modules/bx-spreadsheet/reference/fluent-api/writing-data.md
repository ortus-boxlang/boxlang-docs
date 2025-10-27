---
description: Methods for writing data to cells, rows, and columns
icon: pen-to-square
---

# ✏️ Writing Data

Methods for adding and modifying data in spreadsheet cells, rows, and columns.

---

## setCellValue()

Sets the value of a specific cell.

**Signature:**
```js
setCellValue( numeric row, numeric column, any value )
```

**Parameters:**
- `row` (required) - Row number (1-based)
- `column` (required) - Column number (1-based)
- `value` (required) - Value to set (string, numeric, date, boolean)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx" )
    .setCellValue( 1, 1, "Name" )
    .setCellValue( 1, 2, "Age" )
    .setCellValue( 2, 1, "John Doe" )
    .setCellValue( 2, 2, 30 )
    .save();
```

---

## setRowData()

Sets values for an entire row.

**Signature:**
```js
setRowData( numeric rowNumber, array values )
```

**Parameters:**
- `rowNumber` (required) - Row number to set
- `values` (required) - Array of values

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "employees.xlsx" )
    .setRowData( 1, [ "Name", "Department", "Salary" ] )
    .setRowData( 2, [ "John Doe", "Engineering", 95000 ] )
    .setRowData( 3, [ "Jane Smith", "Marketing", 85000 ] )
    .save();
```

---

## addRow()

Adds a new row at the end of the current data.

**Signature:**
```js
addRow( array values, [numeric startRow] )
```

**Parameters:**
- `values` (required) - Array of values for the row
- `startRow` (optional) - Row number to start at (appends after last row if not specified)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx" )
    .setRowData( 1, [ "Product", "Price" ] )
    .addRow( [ "Widget", 29.99 ] )
    .addRow( [ "Gadget", 49.99 ] )
    .save();

// Add at specific position
sheet.addRow( [ "Gizmo", 19.99 ], startRow = 2 );
```

---

## addRows()

Adds multiple rows to the spreadsheet.

**Signature:**
```js
addRows( any data, [boolean includeColumnNames=false], [numeric startRow] )
```

**Parameters:**
- `data` (required) - Array of arrays, array of structs, or query object
- `includeColumnNames` (optional) - Whether to include column names as first row
- `startRow` (optional) - Row number to start at

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Array of arrays
data = [
    [ "John", "Engineering" ],
    [ "Jane", "Marketing" ]
];

Spreadsheet( "employees.xlsx" )
    .setRowData( 1, [ "Name", "Department" ] )
    .addRows( data )
    .save();

// From query
employees = queryExecute( "SELECT name, department FROM employees" );

Spreadsheet( "export.xlsx" )
    .addRows( employees, includeColumnNames = true )
    .save();

// Array of structs
data = [
    { name: "John", dept: "Engineering" },
    { name: "Jane", dept: "Marketing" }
];

sheet.addRows( data );
```

---

## addColumn()

Adds a column at the end of existing columns.

**Signature:**
```js
addColumn( array values )
```

**Parameters:**
- `values` (required) - Array of values for the column

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "quarters.xlsx" )
    .setRowData( 1, [ "Q1", "Q2", "Q3" ] )
    .addRow( [ 100, 200, 150 ] )
    // Add Q4 column
    .addColumn( [ "Q4", 175 ] )
    .save();
```

---

## insertColumn()

Inserts a column at a specific position.

**Signature:**
```js
insertColumn( numeric columnNumber, array values )
```

**Parameters:**
- `columnNumber` (required) - Position to insert column
- `values` (required) - Array of values

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx" )
    .setRowData( 1, [ "First", "Third" ] )
    .addRow( [ "A", "C" ] )
    // Insert "Second" column between them
    .insertColumn( 2, [ "Second", "B" ] )
    .save();
```

---

## setCellFormula()

Sets a formula in a cell.

**Signature:**
```js
setCellFormula( numeric row, numeric column, string formula )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number
- `formula` (required) - Excel formula (without leading =)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "calculations.xlsx" )
    .setRowData( 1, [ "Price", "Qty", "Total" ] )
    .addRow( [ 29.99, 5 ] )
    .setCellFormula( 2, 3, "A2*B2" )
    .save();

// With absolute references
sheet.setCellFormula( 2, 3, "$A$1*B2" );

// Complex formula
sheet.setCellFormula( 5, 1, "SUM(A1:A4)" );
sheet.setCellFormula( 6, 1, "AVERAGE(A1:A4)" );
```

---

## setCellRangeValue()

Sets the same value for a range of cells.

**Signature:**
```js
setCellRangeValue( numeric startRow, numeric startColumn, numeric endRow, numeric endColumn, any value )
```

**Parameters:**
- `startRow` (required) - Starting row
- `startColumn` (required) - Starting column
- `endRow` (required) - Ending row
- `endColumn` (required) - Ending column
- `value` (required) - Value to set

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Fill range with same value
Spreadsheet( "filled.xlsx" )
    .setCellRangeValue(
        startRow = 2,
        startColumn = 2,
        endRow = 5,
        endColumn = 4,
        value = 0
    )
    .save();
```

---

## setCellComment()

Adds a comment to a cell.

**Signature:**
```js
setCellComment( numeric row, numeric column, string comment, [string author] )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number
- `comment` (required) - Comment text
- `author` (optional) - Comment author name

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "reviewed.xlsx" )
    .setRowData( 1, [ "Item", "Value" ] )
    .addRow( [ "Total", 1000 ] )
    .setCellComment( 2, 2, "Verified by accounting", "Manager" )
    .save();

// Comment without author
sheet.setCellComment( 1, 1, "Important field" );
```

---

## clearCell()

Clears the content of a specific cell.

**Signature:**
```js
clearCell( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .clearCell( 2, 3 )
    .save();
```

---

## clearRow()

Clears all cells in a row.

**Signature:**
```js
clearRow( numeric rowNumber )
```

**Parameters:**
- `rowNumber` (required) - Row to clear

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .clearRow( 5 )
    .save();
```

---

## clearCellRange()

Clears a range of cells.

**Signature:**
```js
clearCellRange( numeric startRow, numeric endRow, numeric startColumn, numeric endColumn )
```

**Parameters:**
- `startRow` (required) - Starting row
- `endRow` (required) - Ending row
- `startColumn` (required) - Starting column
- `endColumn` (required) - Ending column

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .clearCellRange(
        startRow = 5,
        endRow = 10,
        startColumn = 1,
        endColumn = 5
    )
    .save();
```

---

## deleteRow()

Deletes a row from the spreadsheet.

**Signature:**
```js
deleteRow( numeric rowNumber )
```

**Parameters:**
- `rowNumber` (required) - Row to delete

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .deleteRow( 3 )
    .save();
```

---

## deleteRows()

Deletes multiple rows.

**Signature:**
```js
deleteRows( numeric startRow, numeric endRow )
```

**Parameters:**
- `startRow` (required) - Starting row
- `endRow` (required) - Ending row

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .deleteRows( startRow = 5, endRow = 10 )
    .save();
```

---

## deleteColumn()

Deletes a column from the spreadsheet.

**Signature:**
```js
deleteColumn( numeric columnNumber )
```

**Parameters:**
- `columnNumber` (required) - Column to delete

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .deleteColumn( 2 )
    .save();
```

---

## deleteColumns()

Deletes multiple columns.

**Signature:**
```js
deleteColumns( numeric startColumn, numeric endColumn )
```

**Parameters:**
- `startColumn` (required) - Starting column
- `endColumn` (required) - Ending column

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true )
    .deleteColumns( startColumn = 3, endColumn = 5 )
    .save();
```

---

## 💡 Usage Patterns

### Building Row by Row

```js
Spreadsheet( "built.xlsx" )
    .setRowData( 1, [ "Header 1", "Header 2" ] )
    .addRow( [ "Row 1 Data 1", "Row 1 Data 2" ] )
    .addRow( [ "Row 2 Data 1", "Row 2 Data 2" ] )
    .save();
```

### Bulk Data Import

```js
employees = queryExecute( "SELECT * FROM employees" );

Spreadsheet( "employees.xlsx" )
    .addRows( employees, includeColumnNames = true )
    .save();
```

### With Formulas

```js
Spreadsheet( "totals.xlsx" )
    .setRowData( 1, [ "Item", "Price", "Qty", "Total" ] )
    .addRow( [ "Widget", 29.99, 5 ] )
    .setCellFormula( 2, 4, "B2*C2" )
    .save();
```

### Modify Existing

```js
Spreadsheet( "existing.xlsx", load = true )
    .addRow( [ "New data" ] )
    .setCellValue( 2, 3, "Updated" )
    .deleteRow( 5 )
    .save();
```

---

## 📚 See Also

- [Reading Data](reading-data.md)
- [Formulas](formulas.md)
- [User Guide - Creating Spreadsheets](../../user-guide.md#creating-spreadsheets)
