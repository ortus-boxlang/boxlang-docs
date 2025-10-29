---
description: Comprehensive guide to using the BoxLang Spreadsheet Module with the Fluent API
icon: book
---

# 📖 User Guide

This comprehensive guide covers all aspects of working with spreadsheets in BoxLang using the modern **Fluent API**. The Fluent API provides a chainable, intuitive interface for all spreadsheet operations.

{% hint style="info" %}
**Recommended Approach**: This guide focuses on the Fluent API, which is the recommended way to work with spreadsheets in BoxLang. For CFML migration scenarios, see the [Built-In Functions Reference](reference/built-in-functions/).
{% endhint %}

---

## 🎯 Core Concepts

### The SpreadsheetFile Object

The Fluent API centers around the `SpreadsheetFile` object, created using the `Spreadsheet()` function:

```js
// Create new spreadsheet
sheet = Spreadsheet( "myfile.xlsx" );

// Load existing spreadsheet
sheet = Spreadsheet( "existing.xlsx", load = true );

// Create in-memory spreadsheet
sheet = Spreadsheet();
```

### Method Chaining

Most methods return the `SpreadsheetFile` object, enabling fluent chaining:

```js
Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Name", "Value" ] )
    .addRow( [ "Item 1", 100 ] )
    .formatRow( 1, { bold: true } )
    .autoSizeColumns()
    .save();
```

### Working with Sheets

Every spreadsheet has one or more worksheets. Methods operate on the currently selected sheet:

```js
sheet = Spreadsheet( "multi-sheet.xlsx" )
    .createSheet( "Data" )        // Create new sheet
    .selectSheet( "Data" )         // Switch to it
    .addRow( [ "value1", "value2" ] );
```

---

## 📝 Creating Spreadsheets

### Creating a New File

```js
// Method 1: Direct save
Spreadsheet( "output.xlsx" )
    .setRowData( 1, [ "Column 1", "Column 2" ] )
    .save();

// Method 2: Create, work with, then save
sheet = Spreadsheet();
sheet.setRowData( 1, [ "Header 1", "Header 2" ] );
sheet.addRow( [ "Data 1", "Data 2" ] );
sheet.save( "output.xlsx" );
```

### Setting Cell Values

```js
sheet = Spreadsheet( "data.xlsx" );

// Set individual cell
sheet.setCellValue( 1, 1, "Hello" );        // Row 1, Column 1
sheet.setCellValue( 1, 2, 42 );             // Row 1, Column 2
sheet.setCellValue( 1, 3, now() );          // Row 1, Column 3

// Set entire row
sheet.setRowData( 2, [ "Value1", "Value2", "Value3" ] );

// Set range of cells
sheet.setCellRangeValue(
    startRow = 3,
    startColumn = 1,
    endRow = 5,
    endColumn = 3,
    value = "Same value"
);

sheet.save();
```

### Adding Rows

```js
sheet = Spreadsheet( "employees.xlsx" );

// Add single row
sheet.addRow( [ "John Doe", "Engineering", 95000 ] );

// Add multiple rows from array
data = [
    [ "Jane Smith", "Marketing", 85000 ],
    [ "Bob Johnson", "Sales", 75000 ]
];
sheet.addRows( data );

// Add rows from query
employees = queryExecute( "SELECT name, dept, salary FROM employees" );
sheet.addRows( employees, includeColumnNames = true );

sheet.save();
```

### Adding Columns

```js
sheet = Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Q1", "Q2", "Q3" ] )
    .addRow( [ 100, 200, 300 ] );

// Add column at end
sheet.addColumn( [ "Q4", 400 ] );

// Insert column at position
sheet.insertColumn( 2, [ "Q1.5", 150 ] );

sheet.save();
```

---

## 📖 Reading Spreadsheets

### Loading Files

```js
// Load file into SpreadsheetFile object
sheet = Spreadsheet( "data.xlsx", load = true );

// Or use explicit load method
sheet = Spreadsheet().load( "data.xlsx" );
```

### Reading Cell Values

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Read single cell
value = sheet.getCellValue( 1, 1 );

// Read with row/column names
value = sheet.getCellValue( row = 1, column = 1 );

// Check cell type
type = sheet.getCellType( 1, 1 );  // Returns: "blank", "numeric", "string", "formula", etc.
```

### Reading Rows and Columns

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get entire row as array
row = sheet.getRow( 1 );

// Get entire column as array
column = sheet.getColumn( 1 );

// Get range of rows
rows = sheet.getRows( startRow = 2, endRow = 10 );

// Get range of columns
columns = sheet.getColumns( startColumn = 1, endColumn = 5 );
```

### Converting to Data Structures

```js
sheet = Spreadsheet( "employees.xlsx", load = true );

// Convert to array of structs (uses first row as headers)
employees = sheet.toArray();
// Result: [ { "Name": "John", "Dept": "Engineering" }, ... ]

// Convert to query object
qry = sheet.toQuery();

// Convert to JSON
json = sheet.toJson();

// Convert to CSV
csv = sheet.toCSV();
```

### Streaming Large Files

For large spreadsheets with thousands of rows, use the `process()` method to stream data row-by-row without loading the entire file into memory:

```js
// Stream all rows from a file
Spreadsheet().process( "large-file.xlsx", ( row ) => {
    // Process each row immediately
    println( "Processing: #row[1]#" );
    saveToDatabase( row );
});

// Stream specific sheet
Spreadsheet().process( "report.xlsx", "Sales Data", ( row ) => {
    processOrder( row );
});

// Stream with filtering
rowCount = 0;
Spreadsheet().process( "huge-file.xlsx", ( row ) => {
    if ( row[1] != "Header" ) {  // Skip header
        importData( row );
        rowCount++;
    }
});
println( "Imported #rowCount# rows" );
```

{% hint style="success" %}
**Memory Efficient**: Streaming keeps only ~100 rows in memory at a time, allowing you to process files with millions of rows. See the [Large File Streaming Guide](streaming.md) for complete details.
{% endhint %}

**When to use streaming:**

- Files with > 10,000 rows
- Import/export operations
- Sequential data processing
- Memory-constrained environments

**When to use traditional loading:**

- Files with < 10,000 rows
- Random access to rows
- Modifying and saving files
- Multiple passes over data

---

## 🎨 Formatting

### Cell Formatting

```js
sheet = Spreadsheet( "styled.xlsx" )
    .setRowData( 1, [ "Product", "Price", "Status" ] )
    .addRow( [ "Widget", 29.99, "Available" ] );

// Format single cell
sheet.formatCell( 1, 1, {
    bold: true,
    italic: false,
    underline: false,
    strikeout: false,
    fontsize: 14,
    font: "Arial",
    fontColor: "white",
    fgcolor: "blue",
    alignment: "center",
    verticalalignment: "center"
} );

// Format with data format
sheet.formatCell( 2, 2, {
    dataformat: "$#,##0.00"  // Currency format
} );

sheet.save();
```

### Row and Column Formatting

```js
sheet = Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Q1", "Q2", "Q3", "Q4", "Total" ] )
    .addRow( [ 1000, 1200, 1100, 1300, 4600 ] );

// Format entire row
sheet.formatRow( 1, {
    bold: true,
    fgcolor: "darkblue",
    fontColor: "white",
    alignment: "center"
} );

// Format specific column
sheet.formatColumn( 2, {
    dataformat: "#,##0",
    alignment: "right"
} );

// Format multiple columns
sheet.formatColumns( "2-5", {
    dataformat: "#,##0",
    alignment: "right"
} );

sheet.save();
```

### Range Formatting

```js
sheet = Spreadsheet( "dashboard.xlsx" )
    .setRowData( 1, [ "Region", "Q1", "Q2", "Q3", "Q4" ] )
    .addRow( [ "North", 1000, 1200, 1100, 1300 ] )
    .addRow( [ "South", 800, 900, 950, 1050 ] );

// Format specific range
sheet.formatCellRange(
    startRow = 2,
    endRow = 3,
    startColumn = 2,
    endColumn = 5,
    format = {
        dataformat: "#,##0",
        fgcolor: "lightgray"
    }
);

sheet.save();
```

### Column Widths

```js
sheet = Spreadsheet( "sized.xlsx" )
    .setRowData( 1, [ "Short", "Medium Column", "Very Long Column Name" ] );

// Auto-size all columns
sheet.autoSizeColumns();

// Set specific column width
sheet.setColumnWidth( 1, 15 );

// Set multiple column widths
sheet.setColumnWidth( "2-3", 25 );

sheet.save();
```

---

## 🔢 Working with Formulas

### Adding Formulas

```js
sheet = Spreadsheet( "calculations.xlsx" )
    .setRowData( 1, [ "Item", "Price", "Qty", "Total" ] )
    .addRow( [ "Widget", 29.99, 5 ] )
    .addRow( [ "Gadget", 49.99, 3 ] );

// Add formula to cell
sheet.setCellFormula( 2, 4, "B2*C2" );
sheet.setCellFormula( 3, 4, "B3*C3" );

// Add SUM formula
sheet.setCellFormula( 4, 4, "SUM(D2:D3)" );

sheet.save();
```

### Working with Formula Results

```js
sheet = Spreadsheet( "with-formulas.xlsx", load = true );

// Get formula text
formula = sheet.getCellFormula( 2, 4 );  // Returns: "B2*C2"

// Get calculated value
value = sheet.getCellValue( 2, 4 );      // Returns: 149.95

// Force recalculation
sheet.recalculateAllFormulas();
```

### Advanced Formulas

```js
sheet = Spreadsheet( "advanced.xlsx" )
    .setRowData( 1, [ "Value", "Status" ] )
    .addRow( [ 85 ] );

// IF formula
sheet.setCellFormula( 2, 2, "IF(A2>=90,'Excellent',IF(A2>=70,'Good','Needs Improvement'))" );

// VLOOKUP example
sheet.createSheet( "Lookup" )
    .setRowData( 1, [ "ID", "Name" ] )
    .addRow( [ 1, "Product A" ] )
    .addRow( [ 2, "Product B" ] );

sheet.selectSheet( "Sheet1" )
    .setRowData( 1, [ "ID", "Product Name" ] )
    .addRow( [ 2 ] )
    .setCellFormula( 2, 2, "VLOOKUP(A2,Lookup!A:B,2,FALSE)" );

sheet.save();
```

---

## 📊 Multiple Sheets

### Creating and Managing Sheets

```js
sheet = Spreadsheet( "workbook.xlsx" );

// Create new sheet (default name: "Sheet2", "Sheet3", etc.)
sheet.createSheet();

// Create sheet with custom name
sheet.createSheet( "Sales Data" );

// Create and immediately select
sheet.createAndSelectSheet( "Summary" );

// Rename sheet
sheet.renameSheet( "Sheet1", "Overview" );

// Get all sheet names
names = sheet.getSheetNames();  // Returns: [ "Overview", "Sales Data", "Summary" ]

// Delete sheet
sheet.deleteSheet( "Sales Data" );

sheet.save();
```

### Working Across Sheets

```js
sheet = Spreadsheet( "multi-sheet.xlsx" );

// Add data to first sheet
sheet.selectSheet( "Sheet1" )
    .setRowData( 1, [ "Summary" ] )
    .addRow( [ "Total Sales: 100,000" ] );

// Switch to second sheet
sheet.createAndSelectSheet( "Details" )
    .setRowData( 1, [ "Date", "Amount" ] )
    .addRow( [ "2024-01-15", 1000 ] )
    .addRow( [ "2024-01-16", 1500 ] );

// Use cross-sheet formulas
sheet.selectSheet( "Sheet1" )
    .setCellFormula( 2, 2, "SUM(Details!B2:B100)" );

sheet.save();
```

---

## 🔀 Advanced Operations

### Merging Cells

```js
sheet = Spreadsheet( "merged.xlsx" )
    .setCellValue( 1, 1, "Merged Header" )
    .mergeCells(
        startRow = 1,
        startColumn = 1,
        endRow = 1,
        endColumn = 5
    )
    .formatCell( 1, 1, {
        bold: true,
        alignment: "center",
        fontsize: 16
    } )
    .save();
```

### Adding Comments

```js
sheet = Spreadsheet( "with-comments.xlsx" )
    .setRowData( 1, [ "Name", "Salary" ] )
    .addRow( [ "John Doe", 95000 ] );

// Add comment to cell
sheet.setCellComment( 2, 2, "Includes annual bonus", "Manager" );

// Add comment without author
sheet.setCellComment( 2, 1, "Employee of the month" );

sheet.save();
```

### Hiding Rows and Columns

```js
sheet = Spreadsheet( "hidden.xlsx" )
    .setRowData( 1, [ "Visible", "Hidden", "Also Visible" ] )
    .addRow( [ "Data 1", "Secret", "Data 2" ] );

// Hide column
sheet.hideColumn( 2 );

// Hide row
sheet.hideRow( 3 );

// Show hidden column
sheet.showColumn( 2 );

sheet.save();
```

### Freeze Panes

```js
sheet = Spreadsheet( "frozen.xlsx" )
    .setRowData( 1, [ "Name", "Q1", "Q2", "Q3", "Q4" ] )
    .addRow( [ "Product A", 100, 200, 150, 175 ] );

// Freeze first row (header)
sheet.addFreezePane( 0, 1 );

// Freeze first column and first row
sheet.addFreezePane( 1, 1 );

sheet.save();
```

### Data Validation

```js
sheet = Spreadsheet( "validated.xlsx" )
    .setRowData( 1, [ "Product", "Status" ] );

// Add dropdown validation
sheet.addDataValidation(
    startRow = 2,
    startColumn = 2,
    endRow = 100,
    endColumn = 2,
    type = "list",
    values = [ "Active", "Inactive", "Pending" ]
);

sheet.save();
```

---

## 💾 Saving and Exporting

### Save Methods

```js
sheet = Spreadsheet()
    .setRowData( 1, [ "Data" ] );

// Save to file
sheet.save( "output.xlsx" );

// Save and overwrite
sheet.save( "output.xlsx", overwrite = true );

// Get as binary
binary = sheet.toBinary();

// Save binary manually
fileWrite( "output.xlsx", binary );
```

### Export Formats

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Export to CSV
csv = sheet.toCSV();
fileWrite( "export.csv", csv );

// Export to JSON
json = sheet.toJson();
fileWrite( "export.json", json );

// Export to HTML
html = sheet.toHtml();
fileWrite( "export.html", html );
```

---

## 🔧 Utility Operations

### Sheet Information

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get row count
rowCount = sheet.getRowCount();

// Get column count
colCount = sheet.getColumnCount();

// Get cell info
info = sheet.getCellInfo( 1, 1 );
// Returns struct with: value, formula, type, format, etc.

// Get sheet info
sheetInfo = sheet.getSheetInfo();
// Returns struct with sheet properties
```

### Clearing Content

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Clear specific cell
sheet.clearCell( 1, 1 );

// Clear range
sheet.clearCellRange( startRow = 2, endRow = 10, startColumn = 1, endColumn = 5 );

// Clear entire row
sheet.clearRow( 5 );

// Clear entire sheet
sheet.clearSheet();

sheet.save();
```

### Deleting Rows and Columns

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Delete row
sheet.deleteRow( 3 );

// Delete multiple rows
sheet.deleteRows( startRow = 5, endRow = 10 );

// Delete column
sheet.deleteColumn( 2 );

// Delete multiple columns
sheet.deleteColumns( startColumn = 3, endColumn = 5 );

sheet.save();
```

---

## 🎯 Best Practices

### 1. Use Method Chaining

**Good:**

```js
Spreadsheet( "report.xlsx" )
    .setRowData( 1, headers )
    .addRows( data )
    .formatRow( 1, { bold: true } )
    .autoSizeColumns()
    .save();
```

**Avoid:**

```js
sheet = Spreadsheet( "report.xlsx" );
sheet.setRowData( 1, headers );
sheet.addRows( data );
sheet.formatRow( 1, { bold: true } );
sheet.autoSizeColumns();
sheet.save();
```

### 2. Format After Adding Data

Add all data first, then apply formatting for better performance:

```js
Spreadsheet( "report.xlsx" )
    // Add all data
    .setRowData( 1, headers )
    .addRows( data )
    // Then format
    .formatRow( 1, { bold: true } )
    .formatColumns( "2-5", { dataformat: "#,##0" } )
    .autoSizeColumns()
    .save();
```

### 3. Use Auto-sizing Wisely

Call `autoSizeColumns()` once after all data is added:

```js
Spreadsheet( "data.xlsx" )
    .setRowData( 1, headers )
    .addRows( largeDataset )
    .autoSizeColumns()  // Call once at end
    .save();
```

### 4. Handle Errors Gracefully

```js
try {
    sheet = Spreadsheet( "data.xlsx", load = true )
        .addRow( newData )
        .save();
} catch ( any e ) {
    writeLog( "Error processing spreadsheet: #e.message#" );
    // Handle error appropriately
}
```

### 5. Close Large Files

For very large files, explicitly clear references:

```js
sheet = Spreadsheet( "large-file.xlsx", load = true );
data = sheet.toArray();
sheet = null;  // Release memory
```

---

## 🔍 Common Patterns

### Pattern: Database Export with Formatting

```js
// Query data
employees = queryExecute(
    "SELECT name, department, salary, hire_date FROM employees ORDER BY name"
);

// Create formatted export
Spreadsheet( "employee-report.xlsx" )
    // Add headers
    .setRowData( 1, [ "Name", "Department", "Salary", "Hire Date" ] )
    // Add data
    .addRows( employees )
    // Format header
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white",
        alignment: "center"
    } )
    // Format currency column
    .formatColumn( 3, { dataformat: "$#,##0.00" } )
    // Format date column
    .formatColumn( 4, { dataformat: "mm/dd/yyyy" } )
    // Auto-size
    .autoSizeColumns()
    .save();
```

### Pattern: Template-Based Reporting

```js
// Load template
report = Spreadsheet( "monthly-template.xlsx", load = true );

// Fill in report details
report.setCellValue( 2, 2, "January 2024" )
    .setCellValue( 3, 2, dateFormat( now(), "yyyy-mm-dd" ) );

// Add data to specific sheet and location
report.selectSheet( "Data" )
    .addRows( getData(), startRow = 5 );

// Recalculate formulas in template
report.recalculateAllFormulas();

// Save with new name
report.save( "January-2024-Report.xlsx" );
```

### Pattern: Multi-Sheet Workbook

```js
// Create workbook with multiple related sheets
workbook = Spreadsheet( "annual-report.xlsx" );

// Summary sheet
workbook.createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Annual Summary 2024" ] )
    .mergeCells( 1, 1, 1, 5 )
    .formatCell( 1, 1, { bold: true, fontsize: 16, alignment: "center" } )
    .addRow( [ "Total Revenue:", "=SUM(Q1!B:B,Q2!B:B,Q3!B:B,Q4!B:B)" ] );

// Quarterly sheets
[ "Q1", "Q2", "Q3", "Q4" ].each( ( quarter ) => {
    workbook.createAndSelectSheet( quarter )
        .setRowData( 1, [ "Month", "Revenue" ] )
        .addRows( getQuarterlyData( quarter ) )
        .formatRow( 1, { bold: true } );
} );

workbook.save();
```

---

## 📚 Next Steps

Explore specific topics in detail:

{% content-ref url="formatting.md" %}
[formatting.md](formatting.md)
{% endcontent-ref %}

{% content-ref url="formulas.md" %}
[formulas.md](formulas.md)
{% endcontent-ref %}

{% content-ref url="data-export.md" %}
[data-export.md](data-export.md)
{% endcontent-ref %}

{% content-ref url="advanced-features.md" %}
[advanced-features.md](advanced-features.md)
{% endcontent-ref %}

{% content-ref url="examples.md" %}
[examples.md](examples.md)
{% endcontent-ref %}

### Complete API Reference

{% content-ref url="reference/fluent-api/" %}
[fluent-api](reference/fluent-api/)
{% endcontent-ref %}
