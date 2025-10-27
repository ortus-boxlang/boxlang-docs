[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetRepeatingRows`

Sets rows to repeat on every printed page of a spreadsheet.

## Method Signature

```
SpreadsheetSetRepeatingRows(spreadsheetObj=[any], startRow=[any], endRow=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `startRow` | `NUMERIC` | `true` | The starting row number (1-based). |  |
| `endRow` | `NUMERIC` | `true` | The ending row number (1-based). |  |


## Examples

Set repeating rows for printing:

```js
// Repeat header row on each page
var spreadsheet = SpreadsheetNew();
SpreadsheetSetRepeatingRows( spreadsheet, "1:1" );
```

## Related

- [SpreadsheetSetRepeatingColumns()](./SpreadsheetSetRepeatingColumns.md) - Set columns
- [SpreadsheetSetHeader()](./SpreadsheetSetHeader.md) - Set header
