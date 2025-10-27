---
description: Real-world examples and complete code samples for common spreadsheet tasks
icon: code
---

# 💡 Examples

Real-world examples demonstrating common spreadsheet tasks using the BoxLang Fluent API. Copy and adapt these patterns for your own projects.

---

## 📊 Report Generation

### Monthly Sales Report

```js
// Query sales data
sales = queryExecute("
    SELECT
        product_name,
        SUM(quantity) as units_sold,
        SUM(total_amount) as revenue,
        COUNT(DISTINCT order_id) as orders
    FROM sales
    WHERE MONTH(sale_date) = MONTH(CURRENT_DATE)
    GROUP BY product_name
    ORDER BY revenue DESC
");

// Create report
Spreadsheet( "monthly-sales-#month(now())#-#year(now())#.xlsx" )
    // Title
    .setCellValue( 1, 1, "Monthly Sales Report" )
    .mergeCells( 1, 1, 1, 4 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 16,
        alignment: "center",
        fgcolor: "darkblue",
        fontColor: "white"
    } )
    .setRowHeight( 1, 25 )

    // Report date
    .setCellValue( 2, 1, "Report Date:" )
    .setCellValue( 2, 2, dateFormat( now(), "mmmm dd, yyyy" ) )
    .formatRow( 2, { italic: true } )

    // Headers
    .setRowData( 4, [ "Product", "Units Sold", "Revenue", "Orders" ] )
    .formatRow( 4, {
        bold: true,
        fgcolor: "lightblue",
        alignment: "center"
    } )

    // Data
    .addRows( sales, startRow = 5 )

    // Totals
    .setRowData( sales.recordCount + 5, [
        "TOTAL",
        "=SUM(B5:B#sales.recordCount + 4#)",
        "=SUM(C5:C#sales.recordCount + 4#)",
        "=SUM(D5:D#sales.recordCount + 4#)"
    ] )
    .formatRow( sales.recordCount + 5, {
        bold: true,
        fgcolor: "lightgray",
        topborder: "double"
    } )

    // Format columns
    .formatColumn( 2, { dataformat: "#,##0", alignment: "right" } )
    .formatColumn( 3, { dataformat: "$#,##0.00", alignment: "right" } )
    .formatColumn( 4, { dataformat: "#,##0", alignment: "right" } )

    // Auto-size and freeze header
    .autoSizeColumns()
    .addFreezePane( 0, 4 )

    .save();
```

### Financial Statement

```js
// Create balance sheet
Spreadsheet( "balance-sheet-#year(now())#.xlsx" )
    // Title
    .setCellValue( 1, 1, "Balance Sheet" )
    .setCellValue( 2, 1, "As of #dateFormat(now(), 'mmmm dd, yyyy')#" )
    .mergeCells( 1, 1, 1, 3 )
    .mergeCells( 2, 1, 2, 3 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 18,
        alignment: "center"
    } )
    .formatCell( 2, 1, {
        italic: true,
        alignment: "center"
    } )

    // Assets section
    .setCellValue( 4, 1, "ASSETS" )
    .formatCell( 4, 1, {
        bold: true,
        underline: true,
        fontsize: 14
    } )
    .setRowData( 5, [ "Current Assets" ] )
    .setRowData( 6, [ "  Cash", 50000 ] )
    .setRowData( 7, [ "  Accounts Receivable", 25000 ] )
    .setRowData( 8, [ "  Inventory", 15000 ] )
    .setRowData( 9, [ "Total Current Assets", "=SUM(B6:B8)" ] )
    .formatRow( 9, { bold: true, topborder: "thin" } )

    .setRowData( 11, [ "Fixed Assets" ] )
    .setRowData( 12, [ "  Equipment", 100000 ] )
    .setRowData( 13, [ "  Buildings", 250000 ] )
    .setRowData( 14, [ "Total Fixed Assets", "=SUM(B12:B13)" ] )
    .formatRow( 14, { bold: true, topborder: "thin" } )

    .setRowData( 16, [ "TOTAL ASSETS", "=B9+B14" ] )
    .formatRow( 16, {
        bold: true,
        topborder: "double",
        bottomborder: "double",
        fgcolor: "lightgray"
    } )

    // Liabilities section
    .setCellValue( 18, 1, "LIABILITIES & EQUITY" )
    .formatCell( 18, 1, {
        bold: true,
        underline: true,
        fontsize: 14
    } )
    .setRowData( 19, [ "Current Liabilities" ] )
    .setRowData( 20, [ "  Accounts Payable", 20000 ] )
    .setRowData( 21, [ "  Short-term Loans", 10000 ] )
    .setRowData( 22, [ "Total Current Liabilities", "=SUM(B20:B21)" ] )
    .formatRow( 22, { bold: true, topborder: "thin" } )

    .setRowData( 24, [ "Owner's Equity", "=B16-B22" ] )
    .formatRow( 24, { bold: true } )

    .setRowData( 26, [ "TOTAL LIABILITIES & EQUITY", "=B22+B24" ] )
    .formatRow( 26, {
        bold: true,
        topborder: "double",
        bottomborder: "double",
        fgcolor: "lightgray"
    } )

    // Format all currency
    .formatColumn( 2, {
        dataformat: "$#,##0.00",
        alignment: "right"
    } )

    .setColumnWidth( 1, 30 )
    .setColumnWidth( 2, 20 )

    .save();
```

---

## 📈 Data Analysis

### Sales Trend Analysis

```js
// Get monthly sales data
monthlySales = queryExecute("
    SELECT
        DATE_FORMAT(sale_date, '%Y-%m') as month,
        SUM(total_amount) as revenue
    FROM sales
    WHERE sale_date >= DATE_SUB(CURRENT_DATE, INTERVAL 12 MONTH)
    GROUP BY month
    ORDER BY month
");

Spreadsheet( "sales-trend-analysis.xlsx" )
    .setRowData( 1, [ "Month", "Revenue", "Prior Month", "Change", "% Change" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white"
    } )

    // Add data
    .addRows( monthlySales, startRow = 2 )

    // Calculate month-over-month change
    .setCellValue( 2, 3, "" )  // No prior month for first row
    .setCellValue( 2, 4, "" )
    .setCellValue( 2, 5, "" );

// Add formulas for remaining rows
for ( i = 3; i <= monthlySales.recordCount + 1; i++ ) {
    sheet.setCellFormula( i, 3, "B#i-1#" )  // Prior month
        .setCellFormula( i, 4, "B#i#-C#i#" )  // Change
        .setCellFormula( i, 5, "D#i#/C#i#" );  // % Change
}

sheet.formatColumn( 2, { dataformat: "$#,##0.00" } )
    .formatColumn( 3, { dataformat: "$#,##0.00" } )
    .formatColumn( 4, { dataformat: "$#,##0.00" } )
    .formatColumn( 5, { dataformat: "0.0%" } )
    .autoSizeColumns()
    .save();
```

### Customer Segmentation

```js
// Segment customers by purchase behavior
customers = queryExecute("
    SELECT
        customer_name,
        total_orders,
        total_spent,
        avg_order_value,
        last_order_date
    FROM customer_summary
    ORDER BY total_spent DESC
");

sheet = Spreadsheet( "customer-segmentation.xlsx" )
    .setRowData( 1, [ "Customer", "Orders", "Total Spent", "Avg Order", "Last Order", "Segment" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkgreen",
        fontColor: "white"
    } )
    .addRows( customers, startRow = 2 );

// Apply segmentation logic
for ( i = 2; i <= customers.recordCount + 1; i++ ) {
    // Get values
    totalSpent = sheet.getCellValue( i, 3 );

    // Determine segment
    if ( totalSpent >= 10000 ) {
        segment = "VIP";
        format = { fgcolor: "gold", bold: true };
    } else if ( totalSpent >= 5000 ) {
        segment = "Premium";
        format = { fgcolor: "lightblue" };
    } else if ( totalSpent >= 1000 ) {
        segment = "Standard";
        format = { fgcolor: "lightgreen" };
    } else {
        segment = "New";
        format = { fgcolor: "lightgray" };
    }

    sheet.setCellValue( i, 6, segment )
        .formatCell( i, 6, format );
}

sheet.formatColumn( 3, { dataformat: "$#,##0.00" } )
    .formatColumn( 4, { dataformat: "$#,##0.00" } )
    .formatColumn( 5, { dataformat: "mm/dd/yyyy" } )
    .autoSizeColumns()
    .addFreezePane( 0, 1 )
    .save();
```

---

## 📋 Inventory Management

### Stock Level Report

```js
// Get inventory data
inventory = queryExecute("
    SELECT
        product_code,
        product_name,
        current_stock,
        reorder_level,
        reorder_quantity,
        unit_cost
    FROM inventory
    ORDER BY product_name
");

sheet = Spreadsheet( "inventory-#dateFormat(now(), 'yyyymmdd')#.xlsx" )
    .setRowData( 1, [ "Code", "Product", "Stock", "Reorder At", "Reorder Qty", "Unit Cost", "Status" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white",
        alignment: "center"
    } )
    .addRows( inventory, startRow = 2 );

// Add status and formatting
for ( i = 2; i <= inventory.recordCount + 1; i++ ) {
    stock = sheet.getCellValue( i, 3 );
    reorderLevel = sheet.getCellValue( i, 4 );

    if ( stock <= 0 ) {
        status = "OUT OF STOCK";
        format = { fgcolor: "red", fontColor: "white", bold: true };
    } else if ( stock <= reorderLevel ) {
        status = "REORDER NOW";
        format = { fgcolor: "orange", bold: true };
    } else if ( stock <= reorderLevel * 1.5 ) {
        status = "Low Stock";
        format = { fgcolor: "yellow" };
    } else {
        status = "OK";
        format = { fgcolor: "lightgreen" };
    }

    sheet.setCellValue( i, 7, status )
        .formatCell( i, 7, format );
}

sheet.formatColumn( 6, { dataformat: "$#,##0.00" } )
    .formatColumns( "3-5", { dataformat: "#,##0", alignment: "right" } )
    .autoSizeColumns()
    .addFreezePane( 0, 1 )
    .save();
```

---

## 👥 HR & Employee Management

### Employee Directory

```js
employees = queryExecute("
    SELECT
        employee_id,
        first_name,
        last_name,
        department,
        title,
        email,
        phone,
        hire_date
    FROM employees
    WHERE active = 1
    ORDER BY last_name, first_name
");

Spreadsheet( "employee-directory.xlsx" )
    .setRowData( 1, [ "ID", "First Name", "Last Name", "Department", "Title", "Email", "Phone", "Hire Date", "Years" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white",
        alignment: "center"
    } )
    .addRows( employees, startRow = 2 );

// Calculate years of service
lastRow = employees.recordCount + 1;
for ( i = 2; i <= lastRow; i++ ) {
    sheet.setCellFormula( i, 9, "DATEDIF(H#i#,TODAY(),""Y"")" );
}

sheet.formatColumn( 8, { dataformat: "mm/dd/yyyy" } )
    .formatColumn( 9, { alignment: "center" } )
    .autoSizeColumns()
    .addFreezePane( 0, 1 )
    .save();
```

### Payroll Summary

```js
payroll = queryExecute("
    SELECT
        employee_name,
        base_salary,
        overtime_hours,
        overtime_rate,
        bonus
    FROM current_payroll
    ORDER BY employee_name
");

Spreadsheet( "payroll-#month(now())#-#year(now())#.xlsx" )
    .setRowData( 1, [ "Employee", "Base Salary", "OT Hours", "OT Rate", "OT Pay", "Bonus", "Gross Pay" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkgreen",
        fontColor: "white"
    } )
    .addRows( payroll, startRow = 2 );

// Calculate overtime pay and gross pay
for ( i = 2; i <= payroll.recordCount + 1; i++ ) {
    sheet.setCellFormula( i, 5, "C#i#*D#i#" )  // OT Pay
        .setCellFormula( i, 7, "B#i#+E#i#+F#i#" );  // Gross Pay
}

// Add totals
totalRow = payroll.recordCount + 2;
sheet.setRowData( totalRow, [
    "TOTAL",
    "=SUM(B2:B#payroll.recordCount + 1#)",
    "",
    "",
    "=SUM(E2:E#payroll.recordCount + 1#)",
    "=SUM(F2:F#payroll.recordCount + 1#)",
    "=SUM(G2:G#payroll.recordCount + 1#)"
] )
.formatRow( totalRow, {
    bold: true,
    topborder: "double",
    fgcolor: "lightgray"
} );

sheet.formatColumns( "2,4-7", { dataformat: "$#,##0.00" } )
    .formatColumn( 3, { dataformat: "0.0", alignment: "right" } )
    .autoSizeColumns()
    .protectSheet( password = "payroll2024" )  // Protect sensitive data
    .save();
```

---

## 🎓 Education

### Grade Book

```js
students = queryExecute("
    SELECT
        student_name,
        exam1,
        exam2,
        exam3,
        project,
        participation
    FROM grades
    WHERE class_id = ?
    ORDER BY student_name
", [ classId ]);

Spreadsheet( "gradebook-#className#.xlsx" )
    // Title
    .setCellValue( 1, 1, "#className# - Grade Book" )
    .mergeCells( 1, 1, 1, 8 )
    .formatCell( 1, 1, {
        bold: true,
        fontsize: 16,
        alignment: "center",
        fgcolor: "darkblue",
        fontColor: "white"
    } )

    // Headers
    .setRowData( 2, [ "Student", "Exam 1", "Exam 2", "Exam 3", "Project", "Participation", "Final Grade", "Letter" ] )
    .formatRow( 2, {
        bold: true,
        fgcolor: "lightblue",
        alignment: "center"
    } )

    // Add student data
    .addRows( students, startRow = 3 );

// Calculate final grades
// Weights: Exams (20% each), Project (30%), Participation (10%)
for ( i = 3; i <= students.recordCount + 2; i++ ) {
    // Final grade calculation
    sheet.setCellFormula( i, 7, "(B#i#*0.2)+(C#i#*0.2)+(D#i#*0.2)+(E#i#*0.3)+(F#i#*0.1)" );

    // Letter grade
    sheet.setCellFormula( i, 8,
        'IF(G#i#>=90,"A",IF(G#i#>=80,"B",IF(G#i#>=70,"C",IF(G#i#>=60,"D","F"))))'
    );
}

// Format and conditional formatting for letter grades
sheet.formatColumns( "2-7", { dataformat: "0.0", alignment: "center" } );

for ( i = 3; i <= students.recordCount + 2; i++ ) {
    grade = sheet.getCellValue( i, 8 );

    switch ( grade ) {
        case "A":
            format = { fgcolor: "lightgreen", bold: true };
            break;
        case "B":
            format = { fgcolor: "lightblue" };
            break;
        case "C":
            format = { fgcolor: "yellow" };
            break;
        case "D":
        case "F":
            format = { fgcolor: "red", fontColor: "white", bold: true };
            break;
    }

    sheet.formatCell( i, 8, format );
}

sheet.autoSizeColumns()
    .addFreezePane( 0, 2 )
    .save();
```

---

## 🛒 E-commerce

### Order Export

```js
orders = queryExecute("
    SELECT
        o.order_number,
        o.order_date,
        c.customer_name,
        c.email,
        o.subtotal,
        o.tax,
        o.shipping,
        o.total,
        o.status
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    WHERE o.order_date >= ?
    ORDER BY o.order_date DESC
", [ dateAdd( "d", -30, now() ) ]);

Spreadsheet( "orders-#dateFormat(now(), 'yyyymmdd')#.xlsx" )
    .setRowData( 1, [ "Order ##", "Date", "Customer", "Email", "Subtotal", "Tax", "Shipping", "Total", "Status" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white"
    } )
    .addRows( orders, startRow = 2 );

// Format and color-code by status
for ( i = 2; i <= orders.recordCount + 1; i++ ) {
    status = sheet.getCellValue( i, 9 );

    switch ( status ) {
        case "Completed":
            format = { fgcolor: "lightgreen" };
            break;
        case "Processing":
            format = { fgcolor: "yellow" };
            break;
        case "Pending":
            format = { fgcolor: "orange" };
            break;
        case "Cancelled":
            format = { fgcolor: "lightgray" };
            break;
    }

    if ( !isNull( format ) ) {
        sheet.formatCell( i, 9, format );
    }
}

// Add summary
summaryRow = orders.recordCount + 3;
sheet.setRowData( summaryRow, [ "SUMMARY" ] )
    .formatRow( summaryRow, { bold: true, fontsize: 12 } )
    .setRowData( summaryRow + 1, [ "Total Orders:", orders.recordCount ] )
    .setRowData( summaryRow + 2, [ "Total Revenue:", "=SUM(H2:H#orders.recordCount + 1#)" ] )
    .formatCell( summaryRow + 2, 2, { dataformat: "$#,##0.00", bold: true } );

sheet.formatColumn( 2, { dataformat: "mm/dd/yyyy" } )
    .formatColumns( "5-8", { dataformat: "$#,##0.00" } )
    .autoSizeColumns()
    .addFreezePane( 0, 1 )
    .save();
```

---

## 🏥 Healthcare

### Patient Appointment Schedule

```js
appointments = queryExecute("
    SELECT
        appointment_date,
        appointment_time,
        patient_name,
        patient_phone,
        doctor_name,
        appointment_type,
        status
    FROM appointments
    WHERE appointment_date BETWEEN ? AND ?
    ORDER BY appointment_date, appointment_time
", [ startDate, endDate ]);

Spreadsheet( "appointments-#dateFormat(startDate, 'yyyymmdd')#.xlsx" )
    .setRowData( 1, [ "Date", "Time", "Patient", "Phone", "Doctor", "Type", "Status" ] )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white",
        alignment: "center"
    } )
    .addRows( appointments, startRow = 2 );

// Status color coding
for ( i = 2; i <= appointments.recordCount + 1; i++ ) {
    status = sheet.getCellValue( i, 7 );

    switch ( status ) {
        case "Confirmed":
            format = { fgcolor: "lightgreen", bold: true };
            break;
        case "Pending":
            format = { fgcolor: "yellow" };
            break;
        case "Cancelled":
            format = { fgcolor: "red", fontColor: "white" };
            break;
        case "Completed":
            format = { fgcolor: "lightgray" };
            break;
    }

    sheet.formatCell( i, 7, format );
}

sheet.formatColumn( 1, { dataformat: "mm/dd/yyyy" } )
    .formatColumn( 2, { dataformat: "h:mm AM/PM" } )
    .autoSizeColumns()
    .addFreezePane( 0, 1 )
    .protectSheet( password = "medical2024" )  // HIPAA protection
    .save();
```

---

## 📚 Next Steps

Now that you've seen practical examples, explore the complete API reference:

{% content-ref url="reference/fluent-api/" %}
[fluent-api](reference/fluent-api/)
{% endcontent-ref %}

{% content-ref url="reference/built-in-functions/" %}
[built-in-functions](reference/built-in-functions/)
{% endcontent-ref %}

{% content-ref url="reference/components/" %}
[components](reference/components/)
{% endcontent-ref %}
