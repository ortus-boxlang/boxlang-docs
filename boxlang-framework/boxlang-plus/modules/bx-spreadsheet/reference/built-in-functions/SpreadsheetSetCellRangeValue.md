[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetCellRangeValue`

Sets the same value to a range of cells.

## Method Signature

```
SpreadsheetSetCellRangeValue(spreadsheetObj=[any], value=[any], startRow=[any], endRow=[any], startColumn=[any], endColumn=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `value` | `ANY` | `true` | The value to set for all cells in the range. |  |
| `startRow` | `NUMERIC` | `true` | The starting row number (1-based). |  |
| `endRow` | `NUMERIC` | `true` | The ending row number (1-based). |  |
| `startColumn` | `NUMERIC` | `true` | The starting column number (1-based). |  |
| `endColumn` | `NUMERIC` | `true` | The ending column number (1-based). |  |


## Examples

Set value for a range of cells:

```js
// Fill range with value
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellRangeValue( spreadsheet, "Sample", 1, 1, 3, 3 );
```

## Related

- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set single cell
- [SpreadsheetClearCellRange()](./SpreadsheetClearCellRange.md) - Clear range
