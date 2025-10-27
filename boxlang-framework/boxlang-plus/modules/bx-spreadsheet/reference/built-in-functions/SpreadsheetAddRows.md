[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddRows`

Adds multiple rows from a query to an Excel spreadsheet object.

## Method Signature

```
SpreadsheetAddRows(spreadsheetObj=[any], data=[any], row=[any], column=[any], insert=[any], datatype=[any], includeColumnNames=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. * * |  |
| `data` | `ANY` | `true` | The data to add - can be an array of arrays or an array of structs. * * |  |
| `row` | `NUMERIC` | `false` | The row number where to start inserting the data (1-based). If not specified, adds to the end. * * |  |
| `column` | `NUMERIC` | `false` | The column number where to start inserting the data (1-based). Default is 1. * * |  |
| `insert` | `BOOLEAN` | `false` | Whether to insert new rows or overwrite existing rows. Default is false. * * | true |
| `datatype` | `BOOLEAN` | `false` | The data type to apply to the cells (not implemented in this version). * * | false |
| `includeColumnNames` | `any` | `false` | Whether to include column names as the first row. Default is false. * * |  |


## Examples



## Related

