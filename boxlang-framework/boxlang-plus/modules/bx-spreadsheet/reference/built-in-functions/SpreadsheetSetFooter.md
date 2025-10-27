[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetFooter`

Sets a footer in a spreadsheet.

## Method Signature

```
SpreadsheetSetFooter(spreadsheetObj=[any], footer=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `footer` | `STRUCT` | `true` | A structure containing footer configuration (left, center, right text). |  |


## Examples

Set page footer:

```js
// Add footer with date
var spreadsheet = SpreadsheetNew();
SpreadsheetSetFooter( spreadsheet, 1, "", "Page &P - &D" );
```

## Related

- [SpreadsheetSetHeader()](./SpreadsheetSetHeader.md) - Set header
- [SpreadsheetSetPrintOrientation()](./SpreadsheetSetPrintOrientation.md) - Set orientation
- [Print Settings Guide](../../print-settings.md) - Printing configuration
