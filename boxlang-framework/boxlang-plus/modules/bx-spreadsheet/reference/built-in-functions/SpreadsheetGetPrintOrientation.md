[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetPrintOrientation`

Retrieves the print orientation of a spreadsheet.

## Method Signature

```
SpreadsheetGetPrintOrientation(spreadsheetObj=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |


## Examples

Get print orientation:

```js
// Check current print orientation
var spreadsheet = SpreadsheetNew();
var orientation = SpreadsheetGetPrintOrientation( spreadsheet );
println( "Orientation: " & orientation );
```

## Related

- [SpreadsheetSetPrintOrientation()](./SpreadsheetSetPrintOrientation.md) - Set orientation
- [SpreadsheetSetHeader()](./SpreadsheetSetHeader.md) - Set header
