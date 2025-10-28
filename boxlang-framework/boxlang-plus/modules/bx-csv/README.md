---
description: >-
  Premium CSV processing module for high-performance parsing and generation of
  delimited datasets in BoxLang+ applications.
icon: table
---

# CSV +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](./bx-plus/README.md) with a limited trial.
{% endhint %}

The BoxLang CSV module provides a comprehensive and modern API for working with CSV (Comma-Separated Values) files in BoxLang. Built on top of Apache Commons CSV, this module offers both traditional BIF-style functions and a powerful **fluent API** for creating, reading, parsing, and manipulating CSV files.

## ✨ Key Features

- 📊 **Create & Manipulate** - Create new CSV files or work with existing files
- 🔄 **Format Flexibility** - Support for custom delimiters, quotes, escapes, and line separators
- ⚡ **Fluent API** - Modern, chainable interface for elegant code
- 🎯 **Type Support** - Handles strings, numbers, dates, and complex data
- 📦 **Export/Import** - Convert to/from JSON, Query, and arrays of structs
- 🚀 **Streaming** - Memory-efficient processing for large files with `process()`
- 🔍 **Filter & Map** - Transform data on-the-fly during load operations `filter() map()`
- 🎨 **Header Support** - Automatic header detection and manipulation
- 🛠️ **Configurable** - Extensive configuration options for parsing and writing

## 📦 Installation

Install the module using CommandBox:

```bash
box install bx-csv
```

## 🚀 Quick Start

Here's a taste of what you can do with the fluent API:

```javascript
// Create and write a CSV file with fluent API (recommended)
CSV()
    .setHeaders( "Name", "Email", "Age" )
    .addRow( [ "John Doe", "john@example.com", 30 ] )
    .addRow( [ "Jane Smith", "jane@example.com", 25 ] )
    .save( "contacts.csv" );

// Load and parse an existing CSV file
data = CSV( "data.csv" ).toArray();

// Stream process a large file
CSV().process( "huge-file.csv", ( row ) => {
    // Process each row without loading entire file into memory
    println( "Name: " & row[1] );
} );
```

> 💡 **Best Practice**: We recommend using the fluent `CSV()` API directly over the individual BIFs for a more modern, readable, and maintainable codebase.

---

## 🎯 Basic Usage

### Creating a New CSV File

There are multiple ways to create CSV files: using the fluent API (recommended), traditional BIFs, or static constructors.

#### Using Fluent API (Recommended) ✨

```javascript
// Create a new empty CSV file
csv = CSV();

// Create from a path
csv = CSV( "data.csv" );

// Create with custom delimiter
csv = CSV( path="data.csv", delimiter="|" );

// Create with configuration
csv = CSV()
    .delimiter( '|' )
    .headers( true )
    .trim( true );
```

#### Using Static Constructors

```javascript
// Create from JSON
jsonData = '[{"name":"John","age":30},{"name":"Jane","age":25}]';
csv = CSVFile.fromJson( jsonData );

// Create from Array of Structs
data = [
    { "name": "John", "age": 30 },
    { "name": "Jane", "age": 25 }
];
csv = CSVFile.fromArray( data );

// Create from Query
qData = queryExecute( "SELECT name, email FROM users" );
csv = CSVFile.fromQuery( qData );

// Create empty
csv = CSVFile.empty();
```

### Writing Data

#### Setting Headers and Adding Rows

```javascript
// Fluent API - build CSV data
CSV()
    .setHeaders( "Name", "Email", "Age" )
    .addRow( [ "John Doe", "john@example.com", 30 ] )
    .addRow( [ "Jane Smith", "jane@example.com", 25 ] )
    .addRow( [ "Bob Johnson", "bob@example.com", 35 ] )
    .save( "contacts.csv" );
```

#### Setting Row Data by Row Number

```javascript
// Set specific rows (1-based indexing)
CSV()
    .setRowData( 1, [ "Product", "Price", "Quantity" ] )
    .setRowData( 2, [ "Widget A", 10.99, 100 ] )
    .setRowData( 3, [ "Widget B", 15.99, 50 ] )
    .save( "products.csv" );
```

### Reading Data

#### Loading from File

```javascript
// Load entire file into memory
csv = CSV( "data.csv" );

// Or load explicitly
csv = CSV().load( "data.csv" );

// Get all data as array
allData = csv.toArray();

// Get headers
headers = csv.getHeaders();

// Get row count
rowCount = csv.getRowCount();

// Get specific row (1-based)
row2 = csv.getRowData( 2 );
```

#### Loading from String

```javascript
// Parse CSV content from a string
csvContent = "Name,Age,City
John,30,NYC
Jane,25,LA";

csv = CSV().loadFromString( csvContent );
data = csv.toArray();
```

#### Loading with Configuration

```javascript
// Load with custom delimiter and options
csv = CSV()
    .delimiter( '|' )
    .trim( true )
    .skipHeaderRecord( false )
    .load( "data.txt" );
```

### Saving CSV Files

```javascript
// Save to file
csv = CSV()
    .setHeaders( "Col1", "Col2", "Col3" )
    .addRow( [ "A", "B", "C" ] )
    .save( "output.csv" );

// Save with overwrite
csv.overwrite( true ).save( "existing.csv" );

// Save to specific path
csv.setPath( "reports/data.csv" ).save();
```

### Exporting and Importing Data

The CSVFile class provides convenient methods for exporting CSV data to various formats and importing data from those formats.

#### Exporting to JSON

```javascript
// Create CSV and export to JSON
csv = CSV()
    .setHeaders( "Name", "Age", "City" )
    .addRow( [ "John", 30, "New York" ] )
    .addRow( [ "Jane", 25, "Los Angeles" ] );

jsonString = csv.toJson();
// Returns: [{"Name":"John","Age":"30","City":"New York"},{"Name":"Jane","Age":"25","City":"Los Angeles"}]

// Pretty-print JSON
jsonPretty = csv.toJson( true );
```

#### Exporting to Query

```javascript
// Convert CSV to BoxLang Query object
csv = CSV()
    .setHeaders( "Product", "Price", "Quantity" )
    .addRow( [ "Widget A", "10.99", "100" ] )
    .addRow( [ "Widget B", "15.99", "50" ] );

query = csv.toQuery();
// Query object with VARCHAR columns
```

#### Exporting to Array

```javascript
// Export as array of arrays
csv = CSV( "data.csv" );
arrayData = csv.toArray();
```

#### Exporting to String

```javascript
// Convert to CSV string
csv = CSV()
    .setHeaders( "A", "B", "C" )
    .addRow( [ "1", "2", "3" ] );

csvString = csv.toString();
// Returns: "A,B,C\n1,2,3\n"
```

#### Importing from JSON

```javascript
// Create CSV from JSON string
jsonData = '[{"Name":"Alice","Score":95},{"Name":"Bob","Score":87}]';
csv = CSVFile.fromJson( jsonData );
csv.save( "scores.csv" );
```

#### Importing from Array of Structs

```javascript
// Create CSV from array of structs
data = [
    { "Product": "Widget A", "Price": 10.99, "InStock": true },
    { "Product": "Widget B", "Price": 15.99, "InStock": false }
];

csv = CSVFile.fromArray( data );
csv.save( "products.csv" );
```

#### Importing from Query

```javascript
// Create CSV from query results
qData = queryExecute( "SELECT name, email, status FROM users" );
csv = CSVFile.fromQuery( qData );
csv.save( "users-export.csv" );
```

#### Round-trip Export/Import Example

```javascript
// Export to JSON, modify, and import back
original = CSV()
    .setHeaders( "Name", "Email" )
    .addRow( [ "John", "john@example.com" ] );

json = original.toJson();

// Send JSON to API, save to database, etc.
// ...

// Later, import back
imported = CSVFile.fromJson( json );
imported.save( "restored.csv" );
```

---

## 🎨 Intermediate Usage

### Working with Headers

```javascript
// CSV with headers enabled (default)
csv = CSV()
    .headers( true )
    .setHeaders( "Name", "Age", "Email" )
    .addRow( [ "John", 30, "john@example.com" ] );

// Get headers
headers = csv.getHeaders();
// Returns: ["Name", "Age", "Email"]

// CSV without headers
csv = CSV()
    .headers( false )
    .addRow( [ "John", "30", "john@example.com" ] )
    .addRow( [ "Jane", "25", "jane@example.com" ] );
```

### Custom Delimiters and Quotes

```javascript
// Pipe-delimited file
csv = CSV()
    .delimiter( '|' )
    .setHeaders( "Name", "Age", "City" )
    .addRow( [ "John", 30, "New York" ] )
    .save( "data.txt" );

// Tab-delimited (TSV)
csv = CSV()
    .delimiter( '\t' )
    .load( "data.tsv" );

// Custom quote character
csv = CSV()
    .quote( '\'' )
    .escape( '\'' )
    .load( "data.csv" );
```

### Filtering and Mapping Data

```javascript
// Filter rows during load (only include adults)
csv = CSV()
    .filter( ( row ) => {
        return row[2] >= 18; // Age column
    } )
    .load( "people.csv" );

// Transform rows during load (uppercase names)
csv = CSV()
    .map( ( row ) => {
        row[0] = row[0].toUpperCase();
        return row;
    } )
    .load( "data.csv" );

// Combine filter and map
csv = CSV()
    .filter( ( row ) => row[1] != "" ) // Skip empty emails
    .map( ( row ) => {
        row[1] = row[1].trim().toLowerCase();
        return row;
    } )
    .load( "contacts.csv" );
```

### Working with Different Line Separators

```javascript
// Unix line endings
csv = CSV()
    .lineSeparator( "\n" )
    .save( "unix.csv" );

// Windows line endings
csv = CSV()
    .lineSeparator( "\r\n" )
    .save( "windows.csv" );

// Mac classic line endings
csv = CSV()
    .lineSeparator( "\r" )
    .save( "mac.csv" );
```

### Trimming and Space Handling

```javascript
// Trim whitespace from values
csv = CSV()
    .trim( true )
    .load( "data.csv" );

// Ignore surrounding spaces (more comprehensive than trim)
csv = CSV()
    .ignoreSurroundingSpaces( true )
    .load( "data.csv" );
```

### Handling Empty Lines and Comments

```javascript
// Skip empty lines (default: true)
csv = CSV()
    .ignoreEmptyLines( true )
    .load( "data.csv" );

// Support comment lines
csv = CSV()
    .commentMarker( '#' )
    .load( "data.csv" );
// Lines starting with # will be ignored

// Add header comments when writing
csv = CSV()
    .commentMarker( '#' )
    .headerComments( "Generated on " & now(), "Author: System" )
    .setHeaders( "Col1", "Col2" )
    .addRow( [ "A", "B" ] )
    .save( "data.csv" );
```

### Null String Handling

```javascript
// Represent null values as "NULL"
csv = CSV()
    .nullString( "NULL" )
    .addRow( [ "John", null, "NYC" ] )
    .save( "data.csv" );
// Output: John,NULL,NYC

// Read null strings back
csv = CSV()
    .nullString( "NULL" )
    .load( "data.csv" );
```

### Quote Modes

```javascript
// Quote all values
csv = CSV()
    .quoteMode( "ALL" )
    .save( "quoted.csv" );

// Quote only when necessary (default)
csv = CSV()
    .quoteMode( "MINIMAL" )
    .save( "minimal.csv" );

// Quote non-numeric values
csv = CSV()
    .quoteMode( "NON_NUMERIC" )
    .save( "numbers.csv" );

// Never quote
csv = CSV()
    .quoteMode( "NONE" )
    .save( "unquoted.csv" );
```

---

## 🚀 Advanced Usage

### Streaming Large Files

For large CSV files that don't fit in memory, use the `process()` method to stream through rows:

```javascript
// Process a large file without loading into memory
CSV().process( "huge-file.csv", ( row ) => {
    // Process each row individually
    println( "Processing: " & row[1] );

    // Do something with the row (database insert, API call, etc.)
    queryExecute(
        "INSERT INTO table (col1, col2) VALUES (?, ?)",
        [ row[1], row[2] ]
    );
} );

// Process with pre-configured CSV settings
CSV()
    .delimiter( '|' )
    .trim( true )
    .filter( ( row ) => row[2] > 0 ) // Only process positive values
    .process( "data.txt", ( row ) => {
        // Process filtered rows
        processRow( row );
    } );

// Stream with path set beforehand
CSV()
    .setPath( "large-file.csv" )
    .process( ( row ) => {
        // Process each row
        println( row[0] & ": " & row[1] );
    } );
```

### Complex Fluent API Examples

#### Building a Report from Database Query

```javascript
// Query database and export to CSV
qData = queryExecute( "
    SELECT
        customer_name,
        order_date,
        product_name,
        quantity,
        unit_price,
        (quantity * unit_price) AS total
    FROM orders
    WHERE order_date >= ?
", [ dateAdd( "m", -1, now() ) ] );

// Convert to CSV with formatting
CSVFile.fromQuery( qData )
    .delimiter( ',' )
    .quoteMode( "MINIMAL" )
    .trim( true )
    .save( "reports/monthly-orders.csv" );
```

#### Loading, Transforming, and Saving

```javascript
// Load existing CSV, transform data, save to new file
CSV( "input/raw-data.csv" )
    .filter( ( row ) => {
        // Only include rows with valid email
        return row[2].find( "@" ) > 0;
    } )
    .map( ( row ) => {
        // Normalize data
        row[0] = row[0].trim().toUpperCase(); // Name
        row[1] = row[1].trim(); // Phone
        row[2] = row[2].trim().toLowerCase(); // Email
        return row;
    } )
    .trim( true )
    .save( "output/cleaned-data.csv" );
```

#### Processing Multiple Files and Combining

```javascript
// Combine multiple CSV files into one
combined = CSV().setHeaders( "Name", "Email", "Source" );

// Process each file and add to combined
[ "file1.csv", "file2.csv", "file3.csv" ].each( ( file ) => {
    CSV().process( file, ( row ) => {
        // Skip header row if present
        if ( row[1] != "Name" ) {
            // Add source file name
            combined.addRow( [ row[1], row[2], file ] );
        }
    } );
} );

combined.save( "combined-output.csv" );
```

#### Converting Between Formats

```javascript
// CSV to JSON
CSV( "data.csv" ).toJson( true ); // Pretty-printed

// JSON to CSV
CSVFile.fromJson( myJsonString ).save( "output.csv" );

// Query to CSV
CSVFile.fromQuery( myQuery ).save( "export.csv" );

// CSV to Query
query = CSV( "data.csv" ).toQuery();
```

### Handling Duplicate Headers

```javascript
// Allow duplicate column names
csv = CSV()
    .allowDuplicateHeaderNames( true )
    .load( "data-with-dupes.csv" );

// Disallow duplicates (throws exception)
csv = CSV()
    .allowDuplicateHeaderNames( false )
    .load( "data.csv" );
```

### Skip Header Record Configuration

```javascript
// Skip first row as header (default: true)
csv = CSV()
    .skipHeaderRecord( true )
    .load( "data.csv" );
// First row becomes column names, not included in data

// Include header row in data (skipHeaderRecord=false)
csv = CSV()
    .skipHeaderRecord( false )
    .load( "data.csv" );
// First row is treated as data
```

### Auto-flush and Trailing Delimiters

```javascript
// Auto-flush after each record (better reliability, slower)
csv = CSV()
    .autoFlush( true )
    .addRow( [ "A", "B", "C" ] )
    .save( "data.csv" );

// Add trailing delimiter at end of each row
csv = CSV()
    .trailingDelimiter( true )
    .save( "data.csv" );
// Output: A,B,C,
```

### Performance Tips

```javascript
// For large in-memory datasets:
// - Use filter/map to reduce data size during load
// - Use streaming process() for files > 100MB

// For frequent writes:
// - Disable autoFlush for better performance
// - Build data in memory, save once

// For reading multiple files:
// - Use process() to avoid memory issues
// - Consider parallel processing in separate threads

// Example: Efficient processing
CSV()
    .ignoreEmptyLines( true )
    .trim( true )
    .filter( ( row ) => row[1] != "" ) // Skip invalid rows early
    .process( "large-file.csv", ( row ) => {
        // Minimal processing per row
        saveToDatabase( row );
    } );
```

---

## 📚 Reference Documentation

For complete API documentation and detailed method references:

- **[CSV BIF Reference](reference/built-in-functions/CSV.md)** - Complete documentation for the `CSV()` function
- **[Fluent API Reference](reference/Fluent%20API/README.md)** - Complete list of all chainable methods
- **[Reference Overview](reference/README.md)** - Browse all available references

---

## 🤝 Support & Community

- 📖 **[BoxLang Documentation](https://boxlang.ortusbooks.com)** - Official language documentation
- 💬 **[Community Slack](https://community.ortussolutions.com)** - Get help from the community
- 🐛 **[Issue Tracker](https://github.com/ortus-boxlang/boxlang/issues)** - Report bugs and request features
- 📧 **[Professional Support](https://www.ortussolutions.com/services)** - Commercial support options
