---
description: Methods for working with Excel formulas and calculations
icon: calculator
---

# 🔢 Formulas

Methods for adding, modifying, and recalculating Excel formulas.

---

## setCellFormula()

Sets a formula in a cell.

**Signature:**
```js
setCellFormula( numeric row, numeric column, string formula )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number
- `formula` (required) - Excel formula (without leading =)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Simple arithmetic
sheet.setCellFormula( 2, 3, "A2*B2" );

// SUM function
sheet.setCellFormula( 10, 1, "SUM(A1:A9)" );

// Complex nested formula
sheet.setCellFormula( 2, 4, 'IF(C2>100,"High","Low")' );

// Absolute references
sheet.setCellFormula( 2, 3, "B2*$D$1" );

// Cross-sheet reference
sheet.setCellFormula( 2, 1, "Sheet2!A1+Sheet2!B1" );
```

---

## getCellFormula()

Gets the formula from a cell.

**Signature:**
```js
getCellFormula( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** String (formula without =) or empty string

**Examples:**

```js
formula = sheet.getCellFormula( 2, 3 );
// Returns: "A2*B2"

// Check if cell has formula
if ( formula.len() > 0 ) {
    writeOutput( "Cell contains formula: #formula#" );
}
```

---

## recalculateAllFormulas()

Forces recalculation of all formulas in the spreadsheet.

**Signature:**
```js
recalculateAllFormulas()
```

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Load, modify data, recalculate
Spreadsheet( "calculations.xlsx", load = true )
    .setCellValue( 1, 1, 100 )  // Update source value
    .recalculateAllFormulas()    // Recalculate dependent formulas
    .save();
```

---

## 💡 Formula Patterns

### SUM Totals

```js
Spreadsheet( "totals.xlsx" )
    .setRowData( 1, [ "Item", "Amount" ] )
    .addRow( [ "Item 1", 100 ] )
    .addRow( [ "Item 2", 200 ] )
    .addRow( [ "Item 3", 150 ] )
    .setRowData( 5, [ "Total", "=SUM(B2:B4)" ] )
    .save();
```

### Conditional Logic

```js
// IF statements
sheet.setCellFormula( 2, 3, 'IF(B2>=90,"A",IF(B2>=80,"B","C"))' );

// SUMIF
sheet.setCellFormula( 10, 1, 'SUMIF(A2:A9,"Widget",B2:B9)' );
```

### Cell References

```js
// Relative (adjusts when copied)
sheet.setCellFormula( 2, 3, "A2*B2" );

// Absolute (fixed)
sheet.setCellFormula( 2, 3, "$A$1*B2" );

// Mixed
sheet.setCellFormula( 2, 3, "$A2*B$1" );
```

### Cross-Sheet Formulas

```js
sheet.createSheet( "Data" )
    .setRowData( 1, [ "Value", 100 ] );

sheet.createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Total", "=Data!B1*2" ] );
```

---

## 📚 See Also

- [Formulas Guide](../../formulas.md) - Complete formula reference
- [Writing Data](writing-data.md)
- [Reading Data](reading-data.md)
