[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetInfo`

Returns the properties of a spreadsheet object.

## Method Signature

```
SpreadsheetInfo(spreadsheetObj=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |

## Examples

Get complete spreadsheet information:

```js
// Get all information about a spreadsheet
var spreadsheet = SpreadsheetNew( sheetname = "Sales" );
SpreadsheetAddRow( spreadsheet, [ "Month", "Revenue" ] );
SpreadsheetAddRow( spreadsheet, [ "January", 5000 ] );

var info = SpreadsheetInfo( spreadsheet );
println( "Sheet names: " & info.sheets );
println( "Column count: " & info.columncount );
println( "Row count: " & info.rowcount );
```

Extract specific sheet information:

```js
// Get info about a specific sheet
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
var info = SpreadsheetInfo( spreadsheet );

for ( var sheet in info.sheets ) {
    println( "Sheet: " & sheet );
}
```

Monitor spreadsheet structure:

```js
// Use info for validation before operations
var spreadsheet = SpreadsheetNew();
var info = SpreadsheetInfo( spreadsheet );

if ( info.rowcount == 0 ) {
    println( "Empty spreadsheet, adding headers..." );
    SpreadsheetAddRow( spreadsheet, [ "ID", "Name", "Email" ] );
}
```

## Related

- [SpreadsheetNew()](./SpreadsheetNew.md) - Create a spreadsheet
- [SpreadsheetRead()](./SpreadsheetRead.md) - Read spreadsheet files
- [SpreadsheetGetColumnCount()](./SpreadsheetGetColumnCount.md) - Get column count
- [SpreadsheetGetLastRowNumber()](./SpreadsheetGetLastRowNumber.md) - Get last row
- [Query Access Guide](../../query-access.md) - Converting spreadsheets to queries
