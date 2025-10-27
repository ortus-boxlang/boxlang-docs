[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddPageBreaks`

Adds multiple page breaks (rows and/or columns) to the active sheet

## Method Signature

```
SpreadsheetAddPageBreaks(spreadsheetObj=[any], rows=[any], columns=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `rows` | `ANY` | `false` | A number or array of row numbers (1-based) where page breaks should be added. |  |
| `columns` | `ANY` | `false` | A number or array of column numbers (1-based) where page breaks should be added. |  |


## Examples

Add page breaks for printing:

```js
// Add page break after row 20
var spreadsheet = SpreadsheetNew();
SpreadsheetAddPageBreaks( spreadsheet, 20, 0 );
```

## Related

- [SpreadsheetSetFitToPage()](./SpreadsheetSetFitToPage.md) - Fit to page
- [SpreadsheetSetHeader()](./SpreadsheetSetHeader.md) - Set header
- [Print Settings Guide](../../print-settings.md) - Printing configuration
