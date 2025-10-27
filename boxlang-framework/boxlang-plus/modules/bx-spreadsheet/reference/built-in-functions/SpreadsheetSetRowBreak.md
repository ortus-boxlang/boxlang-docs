[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetRowBreak`

Sets a page (row) break on the active sheet at the given row

## Method Signature

```
SpreadsheetSetRowBreak(spreadsheetObj=[any], row=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |


## Examples

Set row page break:

```js
// Add page break after row 20
var spreadsheet = SpreadsheetNew();
SpreadsheetSetRowBreak( spreadsheet, 20 );
```

## Related

- [SpreadsheetRemoveRowBreak()](./SpreadsheetRemoveRowBreak.md) - Remove break
- [SpreadsheetSetColumnBreak()](./SpreadsheetSetColumnBreak.md) - Set column break
