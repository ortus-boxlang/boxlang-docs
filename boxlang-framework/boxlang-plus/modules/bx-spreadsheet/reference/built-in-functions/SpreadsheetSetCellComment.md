[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetCellComment`

Sets a comment on a cell in a spreadsheet.

## Method Signature

```
SpreadsheetSetCellComment(spreadsheetObj=[any], comment=[any], row=[any], column=[any], author=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `comment` | `ANY` | `true` | The comment (String or Struct with formatting options). |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |
| `author` | `STRING` | `false` | The author of the comment (optional, only used if comment is a String). |  |


## Examples

Add a comment to a cell:

```js
// Add note to cell
var spreadsheet = SpreadsheetNew();
SpreadsheetSetCellValue( spreadsheet, 1, 1, "Data" );
SpreadsheetSetCellComment( spreadsheet, 1, 1, "Important: review this value" );
```

Document spreadsheet data:

```js
// Add explanatory comments
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "ProjectID", "Status", "Progress" ] );
SpreadsheetAddRow( spreadsheet, [ 101, "Active", 0.75 ] );

SpreadsheetSetCellComment( spreadsheet, 1, 2, "Current project status" );
SpreadsheetSetCellComment( spreadsheet, 2, 3, "75% complete as of today" );
```

## Related

- [SpreadsheetGetCellComment()](./SpreadsheetGetCellComment.md) - Get comment
- [SpreadsheetSetCellValue()](./SpreadsheetSetCellValue.md) - Set cell value
- [SpreadsheetFormatCell()](./SpreadsheetFormatCell.md) - Format cell
