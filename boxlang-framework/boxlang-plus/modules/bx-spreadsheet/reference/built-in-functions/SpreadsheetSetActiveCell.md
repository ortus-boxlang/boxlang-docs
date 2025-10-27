[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetActiveCell`

Sets the active/selected cell.

## Method Signature

```
SpreadsheetSetActiveCell(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Set active cell:

```js
// Set cursor to cell B3
var spreadsheet = SpreadsheetNew();
SpreadsheetSetActiveCell( spreadsheet, 3, 2 );
```

## Related

- [SpreadsheetGetActiveCell()](./SpreadsheetGetActiveCell.md) - Get active cell
- [SpreadsheetSetActiveSheet()](./SpreadsheetSetActiveSheet.md) - Set active sheet
