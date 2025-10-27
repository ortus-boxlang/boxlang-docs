[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetUngroupRows`

Removes row grouping in a spreadsheet

## Method Signature

```
SpreadsheetUngroupRows()
```

### Arguments

No arguments.

## Examples

Ungroup rows:

```js
// Remove grouping from rows 2-5
var spreadsheet = SpreadsheetNew();
SpreadsheetGroupRows( spreadsheet, 2, 5 );
SpreadsheetUngroupRows( spreadsheet, 2, 5 );
```

## Related

- [SpreadsheetGroupRows()](./SpreadsheetGroupRows.md) - Group rows
- [SpreadsheetUngroupColumns()](./SpreadsheetUngroupColumns.md) - Ungroup columns
