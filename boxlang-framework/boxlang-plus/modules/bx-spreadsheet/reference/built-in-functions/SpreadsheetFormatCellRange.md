[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetFormatCellRange`

Formats a range of cells in a spreadsheet with a single format struct.

## Method Signature

```
SpreadsheetFormatCellRange(spreadsheetObj=[any], format=[any], startRow=[any], startColumn=[any], endRow=[any], endColumn=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `format` | `STRUCT` | `true` | The format struct containing style properties (alignment, bold, color, etc.). |  |
| `startRow` | `NUMERIC` | `true` | The starting row number (1-based). |  |
| `startColumn` | `NUMERIC` | `true` | The starting column number (1-based). |  |
| `endRow` | `NUMERIC` | `true` | The ending row number (1-based). |  |
| `endColumn` | `NUMERIC` | `true` | The ending column number (1-based). |  |


## Examples

Format a range of cells:

```js
// Format cells A1:C3
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRows( spreadsheet, [ ["A", "B", "C"], ["1", "2", "3"], ["X", "Y", "Z"] ] );

var format = { bold = true, background = "FFFF00", alignment = "center" };
SpreadsheetFormatCellRange( spreadsheet, 1, 1, 3, 3, format );
```

Style table headers:

```js
// Format header row
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Email", "Phone" ] );
SpreadsheetAddRow( spreadsheet, [ "John", "john@example.com", "555-1234" ] );

var headerFormat = { bold = true, color = "FFFFFF", background = "000000" };
SpreadsheetFormatCellRange( spreadsheet, 1, 1, 1, 3, headerFormat );
```

## Related

- [SpreadsheetFormatCell()](./SpreadsheetFormatCell.md) - Format single cell
- [SpreadsheetFormatRow()](./SpreadsheetFormatRow.md) - Format entire row
- [SpreadsheetFormatColumn()](./SpreadsheetFormatColumn.md) - Format entire column
