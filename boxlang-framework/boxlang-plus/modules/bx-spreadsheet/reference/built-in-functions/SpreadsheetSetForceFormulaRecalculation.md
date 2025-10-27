[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetForceFormulaRecalculation`

Sets whether formulas will be recalculated when the spreadsheet is opened

## Method Signature

```
SpreadsheetSetForceFormulaRecalculation()
```

### Arguments

No arguments.

## Examples

Force formula recalculation:

```js
// Force Excel to recalculate all formulas on open
var spreadsheet = SpreadsheetNew();
SpreadsheetSetForceFormulaRecalculation( spreadsheet, true );
```

## Related

- [SpreadsheetGetForceFormulaRecalculation()](./SpreadsheetGetForceFormulaRecalculation.md) - Get setting
- [SpreadsheetSetAutoCalculate()](./SpreadsheetSetAutoCalculate.md) - Set auto-calc
