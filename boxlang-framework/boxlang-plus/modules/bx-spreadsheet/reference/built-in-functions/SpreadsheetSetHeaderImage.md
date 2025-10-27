[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetHeaderImage`

Adds an image to the header of a spreadsheet.

## Method Signature

```
SpreadsheetSetHeaderImage(spreadsheetObj=[any], alignment=[any], image=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `alignment` | `STRING` | `true` | The image's alignment in the header. Values: left, center, right. |  |
| `image` | `STRING` | `true` | The filepath of the image to add. |  |


## Examples

Add image to header:

```js
// Add logo to header
var spreadsheet = SpreadsheetNew();
SpreadsheetSetHeaderImage( spreadsheet, "/path/to/logo.png" );
```

## Related

- [SpreadsheetSetHeader()](./SpreadsheetSetHeader.md) - Set text header
- [SpreadsheetSetFooterImage()](./SpreadsheetSetFooterImage.md) - Add image to footer
- [SpreadsheetAddImage()](./SpreadsheetAddImage.md) - Add image to sheet
