[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetActiveSheet`

Sets a sheet in a spreadsheet as active.

## Method Signature

```
SpreadsheetSetActiveSheet(spreadsheetObj=[any], sheetName=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `sheetName` | `STRING` | `true` | The name of the sheet to make active. |  |


## Examples

Set active sheet:

```js
// Activate a specific sheet
var spreadsheet = SpreadsheetNew();
SpreadsheetCreateSheet( spreadsheet, "Data" );
SpreadsheetSetActiveSheet( spreadsheet, "Data" );
```

## Related

- [SpreadsheetCreateSheet()](./SpreadsheetCreateSheet.md) - Create sheet
- [SpreadsheetSetActiveCell()](./SpreadsheetSetActiveCell.md) - Set active cell
- [SpreadsheetGetActiveCell()](./SpreadsheetGetActiveCell.md) - Get active cell
