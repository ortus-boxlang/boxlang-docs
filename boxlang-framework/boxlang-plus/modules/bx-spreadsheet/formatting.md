---
description: Complete guide to formatting spreadsheets - fonts, colors, borders, alignment, and data formats
icon: palette
---

# 🎨 Formatting Guide

Master spreadsheet formatting with the BoxLang Fluent API. This guide covers all visual styling options to create professional-looking spreadsheets.

---

## 📋 Format Options Reference

### Complete Format Structure

```js
formatOptions = {
    // Font properties
    bold: true,
    italic: false,
    underline: false,
    strikeout: false,
    font: "Arial",
    fontsize: 11,
    fontColor: "black",

    // Background color
    fgcolor: "white",
    bgcolor: "white",  // Alias for fgcolor

    // Alignment
    alignment: "left",              // left, center, right, justify
    verticalalignment: "top",       // top, center, bottom

    // Data format
    dataformat: "General",          // Excel format code

    // Borders
    leftborder: "thin",             // none, thin, medium, thick
    rightborder: "thin",
    topborder: "thin",
    bottomborder: "thin",
    leftbordercolor: "black",
    rightbordercolor: "black",
    topbordercolor: "black",
    bottombordercolor: "black",

    // Text control
    wraptext: false,
    locked: false,
    hidden: false
};
```

---

## 🔤 Font Formatting

### Font Styles

```js
Spreadsheet( "fonts.xlsx" )
    .setRowData( 1, [ "Bold", "Italic", "Underline", "Strikeout" ] )

    // Bold text
    .setCellValue( 2, 1, "Important" )
    .formatCell( 2, 1, { bold: true } )

    // Italic text
    .setCellValue( 2, 2, "Emphasis" )
    .formatCell( 2, 2, { italic: true } )

    // Underlined text
    .setCellValue( 2, 3, "Underlined" )
    .formatCell( 2, 3, { underline: true } )

    // Strikethrough text
    .setCellValue( 2, 4, "Removed" )
    .formatCell( 2, 4, { strikeout: true } )

    .save();
```

### Font Family and Size

```js
Spreadsheet( "font-styles.xlsx" )
    .setRowData( 1, [ "Default", "Large", "Custom Font" ] )

    // Large font
    .setCellValue( 2, 2, "Title Text" )
    .formatCell( 2, 2, { fontsize: 18, bold: true } )

    // Custom font family
    .setCellValue( 2, 3, "Courier Text" )
    .formatCell( 2, 3, { font: "Courier New", fontsize: 12 } )

    .save();
```

### Font Colors

```js
Spreadsheet( "colors.xlsx" )
    .setRowData( 1, [ "Red", "Blue", "Green", "Custom" ] )

    // Named colors
    .setCellValue( 2, 1, "Error" )
    .formatCell( 2, 1, { fontColor: "red", bold: true } )

    .setCellValue( 2, 2, "Info" )
    .formatCell( 2, 2, { fontColor: "blue" } )

    .setCellValue( 2, 3, "Success" )
    .formatCell( 2, 3, { fontColor: "green", bold: true } )

    // Hex color
    .setCellValue( 2, 4, "Custom" )
    .formatCell( 2, 4, { fontColor: "##FF6600" } )

    .save();
```

**Supported Color Names:**
- `black`, `white`, `red`, `green`, `blue`
- `yellow`, `cyan`, `magenta`
- `orange`, `pink`, `purple`
- `gray`, `grey`, `darkgray`, `lightgray`
- `darkblue`, `lightblue`
- `darkgreen`, `lightgreen`
- `darkred`, `brown`
- Or use hex codes: `##RRGGBB`

---

## 🎨 Background Colors

### Cell Backgrounds

```js
Spreadsheet( "backgrounds.xlsx" )
    .setRowData( 1, [ "Status", "Priority", "Category" ] )
    .addRow( [ "Active", "High", "Sales" ] )

    // Green background for status
    .formatCell( 2, 1, {
        fgcolor: "lightgreen",
        bold: true
    } )

    // Red background for high priority
    .formatCell( 2, 2, {
        fgcolor: "red",
        fontColor: "white",
        bold: true
    } )

    // Blue background for category
    .formatCell( 2, 3, {
        fgcolor: "lightblue"
    } )

    .save();
```

### Alternating Row Colors

```js
data = [
    [ "Product A", 100 ],
    [ "Product B", 200 ],
    [ "Product C", 150 ],
    [ "Product D", 175 ]
];

sheet = Spreadsheet( "striped.xlsx" )
    .setRowData( 1, [ "Product", "Sales" ] )
    .addRows( data );

// Apply alternating colors
for ( i = 2; i <= data.len() + 1; i++ ) {
    bgcolor = ( i % 2 == 0 ) ? "lightgray" : "white";
    sheet.formatRow( i, { fgcolor: bgcolor } );
}

sheet.save();
```

---

## 📐 Alignment

### Horizontal Alignment

```js
Spreadsheet( "alignment.xlsx" )
    .setRowData( 1, [ "Left", "Center", "Right", "Justify" ] )

    // Left aligned (default)
    .setCellValue( 2, 1, "Left aligned text" )
    .formatCell( 2, 1, { alignment: "left" } )

    // Center aligned
    .setCellValue( 2, 2, "Centered" )
    .formatCell( 2, 2, { alignment: "center" } )

    // Right aligned
    .setCellValue( 2, 3, "Right aligned" )
    .formatCell( 2, 3, { alignment: "right" } )

    // Justified (for multi-line cells)
    .setCellValue( 2, 4, "Justified text wraps" )
    .formatCell( 2, 4, {
        alignment: "justify",
        wraptext: true
    } )
    .setColumnWidth( 4, 20 )

    .save();
```

### Vertical Alignment

```js
Spreadsheet( "vertical.xlsx" )
    .setRowData( 1, [ "Top", "Middle", "Bottom" ] )
    .setRowHeight( 2, 40 )  // Make row taller

    // Top aligned (default)
    .setCellValue( 2, 1, "Top" )
    .formatCell( 2, 1, { verticalalignment: "top" } )

    // Center aligned
    .setCellValue( 2, 2, "Middle" )
    .formatCell( 2, 2, { verticalalignment: "center" } )

    // Bottom aligned
    .setCellValue( 2, 3, "Bottom" )
    .formatCell( 2, 3, { verticalalignment: "bottom" } )

    .save();
```

### Text Wrapping

```js
Spreadsheet( "wrapped.xlsx" )
    .setCellValue( 1, 1, "This is a long text that will wrap within the cell" )
    .formatCell( 1, 1, {
        wraptext: true,
        alignment: "left",
        verticalalignment: "top"
    } )
    .setColumnWidth( 1, 30 )
    .save();
```

---

## 🔢 Data Formats

### Number Formats

```js
Spreadsheet( "numbers.xlsx" )
    .setRowData( 1, [ "Type", "Value" ] )
    .addRow( [ "Integer", 1234567 ] )
    .addRow( [ "Decimal", 1234.5678 ] )
    .addRow( [ "Percentage", 0.125 ] )
    .addRow( [ "Scientific", 1234567890 ] )
    .addRow( [ "Fraction", 0.75 ] )

    // Integer with thousands separator
    .formatCell( 2, 2, { dataformat: "#,##0" } )

    // Two decimal places
    .formatCell( 3, 2, { dataformat: "#,##0.00" } )

    // Percentage
    .formatCell( 4, 2, { dataformat: "0.00%" } )

    // Scientific notation
    .formatCell( 5, 2, { dataformat: "0.00E+00" } )

    // Fraction
    .formatCell( 6, 2, { dataformat: "# ?/?" } )

    .save();
```

### Currency Formats

```js
Spreadsheet( "currency.xlsx" )
    .setRowData( 1, [ "Currency", "Amount" ] )
    .addRow( [ "US Dollar", 1234.56 ] )
    .addRow( [ "Euro", 1234.56 ] )
    .addRow( [ "Pound", 1234.56 ] )
    .addRow( [ "Yen", 123456 ] )

    // US Dollar
    .formatCell( 2, 2, { dataformat: "$#,##0.00" } )

    // Euro
    .formatCell( 3, 2, { dataformat: "€#,##0.00" } )

    // British Pound
    .formatCell( 4, 2, { dataformat: "£#,##0.00" } )

    // Japanese Yen (no decimal)
    .formatCell( 5, 2, { dataformat: "¥#,##0" } )

    .save();
```

### Date and Time Formats

```js
now = now();

Spreadsheet( "dates.xlsx" )
    .setRowData( 1, [ "Format", "Value" ] )
    .addRow( [ "Short Date", now ] )
    .addRow( [ "Long Date", now ] )
    .addRow( [ "Date and Time", now ] )
    .addRow( [ "Time Only", now ] )
    .addRow( [ "Custom", now ] )

    // Short date: 01/15/2024
    .formatCell( 2, 2, { dataformat: "mm/dd/yyyy" } )

    // Long date: January 15, 2024
    .formatCell( 3, 2, { dataformat: "mmmm dd, yyyy" } )

    // Date and time: 01/15/2024 14:30
    .formatCell( 4, 2, { dataformat: "mm/dd/yyyy hh:mm" } )

    // Time only: 2:30 PM
    .formatCell( 5, 2, { dataformat: "h:mm AM/PM" } )

    // Custom: Monday, Jan 15, 2024
    .formatCell( 6, 2, { dataformat: "dddd, mmm dd, yyyy" } )

    .save();
```

**Common Date Format Codes:**
- `m` - Month (1-12)
- `mm` - Month (01-12)
- `mmm` - Month (Jan-Dec)
- `mmmm` - Month (January-December)
- `d` - Day (1-31)
- `dd` - Day (01-31)
- `ddd` - Day (Mon-Sun)
- `dddd` - Day (Monday-Sunday)
- `yy` - Year (24)
- `yyyy` - Year (2024)
- `h` - Hour (0-23)
- `hh` - Hour (00-23)
- `mm` - Minute (00-59)
- `ss` - Second (00-59)

### Custom Formats

```js
Spreadsheet( "custom.xlsx" )
    .setRowData( 1, [ "Format", "Value" ] )

    // Positive/Negative/Zero different colors
    .addRow( [ "Colored Numbers", 100 ] )
    .formatCell( 2, 2, {
        dataformat: "[Green]#,##0;[Red](#,##0);[Blue]0"
    } )

    // Text format with prefix
    .addRow( [ "With Text", 12345 ] )
    .formatCell( 3, 2, {
        dataformat: '"Order "#0000'
    } )

    // Conditional format
    .addRow( [ "Conditional", 75 ] )
    .formatCell( 4, 2, {
        dataformat: '[>=80]"Pass";[<80]"Fail"'
    } )

    .save();
```

---

## 🔲 Borders

### Simple Borders

```js
Spreadsheet( "borders.xlsx" )
    .setRowData( 1, [ "No Border", "All Borders", "Bottom Only" ] )
    .addRow( [ "Cell 1", "Cell 2", "Cell 3" ] )

    // All borders
    .formatCell( 2, 2, {
        leftborder: "thin",
        rightborder: "thin",
        topborder: "thin",
        bottomborder: "thin"
    } )

    // Bottom border only (underline effect)
    .formatCell( 2, 3, {
        bottomborder: "medium"
    } )

    .save();
```

### Border Styles

```js
Spreadsheet( "border-styles.xlsx" )
    .setRowData( 1, [ "Thin", "Medium", "Thick" ] )
    .addRow( [ "Style 1", "Style 2", "Style 3" ] )

    // Thin borders
    .formatCell( 2, 1, {
        leftborder: "thin",
        rightborder: "thin",
        topborder: "thin",
        bottomborder: "thin"
    } )

    // Medium borders
    .formatCell( 2, 2, {
        leftborder: "medium",
        rightborder: "medium",
        topborder: "medium",
        bottomborder: "medium"
    } )

    // Thick borders
    .formatCell( 2, 3, {
        leftborder: "thick",
        rightborder: "thick",
        topborder: "thick",
        bottomborder: "thick"
    } )

    .save();
```

**Border Styles:**
- `none` - No border
- `thin` - Thin line
- `medium` - Medium line
- `thick` - Thick line
- `dashed` - Dashed line
- `dotted` - Dotted line
- `double` - Double line

### Border Colors

```js
Spreadsheet( "border-colors.xlsx" )
    .setRowData( 1, [ "Colored Borders" ] )
    .formatCell( 1, 1, {
        leftborder: "thick",
        leftbordercolor: "red",
        rightborder: "thick",
        rightbordercolor: "blue",
        topborder: "thick",
        topbordercolor: "green",
        bottomborder: "thick",
        bottombordercolor: "orange"
    } )
    .save();
```

### Table Borders

```js
// Create a bordered table
data = [
    [ "Name", "Age", "City" ],
    [ "John", 30, "New York" ],
    [ "Jane", 25, "Boston" ],
    [ "Bob", 35, "Chicago" ]
];

sheet = Spreadsheet( "table.xlsx" );

// Add data
data.each( ( row, index ) => {
    sheet.setRowData( index, row );
} );

// Add borders to all cells
for ( row = 1; row <= data.len(); row++ ) {
    for ( col = 1; col <= data[1].len(); col++ ) {
        sheet.formatCell( row, col, {
            leftborder: "thin",
            rightborder: "thin",
            topborder: "thin",
            bottomborder: "thin",
            leftbordercolor: "black",
            rightbordercolor: "black",
            topbordercolor: "black",
            bottombordercolor: "black"
        } );
    }
}

// Bold header
sheet.formatRow( 1, { bold: true } );

sheet.save();
```

---

## 🎯 Formatting Scopes

### Single Cell Formatting

```js
sheet = Spreadsheet( "single.xlsx" )
    .setCellValue( 1, 1, "Formatted Cell" )
    .formatCell( 1, 1, {
        bold: true,
        fontColor: "white",
        fgcolor: "darkblue",
        alignment: "center"
    } );
```

### Row Formatting

```js
sheet = Spreadsheet( "rows.xlsx" )
    .setRowData( 1, [ "Col1", "Col2", "Col3" ] )
    .setRowData( 2, [ "Data1", "Data2", "Data3" ] )

    // Format entire row
    .formatRow( 1, {
        bold: true,
        fgcolor: "lightblue",
        alignment: "center"
    } );
```

### Column Formatting

```js
sheet = Spreadsheet( "columns.xlsx" )
    .setRowData( 1, [ "Name", "Price", "Quantity" ] )
    .addRow( [ "Widget", 29.99, 5 ] )

    // Format single column
    .formatColumn( 2, {
        dataformat: "$#,##0.00",
        alignment: "right"
    } )

    // Format multiple columns
    .formatColumns( "1,3", {
        alignment: "center"
    } );
```

### Range Formatting

```js
sheet = Spreadsheet( "range.xlsx" )
    .setRowData( 1, [ "Q1", "Q2", "Q3", "Q4" ] )
    .addRow( [ 1000, 1200, 1100, 1300 ] )
    .addRow( [ 800, 900, 950, 1050 ] )

    // Format specific range
    .formatCellRange(
        startRow = 2,
        endRow = 3,
        startColumn = 1,
        endColumn = 4,
        format = {
            dataformat: "#,##0",
            fgcolor: "lightgray",
            alignment: "right"
        }
    );
```

---

## 💡 Formatting Patterns

### Professional Headers

```js
Spreadsheet( "headers.xlsx" )
    .setRowData( 1, [ "Employee", "Department", "Salary", "Start Date" ] )
    .formatRow( 1, {
        bold: true,
        fontsize: 12,
        fontColor: "white",
        fgcolor: "darkblue",
        alignment: "center",
        verticalalignment: "center",
        topborder: "medium",
        bottomborder: "medium",
        leftborder: "thin",
        rightborder: "thin"
    } )
    .setRowHeight( 1, 20 )
    .save();
```

### Financial Reports

```js
Spreadsheet( "financial.xlsx" )
    .setRowData( 1, [ "Account", "Debit", "Credit" ] )
    .addRow( [ "Revenue", "", 100000 ] )
    .addRow( [ "Expenses", 75000, "" ] )
    .addRow( [ "Net Income", "", 25000 ] )

    // Header formatting
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkgreen",
        fontColor: "white",
        alignment: "center"
    } )

    // Currency formatting
    .formatColumns( "2-3", {
        dataformat: "$#,##0.00",
        alignment: "right"
    } )

    // Total row
    .formatRow( 4, {
        bold: true,
        topborder: "double",
        fgcolor: "lightgray"
    } )

    .autoSizeColumns()
    .save();
```

### Status Indicators

```js
// Helper function for status formatting
function getStatusFormat( status ) {
    switch ( status ) {
        case "Active":
            return { fgcolor: "lightgreen", fontColor: "darkgreen", bold: true };
        case "Pending":
            return { fgcolor: "yellow", fontColor: "darkorange", bold: true };
        case "Inactive":
            return { fgcolor: "lightgray", fontColor: "darkgray" };
        default:
            return {};
    }
}

sheet = Spreadsheet( "status.xlsx" )
    .setRowData( 1, [ "Item", "Status" ] );

data = [
    [ "Task 1", "Active" ],
    [ "Task 2", "Pending" ],
    [ "Task 3", "Inactive" ]
];

data.each( ( row, index ) => {
    rowNum = index + 1;
    sheet.setRowData( rowNum, row )
        .formatCell( rowNum, 2, getStatusFormat( row[2] ) );
} );

sheet.save();
```

### Conditional Formatting (Manual)

```js
// Apply formatting based on value
sheet = Spreadsheet( "conditional.xlsx" )
    .setRowData( 1, [ "Student", "Score" ] );

scores = [
    [ "John", 95 ],
    [ "Jane", 72 ],
    [ "Bob", 58 ]
];

scores.each( ( row, index ) => {
    rowNum = index + 1;
    sheet.setRowData( rowNum, row );

    score = row[2];
    format = {};

    if ( score >= 90 ) {
        format = { fgcolor: "lightgreen", bold: true };
    } else if ( score >= 70 ) {
        format = { fgcolor: "yellow" };
    } else {
        format = { fgcolor: "red", fontColor: "white", bold: true };
    }

    sheet.formatCell( rowNum, 2, format );
} );

sheet.save();
```

---

## 📚 Next Steps

{% content-ref url="formulas.md" %}
[formulas.md](formulas.md)
{% endcontent-ref %}

{% content-ref url="advanced-features.md" %}
[advanced-features.md](advanced-features.md)
{% endcontent-ref %}

{% content-ref url="examples.md" %}
[examples.md](examples.md)
{% endcontent-ref %}
