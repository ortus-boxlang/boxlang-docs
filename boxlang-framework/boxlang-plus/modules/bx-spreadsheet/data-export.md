---
description: Export spreadsheet data to CSV, JSON, HTML, and query formats
icon: file-export
---

# 💾 Data Export Guide

Learn how to export spreadsheet data to various formats using the BoxLang Fluent API. Convert Excel files to CSV, JSON, HTML, queries, and more.

---

## 📄 Export to CSV

### Basic CSV Export

```js
// Load and export to CSV
csv = Spreadsheet( "employees.xlsx", load = true ).toCSV();

// Save to file
fileWrite( "employees.csv", csv );
```

### CSV with Custom Delimiter

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Export with semicolon delimiter
csv = sheet.toCSV( delimiter = ";" );

// Export with tab delimiter
csv = sheet.toCSV( delimiter = chr(9) );

fileWrite( "data.csv", csv );
```

### CSV from Specific Sheet

```js
sheet = Spreadsheet( "workbook.xlsx", load = true );

// Select specific sheet
sheet.selectSheet( "Sales Data" );

// Export that sheet only
csv = sheet.toCSV();

fileWrite( "sales.csv", csv );
```

### CSV with Headers

```js
data = [
    [ "John Doe", "Engineering", 95000 ],
    [ "Jane Smith", "Marketing", 85000 ]
];

csv = Spreadsheet()
    .setRowData( 1, [ "Name", "Department", "Salary" ] )
    .addRows( data )
    .toCSV();

fileWrite( "employees.csv", csv );
```

---

## 🔤 Export to JSON

### Array of Objects

```js
// Load spreadsheet
sheet = Spreadsheet( "employees.xlsx", load = true );

// Convert to JSON (uses first row as keys)
json = sheet.toJson();

// Result format:
// [
//     {"Name":"John Doe","Department":"Engineering","Salary":95000},
//     {"Name":"Jane Smith","Department":"Marketing","Salary":85000}
// ]

fileWrite( "employees.json", json );
```

### Pretty-Printed JSON

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get as array first
data = sheet.toArray();

// Serialize with formatting
json = serializeJSON( data, true );

fileWrite( "data-pretty.json", json );
```

### JSON with Custom Structure

```js
sheet = Spreadsheet( "products.xlsx", load = true );

// Convert to array
products = sheet.toArray();

// Transform structure
output = {
    "exportDate": dateFormat( now(), "yyyy-mm-dd" ),
    "totalProducts": products.len(),
    "products": products
};

fileWrite( "products.json", serializeJSON( output, true ) );
```

---

## 🗄️ Export to Query

### Basic Query Conversion

```js
// Load and convert to query
qry = Spreadsheet( "employees.xlsx", load = true ).toQuery();

// Now you can use query functions
writeDump( qry );

// Loop through query
for ( row in qry ) {
    writeOutput( "#row.Name# - #row.Department#<br>" );
}
```

### Query with Custom Column Names

```js
sheet = Spreadsheet()
    .setRowData( 1, [ "Full Name", "Job Title", "Annual Salary" ] )
    .addRow( [ "John Doe", "Engineer", 95000 ] );

// First row becomes column names (spaces replaced with underscores)
qry = sheet.toQuery();

// Access with: qry.Full_Name, qry.Job_Title, qry.Annual_Salary
```

### Query from Specific Range

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get specific rows as array
rows = sheet.getRows( startRow = 5, endRow = 20 );

// Convert to query
qry = queryNew( "Col1,Col2,Col3", "varchar,varchar,numeric" );

for ( row in rows ) {
    queryAddRow( qry, {
        "Col1": row[1],
        "Col2": row[2],
        "Col3": row[3]
    } );
}
```

---

## 🌐 Export to HTML

### Simple HTML Table

```js
html = Spreadsheet( "report.xlsx", load = true ).toHtml();

// Generates complete HTML table
fileWrite( "report.html", html );
```

### HTML with Custom Styling

```js
sheet = Spreadsheet( "data.xlsx", load = true );

html = '
<!DOCTYPE html>
<html>
<head>
    <title>Data Export</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        th { background: ##4CAF50; color: white; padding: 10px; }
        td { border: 1px solid ##ddd; padding: 8px; }
        tr:nth-child(even) { background: ##f2f2f2; }
    </style>
</head>
<body>
    <h1>Exported Data</h1>
    #sheet.toHtml()#
</body>
</html>
';

fileWrite( "styled-report.html", html );
```

---

## 📦 Export to Array

### Array of Arrays

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get all data as array of arrays
data = sheet.toArray( includeHeaderRow = false );

// Result: [ ["John", "Engineering"], ["Jane", "Marketing"] ]

// Access data
for ( row in data ) {
    writeOutput( "#row[1]# - #row[2]#<br>" );
}
```

### Array of Structs

```js
sheet = Spreadsheet( "employees.xlsx", load = true );

// Convert to array of structs (default behavior)
employees = sheet.toArray();

// Result: [
//     { "Name": "John", "Department": "Engineering" },
//     { "Name": "Jane", "Department": "Marketing" }
// ]

// Access using keys
for ( employee in employees ) {
    writeOutput( "#employee.Name# works in #employee.Department#<br>" );
}
```

### Array with Specific Columns

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get specific columns
names = sheet.getColumn( 1 );       // First column
salaries = sheet.getColumn( 3 );    // Third column

// Combine into new structure
data = names.map( ( name, index ) => {
    return {
        "name": name,
        "salary": salaries[ index ]
    };
} );
```

---

## 🔄 Batch Export

### Export All Sheets to CSV

```js
sheet = Spreadsheet( "workbook.xlsx", load = true );

// Get all sheet names
sheetNames = sheet.getSheetNames();

// Export each sheet
for ( sheetName in sheetNames ) {
    sheet.selectSheet( sheetName );
    csv = sheet.toCSV();

    // Save with sheet name
    fileName = "#sheetName#.csv";
    fileWrite( fileName, csv );
}
```

### Export Multiple Formats

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Export to multiple formats
formats = [
    { extension: "csv", content: sheet.toCSV() },
    { extension: "json", content: sheet.toJson() },
    { extension: "html", content: sheet.toHtml() }
];

// Save each format
for ( format in formats ) {
    fileWrite( "export.#format.extension#", format.content );
}
```

---

## 🎯 Export Patterns

### Pattern: Filtered Export

```js
// Load data
employees = Spreadsheet( "employees.xlsx", load = true ).toArray();

// Filter data
engineeringStaff = employees.filter( ( emp ) => emp.Department == "Engineering" );

// Export filtered data
Spreadsheet()
    .setRowData( 1, [ "Name", "Department", "Salary" ] )
    .addRows( engineeringStaff.map( ( emp ) =>
        [ emp.Name, emp.Department, emp.Salary ]
    ) )
    .save( "engineering-staff.xlsx" );
```

### Pattern: Transformed Export

```js
// Load data
products = Spreadsheet( "products.xlsx", load = true ).toArray();

// Transform data
transformed = products.map( ( product ) => {
    return {
        "code": product.ProductCode,
        "name": product.ProductName,
        "price": dollarFormat( product.Price ),
        "available": product.Stock > 0 ? "Yes" : "No"
    };
} );

// Export as JSON
fileWrite( "products-api.json", serializeJSON( transformed, true ) );
```

### Pattern: Export with Metadata

```js
// Load and process data
sheet = Spreadsheet( "sales.xlsx", load = true );
data = sheet.toArray();

// Create export package
export = {
    "metadata": {
        "exportDate": dateFormat( now(), "yyyy-mm-dd HH:nn:ss" ),
        "recordCount": data.len(),
        "source": "sales.xlsx",
        "version": "1.0"
    },
    "data": data
};

fileWrite( "sales-export.json", serializeJSON( export, true ) );
```

### Pattern: Chunked Export

```js
// Load large dataset
sheet = Spreadsheet( "large-file.xlsx", load = true );
allData = sheet.toArray();

// Export in chunks
chunkSize = 1000;
chunks = ceiling( allData.len() / chunkSize );

for ( i = 1; i <= chunks; i++ ) {
    startIdx = ( i - 1 ) * chunkSize + 1;
    endIdx = min( i * chunkSize, allData.len() );

    chunk = allData.slice( startIdx, endIdx );

    // Export chunk
    json = serializeJSON( chunk );
    fileWrite( "chunk-#i#.json", json );
}
```

---

## 📊 Export for APIs

### REST API Response

```js
// Load data
products = Spreadsheet( "products.xlsx", load = true ).toArray();

// Transform for API
apiResponse = {
    "success": true,
    "count": products.len(),
    "data": products.map( ( p ) => {
        return {
            "id": p.ID,
            "name": p.Name,
            "price": numberFormat( p.Price, "0.00" ),
            "inStock": p.Stock > 0
        };
    } )
};

// Return as JSON (in API handler)
return serializeJSON( apiResponse );
```

### GraphQL Response Format

```js
// Load data
employees = Spreadsheet( "employees.xlsx", load = true ).toArray();

// Format for GraphQL
graphQLResponse = {
    "data": {
        "employees": employees.map( ( emp ) => {
            return {
                "id": hash( emp.Email ),
                "name": emp.Name,
                "department": {
                    "name": emp.Department
                },
                "salary": emp.Salary
            };
        } )
    }
};

return serializeJSON( graphQLResponse );
```

---

## 📦 Export to Binary

### Get Spreadsheet as Binary

```js
sheet = Spreadsheet()
    .setRowData( 1, [ "Data" ] )
    .addRow( [ "Value" ] );

// Get as binary
binary = sheet.toBinary();

// Save binary
fileWrite( "output.xlsx", binary );

// Or serve as download
cfheader( name="Content-Disposition", value='attachment; filename="export.xlsx"' );
cfcontent( type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", variable=binary );
```

### Stream Binary Download

```js
// Create spreadsheet
sheet = Spreadsheet();
sheet.setRowData( 1, [ "Report Data" ] );
// ... add data ...

// Get binary
binary = sheet.toBinary();

// Set headers for download
cfheader( name="Content-Type", value="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" );
cfheader( name="Content-Disposition", value='attachment; filename="report-#dateFormat(now(),"yyyy-mm-dd")#.xlsx"' );
cfheader( name="Content-Length", value=arrayLen( binary ) );

// Send binary
cfcontent( variable=binary, reset=true );
```

---

## 🔄 Import and Export Pipeline

### CSV to Excel

```js
// Read CSV file
csvData = fileRead( "input.csv" );
lines = csvData.split( chr(10) );

// Create Excel file
sheet = Spreadsheet( "output.xlsx" );

for ( line in lines ) {
    row = line.split( "," );
    sheet.addRow( row );
}

// Format and save
sheet.formatRow( 1, { bold: true } )
    .autoSizeColumns()
    .save();
```

### Excel to Database

```js
// Load Excel file
employees = Spreadsheet( "new-employees.xlsx", load = true ).toArray();

// Insert into database
for ( emp in employees ) {
    queryExecute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        [ emp.Name, emp.Department, emp.Salary ]
    );
}
```

### Database to Excel Export

```js
// Query database
employees = queryExecute(
    "SELECT name, department, salary, hire_date FROM employees ORDER BY name"
);

// Export to Excel
Spreadsheet( "employee-export.xlsx" )
    .addRows( employees, includeColumnNames = true )
    .formatRow( 1, {
        bold: true,
        fgcolor: "darkblue",
        fontColor: "white"
    } )
    .formatColumn( 3, { dataformat: "$#,##0.00" } )
    .formatColumn( 4, { dataformat: "mm/dd/yyyy" } )
    .autoSizeColumns()
    .save();

// Also export to CSV
csv = Spreadsheet( "employee-export.xlsx", load = true ).toCSV();
fileWrite( "employee-export.csv", csv );
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
