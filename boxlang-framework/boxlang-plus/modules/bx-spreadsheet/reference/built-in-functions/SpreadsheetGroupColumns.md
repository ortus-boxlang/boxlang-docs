[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetGroupColumns`

Groups columns together in a spreadsheet for outline/collapse functionality

## Method Signature

```
SpreadsheetGroupColumns()
```

### Arguments

No arguments.

## Examples

Group columns:

```js
// Group columns 2 through 4
var spreadsheet = SpreadsheetNew();
SpreadsheetGroupColumns( spreadsheet, 2, 4 );
```

## Related

- [SpreadsheetUngroupColumns()](./SpreadsheetUngroupColumns.md) - Ungroup
- [SpreadsheetGroupRows()](./SpreadsheetGroupRows.md) - Group rows
- [Data Organization Guide](../../data-organization.md) - Organizing data
