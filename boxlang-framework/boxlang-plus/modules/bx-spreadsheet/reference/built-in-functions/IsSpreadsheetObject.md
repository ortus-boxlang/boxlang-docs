[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsSpreadsheetObject`

Determines whether an object is a BoxLang spreadsheet object.

## Method Signature

```
IsSpreadsheetObject(object=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `value` | `ANY` | `true` | The value to check. |  |

## Examples

Check if a value is a spreadsheet object:

```js
// Check if variable is a spreadsheet
var spreadsheet = SpreadsheetNew();
if ( IsSpreadsheetObject( spreadsheet ) ) {
    println( "This is a valid spreadsheet object" );
}
```

Validate before operations:

```js
// Ensure object is spreadsheet before manipulating
var data = SpreadsheetRead( "/path/to/file.xlsx" );

if ( !IsSpreadsheetObject( data ) ) {
    throw( "Invalid spreadsheet object" );
}

SpreadsheetAddRow( data, [ "Name", "Age" ] );
```

Type validation in functions:

```js
// Type check in utility function
function processSpreadsheet( spreadsheetObj ) {
    if ( !IsSpreadsheetObject( spreadsheetObj ) ) {
        return { success = false, error = "Expected spreadsheet object" };
    }

    // Safe to process
    return { success = true, rows = SpreadsheetGetColumnCount( spreadsheetObj ) };
}
```

## Related

- [IsSpreadsheetFile()](./IsSpreadsheetFile.md) - Check for SpreadsheetFile objects
- [SpreadsheetNew()](./SpreadsheetNew.md) - Create a spreadsheet
- [SpreadsheetInfo()](./SpreadsheetInfo.md) - Get spreadsheet information
- [Type Checking Guide](../../type-checking.md) - BoxLang type validation
