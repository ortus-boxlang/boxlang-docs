[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetShiftRows`

Shifts one or multiple rows up or down in a spreadsheet object.

## Method Signature

```
SpreadsheetShiftRows(spreadsheetObj=[any], start=[any], end=[any], rows=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `start` | `NUMERIC` | `true` | The starting row number (1-based). |  |
| `end` | `NUMERIC` | `false` | The ending row number (1-based). Optional; defaults to start if not provided. |  |
| `rows` | `NUMERIC` | `false` | The number of rows to shift (positive for down, negative for up). Optional; defaults to 1 if not provided. |  |


## Examples

Shift rows up or down:

```js
// Shift rows starting at position 5, 3 rows down
var spreadsheet = SpreadsheetNew();
SpreadsheetShiftRows( spreadsheet, 5, 3 );
```

## Related

- [SpreadsheetShiftColumns()](./SpreadsheetShiftColumns.md) - Shift columns
- [SpreadsheetAddRow()](./SpreadsheetAddRow.md) - Add row
- [SpreadsheetDeleteRow()](./SpreadsheetDeleteRow.md) - Delete row
