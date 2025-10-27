[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddImage`

Adds an image to a spreadsheet.

## Method Signature

```
SpreadsheetAddImage(spreadsheetObj=[any], filepath=[any], row=[any], column=[any], anchor=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `filepath` | `STRING` | `true` | The path to the image file. |  |
| `row` | `NUMERIC` | `false` | The row to place the image (1-based). Default is 1. |  |
| `column` | `NUMERIC` | `false` | The column to place the image (1-based). Default is 1. |  |
| `anchor` | `NUMERIC` | `false` | Anchor type for image positioning. Default is 1. |  |


## Examples

Add image to spreadsheet:

```js
// Insert image at cell A1
var spreadsheet = SpreadsheetNew();
SpreadsheetAddImage( spreadsheet, "/path/to/image.png", 1, 1 );
```

## Related

- [SpreadsheetSetHeaderImage()](./SpreadsheetSetHeaderImage.md) - Add to header
- [SpreadsheetSetFooterImage()](./SpreadsheetSetFooterImage.md) - Add to footer
- [Multimedia Guide](../../multimedia.md) - Working with images
