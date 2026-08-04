[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetReadBinary`

Reads a spreadsheet file into a binary object.

## Method Signature

```
SpreadsheetReadBinary(src=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `src` | `STRING` | `true` | The path to the spreadsheet file. |  |


## Examples

Read legacy Excel file:

```js
// Read .xls file (binary format)
var spreadsheet = SpreadsheetReadBinary( "/path/to/file.xls" );
println( "Read legacy Excel file" );
```

## Related

- [SpreadsheetRead()](./SpreadsheetRead.md) - Read Excel files
- [SpreadsheetWrite()](./SpreadsheetWrite.md) - Write files
- [File Handling Guide](../../../../file-handling/README.md) - File operations
