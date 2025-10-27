---
description: Methods for managing column widths and row heights
icon: arrows-left-right
---

# 📏 Sizing

Methods for controlling column widths, row heights, and auto-sizing.

---

## setColumnWidth()

Sets the width of one or more columns.

**Signature:**
```js
setColumnWidth( any column, numeric width )
```

**Parameters:**
- `column` (required) - Column number or range string (e.g., "2-5")
- `width` (required) - Width in characters

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Single column
sheet.setColumnWidth( 1, 20 );

// Multiple columns
sheet.setColumnWidth( "2-5", 15 );

// Specific columns
sheet.setColumnWidth( "1,3,5", 25 );
```

---

## setRowHeight()

Sets the height of a row.

**Signature:**
```js
setRowHeight( numeric row, numeric height )
```

**Parameters:**
- `row` (required) - Row number
- `height` (required) - Height in points

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Make header row taller
sheet.setRowHeight( 1, 25 );

// Extra tall row
sheet.setRowHeight( 5, 50 );
```

---

## autoSizeColumns()

Automatically sizes columns to fit their content.

**Signature:**
```js
autoSizeColumns( [array columnNumbers] )
```

**Parameters:**
- `columnNumbers` (optional) - Array of column numbers to auto-size (defaults to all columns)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Auto-size all columns
sheet.autoSizeColumns();

// Auto-size specific columns
sheet.autoSizeColumns( [ 1, 2, 3 ] );
```

---

## hideColumn()

Hides a column from view.

**Signature:**
```js
hideColumn( numeric columnNumber )
```

**Parameters:**
- `columnNumber` (required) - Column to hide

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Hide column 2
sheet.hideColumn( 2 );
```

---

## showColumn()

Shows a previously hidden column.

**Signature:**
```js
showColumn( numeric columnNumber )
```

**Parameters:**
- `columnNumber` (required) - Column to show

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Show column 2
sheet.showColumn( 2 );
```

---

## hideRow()

Hides a row from view.

**Signature:**
```js
hideRow( numeric rowNumber )
```

**Parameters:**
- `rowNumber` (required) - Row to hide

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Hide row 3
sheet.hideRow( 3 );
```

---

## showRow()

Shows a previously hidden row.

**Signature:**
```js
showRow( numeric rowNumber )
```

**Parameters:**
- `rowNumber` (required) - Row to show

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Show row 3
sheet.showRow( 3 );
```

---

## 💡 Usage Patterns

### Professional Layout

```js
Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Name", "Department", "Salary" ] )
    .addRow( [ "John Doe", "Engineering", 95000 ] )
    // Make header tall
    .setRowHeight( 1, 25 )
    // Set column widths
    .setColumnWidth( 1, 25 )
    .setColumnWidth( 2, 20 )
    .setColumnWidth( 3, 15 )
    .save();
```

### Auto-sizing Best Practice

```js
// Add all data first, then auto-size
Spreadsheet( "data.xlsx" )
    .setRowData( 1, headers )
    .addRows( data )
    .formatRow( 1, { bold: true } )
    .autoSizeColumns()  // Call once at end
    .save();
```

### Hidden Columns

```js
// Hide sensitive data column
sheet.setRowData( 1, [ "Name", "SSN", "Salary" ] )
    .addRows( employees )
    .hideColumn( 2 )  // Hide SSN column
    .save();
```

---

## 📚 See Also

- [Formatting](formatting.md)
- [User Guide - Sizing](../../user-guide.md#column-widths)
