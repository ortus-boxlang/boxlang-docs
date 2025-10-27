[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetColumnCount`

Gets the number of columns in a worksheet.

## Method Signature

```
SpreadsheetGetColumnCount(spreadsheetObj=[any], sheetName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `sheetName` | `STRING` | `false` | The name of the sheet. If not specified, uses the active sheet. |  |


## Examples

Get the number of columns:

```js
// Get column count
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "A", "B", "C", "D" ] );
var colCount = SpreadsheetGetColumnCount( spreadsheet );
println( "Columns: " & colCount );  // Output: 4
```

Loop through all columns:

```js
// Process all columns
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
var colCount = SpreadsheetGetColumnCount( spreadsheet );

for ( var col = 1; col <= colCount; col++ ) {
    var value = SpreadsheetGetCellValue( spreadsheet, 1, col );
    println( "Column " & col & ": " & value );
}
```

## Related

- [SpreadsheetGetLastRowNumber()](./SpreadsheetGetLastRowNumber.md) - Get last row
- [SpreadsheetInfo()](./SpreadsheetInfo.md) - Get spreadsheet info
- [SpreadsheetGetColumnWidth()](./SpreadsheetGetColumnWidth.md) - Get column width
