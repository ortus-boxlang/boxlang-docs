[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetisRowHidden`

Checks if a row is hidden on the active sheet.

## Method Signature

```
SpreadsheetisRowHidden(spreadsheetObj=[any], row=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |


## Examples

Check if row is hidden:

```js
// Check row visibility
var spreadsheet = SpreadsheetNew();
SpreadsheetSetRowHidden( spreadsheet, 5, true );

if ( SpreadsheetisRowHidden( spreadsheet, 5 ) ) {
    println( "Row 5 is hidden" );
}
```

## Related

- [SpreadsheetSetRowHidden()](./SpreadsheetSetRowHidden.md) - Hide row
- [SpreadsheetisColumnHidden()](./SpreadsheetisColumnHidden.md) - Check column visibility
