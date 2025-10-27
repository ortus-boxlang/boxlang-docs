[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetIsXMLFormat`

Checks if a spreadsheet is in XML format (.xlsx).

## Method Signature

```
SpreadsheetIsXMLFormat(spreadsheetObj=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object to check. |  |


## Examples

Check if spreadsheet is XML format:

```js
// Determine file format
var spreadsheet = SpreadsheetNew();
if ( SpreadsheetIsXMLFormat( spreadsheet ) ) {
    println( "XML (.xlsx) format" );
}
```

## Related

- [SpreadsheetIsBinaryFormat()](./SpreadsheetIsBinaryFormat.md) - Check binary format
- [SpreadsheetNew()](./SpreadsheetNew.md) - Create spreadsheet
