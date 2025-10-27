---
description: Get started with BoxLang Spreadsheet Module in 5 minutes
icon: rocket
---

# 🚀 Quick Start

Get up and running with the BoxLang Spreadsheet Module in just a few minutes!

---

## 📦 Installation

Install the module using CommandBox:

```bash
box install bx-spreadsheet@ortus
```

---

## ✨ Your First Spreadsheet

Let's create a simple employee spreadsheet using the Fluent API:

```js
Spreadsheet( "employees.xlsx" )
    .setRowData( 1, [ "Name", "Department", "Salary" ] )
    .addRow( [ "John Doe", "Engineering", 95000 ] )
    .addRow( [ "Jane Smith", "Marketing", 85000 ] )
    .addRow( [ "Bob Johnson", "Sales", 75000 ] )
    .formatRow( 1, { bold: true, fgcolor: "blue", fontColor: "white" ] )
    .autoSizeColumns()
    .save();
```

That's it! You've just created an Excel file with formatted headers and employee data.

---

## 📖 Reading Spreadsheets

Load and read data from an existing spreadsheet:

```js
// Load and convert to array
employees = Spreadsheet( "employees.xlsx" ).toArray();

// Result: Array of structs with column names as keys
// [
//     { "Name": "John Doe", "Department": "Engineering", "Salary": 95000 },
//     { "Name": "Jane Smith", "Department": "Marketing", "Salary": 85000 },
//     ...
// ]
```

---

## 💾 Export to Different Formats

```js
// Load once
sheet = Spreadsheet( "employees.xlsx" );

// Export to JSON
json = sheet.toJson();
fileWrite( "employees.json", json );

// Export to CSV
csv = sheet.toCSV();
fileWrite( "employees.csv", csv );

// Export to Query
qry = sheet.toQuery();
```

---

## 🎨 Basic Formatting

Add visual styling to your spreadsheets:

```js
Spreadsheet( "styled-report.xlsx" )
    .setRowData( 1, [ "Product", "Q1", "Q2", "Q3", "Q4" ] )
    .addRow( [ "Widget A", 1000, 1200, 1100, 1300 ] )
    .addRow( [ "Widget B", 800, 900, 950, 1050 ] )
    // Format header row
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white",
        alignment: "center"
    } )
    // Format data columns
    .formatColumns( "2-5", { dataformat: "#,##0", alignment: "right" } )
    .autoSizeColumns()
    .save();
```

---

## 🔢 Working with Formulas

Add Excel formulas to calculate values:

```js
Spreadsheet( "calculations.xlsx" )
    .setRowData( 1, [ "Item", "Price", "Quantity", "Total" ] )
    .addRow( [ "Widget", 29.99, 5 ] )
    .addRow( [ "Gadget", 49.99, 3 ] )
    // Add formulas for totals
    .setCellFormula( 2, 4, "B2*C2" )
    .setCellFormula( 3, 4, "B3*C3" )
    // Add summary row
    .setRowData( 4, [ "TOTAL", "", "", "=SUM(D2:D3)" ] )
    .formatRow( 1, { bold: true } )
    .formatRow( 4, { bold: true, fgcolor: "lightgray" } )
    .save();
```

---

## 📊 Multiple Sheets

Work with multiple worksheets:

```js
Spreadsheet( "multi-sheet.xlsx" )
    // Create and populate first sheet
    .createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Report Summary" ] )
    .mergeCells( 1, 1, 1, 5 )
    .formatCell( 1, 1, { bold: true, fontsize: 16 } )

    // Create and populate second sheet
    .createAndSelectSheet( "Details" )
    .setRowData( 1, [ "Date", "Description", "Amount" ] )
    .addRow( [ "2024-01-15", "Purchase", 150.00 ] )
    .addRow( [ "2024-01-16", "Sale", 300.00 ] )

    .save();
```

---

## 🔄 Modify Existing Spreadsheets

Load, modify, and save:

```js
// Load existing file
Spreadsheet( "employees.xlsx" )
    // Add new employee
    .addRow( [ "Alice Cooper", "HR", 80000 ] )
    // Update a cell
    .setCellValue( 2, 3, 98000 ) // Give John a raise!
    // Add a comment
    .setCellComment( 2, 3, "Annual raise applied", "Manager" )
    .save(); // Overwrites the file
```

---

## 🎯 Common Patterns

### Pattern 1: Import CSV to Excel

```js
// Read CSV data
csvData = fileRead( "data.csv" );
lines = csvData.split( chr(10) );

// Create Excel file
sheet = Spreadsheet( "from-csv.xlsx" );

// Add each line
for ( line in lines ) {
    sheet.addRow( line.split( "," ) );
}

sheet.formatRow( 1, { bold: true } )
    .autoSizeColumns()
    .save();
```

### Pattern 2: Database Export

```js
// Query database
employees = queryExecute(
    "SELECT name, department, salary FROM employees ORDER BY name"
);

// Export to Excel
Spreadsheet( "employee-export.xlsx" )
    .addRows( employees, includeColumnNames = true )
    .formatRow( 1, { bold: true } )
    .autoSizeColumns()
    .save();
```

### Pattern 3: Template-Based Reports

```js
// Load template
report = Spreadsheet( "template.xlsx" )
    // Fill in placeholders
    .setCellValue( 2, 2, "Q1 2024" ) // Report period
    .setCellValue( 3, 2, dateFormat( now(), "yyyy-mm-dd" ) ) // Date

    // Add data starting at row 5
    .selectSheet( "Data" )
    .addRows( getData(), startRow = 5 )

    // Recalculate formulas
    .recalculateAllFormulas()

    .save( "Q1-2024-Report.xlsx" );
```

---

## 🎓 Next Steps

Now that you've created your first spreadsheets, explore more advanced features:

{% content-ref url="user-guide.md" %}
[user-guide.md](user-guide.md)
{% endcontent-ref %}

{% content-ref url="formatting.md" %}
[formatting.md](formatting.md)
{% endcontent-ref %}

{% content-ref url="formulas.md" %}
[formulas.md](formulas.md)
{% endcontent-ref %}

{% content-ref url="examples.md" %}
[examples.md](examples.md)
{% endcontent-ref %}

### Complete API Reference

For detailed method documentation:

{% content-ref url="reference/fluent-api/" %}
[fluent-api](reference/fluent-api/)
{% endcontent-ref %}

---

## 💡 Tips

- **Use Fluent API** - The chainable interface is the recommended approach
- **Auto-size columns** - Call `.autoSizeColumns()` for better-looking spreadsheets
- **Format headers** - Make headers stand out with bold text and background colors
- **Check file paths** - Ensure output directories exist before saving
- **Test formulas** - Call `.recalculateAllFormulas()` to ensure calculations are current

---

## 🤔 Need Help?

- 📚 [Complete User Guide](user-guide.md)
- 🔍 [Fluent API Reference](reference/fluent-api/)
- 💡 [Real-World Examples](examples.md)
- 📖 [Full API Documentation](https://apidocs.ortussolutions.com/boxlang-modules/bx-spreadsheet/1.0.0/)
