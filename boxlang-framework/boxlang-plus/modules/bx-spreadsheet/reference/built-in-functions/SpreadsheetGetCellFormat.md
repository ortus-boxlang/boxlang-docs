[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetCellFormat`

Gets the formatting information of a cell.

## Method Signature

```
SpreadsheetGetCellFormat(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Get cell formatting:

```js
// Retrieve cell format
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Styled" ] );

var format = { bold = true, color = "0000FF" };
SpreadsheetFormatCell( spreadsheet, 1, 1, format );

var cellFormat = SpreadsheetGetCellFormat( spreadsheet, 1, 1 );
println( cellFormat );
```

## Related

- [SpreadsheetFormatCell()](./SpreadsheetFormatCell.md) - Format cell
- [SpreadsheetFormatCellRange()](./SpreadsheetFormatCellRange.md) - Format range
- [SpreadsheetGetCellValue()](./SpreadsheetGetCellValue.md) - Get cell value
