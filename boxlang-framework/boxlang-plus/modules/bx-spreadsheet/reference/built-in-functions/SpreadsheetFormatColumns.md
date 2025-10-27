[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetFormatColumns`

Formats multiple columns of an Excel spreadsheet object.

## Method Signature

```
SpreadsheetFormatColumns(spreadsheetObj=[any], format=[any], columns=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. * * |  |
| `format` | `STRUCT` | `true` | A structure containing formatting options (bold, italic, color, etc.). * * |  |
| `columns` | `STRING` | `true` | The columns to format, in one of the following formats: * - startColumn-endColumn for a range (e.g., "1-5") * - column,column,column for individual columns (e.g., "1,3,5") * - combinations like "1-3,5,7-10" * * |  |


## Examples



## Related

