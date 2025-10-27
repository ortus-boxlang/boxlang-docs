---
description: Methods for merging cells and managing cell comments
icon: comment
---

# 💬 Merging and Comments

Methods for merging cells and adding/managing cell comments.

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
// Merge cells for title
sheet.setCellValue( 1, 1, "Annual Report" )
    .mergeCells( 1, 1, 1, 5 )
    .formatCell( 1, 1, {
        bold: true,
        alignment: "center",
        fontsize: 16
    } );

// Merge vertically
sheet.setCellValue( 2, 1, "Category A" )
    .mergeCells( 2, 1, 5, 1 )
    .formatCell( 2, 1, { verticalalignment: "center" } );
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
// Unmerge title cells
sheet.unmergeCells( 1, 1, 1, 5 );
```

---

## setCellComment()

Adds or updates a comment on a cell.

**Signature:**
```js
setCellComment( numeric row, numeric column, string comment, [string author] )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number
- `comment` (required) - Comment text
- `author` (optional) - Author name

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Simple comment
sheet.setCellComment( 2, 3, "This value needs review" );

// Comment with author
sheet.setCellComment(
    row = 5,
    column = 2,
    comment = "Approved by management",
    author = "John Smith"
);

// Multi-line comment
sheet.setCellComment(
    2, 3,
    "Line 1#chr(10)#Line 2#chr(10)#Line 3"
);
```

---

## getCellComment()

Gets the comment from a cell.

**Signature:**
```js
getCellComment( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** String (comment text) or empty string

**Examples:**

```js
comment = sheet.getCellComment( 2, 3 );

if ( comment.len() > 0 ) {
    writeOutput( "Comment: #comment#" );
}
```

---

## removeCellComment()

Removes a comment from a cell.

**Signature:**
```js
removeCellComment( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet.removeCellComment( 2, 3 );
```

---

## 💡 Usage Patterns

### Report Title

```js
Spreadsheet( "report.xlsx" )
    .setCellValue( 1, 1, "Q4 2024 Sales Report" )
    .mergeCells( 1, 1, 1, 6 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 18,
        alignment: "center",
        fgcolor: "darkblue",
        fontColor: "white"
    } )
    .setRowHeight( 1, 30 )
    .save();
```

### Section Headers

```js
sheet.setCellValue( 2, 1, "Product Information" )
    .mergeCells( 2, 1, 2, 4 )
    .formatCell( 2, 1, {
        bold: true,
        fgcolor: "lightblue",
        alignment: "center"
    } );

sheet.setCellValue( 10, 1, "Pricing Details" )
    .mergeCells( 10, 1, 10, 4 )
    .formatCell( 10, 1, {
        bold: true,
        fgcolor: "lightgreen",
        alignment: "center"
    } );
```

### Data with Comments

```js
sheet.setRowData( 1, [ "Item", "Value", "Status" ] )
    .addRow( [ "Revenue", 100000, "Verified" ] )
    .setCellComment( 2, 2, "Includes Q4 adjustments", "Finance Dept" )
    .addRow( [ "Expenses", 75000, "Pending" ] )
    .setCellComment( 3, 3, "Awaiting final invoices" );
```

### Review Comments

```js
// Add review comments
sheet.setCellComment( 5, 3, "Please verify this calculation" )
    .setCellComment( 8, 2, "Missing source data" );

// Later, remove completed reviews
sheet.removeCellComment( 5, 3 );
```

### Grouped Data

```js
// Merge category labels
sheet.setCellValue( 2, 1, "Hardware" )
    .mergeCells( 2, 1, 5, 1 )
    .formatCell( 2, 1, {
        bold: true,
        verticalalignment: "center",
        alignment: "center",
        fgcolor: "lightgray"
    } );

sheet.setCellValue( 6, 1, "Software" )
    .mergeCells( 6, 1, 9, 1 )
    .formatCell( 6, 1, {
        bold: true,
        verticalalignment: "center",
        alignment: "center",
        fgcolor: "lightgray"
    } );
```

---

## 📚 See Also

- [Writing Data](writing-data.md)
- [Formatting](formatting.md)
- [Advanced Features](advanced-features.md)
