---
description: Fluent API methods for CSVFile class in BoxLang Plus
icon: table
---

# CSVFile Fluent API Methods

The CSVFile class provides a fluent, chainable API for all CSV operations.

## Static Constructors

### **`CSVFile.empty()`**

- Creates an empty CSVFile instance
- Returns: CSVFile object

### **`CSVFile.fromJson( jsonString )`**

- Creates CSVFile from JSON array of objects
- Parameters: `jsonString` (string) - JSON array
- Returns: CSVFile object
- Example: `CSVFile.fromJson('[{"name":"John","age":30}]')`

### **`CSVFile.fromArray( arrayOfStructs )`**

- Creates CSVFile from array of structs
- Parameters: `arrayOfStructs` (array) - Array of structs
- Returns: CSVFile object

### **`CSVFile.fromQuery( query )`**

- Creates CSVFile from BoxLang Query
- Parameters: `query` (Query) - Query object
- Returns: CSVFile object

## File I/O Methods

### **`load( path )`**

- Loads CSV file from specified path
- Parameters: `path` (string) - File path
- Returns: this (for chaining)
- Example: `csv.load("data.csv")`

### **`loadFromString( csvContent )`**

- Loads CSV data from a string
- Parameters: `csvContent` (string) - CSV content
- Returns: this (for chaining)

### **`loadFromJson( jsonString )`**

- Loads CSV data from JSON string
- Parameters: `jsonString` (string) - JSON array
- Returns: this (for chaining)

### **`loadFromQuery( query )`**

- Loads CSV data from Query object
- Parameters: `query` (Query) - Query object
- Returns: this (for chaining)

### **`loadFromArray( arrayOfStructs )`**

- Loads CSV data from array of structs
- Parameters: `arrayOfStructs` (array) - Array of structs
- Returns: this (for chaining)

### **`save( path, [overwrite] )`**

- Saves CSV file to specified path
- Parameters:
  - `path` (string) - File path
  - `overwrite` (optional, boolean) - Whether to overwrite existing file
- Returns: this (for chaining)
- Example: `csv.save("output.csv", true)`

### **`save()`**

- Saves CSV file using previously set path
- Returns: this (for chaining)

## Configuration Methods

### **`delimiter( char )`**

- Sets delimiter character
- Parameters: `char` (character) - Delimiter (e.g., ',', '|', '\t')
- Returns: this (for chaining)
- Example: `csv.delimiter('|')`

### **`quote( char )`**

- Sets quote character
- Parameters: `char` (character) - Quote character (default: '"')
- Returns: this (for chaining)

### **`escape( char )`**

- Sets escape character
- Parameters: `char` (character) - Escape character (default: '"')
- Returns: this (for chaining)

### **`lineSeparator( string )`**

- Sets line separator string
- Parameters: `string` (string) - Line separator (e.g., "\n", "\r\n")
- Returns: this (for chaining)

### **`trim( boolean )`**

- Sets whether to trim whitespace from values
- Parameters: `boolean` (boolean) - Enable/disable trimming
- Returns: this (for chaining)

### **`headers( boolean )`**

- Sets whether CSV has headers in first row
- Parameters: `boolean` (boolean) - Enable/disable headers
- Returns: this (for chaining)

### **`skipHeaderRecord( boolean )`**

- Sets whether to skip header record when parsing
- Parameters: `boolean` (boolean) - Enable/disable skipping
- Returns: this (for chaining)

### **`allowMissingColumnNames( boolean )`**

- Sets whether to allow missing column names
- Parameters: `boolean` (boolean) - Enable/disable
- Returns: this (for chaining)

### **`ignoreEmptyLines( boolean )`**

- Sets whether to ignore empty lines
- Parameters: `boolean` (boolean) - Enable/disable
- Returns: this (for chaining)

### **`nullString( string )`**

- Sets string representation for null values
- Parameters: `string` (string) - Null representation (e.g., "NULL", "N/A")
- Returns: this (for chaining)

### **`commentMarker( char )`**

- Sets comment marker character
- Parameters: `char` (character) - Comment marker (e.g., '#')
- Returns: this (for chaining)

### **`ignoreSurroundingSpaces( boolean )`**

- Sets whether to ignore spaces around values
- Parameters: `boolean` (boolean) - Enable/disable
- Returns: this (for chaining)

### **`quoteMode( string )`**

- Sets quote mode for writing
- Parameters: `string` (string) - Quote mode: "ALL", "MINIMAL", "NON_NUMERIC", "NONE", "ALL_NON_NULL"
- Returns: this (for chaining)
- Example: `csv.quoteMode("ALL")`

### **`quoteMode( quoteModeEnum )`**

- Sets quote mode for writing using QuoteMode enum
- Parameters: `quoteModeEnum` (QuoteMode) - QuoteMode enum value
- Returns: this (for chaining)
- Note: This is primarily for Java interoperability

### **`allowDuplicateHeaderNames( boolean )`**

- Sets whether to allow duplicate column names
- Parameters: `boolean` (boolean) - Enable/disable
- Returns: this (for chaining)

### **`autoFlush( boolean )`**

- Sets whether to flush after each record write
- Parameters: `boolean` (boolean) - Enable/disable
- Returns: this (for chaining)

### **`trailingDelimiter( boolean )`**

- Sets whether to add trailing delimiter at end of records
- Parameters: `boolean` (boolean) - Enable/disable
- Returns: this (for chaining)

### **`headerComments( ...comments )`**

- Sets header comments to write before CSV data
- Parameters: `comments` (string...) - Variable arguments of comment strings
- Returns: this (for chaining)
- Example: `csv.headerComments("File created on " & now(), "Author: System")`

### **`headerComments( commentsArray )`**

- Sets header comments to write before CSV data
- Parameters: `commentsArray` (array) - Array of comment strings
- Returns: this (for chaining)
- Example: `csv.headerComments(["File created on " & now(), "Author: System"])`

### **`overwrite( boolean )`**

- Sets whether to overwrite existing files when saving
- Parameters: `boolean` (boolean) - Enable/disable overwriting
- Returns: this (for chaining)

### **`setPath( path )`**

- Sets file path for future operations
- Parameters: `path` (string) - File path
- Returns: this (for chaining)

## Data Manipulation Methods

### **`setHeaders( ...headers )`**

- Sets header columns for the CSV
- Parameters: `headers` (string...) - Variable arguments of header names
- Returns: this (for chaining)
- Example: `csv.setHeaders("Name", "Email", "Age")`

### **`setHeaders( headersArray )`**

- Sets header columns for the CSV
- Parameters: `headersArray` (array) - Array of header names
- Returns: this (for chaining)
- Example: `csv.setHeaders(["Name", "Email", "Age"])`

### **`setRowData( rowNumber, rowData )`**

- Sets data for a specific row (1-based indexing)
- Parameters:
  - `rowNumber` (number) - Row number (1-based)
  - `rowData` (array) - Array of values for the row
- Returns: this (for chaining)
- Example: `csv.setRowData(1, ["A", "B", "C"])`

### **`addRow( rowData )`**

- Adds a new row to the CSV
- Parameters: `rowData` (array) - Array of values for the row
- Returns: this (for chaining)
- Example: `csv.addRow(["John", "john@example.com", 30])`

### **`getRowData( rowNumber )`**

- Gets data for a specific row (1-based indexing)
- Parameters: `rowNumber` (number) - Row number (1-based)
- Returns: Array of values

### **`getRowCount()`**

- Gets the number of rows in the CSV
- Returns: Number of rows

### **`getColumnCount()`**

- Gets the number of columns in the CSV
- Returns: Number of columns

### **`getHeaders()`**

- Gets the header columns
- Returns: Array of header names, or null if no headers

### **`clear()`**

- Clears all data from the CSV
- Returns: this (for chaining)

## Filtering and Mapping Methods

### **`filter( predicate )`**

- Sets a filter predicate to apply when loading CSV data
- Parameters: `predicate` (function) - Function that receives a row array and returns boolean
- Returns: this (for chaining)
- Example: `csv.filter((row) => row[2] >= 18)`

### **`map( mapper )`**

- Sets a mapper function to transform rows when loading CSV data
- Parameters: `mapper` (function) - Function that receives and returns a row array
- Returns: this (for chaining)
- Example: `csv.map((row) => { row[0] = row[0].toUpperCase(); return row; })`

## Streaming Methods

### **`process( path, consumer )`**

- Streams through CSV file row-by-row without loading into memory
- Parameters:
  - `path` (string) - Path to CSV file
  - `consumer` (function) - Function that receives each row array
- Returns: this (for chaining)
- Example: `csv.process("large.csv", (row) => println(row[0]))`

### **`process( consumer )`**

- Streams through CSV file using previously set path
- Parameters: `consumer` (function) - Function that receives each row array
- Returns: this (for chaining)

## Export Methods

### **`toArray()`**

- Converts CSV data to array of arrays
- Returns: Array

### **`toJson( [pretty] )`**

- Converts CSV data to JSON string
- Parameters: `pretty` (optional, boolean) - Pretty-print JSON (default: false)
- Returns: JSON string

### **`toQuery()`**

- Converts CSV data to BoxLang Query object
- Returns: Query object with VARCHAR columns

### **`toString()`**

- Converts CSV data to string representation
- Returns: CSV string

## Information Methods

### **`getPath()`**

- Gets the current file path
- Returns: File path string or null

### **`getDelimiter()`**

- Gets the current delimiter character
- Returns: Character

### **`hasHeaders()`**

- Gets whether the CSV has headers
- Returns: Boolean

### **`getData()`**

- Gets the raw CSV data as list of string arrays
- Returns: List of string arrays
