[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddRow`

Adds a row to an Excel spreadsheet object.

## Method Signature

```
SpreadsheetAddRow(spreadsheetObj=[any], data=[any], row=[any], column=[any], insert=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. * * |  |
| `data` | `ANY` | `true` | An array of data to add to the row, or a comma delimited string of cell entries, one per column * * |  |
| `row` | `NUMERIC` | `false` | The row number where to insert the data (1-based). If not specified, adds to the end. * * |  |
| `column` | `NUMERIC` | `false` | The column number where to start inserting the data (1-based). Default is 1. * * |  |
| `insert` | `BOOLEAN` | `false` | Whether to insert a new row or overwrite existing row. Default is false. * * | true |


## Examples



## Related

