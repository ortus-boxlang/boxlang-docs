---
description: Master Excel formulas - cell references, built-in functions, and complex calculations
icon: calculator
---

# 🔢 Formulas Guide

Learn how to add formulas and calculations to your spreadsheets using the BoxLang Fluent API. This guide covers everything from basic arithmetic to complex Excel functions.

---

## 📝 Formula Basics

### Adding Simple Formulas

```js
Spreadsheet( "calculations.xlsx" )
    .setRowData( 1, [ "Price", "Quantity", "Total" ] )
    .setCellValue( 2, 1, 29.99 )
    .setCellValue( 2, 2, 5 )

    // Add formula
    .setCellFormula( 2, 3, "A2*B2" )

    .save();
```

### Reading Formulas

```js
sheet = Spreadsheet( "with-formulas.xlsx", load = true );

// Get formula text
formula = sheet.getCellFormula( 2, 3 );  // Returns: "A2*B2"

// Get calculated value
value = sheet.getCellValue( 2, 3 );      // Returns: 149.95

// Get cell type
type = sheet.getCellType( 2, 3 );        // Returns: "formula"
```

### Recalculating Formulas

```js
sheet = Spreadsheet( "formulas.xlsx", load = true )
    // Update source data
    .setCellValue( 2, 1, 39.99 )

    // Force recalculation
    .recalculateAllFormulas()

    .save();
```

---

## 🔤 Cell References

### Relative References

```js
Spreadsheet( "relative.xlsx" )
    .setRowData( 1, [ "Item", "Price", "Qty", "Total" ] )
    .addRow( [ "Widget", 29.99, 5 ] )
    .addRow( [ "Gadget", 49.99, 3 ] )
    .addRow( [ "Gizmo", 19.99, 10 ] )

    // Relative references - adjust when copied
    .setCellFormula( 2, 4, "B2*C2" )
    .setCellFormula( 3, 4, "B3*C3" )
    .setCellFormula( 4, 4, "B4*C4" )

    .save();
```

### Absolute References

```js
Spreadsheet( "absolute.xlsx" )
    .setRowData( 1, [ "Tax Rate", 0.08 ] )
    .setRowData( 2, [ "Item", "Price", "Tax", "Total" ] )
    .addRow( [ "Widget", 100 ] )
    .addRow( [ "Gadget", 200 ] )

    // Absolute reference to tax rate ($B$1)
    .setCellFormula( 3, 3, "B3*$B$1" )
    .setCellFormula( 4, 3, "B4*$B$1" )

    // Total with absolute reference
    .setCellFormula( 3, 4, "B3+(B3*$B$1)" )
    .setCellFormula( 4, 4, "B4+(B4*$B$1)" )

    .save();
```

### Mixed References

```js
Spreadsheet( "mixed.xlsx" )
    .setRowData( 1, [ "Multiplier", 2, 3, 4 ] )
    .setRowData( 2, [ "Value", 10 ] )
    .setRowData( 3, [ "Value", 20 ] )

    // Mixed references: $B2 (column fixed), B$1 (row fixed)
    .setCellFormula( 2, 2, "$B2*B$1" )  // 10 * 2 = 20
    .setCellFormula( 2, 3, "$B2*C$1" )  // 10 * 3 = 30
    .setCellFormula( 2, 4, "$B2*D$1" )  // 10 * 4 = 40

    .save();
```

### Range References

```js
Spreadsheet( "ranges.xlsx" )
    .setRowData( 1, [ "Values" ] )
    .addRow( [ 10 ] )
    .addRow( [ 20 ] )
    .addRow( [ 30 ] )
    .addRow( [ 40 ] )
    .setRowData( 6, [ "Sum", "=SUM(A2:A5)" ] )
    .setRowData( 7, [ "Average", "=AVERAGE(A2:A5)" ] )
    .setRowData( 8, [ "Max", "=MAX(A2:A5)" ] )
    .setRowData( 9, [ "Min", "=MIN(A2:A5)" ] )
    .save();
```

---

## ➕ Arithmetic Operations

### Basic Operations

```js
Spreadsheet( "arithmetic.xlsx" )
    .setRowData( 1, [ "Operation", "Formula", "Result" ] )

    // Addition
    .setRowData( 2, [ "Addition", "=10+5" ] )

    // Subtraction
    .setRowData( 3, [ "Subtraction", "=10-5" ] )

    // Multiplication
    .setRowData( 4, [ "Multiplication", "=10*5" ] )

    // Division
    .setRowData( 5, [ "Division", "=10/5" ] )

    // Exponentiation
    .setRowData( 6, [ "Power", "=10^2" ] )

    // Modulo
    .setRowData( 7, [ "Modulo", "=10%3" ] )

    .save();
```

### Order of Operations

```js
Spreadsheet( "order.xlsx" )
    .setRowData( 1, [ "Expression", "Result" ] )

    // Without parentheses
    .setRowData( 2, [ "=2+3*4", "=2+3*4" ] )  // 14 (multiplication first)

    // With parentheses
    .setRowData( 3, [ "=(2+3)*4", "=(2+3)*4" ] )  // 20 (addition first)

    .save();
```

---

## 📊 Common Excel Functions

### SUM Functions

```js
Spreadsheet( "sum.xlsx" )
    .setRowData( 1, [ "Jan", "Feb", "Mar", "Total" ] )
    .addRow( [ 100, 200, 150 ] )

    // Simple SUM
    .setCellFormula( 2, 4, "SUM(A2:C2)" )

    // SUM with multiple ranges
    .setRowData( 3, [ 50, 75, 60 ] )
    .setCellFormula( 3, 4, "SUM(A3:C3)" )
    .setRowData( 4, [ "Total", "", "", "=SUM(D2:D3)" ] )

    .save();
```

### AVERAGE, MIN, MAX

```js
Spreadsheet( "stats.xlsx" )
    .setRowData( 1, [ "Values" ] )
    .addRow( [ 85 ] )
    .addRow( [ 92 ] )
    .addRow( [ 78 ] )
    .addRow( [ 95 ] )
    .addRow( [ 88 ] )

    .setRowData( 7, [ "Average", "=AVERAGE(A2:A6)" ] )
    .setRowData( 8, [ "Minimum", "=MIN(A2:A6)" ] )
    .setRowData( 9, [ "Maximum", "=MAX(A2:A6)" ] )
    .setRowData( 10, [ "Count", "=COUNT(A2:A6)" ] )

    .save();
```

### COUNT Functions

```js
Spreadsheet( "counting.xlsx" )
    .setRowData( 1, [ "Data" ] )
    .addRow( [ 10 ] )
    .addRow( [ "" ] )
    .addRow( [ 20 ] )
    .addRow( [ "Text" ] )
    .addRow( [ 30 ] )

    // COUNT - counts numbers only
    .setRowData( 7, [ "Numbers", "=COUNT(A2:A6)" ] )  // 3

    // COUNTA - counts non-empty cells
    .setRowData( 8, [ "Non-Empty", "=COUNTA(A2:A6)" ] )  // 4

    // COUNTBLANK - counts empty cells
    .setRowData( 9, [ "Empty", "=COUNTBLANK(A2:A6)" ] )  // 1

    .save();
```

### IF Function

```js
Spreadsheet( "if-function.xlsx" )
    .setRowData( 1, [ "Score", "Grade" ] )
    .addRow( [ 95 ] )
    .addRow( [ 82 ] )
    .addRow( [ 67 ] )
    .addRow( [ 55 ] )

    // Simple IF
    .setCellFormula( 2, 2, 'IF(A2>=90,"A","B")' )

    // Nested IF
    .setCellFormula( 3, 2, 'IF(A3>=90,"A",IF(A3>=80,"B","C"))' )
    .setCellFormula( 4, 2, 'IF(A4>=90,"A",IF(A4>=80,"B",IF(A4>=70,"C","F")))' )
    .setCellFormula( 5, 2, 'IF(A5>=90,"A",IF(A5>=80,"B",IF(A5>=70,"C","F")))' )

    .save();
```

### SUMIF and COUNTIF

```js
Spreadsheet( "conditional.xlsx" )
    .setRowData( 1, [ "Product", "Sales", "Region" ] )
    .addRow( [ "Widget", 100, "North" ] )
    .addRow( [ "Gadget", 200, "South" ] )
    .addRow( [ "Widget", 150, "North" ] )
    .addRow( [ "Gizmo", 175, "North" ] )
    .addRow( [ "Widget", 125, "South" ] )

    // SUMIF - sum where condition is met
    .setRowData( 7, [ "Widget Total", '=SUMIF(A2:A6,"Widget",B2:B6)' ] )

    // COUNTIF - count where condition is met
    .setRowData( 8, [ "Widget Count", '=COUNTIF(A2:A6,"Widget")' ] )

    // SUMIF with comparison
    .setRowData( 9, [ "Sales > 150", "=SUMIF(B2:B6,"">150"",B2:B6)" ] )

    .save();
```

### VLOOKUP

```js
Spreadsheet( "vlookup.xlsx" );

// Lookup table
sheet.createSheet( "Products" )
    .setRowData( 1, [ "ID", "Name", "Price" ] )
    .addRow( [ 1, "Widget", 29.99 ] )
    .addRow( [ 2, "Gadget", 49.99 ] )
    .addRow( [ 3, "Gizmo", 19.99 ] );

// Order sheet with lookups
sheet.createAndSelectSheet( "Orders" )
    .setRowData( 1, [ "Product ID", "Product Name", "Price", "Quantity", "Total" ] )
    .addRow( [ 2 ] )
    .addRow( [ 1 ] )
    .addRow( [ 3 ] );

// VLOOKUP formulas
// Lookup name
sheet.setCellFormula( 2, 2, "VLOOKUP(A2,Products!A:C,2,FALSE)" )
    // Lookup price
    .setCellFormula( 2, 3, "VLOOKUP(A2,Products!A:C,3,FALSE)" )
    // Set quantity
    .setCellValue( 2, 4, 5 )
    // Calculate total
    .setCellFormula( 2, 5, "C2*D2" );

// Repeat for other rows
sheet.setCellFormula( 3, 2, "VLOOKUP(A3,Products!A:C,2,FALSE)" )
    .setCellFormula( 3, 3, "VLOOKUP(A3,Products!A:C,3,FALSE)" )
    .setCellValue( 3, 4, 3 )
    .setCellFormula( 3, 5, "C3*D3" );

sheet.save();
```

### TEXT Functions

```js
Spreadsheet( "text-functions.xlsx" )
    .setRowData( 1, [ "Text", "Upper", "Lower", "Length", "Concatenate" ] )
    .addRow( [ "Hello World" ] )

    // UPPER - convert to uppercase
    .setCellFormula( 2, 2, "UPPER(A2)" )

    // LOWER - convert to lowercase
    .setCellFormula( 2, 3, "LOWER(A2)" )

    // LEN - get length
    .setCellFormula( 2, 4, "LEN(A2)" )

    // CONCATENATE or & operator
    .setCellFormula( 2, 5, 'CONCATENATE(A2," - ","Modified")' )

    .save();
```

### DATE Functions

```js
Spreadsheet( "date-functions.xlsx" )
    .setRowData( 1, [ "Function", "Result" ] )

    // TODAY - current date
    .setRowData( 2, [ "Today", "=TODAY()" ] )

    // NOW - current date and time
    .setRowData( 3, [ "Now", "=NOW()" ] )

    // DATE - create specific date
    .setRowData( 4, [ "Custom Date", "=DATE(2024,12,25)" ] )

    // YEAR, MONTH, DAY
    .setRowData( 5, [ "Year", "=YEAR(TODAY())" ] )
    .setRowData( 6, [ "Month", "=MONTH(TODAY())" ] )
    .setRowData( 7, [ "Day", "=DAY(TODAY())" ] )

    // Date arithmetic
    .setRowData( 8, [ "30 Days Later", "=TODAY()+30" ] )
    .setRowData( 9, [ "Days Between", "=DATE(2024,12,31)-TODAY()" ] )

    .save();
```

---

## 🔗 Cross-Sheet Formulas

### Referencing Other Sheets

```js
sheet = Spreadsheet( "cross-sheet.xlsx" );

// Data sheet
sheet.createSheet( "Data" )
    .setRowData( 1, [ "Revenue", 100000 ] )
    .setRowData( 2, [ "Expenses", 75000 ] );

// Summary sheet with formulas
sheet.createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Revenue", "=Data!B1" ] )
    .setRowData( 2, [ "Expenses", "=Data!B2" ] )
    .setRowData( 3, [ "Profit", "=B1-B2" ] );

sheet.save();
```

### Complex Cross-Sheet Calculations

```js
sheet = Spreadsheet( "quarterly.xlsx" );

// Q1 Data
sheet.createSheet( "Q1" )
    .setRowData( 1, [ "Month", "Sales" ] )
    .addRow( [ "Jan", 10000 ] )
    .addRow( [ "Feb", 12000 ] )
    .addRow( [ "Mar", 11000 ] );

// Q2 Data
sheet.createSheet( "Q2" )
    .setRowData( 1, [ "Month", "Sales" ] )
    .addRow( [ "Apr", 13000 ] )
    .addRow( [ "May", 14000 ] )
    .addRow( [ "Jun", 12500 ] );

// Summary with cross-sheet formulas
sheet.createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Quarter", "Total Sales" ] )
    .setRowData( 2, [ "Q1", "=SUM(Q1!B2:B4)" ] )
    .setRowData( 3, [ "Q2", "=SUM(Q2!B2:B4)" ] )
    .setRowData( 4, [ "Total", "=SUM(B2:B3)" ] );

sheet.save();
```

---

## 🎯 Formula Patterns

### Running Totals

```js
Spreadsheet( "running-total.xlsx" )
    .setRowData( 1, [ "Date", "Amount", "Running Total" ] )
    .addRow( [ "2024-01-01", 100 ] )
    .addRow( [ "2024-01-02", 150 ] )
    .addRow( [ "2024-01-03", 75 ] )
    .addRow( [ "2024-01-04", 200 ] )

    // First running total
    .setCellFormula( 2, 3, "B2" )

    // Subsequent running totals
    .setCellFormula( 3, 3, "C2+B3" )
    .setCellFormula( 4, 3, "C3+B4" )
    .setCellFormula( 5, 3, "C4+B5" )

    .save();
```

### Percentage Calculations

```js
Spreadsheet( "percentages.xlsx" )
    .setRowData( 1, [ "Product", "Sales", "% of Total" ] )
    .addRow( [ "Widget", 1000 ] )
    .addRow( [ "Gadget", 1500 ] )
    .addRow( [ "Gizmo", 500 ] )
    .setRowData( 5, [ "Total", "=SUM(B2:B4)" ] )

    // Percentage of total (with absolute reference to total)
    .setCellFormula( 2, 3, "B2/$B$5" )
    .setCellFormula( 3, 3, "B3/$B$5" )
    .setCellFormula( 4, 3, "B4/$B$5" )

    // Format as percentage
    .formatColumn( 3, { dataformat: "0.0%" } )

    .save();
```

### Variance Analysis

```js
Spreadsheet( "variance.xlsx" )
    .setRowData( 1, [ "Item", "Budget", "Actual", "Variance", "% Variance" ] )
    .addRow( [ "Revenue", 100000, 105000 ] )
    .addRow( [ "Salaries", 50000, 52000 ] )
    .addRow( [ "Marketing", 10000, 9500 ] )

    // Variance (Actual - Budget)
    .setCellFormula( 2, 4, "C2-B2" )
    .setCellFormula( 3, 4, "C3-B3" )
    .setCellFormula( 4, 4, "C4-B4" )

    // % Variance
    .setCellFormula( 2, 5, "D2/B2" )
    .setCellFormula( 3, 5, "D3/B3" )
    .setCellFormula( 4, 5, "D4/B4" )

    // Format
    .formatColumn( 5, { dataformat: "0.0%" } )
    .formatColumns( "2-4", { dataformat: "$#,##0" } )

    .save();
```

### Ranking

```js
Spreadsheet( "ranking.xlsx" )
    .setRowData( 1, [ "Student", "Score", "Rank" ] )
    .addRow( [ "John", 95 ] )
    .addRow( [ "Jane", 88 ] )
    .addRow( [ "Bob", 92 ] )
    .addRow( [ "Alice", 97 ] )

    // RANK function
    .setCellFormula( 2, 3, "RANK(B2,$B$2:$B$5)" )
    .setCellFormula( 3, 3, "RANK(B3,$B$2:$B$5)" )
    .setCellFormula( 4, 3, "RANK(B4,$B$2:$B$5)" )
    .setCellFormula( 5, 3, "RANK(B5,$B$2:$B$5)" )

    .save();
```

---

## 🔧 Formula Helpers

### Using BoxLang to Generate Formulas

```js
// Generate SUM formulas for multiple rows
sheet = Spreadsheet( "generated.xlsx" )
    .setRowData( 1, [ "Q1", "Q2", "Q3", "Q4", "Total" ] );

// Add data rows
for ( i = 1; i <= 5; i++ ) {
    row = [
        randRange( 1000, 2000 ),
        randRange( 1000, 2000 ),
        randRange( 1000, 2000 ),
        randRange( 1000, 2000 )
    ];
    sheet.addRow( row );

    // Add SUM formula
    rowNum = i + 1;
    sheet.setCellFormula( rowNum, 5, "SUM(A#rowNum#:D#rowNum#)" );
}

sheet.save();
```

### Dynamic Range Formulas

```js
// Create formula with dynamic range based on data
data = [
    [ "Product A", 100 ],
    [ "Product B", 200 ],
    [ "Product C", 150 ]
];

sheet = Spreadsheet( "dynamic.xlsx" )
    .setRowData( 1, [ "Product", "Sales" ] )
    .addRows( data );

// Calculate last row
lastRow = data.len() + 1;

// Add total with dynamic range
sheet.setRowData( lastRow + 1, [ "Total", "=SUM(B2:B#lastRow#)" ] );

sheet.save();
```

---

## ⚠️ Formula Tips

### String Escaping in Formulas

When formulas contain quotes, use proper escaping:

```js
// Use single quotes inside double-quoted strings
sheet.setCellFormula( 1, 1, 'IF(A1>10,"Pass","Fail")' );

// Or escape double quotes
sheet.setCellFormula( 1, 1, "IF(A1>10,""Pass"",""Fail"")" );
```

### Error Handling

```js
Spreadsheet( "error-handling.xlsx" )
    .setRowData( 1, [ "Value", "Divided by", "Result" ] )
    .addRow( [ 100, 5 ] )
    .addRow( [ 100, 0 ] )  // Will cause #DIV/0! error

    // Without error handling
    .setCellFormula( 2, 3, "A2/B2" )  // Works
    .setCellFormula( 3, 3, "A3/B3" )  // #DIV/0! error

    // With IFERROR
    .setCellFormula( 4, 3, 'IFERROR(A3/B3,"Cannot divide by zero")' )

    .save();
```

### Array Formulas

Some Excel formulas work with arrays:

```js
Spreadsheet( "arrays.xlsx" )
    .setRowData( 1, [ "Values", "Squared" ] )
    .addRow( [ 2 ] )
    .addRow( [ 3 ] )
    .addRow( [ 4 ] )

    // Individual formulas
    .setCellFormula( 2, 2, "A2^2" )
    .setCellFormula( 3, 2, "A3^2" )
    .setCellFormula( 4, 2, "A4^2" )

    .save();
```

---

## 📚 Next Steps

{% content-ref url="advanced-features.md" %}
[advanced-features.md](advanced-features.md)
{% endcontent-ref %}

{% content-ref url="examples.md" %}
[examples.md](examples.md)
{% endcontent-ref %}

{% content-ref url="reference/fluent-api/" %}
[fluent-api](reference/fluent-api/)
{% endcontent-ref %}
