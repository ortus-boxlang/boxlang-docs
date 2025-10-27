[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddAutofilter`

Adds auto filters to a spreadsheet.

## Method Signature

```
SpreadsheetAddAutofilter(spreadsheetObj=[any], row=[any], startColumn=[any], endRow=[any], endColumn=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `row` | `NUMERIC` | `false` | The starting row for the autofilter (1-based). Default is 1. | 1 |
| `startColumn` | `NUMERIC` | `false` | The starting column for the autofilter (1-based). Default is 1. | 1 |
| `endRow` | `NUMERIC` | `false` | The ending row for the autofilter (1-based). If not specified, uses all rows with data. |  |
| `endColumn` | `NUMERIC` | `false` | The ending column for the autofilter (1-based). If not specified, uses all columns with data. |  |


## Examples

Add autofilter to data range:

```js
// Add filter to header row
var spreadsheet = SpreadsheetNew();
SpreadsheetAddRows( spreadsheet, [ 
    [ "Name", "Age", "City" ],
    [ "John", 30, "NYC" ],
    [ "Jane", 25, "LA" ]
] );

SpreadsheetAddAutofilter( spreadsheet, 1, 1, 3, 3 );
```

## Related

- [SpreadsheetAddFreezePane()](./SpreadsheetAddFreezePane.md) - Freeze panes
- [SpreadsheetFormatRow()](./SpreadsheetFormatRow.md) - Format row
- [Data Analysis Guide](../../data-analysis.md) - Data filtering
