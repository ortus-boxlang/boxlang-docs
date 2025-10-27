[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGetCellType`

Gets the Excel data type of a cell.

## Method Signature

```
SpreadsheetGetCellType(spreadsheetObj=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Get the data type of a cell:

```js
// Check cell data type
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1, 1, "Text" );
SpreadsheetSetCellValue( spreadsheet, 1, 2, 42 );
SpreadsheetSetCellValue( spreadsheet, 1, 3, true );

var type1 = SpreadsheetGetCellType( spreadsheet, 1, 1 );
var type2 = SpreadsheetGetCellType( spreadsheet, 1, 2 );
var type3 = SpreadsheetGetCellType( spreadsheet, 1, 3 );
```

Validate data before processing:

```js
// Check types before conversion
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );
var cellType = SpreadsheetGetCellType( spreadsheet, 2, 1 );

if ( cellType == "string" ) {
    var value = SpreadsheetGetCellValue( spreadsheet, 2, 1 );
}
```

## Related

- [SpreadsheetGetCellValue()](./SpreadsheetGetCellValue.md) - Get cell value
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell value
- [SpreadsheetGetCellFormat()](./SpreadsheetGetCellFormat.md) - Get cell formatting
