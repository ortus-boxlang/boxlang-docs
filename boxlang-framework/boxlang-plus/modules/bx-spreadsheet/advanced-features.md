---
description: Advanced spreadsheet features - data validation, images, freeze panes, protection, and more
icon: wand-magic-sparkles
---

# ✨ Advanced Features

Master advanced spreadsheet capabilities with the BoxLang Fluent API. This guide covers data validation, images, freeze panes, cell protection, and other sophisticated features.

---

## ✅ Data Validation

### Dropdown Lists

```js
Spreadsheet( "validation.xlsx" )
    .setRowData( 1, [ "Product", "Status", "Priority" ] )

    // Add dropdown for Status column
    .addDataValidation(
        startRow = 2,
        startColumn = 2,
        endRow = 100,
        endColumn = 2,
        type = "list",
        values = [ "Active", "Inactive", "Pending" ]
    )

    // Add dropdown for Priority column
    .addDataValidation(
        startRow = 2,
        startColumn = 3,
        endRow = 100,
        endColumn = 3,
        type = "list",
        values = [ "High", "Medium", "Low" ]
    )

    .save();
```

### Numeric Validation

```js
Spreadsheet( "numeric-validation.xlsx" )
    .setRowData( 1, [ "Item", "Quantity", "Discount %" ] )

    // Quantity must be between 1 and 1000
    .addDataValidation(
        startRow = 2,
        startColumn = 2,
        endRow = 100,
        endColumn = 2,
        type = "integer",
        operator = "between",
        formula1 = "1",
        formula2 = "1000"
    )

    // Discount must be between 0 and 100
    .addDataValidation(
        startRow = 2,
        startColumn = 3,
        endRow = 100,
        endColumn = 3,
        type = "decimal",
        operator = "between",
        formula1 = "0",
        formula2 = "100"
    )

    .save();
```

### Date Validation

```js
Spreadsheet( "date-validation.xlsx" )
    .setRowData( 1, [ "Event", "Start Date", "End Date" ] )

    // Start date must be after today
    .addDataValidation(
        startRow = 2,
        startColumn = 2,
        endRow = 100,
        endColumn = 2,
        type = "date",
        operator = "greaterThan",
        formula1 = "TODAY()"
    )

    .save();
```

### Custom Validation with Formulas

```js
Spreadsheet( "custom-validation.xlsx" )
    .setRowData( 1, [ "Product", "Price", "Discount Price" ] )
    .addRow( [ "Widget", 100 ] )

    // Discount price must be less than regular price
    .addDataValidation(
        startRow = 2,
        startColumn = 3,
        endRow = 100,
        endColumn = 3,
        type = "custom",
        formula1 = "C2<B2"
    )

    .save();
```

---

## 🖼️ Working with Images

### Adding Images

```js
Spreadsheet( "with-image.xlsx" )
    .setRowData( 1, [ "Company Logo" ] )

    // Add image to specific cell
    .addImage(
        filePath = "/path/to/logo.png",
        row = 2,
        column = 1
    )

    .save();
```

### Positioning Images

```js
Spreadsheet( "positioned-images.xlsx" )
    // Add image with specific size and position
    .addImage(
        filePath = "/path/to/chart.png",
        row = 1,
        column = 1,
        width = 400,
        height = 300
    )

    .save();
```

### Multiple Images

```js
sheet = Spreadsheet( "gallery.xlsx" )
    .setRowData( 1, [ "Image 1", "Image 2", "Image 3" ] );

// Add images to different cells
images = [
    { file: "image1.png", row: 2, col: 1 },
    { file: "image2.png", row: 2, col: 2 },
    { file: "image3.png", row: 2, col: 3 }
];

for ( img in images ) {
    sheet.addImage(
        filePath = "/images/#img.file#",
        row = img.row,
        column = img.col
    );
}

sheet.save();
```

---

## 🔒 Cell Protection

### Protect Worksheet

```js
Spreadsheet( "protected.xlsx" )
    .setRowData( 1, [ "Protected Data" ] )
    .addRow( [ "This sheet is protected" ] )

    // Protect the sheet with password
    .protectSheet( password = "secret123" )

    .save();
```

### Lock Specific Cells

```js
Spreadsheet( "partially-locked.xlsx" )
    .setRowData( 1, [ "Locked", "Editable" ] )
    .addRow( [ "Can't change", "Can change" ] )

    // Lock first column
    .formatColumn( 1, { locked: true } )

    // Unlock second column
    .formatColumn( 2, { locked: false } )

    // Protect sheet (locked cells can't be edited)
    .protectSheet( password = "secret123" )

    .save();
```

### Unprotect Worksheet

```js
sheet = Spreadsheet( "protected.xlsx", load = true )
    // Remove protection
    .unprotectSheet( password = "secret123" )

    // Make changes
    .addRow( [ "New data" ] )

    .save();
```

---

## ❄️ Freeze Panes

### Freeze Top Row

```js
Spreadsheet( "frozen-header.xlsx" )
    .setRowData( 1, [ "Name", "Q1", "Q2", "Q3", "Q4" ] )
    .addRow( [ "Product A", 100, 200, 150, 175 ] )
    .addRow( [ "Product B", 150, 175, 200, 225 ] )

    // Freeze first row (column=0, row=1)
    .addFreezePane( 0, 1 )

    .save();
```

### Freeze First Column

```js
Spreadsheet( "frozen-column.xlsx" )
    .setRowData( 1, [ "Product", 100, 200, 150 ] )
    .addRow( [ "Widget", 10, 20, 15 ] )

    // Freeze first column (column=1, row=0)
    .addFreezePane( 1, 0 )

    .save();
```

### Freeze Both Row and Column

```js
Spreadsheet( "frozen-both.xlsx" )
    .setRowData( 1, [ "Product", "Q1", "Q2", "Q3" ] )
    .addRow( [ "Widget", 100, 200, 150 ] )
    .addRow( [ "Gadget", 150, 175, 200 ] )

    // Freeze first row AND first column
    .addFreezePane( 1, 1 )

    .save();
```

### Remove Freeze Panes

```js
sheet = Spreadsheet( "frozen.xlsx", load = true )
    .removeFreezePane()
    .save();
```

---

## 📏 Row and Column Management

### Setting Row Heights

```js
Spreadsheet( "row-heights.xlsx" )
    .setRowData( 1, [ "Normal Height" ] )
    .setRowData( 2, [ "Tall Row" ] )
    .setRowData( 3, [ "Extra Tall Row" ] )

    // Set specific row heights (in points)
    .setRowHeight( 2, 30 )
    .setRowHeight( 3, 50 )

    .save();
```

### Setting Column Widths

```js
Spreadsheet( "column-widths.xlsx" )
    .setRowData( 1, [ "Narrow", "Normal", "Wide", "Extra Wide" ] )

    // Set specific column widths (in characters)
    .setColumnWidth( 1, 10 )
    .setColumnWidth( 2, 15 )
    .setColumnWidth( 3, 30 )
    .setColumnWidth( 4, 50 )

    .save();
```

### Auto-Sizing Columns

```js
Spreadsheet( "auto-sized.xlsx" )
    .setRowData( 1, [ "Short", "Medium Length", "Very Long Column Header" ] )
    .addRow( [ "A", "Some data", "Lots of data in this cell" ] )

    // Auto-size all columns to fit content
    .autoSizeColumns()

    .save();
```

### Hiding Rows and Columns

```js
Spreadsheet( "hidden.xlsx" )
    .setRowData( 1, [ "Visible", "Hidden Column", "Visible" ] )
    .addRow( [ "Data 1", "Secret", "Data 2" ] )
    .addRow( [ "Hidden Row", "Hidden", "Hidden" ] )
    .addRow( [ "Data 3", "More secret", "Data 4" ] )

    // Hide column 2
    .hideColumn( 2 )

    // Hide row 3
    .hideRow( 3 )

    .save();
```

### Showing Hidden Rows and Columns

```js
sheet = Spreadsheet( "hidden.xlsx", load = true )
    // Show hidden column
    .showColumn( 2 )

    // Show hidden row
    .showRow( 3 )

    .save();
```

---

## 📝 Cell Comments

### Adding Comments

```js
Spreadsheet( "with-comments.xlsx" )
    .setRowData( 1, [ "Name", "Salary" ] )
    .addRow( [ "John Doe", 95000 ] )

    // Add comment with author
    .setCellComment( 2, 2, "Includes annual bonus", "Manager" )

    // Add comment without author
    .setCellComment( 2, 1, "Employee of the month" )

    .save();
```

### Reading Comments

```js
sheet = Spreadsheet( "with-comments.xlsx", load = true );

// Get comment from cell
comment = sheet.getCellComment( 2, 2 );

writeOutput( "Comment: #comment.text#" );
writeOutput( "Author: #comment.author#" );
```

### Removing Comments

```js
sheet = Spreadsheet( "with-comments.xlsx", load = true )
    .removeCellComment( 2, 2 )
    .save();
```

---

## 🔗 Merging Cells

### Merge Cell Range

```js
Spreadsheet( "merged.xlsx" )
    .setCellValue( 1, 1, "Merged Header" )

    // Merge cells A1:E1
    .mergeCells(
        startRow = 1,
        startColumn = 1,
        endRow = 1,
        endColumn = 5
    )

    .formatCell( 1, 1, {
        bold: true,
        fontsize: 16,
        alignment: "center"
    } )

    .save();
```

### Merge for Title

```js
Spreadsheet( "report-title.xlsx" )
    .setCellValue( 1, 1, "Annual Sales Report 2024" )
    .mergeCells( 1, 1, 1, 10 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 18,
        alignment: "center",
        verticalalignment: "center",
        fgcolor: "darkblue",
        fontColor: "white"
    } )
    .setRowHeight( 1, 30 )

    // Add data below
    .setRowData( 2, [ "Month", "Sales", "Target", "Variance" ] )

    .save();
```

### Unmerge Cells

```js
sheet = Spreadsheet( "merged.xlsx", load = true )
    .unmergeCells(
        startRow = 1,
        startColumn = 1,
        endRow = 1,
        endColumn = 5
    )
    .save();
```

---

## 🎨 Conditional Formatting (Manual)

### Color Scale Based on Values

```js
// Load data
data = [
    [ "Product A", 85 ],
    [ "Product B", 92 ],
    [ "Product C", 67 ],
    [ "Product D", 78 ]
];

sheet = Spreadsheet( "color-scale.xlsx" )
    .setRowData( 1, [ "Product", "Score" ] )
    .addRows( data );

// Find min and max for color scale
scores = data.map( ( row ) => row[2] );
minScore = arrayMin( scores );
maxScore = arrayMax( scores );

// Apply color based on value
for ( i = 1; i <= data.len(); i++ ) {
    rowNum = i + 1;
    score = data[i][2];

    // Calculate color (green for high, red for low)
    ratio = ( score - minScore ) / ( maxScore - minScore );

    if ( ratio > 0.66 ) {
        bgcolor = "lightgreen";
    } else if ( ratio > 0.33 ) {
        bgcolor = "yellow";
    } else {
        bgcolor = "red";
        fontcolor = "white";
    }

    sheet.formatCell( rowNum, 2, {
        fgcolor: bgcolor,
        fontColor: fontcolor ?: "black",
        bold: true
    } );
}

sheet.save();
```

### Icon Sets (Using Characters)

```js
// Helper function for status icons
function getStatusIcon( value ) {
    if ( value >= 90 ) return "✅";
    if ( value >= 70 ) return "⚠️";
    return "❌";
}

data = [
    [ "Task 1", 95 ],
    [ "Task 2", 78 ],
    [ "Task 3", 55 ]
];

sheet = Spreadsheet( "icon-sets.xlsx" )
    .setRowData( 1, [ "Task", "Score", "Status" ] )
    .addRows( data );

// Add status icons
for ( i = 1; i <= data.len(); i++ ) {
    rowNum = i + 1;
    score = data[i][2];
    icon = getStatusIcon( score );

    sheet.setCellValue( rowNum, 3, icon );
}

sheet.save();
```

---

## 📊 Named Ranges

### Creating Named Ranges

```js
Spreadsheet( "named-ranges.xlsx" )
    .setRowData( 1, [ "Sales Data" ] )
    .addRow( [ 100 ] )
    .addRow( [ 200 ] )
    .addRow( [ 150 ] )

    // Define named range
    .createNamedRange(
        name = "SalesData",
        range = "A2:A4"
    )

    // Use in formula
    .setRowData( 5, [ "Total", "=SUM(SalesData)" ] )

    .save();
```

### Using Named Ranges

```js
sheet = Spreadsheet( "with-named-ranges.xlsx", load = true );

// Get named range value
range = sheet.getNamedRange( "SalesData" );

// Use in formulas
sheet.setCellFormula( 10, 1, "AVERAGE(SalesData)" );

sheet.save();
```

---

## 🔄 Copying and Moving

### Copy Range

```js
sheet = Spreadsheet( "copy.xlsx" )
    .setRowData( 1, [ "Original", "Data" ] )
    .addRow( [ "Value 1", 100 ] )
    .addRow( [ "Value 2", 200 ] );

// Get range data
data = sheet.getRows( startRow = 1, endRow = 3 );

// Copy to new location
startRow = 5;
for ( row in data ) {
    sheet.setRowData( startRow++, row );
}

sheet.save();
```

### Copy Sheet

```js
sheet = Spreadsheet( "workbook.xlsx", load = true );

// Get data from Sheet1
sheet.selectSheet( "Sheet1" );
data = sheet.toArray( includeHeaderRow = true );

// Create copy in new sheet
sheet.createAndSelectSheet( "Sheet1 Copy" )
    .addRows( data );

sheet.save();
```

---

## 📄 Print Settings

### Set Print Area

```js
Spreadsheet( "print-area.xlsx" )
    .setRowData( 1, [ "Printed Data" ] )
    .addRow( [ "This will print" ] )
    .addRow( [ "This too" ] )

    // Set print area to A1:B3
    .setPrintArea( "A1:B3" )

    .save();
```

### Page Setup

```js
Spreadsheet( "page-setup.xlsx" )
    .setRowData( 1, [ "Data" ] )

    // Set page orientation
    .setOrientation( "landscape" )  // or "portrait"

    // Set paper size
    .setPaperSize( "letter" )  // or "legal", "a4", etc.

    // Set margins (in inches)
    .setMargins(
        left = 0.5,
        right = 0.5,
        top = 0.75,
        bottom = 0.75
    )

    .save();
```

---

## 💡 Advanced Patterns

### Pattern: Dynamic Dashboard

```js
// Create multi-section dashboard
sheet = Spreadsheet( "dashboard.xlsx" );

// Title section
sheet.setCellValue( 1, 1, "Sales Dashboard - Q4 2024" )
    .mergeCells( 1, 1, 1, 10 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 20,
        alignment: "center",
        fgcolor: "darkblue",
        fontColor: "white"
    } )
    .setRowHeight( 1, 35 );

// Summary section
sheet.setRowData( 3, [ "Total Sales", "=SUM(B10:B20)" ] )
    .setRowData( 4, [ "Average", "=AVERAGE(B10:B20)" ] )
    .setRowData( 5, [ "Top Product", "=INDEX(A10:A20,MATCH(MAX(B10:B20),B10:B20,0))" ] )
    .formatCellRange( 3, 1, 5, 2, {
        bold: true,
        fgcolor: "lightgray"
    } );

// Data section
sheet.setRowData( 9, [ "Product", "Sales", "Growth %" ] )
    .formatRow( 9, {
        bold: true,
        fgcolor: "darkgreen",
        fontColor: "white"
    } );

// Add data rows with conditional formatting
// ... add data logic here ...

// Freeze header rows
sheet.addFreezePane( 0, 9 );

sheet.save();
```

### Pattern: Template Generator

```js
// Create reusable template
function createInvoiceTemplate( customerName, invoiceNumber ) {
    return Spreadsheet( "invoice-#invoiceNumber#.xlsx" )
        // Header
        .setCellValue( 1, 1, "INVOICE" )
        .mergeCells( 1, 1, 1, 5 )
        .formatCell( 1, 1, {
            bold: true,
            fontsize: 24,
            alignment: "center"
        } )

        // Customer info
        .setCellValue( 3, 1, "Customer:" )
        .setCellValue( 3, 2, customerName )
        .setCellValue( 4, 1, "Invoice ##:" )
        .setCellValue( 4, 2, invoiceNumber )
        .setCellValue( 5, 1, "Date:" )
        .setCellValue( 5, 2, dateFormat( now(), "mm/dd/yyyy" ) )

        // Line items header
        .setRowData( 7, [ "Item", "Quantity", "Price", "Total" ] )
        .formatRow( 7, {
            bold: true,
            fgcolor: "lightblue"
        } )

        // Add dropdowns for line items
        .addDataValidation(
            startRow = 8,
            endRow = 50,
            startColumn = 1,
            endColumn = 1,
            type = "list",
            values = [ "Service", "Product", "Consultation" ]
        )

        // Formula for totals
        .setCellFormula( 8, 4, "B8*C8" )

        // Grand total
        .setRowData( 52, [ "", "", "TOTAL:", "=SUM(D8:D50)" ] )
        .formatRow( 52, {
            bold: true,
            fgcolor: "lightgray"
        } )

        .save();
}

// Generate invoices
createInvoiceTemplate( "Acme Corp", "INV-001" );
createInvoiceTemplate( "Tech Inc", "INV-002" );
```

---

## 📚 Next Steps

{% content-ref url="examples.md" %}
[examples.md](examples.md)
{% endcontent-ref %}

{% content-ref url="reference/fluent-api/" %}
[fluent-api](reference/fluent-api/)
{% endcontent-ref %}
