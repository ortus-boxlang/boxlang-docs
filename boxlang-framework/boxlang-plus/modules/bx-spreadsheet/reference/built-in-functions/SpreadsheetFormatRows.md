[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetFormatRows`

Formats multiple rows of an Excel spreadsheet object.

## Method Signature

```
SpreadsheetFormatRows(spreadsheetObj=[any], format=[any], rows=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `format` | `STRUCT` | `true` | A structure containing formatting options (bold, italic, color, etc.). |  |
| `rows` | `STRING` | `true` | The rows to format, in one of the following formats: * - startRow-endRow (e.g., "1-5") - Formats rows in a single range * - row,row,row... (e.g., "1,3,5") - Formats individual rows * - Combinations allowed (e.g., "1-5,6,7,9-12") |  |


## Examples

Format multiple rows:

```js
// Apply formatting to rows 1-5
var spreadsheet = SpreadsheetNew();
var format = { bold = false, background = "F5F5F5" };
SpreadsheetFormatRows( spreadsheet, 1, 5, format );
```

## Related

- [SpreadsheetFormatRow()](./SpreadsheetFormatRow.md) - Format single row
- [SpreadsheetFormatColumns()](./SpreadsheetFormatColumns.md) - Format columns
