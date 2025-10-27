[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Spreadsheet`

Work with spreadsheet files

## Method Signature

```
Spreadsheet(path=[any], sheetname=[any], xmlformat=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `path` | `STRING` | `false` | The path to the spreadsheet file to load or the path where the spreadsheet file will be stored at |  |
| `sheetname` | `STRING` | `false` | The name of the sheet to work with (optional). Default is "Sheet1". |  |
| `xmlformat` | `BOOLEAN` | `false` | Whether the spreadsheet should use XML format (.xlsx). Default is true. | true |


## Examples

Work with the fluent API SpreadsheetFile class:

```js
// Using fluent API for method chaining
var sheet = new SpreadsheetFile()
    .createSheet( "Sales" )
    .addRow( [ "Date", "Amount" ] )
    .addRow( [ "2024-01-01", 1500 ] )
    .addRow( [ "2024-01-02", 2000 ] )
    .formatRow( 1, { bold = true, background = "CCCCCC" } );
```

Convert between BIF and fluent APIs:

```js
// BIF approach
var bifSheet = SpreadsheetNew();

// Fluent approach
var fluentSheet = new SpreadsheetFile();

// Both work with same operations
```

## Related

- [SpreadsheetNew()](./SpreadsheetNew.md) - Create with BIF approach
- [Fluent API Guide](../../api-usage.md) - Method chaining reference
