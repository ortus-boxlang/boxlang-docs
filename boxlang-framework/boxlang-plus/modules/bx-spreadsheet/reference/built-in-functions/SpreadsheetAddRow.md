[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddRow`

Adds a row to an Excel spreadsheet object.

## Method Signature

```
SpreadsheetAddRow(spreadsheetObj=[any], data=[any], row=[any], column=[any], insert=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `data` | `ANY` | `true` | An array of data to add to the row, or a comma delimited string of cell entries, one per column |  |
| `row` | `NUMERIC` | `false` | The row number where to insert the data (1-based). If not specified, adds to the end. |  |
| `column` | `NUMERIC` | `false` | The column number where to start inserting the data (1-based). Default is 1. |  |
| `insert` | `BOOLEAN` | `false` | Whether to insert a new row or overwrite existing row. Default is false. | true |

## Examples

Add a row with array data:

```js
// Add a row of data as an array
var spreadsheet = SpreadsheetNew();
var rowData = [ "John", "Sales", 75000 ];
SpreadsheetAddRow( spreadsheet, rowData );
println( "Row added to spreadsheet" );
```

Add a row to the end:

```js
// Append rows to existing spreadsheet
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
SpreadsheetAddRow( spreadsheet, [ "Alice", "Marketing", 65000 ] );
SpreadsheetAddRow( spreadsheet, [ "Bob", "IT", 80000 ] );
```

Insert a row at a specific position:

```js
// Insert a row without overwriting
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Header1", "Header2", "Header3" ] );
SpreadsheetAddRow( spreadsheet, [ "Data1", "Data2", "Data3" ] );

// Insert a new row at position 2 (shifts existing rows down)
SpreadsheetAddRow( spreadsheet, [ "New", "Row", "Data" ], row = 2, insert = true );
```

Add comma-delimited data:

```js
// Add row using comma-delimited string
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, "John,Doe,john@example.com" );
SpreadsheetAddRow( spreadsheet, "Jane,Smith,jane@example.com" );
```

## Related

- [SpreadsheetAddRows()](./SpreadsheetAddRows.md) - Add multiple rows at once
- [SpreadsheetDeleteRow()](./SpreadsheetDeleteRow.md) - Delete a row
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set individual cell values
- [SpreadsheetFormatRow()](./SpreadsheetFormatRow.md) - Format a row
- [Row Operations Guide](../../row-operations.md) - Working with rows
