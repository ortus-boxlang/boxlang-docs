[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetActiveCell`

Gets the currently active/selected cell.

## Method Signature

```
SpreadsheetGetActiveCell(spreadsheetObj=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |


## Examples

Get the active cell:

```js
// Get currently active cell
var spreadsheet = SpreadsheetNew();
SpreadsheetSetActiveCell( spreadsheet, 2, 3 );
var activeCell = SpreadsheetGetActiveCell( spreadsheet );
println( activeCell );
```

## Related

- [SpreadsheetSetActiveCell()](./SpreadsheetSetActiveCell.md) - Set active cell
- [SpreadsheetSetActiveSheet()](./SpreadsheetSetActiveSheet.md) - Set active sheet
