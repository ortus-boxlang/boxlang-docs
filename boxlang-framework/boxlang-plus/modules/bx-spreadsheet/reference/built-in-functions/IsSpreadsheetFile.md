[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsSpreadsheetFile`

Determines whether a file is a spreadsheet file.

## Method Signature

```
IsSpreadsheetFile(filepath=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `value` | `ANY` | `true` | The value to check. |  |

## Examples

Check if a value is a SpreadsheetFile fluent API object:

```js
// Check if object uses fluent API
var spreadsheet = new SpreadsheetFile();

if ( IsSpreadsheetFile( spreadsheet ) ) {
    println( "This is a fluent SpreadsheetFile object" );
}
```

Distinguish between BIF and fluent API:

```js
// BIF approach creates an object
var bifSpreadsheet = SpreadsheetNew();

// Fluent API approach
var fluentSpreadsheet = new SpreadsheetFile();

if ( IsSpreadsheetFile( fluentSpreadsheet ) ) {
    println( "Using fluent API" );
} else if ( IsSpreadsheetObject( bifSpreadsheet ) ) {
    println( "Using BIF approach" );
}
```

Validate for fluent chaining:

```js
// Ensure fluent API available for method chaining
function configureSpreadseet( obj ) {
    if ( IsSpreadsheetFile( obj ) ) {
        // Can use fluent API chaining
        return obj.addRow( [ "Header1", "Header2" ] )
                  .formatRow( 1, { bold = true } );
    }
    return obj;
}
```

## Related

- [IsSpreadsheetObject()](./IsSpreadsheetObject.md) - Check for BIF spreadsheet objects
- [SpreadsheetFile Class](../../api-usage.md) - Fluent API documentation
- [SpreadsheetNew()](./SpreadsheetNew.md) - Create BIF spreadsheet
- [Type Checking Guide](../../type-checking.md) - BoxLang type validation
