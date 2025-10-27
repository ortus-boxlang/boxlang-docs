[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetHeader`

Sets a header in a spreadsheet.

## Method Signature

```
SpreadsheetSetHeader(spreadsheetObj=[any], header=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `header` | `STRUCT` | `true` | A structure containing header configuration (left, center, right text). |  |


## Examples

Set page header:

```js
// Add header text
var spreadsheet = SpreadsheetNew();
SpreadsheetSetHeader( spreadsheet, 1, "Page &P of &N", "" );
```

## Related

- [SpreadsheetSetFooter()](./SpreadsheetSetFooter.md) - Set footer
- [SpreadsheetSetPrintOrientation()](./SpreadsheetSetPrintOrientation.md) - Set orientation
- [Print Settings Guide](../../print-settings.md) - Printing configuration
