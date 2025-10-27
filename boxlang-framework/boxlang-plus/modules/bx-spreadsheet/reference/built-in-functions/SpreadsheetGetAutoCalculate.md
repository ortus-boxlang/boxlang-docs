[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetAutoCalculate`

Gets whether formulas automatically calculate in a spreadsheet

## Method Signature

```
SpreadsheetGetAutoCalculate()
```

### Arguments

No arguments.

## Examples

Check auto-calculation setting:

```js
// Check if formulas auto-calculate
var spreadsheet = SpreadsheetNew();
var autoCalc = SpreadsheetGetAutoCalculate( spreadsheet );
println( "Auto-calculate: " & autoCalc );
```

## Related

- [SpreadsheetSetAutoCalculate()](./SpreadsheetSetAutoCalculate.md) - Set auto-calc
- [SpreadsheetSetCellFormula()](./SpreadsheetSetCellFormula.md) - Set formula
