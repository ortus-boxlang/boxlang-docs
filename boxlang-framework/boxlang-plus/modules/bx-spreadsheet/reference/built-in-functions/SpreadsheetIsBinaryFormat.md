[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetIsBinaryFormat`

Checks if a spreadsheet is in binary format (.xls).

## Method Signature

```
SpreadsheetIsBinaryFormat(spreadsheetObj=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object to check. |  |


## Examples

Check if spreadsheet is binary format:

```js
// Determine file format
var spreadsheet = SpreadsheetNew( xmlformat = false );
if ( SpreadsheetIsBinaryFormat( spreadsheet ) ) {
    println( "Binary (.xls) format" );
}
```

## Related

- [SpreadsheetIsXMLFormat()](./SpreadsheetIsXMLFormat.md) - Check XML format
- [SpreadsheetNew()](./SpreadsheetNew.md) - Create spreadsheet
