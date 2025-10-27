[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetCellFormula`

Gets the formula for a for an Excel spreadsheet object cell, or all formulas for the object.

## Method Signature

```
SpreadsheetGetCellFormula(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `false` | The row number (1-based). If not specified, returns all formulas. |  |
| `column` | `NUMERIC` | `false` | The column number (1-based). If not specified, returns all formulas. |  |


## Examples

Get a cell formula:

```js
// Retrieve formula from cell
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellFormula( spreadsheet, 1, 1, "=SUM(A1:A10)" );

var formula = SpreadsheetGetCellFormula( spreadsheet, 1, 1 );
println( formula );  // Output: =SUM(A1:A10)
```

## Related

- [SpreadsheetSetCellFormula()](./SpreadsheetSetCellFormula.md) - Set formula
- [SpreadsheetGetCellValue()](./SpreadsheetGetCellValue.md) - Get cell value
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell value
