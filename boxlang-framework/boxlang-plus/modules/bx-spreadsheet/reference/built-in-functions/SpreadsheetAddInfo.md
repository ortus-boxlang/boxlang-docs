[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddInfo`

Adds metadata information to a spreadsheet object.

## Method Signature

```
SpreadsheetAddInfo(spreadsheetObj=[any], info=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `info` | `STRUCT` | `true` | A structure containing metadata information (author, title, subject, etc.). |  |


## Examples

Add metadata to a spreadsheet:

```js
// Add title and author info
var spreadsheet = SpreadsheetNew();
SpreadsheetAddInfo( spreadsheet, "title", "Sales Report" );
SpreadsheetAddInfo( spreadsheet, "author", "John Doe" );
SpreadsheetAddInfo( spreadsheet, "subject", "Q4 Sales Analysis" );
```

## Related

- [SpreadsheetInfo()](./SpreadsheetInfo.md) - Get spreadsheet information
- [SpreadsheetNew()](./SpreadsheetNew.md) - Create spreadsheet
