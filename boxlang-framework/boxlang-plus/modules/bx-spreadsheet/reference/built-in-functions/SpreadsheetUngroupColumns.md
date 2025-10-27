[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetUngroupColumns`

Removes column grouping in a spreadsheet

## Method Signature

```
SpreadsheetUngroupColumns()
```

### Arguments

No arguments.

## Examples

Ungroup columns:

```js
// Remove grouping from columns 2-4
var spreadsheet = SpreadsheetNew();
SpreadsheetGroupColumns( spreadsheet, 2, 4 );
SpreadsheetUngroupColumns( spreadsheet, 2, 4 );
```

## Related

- [SpreadsheetGroupColumns()](./SpreadsheetGroupColumns.md) - Group columns
- [SpreadsheetUngroupRows()](./SpreadsheetUngroupRows.md) - Ungroup rows
