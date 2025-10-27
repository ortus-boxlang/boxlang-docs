[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetColumnHidden`

Sets the hidden state of a column on the active sheet.

## Method Signature

```
SpreadsheetSetColumnHidden(spreadsheetObj=[any], column=[any], hide=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |
| `hide` | `BOOLEAN` | `false` | True to hide, false to show. Default is true. | true |


## Examples

Hide a column:

```js
// Hide column C
var spreadsheet = SpreadsheetNew();
SpreadsheetSetColumnHidden( spreadsheet, 3, true );
```

Show hidden columns:

```js
// Unhide column
SpreadsheetSetColumnHidden( spreadsheet, 3, false );
```

## Related

- [SpreadsheetSetRowHidden()](./SpreadsheetSetRowHidden.md) - Hide row
- [SpreadsheetSetColumnWidth()](./SpreadsheetSetColumnWidth.md) - Set column width
- [SpreadsheetisColumnHidden()](./SpreadsheetisColumnHidden.md) - Check if hidden
