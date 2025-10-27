[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetColumnWidth`

Retrieves the width of a column in a spreadsheet.

## Method Signature

```
SpreadsheetGetColumnWidth(spreadsheetObj=[any], column=[any], returnWidthInPixels=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |
| `returnWidthInPixels` | `BOOLEAN` | `false` | If true, returns width in pixels; if false, returns width in points (default: true). |  |


## Examples

Get column width:

```js
// Get width of column A
var spreadsheet = SpreadsheetNew();
SpreadsheetSetColumnWidth( spreadsheet, 1, 150 );

var width = SpreadsheetGetColumnWidth( spreadsheet, 1 );
println( "Column width: " & width );
```

## Related

- [SpreadsheetSetColumnWidth()](./SpreadsheetSetColumnWidth.md) - Set width
- [SpreadsheetAddColumn()](./SpreadsheetAddColumn.md) - Add column
- [SpreadsheetGetColumnCount()](./SpreadsheetGetColumnCount.md) - Get column count
