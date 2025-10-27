[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetRemoveColumnBreak`

Removes a page (column) break on the active sheet at the given column

## Method Signature

```
SpreadsheetRemoveColumnBreak(spreadsheetObj=[any], column=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `column` | `NUMERIC` | `true` | The column number (1-based). |  |


## Examples

Remove a column page break:

```js
// Remove page break
var spreadsheet = SpreadsheetNew();
SpreadsheetSetColumnBreak( spreadsheet, 5 );
SpreadsheetRemoveColumnBreak( spreadsheet, 5 );
```

## Related

- [SpreadsheetSetColumnBreak()](./SpreadsheetSetColumnBreak.md) - Set column break
- [SpreadsheetRemoveRowBreak()](./SpreadsheetRemoveRowBreak.md) - Remove row break
