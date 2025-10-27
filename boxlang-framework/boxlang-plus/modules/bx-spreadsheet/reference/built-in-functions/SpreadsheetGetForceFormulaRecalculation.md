[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetForceFormulaRecalculation`

Gets whether formulas will be recalculated when the spreadsheet is opened

## Method Signature

```
SpreadsheetGetForceFormulaRecalculation()
```

### Arguments

No arguments.

## Examples

Check force recalculation setting:

```js
// Check if formulas force recalculation
var spreadsheet = SpreadsheetNew();
var forceRecalc = SpreadsheetGetForceFormulaRecalculation( spreadsheet );
println( "Force recalculation: " & forceRecalc );
```

## Related

- [SpreadsheetSetForceFormulaRecalculation()](./SpreadsheetSetForceFormulaRecalculation.md) - Set recalc
- [SpreadsheetGetAutoCalculate()](./SpreadsheetGetAutoCalculate.md) - Get auto-calc
