[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetCellHyperlink`

Sets a hyperlink on a cell in a spreadsheet.

## Method Signature

```
SpreadsheetSetCellHyperlink(spreadsheetObj=[any], row=[any], column=[any], hyperlink=[any], label=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |
| `hyperlink` | `STRING` | `true` | The hyperlink URL (e.g., "http://example.com", "mailto:test@example.com"). |  |
| `label` | `STRING` | `false` | The optional display label for the hyperlink. If not provided, the URL is displayed. |  |


## Examples

Add a hyperlink to a cell:

```js
// Add URL to cell
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1, 1, "Visit Website" );
SpreadsheetSetCellHyperlink( spreadsheet, 1, 1, "https://example.com" );
```

Create resource links:

```js
// Add multiple links
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1, 1, "Google" );
SpreadsheetSetCellHyperlink( spreadsheet, 1, 1, "https://google.com" );

SpreadsheetSetCellValue( spreadsheet, 2, 1, "GitHub" );
SpreadsheetSetCellHyperlink( spreadsheet, 2, 1, "https://github.com" );
```

## Related

- [SpreadsheetGetCellHyperlink()](./SpreadsheetGetCellHyperlink.md) - Get hyperlink
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell value
