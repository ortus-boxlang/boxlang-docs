[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetLastRowNumber`

Retrieves the row number of the last row with data in a spreadsheet.

## Method Signature

```
SpreadsheetGetLastRowNumber(spreadsheetObj=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |


## Examples

Get the last row with data:

```js
// Find last row
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRows( spreadsheet, [ ["Row1"], ["Row2"], ["Row3"] ] );
var lastRow = SpreadsheetGetLastRowNumber( spreadsheet );
println( "Last row: " & lastRow );  // Output: 3
```

Append data to end:

```js
// Add to end of spreadsheet
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
var lastRow = SpreadsheetGetLastRowNumber( spreadsheet );
SpreadsheetSetCellValue( spreadsheet, lastRow + 1, 1, "New data" );
```

## Related

- [SpreadsheetGetColumnCount()](./SpreadsheetGetColumnCount.md) - Get column count
- [SpreadsheetInfo()](./SpreadsheetInfo.md) - Get spreadsheet info
- [SpreadsheetAddRow()](./SpreadsheetAddRow.md) - Add a row
