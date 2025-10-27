[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetSetFooterImage`

Adds an image to the footer of a spreadsheet.

## Method Signature

```
SpreadsheetSetFooterImage(spreadsheetObj=[any], alignment=[any], image=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `alignment` | `STRING` | `true` | The image's alignment in the footer. Values: left, center, right. |  |
| `image` | `STRING` | `true` | The filepath of the image to add. |  |


## Examples

Add image to footer:

```js
// Add image to footer
var spreadsheet = SpreadsheetNew();
SpreadsheetSetFooterImage( spreadsheet, "/path/to/image.png" );
```

## Related

- [SpreadsheetSetFooter()](./SpreadsheetSetFooter.md) - Set text footer
- [SpreadsheetSetHeaderImage()](./SpreadsheetSetHeaderImage.md) - Add header image
- [SpreadsheetAddImage()](./SpreadsheetAddImage.md) - Add image to sheet
