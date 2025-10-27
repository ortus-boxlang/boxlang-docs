[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetFormatRow`

Formats a row of an Excel spreadsheet object.

## Method Signature

```
SpreadsheetFormatRow(spreadsheetObj=[any], format=[any], row=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `format` | `STRUCT` | `true` | A structure containing formatting options (bold, italic, color, etc.). |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |


## Examples

Format an entire row:

```js
// Format header row
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Email", "Phone" ] );

var format = { bold = true, background = "000000", color = "FFFFFF" };
SpreadsheetFormatRow( spreadsheet, 1, format );
```

## Related

- [SpreadsheetFormatRows()](./SpreadsheetFormatRows.md) - Format rows
- [SpreadsheetFormatCell()](./SpreadsheetFormatCell.md) - Format cell
