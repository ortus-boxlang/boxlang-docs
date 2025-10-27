[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetRead`

Reads a sheet from a spreadsheet file and stores it in a BoxLang spreadsheet object.

## Method Signature

```
SpreadsheetRead(src=[any], sheet=[any], format=[any], headerrow=[any], password=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `src` | `STRING` | `true` | The path to the spreadsheet file. |  |
| `sheet` | `ANY` | `false` | The name or index of the sheet to read. If not specified, reads the first sheet. |  |
| `format` | `STRING` | `false` | The format of the spreadsheet (not used in this implementation as format is auto-detected). |  |
| `headerrow` | `NUMERIC` | `false` | The row number to start reading from (1-based). Default is 1. |  |
| `password` | `STRING` | `false` | The password for encrypted spreadsheets. |  |

## Examples

Read a spreadsheet file:

```js
// Read an Excel file from disk
var spreadsheet = SpreadsheetRead( src = "/path/to/file.xlsx" );
println( "Read spreadsheet with " & SpreadsheetGetColumnCount( spreadsheet ) & " columns" );
```

Read a specific sheet from a spreadsheet:

```js
// Read a specific sheet by name
var spreadsheet = SpreadsheetRead(
    src = "/path/to/file.xlsx",
    sheet = "Sales"
);
println( "Read sheet: Sales" );
```

Read a spreadsheet starting from a specific row:

```js
// Skip header rows and start reading from row 5
var spreadsheet = SpreadsheetRead(
    src = "/path/to/file.xlsx",
    sheet = 1,
    headerrow = 5
);
```

Read an encrypted spreadsheet:

```js
// Read password-protected spreadsheet
var spreadsheet = SpreadsheetRead(
    src = "/path/to/encrypted.xlsx",
    password = "myPassword"
);
```

## Related

- [SpreadsheetNew()](./SpreadsheetNew.md) - Create a new spreadsheet
- [SpreadsheetReadBinary()](./SpreadsheetReadBinary.md) - Read binary format files
- [SpreadsheetWrite()](./SpreadsheetWrite.md) - Save spreadsheets
- [SpreadsheetInfo()](./SpreadsheetInfo.md) - Get spreadsheet information
- [File Handling Guide](../../file-handling.md) - Working with spreadsheet files
