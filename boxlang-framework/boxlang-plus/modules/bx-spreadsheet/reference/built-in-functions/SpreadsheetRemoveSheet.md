[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetRemoveSheet`

Deletes a spreadsheet.

## Method Signature

```
SpreadsheetRemoveSheet(spreadsheetObj=[any], sheetName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `sheetname` | `STRING` | `true` | The name of the sheet to remove. |  |

## Examples

Remove a sheet:

```js
// Delete a sheet by name
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
SpreadsheetRemoveSheet( spreadsheet, "OldSheet" );
```

## Related

- [SpreadsheetCreateSheet()](./SpreadsheetCreateSheet.md) - Create a sheet
- [SpreadsheetRenameSheet()](./SpreadsheetRenameSheet.md) - Rename sheet
- [SpreadsheetRemoveSheetNumber()](./SpreadsheetRemoveSheetNumber.md) - Remove by index
