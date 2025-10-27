---
description: Methods for formatting cells, rows, columns, and ranges
icon: paintbrush
---

# 🎨 Formatting

Methods for styling spreadsheet cells with fonts, colors, borders, alignment, and data formats.

---

## formatCell()

Applies formatting to a specific cell.

**Signature:**
```js
formatCell( numeric row, numeric column, struct format )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number
- `format` (required) - Struct of format options

**Returns:** `SpreadsheetFile` (chainable)

**Format Options:**
```js
{
    bold: boolean,
    italic: boolean,
    underline: boolean,
    strikeout: boolean,
    font: string,           // Font name (e.g., "Arial")
    fontsize: numeric,      // Font size in points
    fontColor: string,      // Named color or hex (#RRGGBB)
    fgcolor: string,        // Background color
    bgcolor: string,        // Alias for fgcolor
    alignment: string,      // "left", "center", "right", "justify"
    verticalalignment: string, // "top", "center", "bottom"
    dataformat: string,     // Excel format code
    wraptext: boolean,
    leftborder: string,     // "thin", "medium", "thick", "none"
    rightborder: string,
    topborder: string,
    bottomborder: string,
    leftbordercolor: string,
    rightbordercolor: string,
    topbordercolor: string,
    bottombordercolor: string
}
```

**Examples:**

```js
Spreadsheet( "styled.xlsx" )
    .setCellValue( 1, 1, "Bold Header" )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 14,
        fgcolor: "blue",
        fontColor: "white",
        alignment: "center"
    } )
    .save();

// Currency format
sheet.setCellValue( 2, 1, 1234.56 )
    .formatCell( 2, 1, {
        dataformat: "$#,##0.00"
    } );
```

---

## formatRow()

Applies formatting to an entire row.

**Signature:**
```js
formatRow( numeric rowNumber, struct format )
```

**Parameters:**
- `rowNumber` (required) - Row to format
- `format` (required) - Struct of format options (same as formatCell)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Name", "Value", "Status" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white",
        alignment: "center"
    } )
    .save();
```

---

## formatColumn()

Applies formatting to an entire column.

**Signature:**
```js
formatColumn( numeric columnNumber, struct format )
```

**Parameters:**
- `columnNumber` (required) - Column to format
- `format` (required) - Struct of format options

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "financial.xlsx" )
    .setRowData( 1, [ "Item", "Amount" ] )
    .addRow( [ "Revenue", 100000 ] )
    // Format currency column
    .formatColumn( 2, {
        dataformat: "$#,##0.00",
        alignment: "right"
    } )
    .save();
```

---

## formatColumns()

Applies formatting to multiple columns.

**Signature:**
```js
formatColumns( string columnRange, struct format )
```

**Parameters:**
- `columnRange` (required) - Range string (e.g., "2-5" or "1,3,5")
- `format` (required) - Struct of format options

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Format range of columns
sheet.formatColumns( "2-5", {
    dataformat: "#,##0",
    alignment: "right"
} );

// Format specific columns
sheet.formatColumns( "1,3,5", {
    bold: true
} );
```

---

## formatCellRange()

Applies formatting to a range of cells.

**Signature:**
```js
formatCellRange( numeric startRow, numeric startColumn, numeric endRow, numeric endColumn, struct format )
```

**Parameters:**
- `startRow` (required) - Starting row
- `startColumn` (required) - Starting column
- `endRow` (required) - Ending row
- `endColumn` (required) - Ending column
- `format` (required) - Struct of format options

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet.formatCellRange(
    startRow = 2,
    startColumn = 2,
    endRow = 10,
    endColumn = 5,
    format = {
        fgcolor: "lightgray",
        dataformat: "#,##0"
    }
);
```

---

## 💡 Common Format Patterns

### Header Row

```js
sheet.formatRow( 1, {
    bold: true,
    fgcolor: "darkblue",
    fontColor: "white",
    alignment: "center"
} );
```

### Currency Column

```js
sheet.formatColumn( 3, {
    dataformat: "$#,##0.00",
    alignment: "right"
} );
```

### Date Column

```js
sheet.formatColumn( 4, {
    dataformat: "mm/dd/yyyy"
} );
```

### Percentage

```js
sheet.formatColumn( 5, {
    dataformat: "0.0%"
} );
```

### Bordered Table

```js
sheet.formatCellRange( 1, 1, 10, 5, {
    leftborder: "thin",
    rightborder: "thin",
    topborder: "thin",
    bottomborder: "thin"
} );
```

---

## 📚 See Also

- [Formatting Guide](../../formatting.md) - Complete formatting reference
- [Sizing](sizing.md) - Column widths and row heights
