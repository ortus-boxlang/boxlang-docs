[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetWrite`

Writes a spreadsheet object into a file.

## Method Signature

```
SpreadsheetWrite(spreadsheetObj=[any], filename=[any], password=[any], overwrite=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object to write. |  |
| `filename` | `STRING` | `true` | The path where the file should be saved. |  |
| `password` | `STRING` | `false` | Password to protect the spreadsheet (optional). |  |
| `overwrite` | `BOOLEAN` | `false` | Whether to overwrite an existing file. Default is false. |  |

## Examples

Write a spreadsheet to file:

```js
// Create and save spreadsheet
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Name", "Email" ] );
SpreadsheetAddRow( spreadsheet, [ "John Doe", "john@example.com" ] );

SpreadsheetWrite( spreadsheet, "/path/to/output.xlsx" );
println( "Spreadsheet saved successfully" );
```

Export data with overwrite:

```js
// Export and overwrite existing file
var spreadsheet = SpreadsheetRead( "/path/to/original.xlsx" );
SpreadsheetAddRow( spreadsheet, [ "New Row", "Data" ] );

// Write back to same location (overwrite = true by default)
SpreadsheetWrite( spreadsheet, "/path/to/original.xlsx", overwrite = true );
```

Save with password protection:

```js
// Save encrypted spreadsheet
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRows( spreadsheet, [ [ "A", "B" ], [ "1", "2" ] ] );

SpreadsheetWrite(
    spreadsheet,
    "/path/to/secure.xlsx",
    password = "myPassword",
    overwrite = true
);
```

## Related

- [SpreadsheetNew()](./SpreadsheetNew.md) - Create spreadsheet
- [SpreadsheetRead()](./SpreadsheetRead.md) - Read spreadsheet files
- [SpreadsheetWriteBinary()](./SpreadsheetWriteBinary.md) - Write binary format
- [File Handling Guide](../../file-handling.md) - File operations
- [I/O Operations](../../io-operations.md) - Reading and writing
