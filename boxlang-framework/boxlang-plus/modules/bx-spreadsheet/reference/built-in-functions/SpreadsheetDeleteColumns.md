[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetDeleteColumns`

Deletes multiple columns in a spreadsheet.

## Method Signature

```
SpreadsheetDeleteColumns(spreadsheetObj=[any], column=[any], numColumns=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `column` | `NUMERIC` | `true` | The starting column number to delete (1-based). |  |
| `number` | `NUMERIC` | `true` | The number of columns to delete. |  |

## Examples

Delete a range of columns:

```js
// Delete columns 2 through 4
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
SpreadsheetDeleteColumns( spreadsheet, 2, 3 );  // Deletes 3 columns starting at column 2
```

## Related

- [SpreadsheetDeleteColumn()](./SpreadsheetDeleteColumn.md) - Delete a single column
- [SpreadsheetAddColumn()](./SpreadsheetAddColumn.md) - Add a column
