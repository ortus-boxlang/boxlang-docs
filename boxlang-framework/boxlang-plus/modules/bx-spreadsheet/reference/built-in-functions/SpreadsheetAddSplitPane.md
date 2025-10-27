[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddSplitPane`

Adds a split pane to a spreadsheet.

## Method Signature

```
SpreadsheetAddSplitPane(spreadsheetObj=[any], xSplitPos=[any], ySplitPos=[any], leftmostColumn=[any], topRow=[any], activePane=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `xSplitPos` | `NUMERIC` | `true` | The horizontal position of the split in pixels. |  |
| `ySplitPos` | `NUMERIC` | `true` | The vertical position of the split in pixels. |  |
| `leftmostColumn` | `NUMERIC` | `false` | The leftmost column visible in right pane (0-based). Default is 0. |  |
| `topRow` | `NUMERIC` | `false` | The top row visible in bottom pane (0-based). Default is 0. |  |
| `activePane` | `NUMERIC` | `false` | The active pane. Default is 0. |  |


## Examples

Add split pane to spreadsheet:

```js
// Split view into panes
var spreadsheet = SpreadsheetNew();
SpreadsheetAddSplitPane( spreadsheet, 3, 2 );
```

## Related

- [SpreadsheetAddFreezePane()](./SpreadsheetAddFreezePane.md) - Freeze panes
- [SpreadsheetSetActiveCell()](./SpreadsheetSetActiveCell.md) - Set active cell
