[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetCellFormula`

Specifies the formula for an Excel spreadsheet object cell.

## Method Signature

```
SpreadsheetSetCellFormula(spreadsheetObj=[any], formula=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `formula` | `STRING` | `true` | The formula to set in the cell (without the leading =). |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Set a formula in a cell:

```js
// Add SUM formula
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRows( spreadsheet, [ [ 10, 20, 30 ] ] );
SpreadsheetSetCellFormula( spreadsheet, 1, 4, "=SUM(A1:C1)" );
```

Create calculated columns:

```js
// Add formulas for calculations
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Price", "Qty", "Total" ] );
SpreadsheetAddRow( spreadsheet, [ 100, 5, "" ] );
SpreadsheetAddRow( spreadsheet, [ 50, 3, "" ] );

SpreadsheetSetCellFormula( spreadsheet, 2, 3, "=A2*B2" );
SpreadsheetSetCellFormula( spreadsheet, 3, 3, "=A3*B3" );
```

## Related

- [SpreadsheetGetCellFormula()](./SpreadsheetGetCellFormula.md) - Get formula
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell value
- [Formulas Guide](../../formulas.md) - Formula documentation
