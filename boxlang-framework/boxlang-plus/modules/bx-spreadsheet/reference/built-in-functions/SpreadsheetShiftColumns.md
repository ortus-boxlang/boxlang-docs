[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetShiftColumns`

Shifts columns in a spreadsheet left or right.

## Method Signature

```
SpreadsheetShiftColumns(spreadsheetObj=[any], start=[any], end=[any], columns=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `start` | `NUMERIC` | `true` | The starting column number (1-based). |  |
| `end` | `NUMERIC` | `false` | The ending column number (1-based). Optional; defaults to start if not provided. |  |
| `columns` | `NUMERIC` | `false` | The number of columns to shift (positive for right, negative for left). Optional; defaults to 1 if not provided. |  |


## Examples

Shift columns left or right:

```js
// Shift columns starting at position 3, 2 columns right
var spreadsheet = SpreadsheetNew();
SpreadsheetShiftColumns( spreadsheet, 3, 2 );
```

## Related

- [SpreadsheetShiftRows()](./SpreadsheetShiftRows.md) - Shift rows
- [SpreadsheetAddColumn()](./SpreadsheetAddColumn.md) - Add column
- [SpreadsheetDeleteColumn()](./SpreadsheetDeleteColumn.md) - Delete column
