[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetRemovePrintGridlines`

Removes print gridlines from the active sheet or specified sheet.

## Method Signature

```
SpreadsheetRemovePrintGridlines(spreadsheetObj=[any], sheetName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `sheetName` | `STRING` | `false` | The sheet name (optional). If not provided, operates on active sheet. |  |


## Examples

Remove print gridlines:

```js
// Disable gridlines for printing
var spreadsheet = SpreadsheetNew();
SpreadsheetRemovePrintGridlines( spreadsheet );
```

## Related

- [SpreadsheetAddPrintGridlines()](./SpreadsheetAddPrintGridlines.md) - Add gridlines
- [SpreadsheetSetPrintOrientation()](./SpreadsheetSetPrintOrientation.md) - Set orientation
