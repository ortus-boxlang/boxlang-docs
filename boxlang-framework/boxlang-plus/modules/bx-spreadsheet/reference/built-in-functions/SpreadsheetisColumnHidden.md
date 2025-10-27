[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetisColumnHidden`

Checks if a column is hidden on the active sheet.

## Method Signature

```
SpreadsheetisColumnHidden(spreadsheetObj=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Check if column is hidden:

```js
// Check column visibility
var spreadsheet = SpreadsheetNew();
SpreadsheetSetColumnHidden( spreadsheet, 3, true );

if ( SpreadsheetisColumnHidden( spreadsheet, 3 ) ) {
    println( "Column 3 is hidden" );
}
```

## Related

- [SpreadsheetSetColumnHidden()](./SpreadsheetSetColumnHidden.md) - Hide column
- [SpreadsheetisRowHidden()](./SpreadsheetisRowHidden.md) - Check row visibility
