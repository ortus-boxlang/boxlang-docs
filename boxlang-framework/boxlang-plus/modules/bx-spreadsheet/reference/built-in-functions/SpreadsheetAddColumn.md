[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddColumn`

Adds columns to a spreadsheet object.

## Method Signature

```
SpreadsheetAddColumn(spreadsheetObj=[any], data=[any], column=[any], row=[any], insert=[any], datatype=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `data` | `ARRAY` | `true` | An array of data to add to the column. |  |
| `column` | `NUMERIC` | `false` | The column number where to insert the data (1-based). If not specified, adds to the end. |  |
| `row` | `NUMERIC` | `false` | The row number where to start inserting the data (1-based). Default is 1. | 1 |
| `insert` | `BOOLEAN` | `false` | Whether to insert a new column or overwrite existing column. Default is false. | false |
| `datatype` | `STRING` | `false` | The data type to apply to the cells (not implemented in this version). |  |

## Examples

Add a column to a spreadsheet:

```js
// Add a column with data
var spreadsheet = SpreadsheetNew();
SpreadsheetAddColumn( spreadsheet, "ID", [ 1, 2, 3 ] );
```

Add multiple columns:

```js
// Build spreadsheet column by column
var spreadsheet = SpreadsheetNew();
SpreadsheetAddColumn( spreadsheet, "Name", [ "John", "Jane", "Bob" ] );
SpreadsheetAddColumn( spreadsheet, "Age", [ 30, 28, 35 ] );
```

## Related

- [SpreadsheetDeleteColumn()](./SpreadsheetDeleteColumn.md) - Delete a column
- [SpreadsheetSetColumnWidth()](./SpreadsheetSetColumnWidth.md) - Set column width
- [SpreadsheetAddRow()](./SpreadsheetAddRow.md) - Add a row
- [Column Operations Guide](../../column-operations.md) - Working with columns
