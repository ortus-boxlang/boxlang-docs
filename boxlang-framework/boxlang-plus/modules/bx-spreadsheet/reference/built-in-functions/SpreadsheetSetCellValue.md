[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetCellValue`

Specifies the value of an Excel spreadsheet object cell.

## Method Signature

```
SpreadsheetSetCellValue(spreadsheetObj=[any], value=[any], row=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `value` | `ANY` | `true` | The value to set in the cell. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `value` | `ANY` | `true` | The value to set in the cell. |  |

## Examples

Set a simple cell value:

```js
// Write a value to a cell
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1, 1, "Hello" );
SpreadsheetSetCellValue( spreadsheet, 1, 2, 42 );
SpreadsheetSetCellValue( spreadsheet, 1, 3, true );
```

Build a data table:

```js
// Create a structured table
var spreadsheet = SpreadsheetNew();

// Headers
SpreadsheetSetCellValue( spreadsheet, 1, 1, "Name" );
SpreadsheetSetCellValue( spreadsheet, 1, 2, "Age" );
SpreadsheetSetCellValue( spreadsheet, 1, 3, "Email" );

// Data rows
SpreadsheetSetCellValue( spreadsheet, 2, 1, "Alice" );
SpreadsheetSetCellValue( spreadsheet, 2, 2, 28 );
SpreadsheetSetCellValue( spreadsheet, 2, 3, "alice@example.com" );
```

Update existing cells:

```js
// Modify spreadsheet data
var spreadsheet = SpreadsheetRead( "/path/to/file.xlsx" );

// Update pricing information
SpreadsheetSetCellValue( spreadsheet, 5, 3, 99.99 );
SpreadsheetSetCellValue( spreadsheet, 6, 3, 149.99 );

SpreadsheetWrite( spreadsheet, "/path/to/updated.xlsx" );
```

## Related

- [SpreadsheetGetCellValue()](./SpreadsheetGetCellValue.md) - Read cell values
- [SpreadsheetClearCell()](./SpreadsheetClearCell.md) - Clear cell contents
- [SpreadsheetSetCellFormula()](./SpreadsheetSetCellFormula.md) - Set cell formulas
- [SpreadsheetFormatCell()](./SpreadsheetFormatCell.md) - Format cells
- [Cell Operations Guide](../../cell-operations.md) - Working with cells
