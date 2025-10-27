[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetClearCellRange`

Clears the specified cell range of all styles and values.

## Method Signature

```
SpreadsheetClearCellRange(spreadsheetObj=[any], startRow=[any], startColumn=[any], endRow=[any], endColumn=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `startRow` | `NUMERIC` | `true` | The starting row number (1-based). |  |
| `startColumn` | `NUMERIC` | `true` | The starting column number (1-based). |  |
| `endRow` | `NUMERIC` | `true` | The ending row number (1-based). |  |
| `endColumn` | `NUMERIC` | `true` | The ending column number (1-based). |  |


## Examples

Clear a range of cells:

```js
// Clear cells A1:C5
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRows( spreadsheet, [ ["A", "B", "C"], ["1", "2", "3"] ] );
SpreadsheetClearCellRange( spreadsheet, 1, 1, 5, 3 );
```

Reset section of spreadsheet:

```js
// Clear data range but keep headers
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
SpreadsheetClearCellRange( spreadsheet, 2, 1, 100, 10 );  // Clear rows 2-100, columns 1-10
```

## Related

- [SpreadsheetClearCell()](./SpreadsheetClearCell.md) - Clear a single cell
- [SpreadsheetDeleteRows()](./SpreadsheetDeleteRows.md) - Delete rows
- [SpreadsheetDeleteColumns()](./SpreadsheetDeleteColumns.md) - Delete columns
