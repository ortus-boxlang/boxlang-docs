[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetClearCell`

Clears the specified cell of all styles and values.

## Method Signature

```
SpreadsheetClearCell(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Clear a cell of all content and formatting:

```js
// Clear cell A1
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1, 1, "To be cleared" );
SpreadsheetClearCell( spreadsheet, 1, 1 );
```

Remove specific cell data:

```js
// Clear cell while preserving adjacent cells
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
SpreadsheetClearCell( spreadsheet, 5, 3 );  // Clear row 5, column 3
```

## Related

- [SpreadsheetClearCellRange()](./SpreadsheetClearCellRange.md) - Clear multiple cells
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell value
- [SpreadsheetDeleteRow()](./SpreadsheetDeleteRow.md) - Delete entire row
