---
description: Methods for images, freeze panes, merging cells, and advanced operations
icon: sparkles
---

# ✨ Advanced Features

Methods for working with images, freezing panes, merging cells, and other advanced spreadsheet capabilities.

---

## addImage()

Adds an image to the spreadsheet.

**Signature:**
```js
addImage( string imagePath, numeric row, numeric column, [numeric width], [numeric height] )
```

**Parameters:**
- `imagePath` (required) - Path to image file (PNG, JPG, GIF)
- `row` (required) - Row to place image (1-based)
- `column` (required) - Column to place image (1-based)
- `width` (optional) - Image width in pixels
- `height` (optional) - Image height in pixels

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Add with original size
sheet.addImage( "/path/to/logo.png", 1, 1 );

// Add with specific dimensions
sheet.addImage(
    imagePath = "/path/to/chart.png",
    row = 5,
    column = 2,
    width = 400,
    height = 300
);
```

---

## freezePanes()

Freezes rows and/or columns to keep them visible during scrolling.

**Signature:**
```js
freezePanes( numeric freezeRow, [numeric freezeColumn] )
```

**Parameters:**
- `freezeRow` (required) - Row number to freeze above (0 = no freeze)
- `freezeColumn` (optional) - Column number to freeze left of (0 = no freeze)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Freeze top row (header)
sheet.freezePanes( 1 );

// Freeze first column
sheet.freezePanes( 0, 1 );

// Freeze both top row and first column
sheet.freezePanes( 1, 1 );
```

---

## mergeCells()

Merges a range of cells into a single cell.

**Signature:**
```js
mergeCells( numeric startRow, numeric startColumn, numeric endRow, numeric endColumn )
```

**Parameters:**
- `startRow` (required) - Starting row
- `startColumn` (required) - Starting column
- `endRow` (required) - Ending row
- `endColumn` (required) - Ending column

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Merge cells for header
sheet.setCellValue( 1, 1, "Report Title" )
    .mergeCells( 1, 1, 1, 5 )
    .formatCell( 1, 1, {
        bold: true,
        alignment: "center",
        fontsize: 16
    } );
```

---

## unmergeCells()

Unmerges previously merged cells.

**Signature:**
```js
unmergeCells( numeric startRow, numeric startColumn, numeric endRow, numeric endColumn )
```

**Parameters:**
Same as `mergeCells()`

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet.unmergeCells( 1, 1, 1, 5 );
```

---

## setRepeatingRows()

Sets rows to repeat at the top of each printed page.

**Signature:**
```js
setRepeatingRows( numeric startRow, numeric endRow )
```

**Parameters:**
- `startRow` (required) - First row to repeat
- `endRow` (required) - Last row to repeat

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Repeat header row on every page
sheet.setRepeatingRows( 1, 1 );
```

---

## setRepeatingColumns()

Sets columns to repeat at the left of each printed page.

**Signature:**
```js
setRepeatingColumns( numeric startColumn, numeric endColumn )
```

**Parameters:**
- `startColumn` (required) - First column to repeat
- `endColumn` (required) - Last column to repeat

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Repeat first column on every page
sheet.setRepeatingColumns( 1, 1 );
```

---

## setPrintArea()

Defines which cells should be printed.

**Signature:**
```js
setPrintArea( numeric startRow, numeric startColumn, numeric endRow, numeric endColumn )
```

**Parameters:**
- `startRow` (required) - Starting row
- `startColumn` (required) - Starting column
- `endRow` (required) - Ending row
- `endColumn` (required) - Ending column

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Set print area to exclude working columns
sheet.setPrintArea( 1, 1, 100, 5 );
```

---

## 💡 Usage Patterns

### Report with Logo

```js
Spreadsheet( "report.xlsx" )
    .addImage( "/path/to/logo.png", 1, 1, 150, 50 )
    .setCellValue( 1, 3, "Quarterly Report" )
    .formatCell( 1, 3, { bold: true, fontsize: 18 } )
    .setRowData( 3, [ "Item", "Q1", "Q2", "Q3", "Q4" ] )
    .formatRow( 3, { bold: true } )
    .freezePanes( 3 )
    .save();
```

### Merged Header

```js
sheet.setCellValue( 1, 1, "Sales Report - Q1 2024" )
    .mergeCells( 1, 1, 1, 6 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 16,
        alignment: "center",
        fgcolor: "darkblue",
        fontColor: "white"
    } );
```

### Printable Report

```js
sheet.setRowData( 1, headers )
    .formatRow( 1, { bold: true } )
    .addRows( data )
    // Freeze header
    .freezePanes( 1 )
    // Repeat header on each page
    .setRepeatingRows( 1, 1 )
    // Set print area
    .setPrintArea( 1, 1, 100, 6 )
    .save();
```

### Dashboard with Charts

```js
sheet.setCellValue( 1, 1, "Sales Dashboard" )
    .mergeCells( 1, 1, 1, 4 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 18,
        alignment: "center"
    } )
    // Add chart images
    .addImage( "/charts/sales-trend.png", 3, 1, 400, 250 )
    .addImage( "/charts/by-region.png", 3, 5, 400, 250 )
    .addImage( "/charts/by-product.png", 15, 1, 400, 250 )
    .save();
```

---

## 📚 See Also

- [Advanced Features Guide](../../advanced-features.md)
- [Formatting](formatting.md)
- [User Guide - Advanced Operations](../../user-guide.md#advanced-operations)
