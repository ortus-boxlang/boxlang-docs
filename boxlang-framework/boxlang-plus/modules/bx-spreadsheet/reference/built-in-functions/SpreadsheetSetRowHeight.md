[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetRowHeight`

Sets the height of a row in a spreadsheet object.

## Method Signature

```
SpreadsheetSetRowHeight(spreadsheetObj=[any], row=[any], height=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `true` | The row number (1-based). |  |
| `height` | `NUMERIC` | `true` | The height to set for the row in points. |  |


## Examples

Set row height:

```js
// Set row height in pixels
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRow( spreadsheet, [ "Tall Row" ] );

SpreadsheetSetRowHeight( spreadsheet, 1, 50 );
```

## Related

- [SpreadsheetSetColumnWidth()](./SpreadsheetSetColumnWidth.md) - Set column width
- [SpreadsheetFormatRow()](./SpreadsheetFormatRow.md) - Format row
- [SpreadsheetAddRow()](./SpreadsheetAddRow.md) - Add row
