[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetCellValue`

Gets the value for a for an Excel spreadsheet object cell.

## Method Signature

```
SpreadsheetGetCellValue(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |

## Examples

Get a single cell value:

```js
// Read a cell value
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
var cellValue = SpreadsheetGetCellValue( spreadsheet, 1, 1 );
println( "Cell A1 contains: " & cellValue );
```

Extract data with type checking:

```js
// Get cell values and check types
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Age", "Active" ] );
SpreadsheetAddRow( spreadsheet, [ "John", 30, true ] );

var name = SpreadsheetGetCellValue( spreadsheet, 2, 1 );
var age = SpreadsheetGetCellValue( spreadsheet, 2, 2 );
var active = SpreadsheetGetCellValue( spreadsheet, 2, 3 );

println( "Name: " & name & " (Type: " & typeof(name) & ")" );
```

Build arrays from cell values:

```js
// Extract entire row as array
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
var rowData = [];
var colCount = SpreadsheetGetColumnCount( spreadsheet );

for ( var col = 1; col <= colCount; col++ ) {
    rowData.append( SpreadsheetGetCellValue( spreadsheet, 1, col ) );
}

println( "Row data: " & rowData );
```

## Related

- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell values
- [SpreadsheetClearCell()](./SpreadsheetClearCell.md) - Clear cell contents
- [SpreadsheetGetCellType()](./SpreadsheetGetCellType.md) - Get cell data type
- [SpreadsheetGetCellFormat()](./SpreadsheetGetCellFormat.md) - Get cell formatting
- [Cell Operations Guide](../../cell-operations.md) - Working with cells
