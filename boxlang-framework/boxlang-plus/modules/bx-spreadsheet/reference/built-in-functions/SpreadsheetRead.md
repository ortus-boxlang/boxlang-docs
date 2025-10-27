[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetRead`

Reads a sheet from a spreadsheet file and stores it in a BoxLang spreadsheet object.

## Method Signature

```
SpreadsheetRead(src=[any], sheet=[any], format=[any], headerrow=[any], password=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `src` | `STRING` | `true` | The path to the spreadsheet file. * * |  |
| `sheet` | `ANY` | `false` | The name or index of the sheet to read. If not specified, reads the first sheet. * * |  |
| `format` | `STRING` | `false` | The format of the spreadsheet (not used in this implementation as format is auto-detected). * * |  |
| `headerrow` | `NUMERIC` | `false` | The row number to start reading from (1-based). Default is 1. * * |  |
| `password` | `STRING` | `false` | The password for encrypted spreadsheets. * * |  |


## Examples



## Related

