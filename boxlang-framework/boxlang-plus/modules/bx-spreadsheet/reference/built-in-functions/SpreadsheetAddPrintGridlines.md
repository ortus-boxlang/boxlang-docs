[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddPrintGridlines`

Adds print gridlines to the active sheet or specified sheet.

## Method Signature

```
SpreadsheetAddPrintGridlines(spreadsheetObj=[any], sheetName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |

## Examples

Enable print gridlines:

```js
// Display gridlines when printing
var spreadsheet = SpreadsheetNew();
SpreadsheetAddPrintGridlines( spreadsheet );
```

## Related

- [SpreadsheetRemovePrintGridlines()](./SpreadsheetRemovePrintGridlines.md) - Disable gridlines
- [SpreadsheetSetPrintOrientation()](./SpreadsheetSetPrintOrientation.md) - Set orientation
- [Print Settings Guide](../../print-settings.md) - Printing configuration

| `sheetName` | `STRING` | `false` | The sheet name (optional). If not provided, operates on active sheet. |  |


## Examples



## Related
