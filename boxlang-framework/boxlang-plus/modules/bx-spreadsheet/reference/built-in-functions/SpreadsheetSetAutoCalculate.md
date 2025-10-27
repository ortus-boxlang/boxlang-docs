[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetAutoCalculate`

Sets whether formulas automatically calculate in a spreadsheet

## Method Signature

```
SpreadsheetSetAutoCalculate()
```

### Arguments

No arguments.

## Examples

Enable/disable auto-calculation:

```js
// Disable automatic formula calculation
var spreadsheet = SpreadsheetNew();
SpreadsheetSetAutoCalculate( spreadsheet, false );
```

## Related

- [SpreadsheetGetAutoCalculate()](./SpreadsheetGetAutoCalculate.md) - Get setting
- [SpreadsheetSetCellFormula()](./SpreadsheetSetCellFormula.md) - Set formula
