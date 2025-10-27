[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGroupRows`

Groups rows together in a spreadsheet for outline/collapse functionality

## Method Signature

```
SpreadsheetGroupRows()
```

### Arguments

No arguments.

## Examples

Group rows:

```js
// Group rows 2 through 5
var spreadsheet = SpreadsheetNew();
SpreadsheetGroupRows( spreadsheet, 2, 5 );
```

## Related

- [SpreadsheetUngroupRows()](./SpreadsheetUngroupRows.md) - Ungroup rows
- [SpreadsheetGroupColumns()](./SpreadsheetGroupColumns.md) - Group columns
- [Data Organization Guide](../../data-organization.md) - Organizing data
