[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetCellComment`

Gets all or a single comment from a cell in a spreadsheet.

## Method Signature

```
SpreadsheetGetCellComment(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `false` | The row number (1-based). Optional. |  |
| `column` | `NUMERIC` | `false` | The column number (1-based). Optional. |  |


## Examples

Get a cell comment:

```js
// Retrieve comment from cell
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellComment( spreadsheet, 1, 1, "This is a note" );

var comment = SpreadsheetGetCellComment( spreadsheet, 1, 1 );
println( comment );
```

## Related

- [SpreadsheetSetCellComment()](./SpreadsheetSetCellComment.md) - Set comment
- [SpreadsheetGetCellValue()](./SpreadsheetGetCellValue.md) - Get cell value
