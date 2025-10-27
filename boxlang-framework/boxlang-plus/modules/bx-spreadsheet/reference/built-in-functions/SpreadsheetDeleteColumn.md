[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetDeleteColumn`

Deletes a column in a spreadsheet.

## Method Signature

```
SpreadsheetDeleteColumn(spreadsheetObj=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `column` | `NUMERIC` | `true` | The column number to delete (1-based). |  |

## Examples

Delete a single column:

```js
// Delete column C
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
SpreadsheetDeleteColumn( spreadsheet, 3 );
```

## Related

- [SpreadsheetDeleteColumns()](./SpreadsheetDeleteColumns.md) - Delete multiple columns
- [SpreadsheetAddColumn()](./SpreadsheetAddColumn.md) - Add a column
- [SpreadsheetGetColumnCount()](./SpreadsheetGetColumnCount.md) - Get column count
