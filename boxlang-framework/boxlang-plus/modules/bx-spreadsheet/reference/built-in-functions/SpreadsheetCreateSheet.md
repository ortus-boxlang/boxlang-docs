[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetCreateSheet`

Creates a spreadsheet object.

## Method Signature

```
SpreadsheetCreateSheet(spreadsheetObj=[any], sheetName=[any], overwrite=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `sheetname` | `STRING` | `false` | The name for the new sheet. If not provided, a default name is generated. |  |

## Examples

Create a new sheet:

```js
// Add a new sheet to spreadsheet
var spreadsheet = SpreadsheetNew();
SpreadsheetCreateSheet( spreadsheet, "Sales" );
SpreadsheetCreateSheet( spreadsheet, "Expenses" );
```

## Related

- [SpreadsheetRemoveSheet()](./SpreadsheetRemoveSheet.md) - Delete a sheet
- [SpreadsheetRenameSheet()](./SpreadsheetRenameSheet.md) - Rename sheet
- [SpreadsheetSetActiveSheet()](./SpreadsheetSetActiveSheet.md) - Set active sheet
- [Sheet Operations Guide](../../sheet-operations.md) - Working with sheets

| `overwrite` | `BOOLEAN` | `false` | Whether to overwrite an existing sheet with the same name (optional, default is false). | false |


## Examples



## Related
