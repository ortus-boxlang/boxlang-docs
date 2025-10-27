[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetActiveSheetNumber`

Sets a sheet number in a spreadsheet as active.

## Method Signature

```
SpreadsheetSetActiveSheetNumber(spreadsheetObj=[any], sheetNumber=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `sheetNumber` | `NUMERIC` | `true` | The number of the sheet to make active (1-based). |  |


## Examples

Set active sheet by number:

```js
// Switch to second sheet
var spreadsheet = SpreadsheetNew();
SpreadsheetCreateSheet( spreadsheet, "Data" );
SpreadsheetSetActiveSheetNumber( spreadsheet, 2 );
```

## Related

- [SpreadsheetSetActiveSheet()](./SpreadsheetSetActiveSheet.md) - Set by name
- [SpreadsheetCreateSheet()](./SpreadsheetCreateSheet.md) - Create sheet
